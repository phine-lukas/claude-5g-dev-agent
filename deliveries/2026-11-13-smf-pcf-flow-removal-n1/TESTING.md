# Testing — 2026-11-13-smf-pcf-flow-removal-n1

## Tier table

| Tier | Command | Where | Result | Duration |
|---|---|---|---|---|
| T0 build | `build/scripts/build_smf --clean --build-type Release --jobs --tests` | cloud | **PASSED** — no warnings | 33:32 |
| T1 unit | same command (builds and runs ctest) | cloud | **PASSED** — 57/57, 11 new | 0.98 s |
| T2 integration (no RF) | Robot suites from `oai-cn5g-fed` | cloud | **SKIPPED** (`oai-cn5g-fed` not in the session; also needs a running compose deployment) | — |
| T3 container E2E | `docker-compose/core-network.py` + Robot | cloud | **SKIPPED** (no docker daemon in this VM; and not opted in — the task did not say `E2E`) | — |
| T4 testbed / hardware | mini QoS-with-AF scenario, OAI gNB + nrUE in rfsim | local | **LOCAL ONLY** | — |

VM capabilities behind the SKIPPED entries (`scripts/probe_env.sh`):

```
  daemon reachable         no
  compose plugin           no
  can run a container      no
  --privileged works       no
  /dev/net/tun usable      yes
  SCTP sockets             no
  T0   CAN RUN  cmake present, 4 cores, 30 GB free
  T1   CAN RUN  unit tests only need the build to succeed
  T3   NO       no usable docker daemon
```

## Cloud results

### T0 — build

```bash
sudo apt-get install -y libgtest-dev libgmock-dev    # --install-deps does not cover these
cd oai-cn5g-smf/build/scripts
./build_smf --clean --build-type Release --jobs --tests
```

Clean build of the SMF and of the vendored NAS/NGAP/PFCP libraries, from the
final commit of the series. No compiler warnings (`grep -c "warning:"` → 0); the
only CMake output is the pre-existing `cmake_minimum_required` deprecation
notice, which is present on the base commit too.

### T1 — unit tests

- Total: **57 tests, all passed** (`100% tests passed, 0 tests failed out of 57`,
  total ctest time 0.98 s). 11 of them are new in this delivery; the 46 others
  are pre-existing and pass unchanged.
- New tests:
  - `NasModificationCommandTest.DeleteQosRule_IsFourOctetsWithLengthOne` — a
    DELETE rule is 4 octets, length indicator 1, octets `id 00 01 40`.
  - `…DeleteQosRule_CarriesNoQfiOrPrecedence`
  - `…QosRule_EncodedSizeMatchesReportedLength` — for create and delete rules.
  - `…QosRule_RejectsABufferSmallerThanTheIe` — the overrun guard.
  - `…QosRules_AggregateLengthMatchesEncodedSize`
  - `…ModificationCommand_DeleteCase_Encodes` — `Encode() == GetLength()`.
  - `…ModificationCommand_CreateCase_Encodes`
  - `…ModificationCommand_OptionalIesCarryTheirIei` — 0x2a, 0x7a, 0x79.
  - `…ModificationCommand_RoundTripsThroughDecode`
  - `SessionHandlerTest.MarkQfiForRelease_BuildsASpecCompliantDeleteRule`
  - `SessionHandlerTest.MarkQfiForRelease_OmitsTheRuleWhenNoIdentifierExists`

That is 11 cases: 9 in the new file, 2 added to `test_session_handler.cpp`.

**Reproduction before the fix.** The new tests were written first and run
against the unmodified base, which is how the root cause was pinned down.
7 of them failed and all 46 pre-existing tests passed (55 total at that point,
since the 2 session-handler cases came with the fix):

```
39 - NasModificationCommandTest.DeleteQosRule_IsFourOctetsWithLengthOne (Failed)
41 - NasModificationCommandTest.QosRule_EncodedSizeMatchesReportedLength (Failed)
42 - NasModificationCommandTest.QosRule_RejectsABufferSmallerThanTheIe (Failed)
43 - NasModificationCommandTest.QosRules_AggregateLengthMatchesEncodedSize (Failed)
44 - NasModificationCommandTest.ModificationCommand_DeleteCase_Encodes (Failed)
46 - NasModificationCommandTest.ModificationCommand_OptionalIesCarryTheirIei (Failed)
47 - NasModificationCommandTest.ModificationCommand_RoundTripsThroughDecode (Failed)
```

with the numbers that identify the bug:

```
test_nas_modification_command.cpp:101: rule.GetLengthIndicator()  Which is: 4   (expected 1)
test_nas_modification_command.cpp:102: rule.GetIeLength()         Which is: 7   (expected 4)
test_nas_modification_command.cpp:106: encoded                    Which is: 6   (expected 4)
test_nas_modification_command.cpp:161: encoded 14  vs  GetIeLength() 16
```

A delete rule reported 7 octets, encoded 6, and should be 4. The 6 is the
unbraced-macro bug: the precedence and the segregation/QFI stores were skipped
but `encoded_size` advanced for both anyway. The 7 is the stale constructor
length, because neither `SetRuleOperationCode()` nor
`SetNumberOfPacketFilters()` recomputed the indicator.

This reproduces the failure in the task description exactly. With
`GetIeLength()` = 5 per rule in the reported build:

```
GetLength() = 4 (hdr) + 2 (cause+IEI) + 7 (AMBR) + 12 (rules) + 8 (flowdesc) = 33
Encode()    = 4 + 2 + 7 + 14 (rules) = 27 consumed
              -> 33-27 = 6 < 8 -> "Buffer length is less than the minimum
                 length of this IE (8 octet)" -> "Encoding QoS Flow
                 Descriptions error"
```

which is the reported `33` and the reported error, from the same arithmetic.

### T2 — integration without RF

SKIPPED. The Robot suites live in `oai-cn5g-fed`, which is not part of this
session, and they expect a compose deployment that is already up — which this
VM cannot provide (no docker daemon).

### T3 — container end-to-end

SKIPPED, and not opted in: the task did not contain `E2E`. The VM has no usable
docker daemon, so it could not have run even with the opt-in. Steps are below
as L1.

## Fix log

No failure was caused by the change. The 7 failures above are the deliberate
pre-fix reproduction, not regressions. The 46 pre-existing tests passed both
before and after.

One course correction worth recording: the task description's leading theory for
the delete-case encode failure was a missing octet in the QoS rule layout
(precedence present at encode time, or the uninitialised members). The
characterisation run showed the uninitialised members are real but explain the
*7*, while the *6* comes from the `ENCODE_U8` macro expanding to two statements
under an unbraced `if`. Both are fixed; the macro one is the one that broke the
message.

## Still to run locally

### L1 — end-to-end QoD create/delete (was T3/T4)

**Why it is local:** no docker daemon in the cloud VM, and the RAN side needs
the rfsimulator; `oai-cn5g-fed` is not in the session either.

**Prerequisites:** both patch series applied (see APPLY.md — `common-src`
first), an SMF image rebuilt **from your patched branch**, and the mini
QoS-with-AF scenario from `oai-cn5g-fed` branch `feat-closed-loop-qos`.

```bash
# 1. Build the SMF image from the patched tree
cd <smf-checkout>
docker build --target oai-smf -f docker/Dockerfile.smf.ubuntu -t oai-smf:qos-n1-fix .

# 2. Point the scenario's compose file at that tag, then confirm it really runs
#    your build and not a pulled :develop
cd <fed-checkout>/docker-compose
grep -n "image:.*oai-smf" <your-compose-file>.yaml
docker image inspect oai-smf:qos-n1-fix --format '{{.Id}} {{.Created}}'

# 3. Bring the core up, then the gNB and nrUE in rfsim, then run one
#    QoD create/delete cycle through the AF
```

**Watch for — create:**

- nrUE: `CREATE new QoS rule`, and **no** `PDU SESSION MODIFICATION COMMAND -
  Unknown IEI 0x06` and no `decode_pdu_session_modification_command failure`.
- SMF: the N1 payload now starts `cb 59 … 2a … 7a … 79 …` — cause, then
  Session-AMBR behind IEI `0x2a`, QoS rules behind `0x7a`, flow descriptions
  behind `0x79`. Before the fix it was `cb 59 00 06 06 00 64 06 00 32 00 3a …`,
  with the AMBR length octet `0x06` immediately after the cause.

**Watch for — delete:**

- SMF: `N2 QoS Flow To Release List built with 2 flow(s)`, and **no**
  `Encode PDU Session Modification Command message error`.
- gNB: a `PDUSESSIONModify initiating message`, and the DRBs of the removed
  QFIs released.
- nrUE: `DELETE QoS rule`.

**Pass criteria:** the UE installs the rules on create and removes them on
delete, and the gNB releases the DRBs. Upstream OAI nrUE `develop` handles the
delete rule operation and skips the flow descriptions IE, so both sides are
observable.

**If it fails:** take the N1 payload from the SMF log first and check the three
IEIs are present — that separates an encoding problem from a UE-side one. If the
gNB sees nothing on delete, check the SMF for the two new error lines from
commit #2 (`…it will not be part of the N1N2MessageTransfer`), which now say
explicitly when a container was dropped instead of failing silently.

**Also watch, per the task description:** after a release-only modify the SMF
runs a UPF update step that copies the gNB tunnel ID from the response onto the
downlink edges (`src/smf_app/smf_procedure.cpp` around line 1608). A response
carrying no tunnel info would write zero there. Not reproduced and not changed
by this delivery — see OPEN_ISSUES.md item 9.

### L2 — Robot regression (was T2)

```bash
cd <fed-checkout>
# bring up the deployment the suite expects, then:
robot test/qos_tests.robot
robot test/smf_tests.robot
```

**Pass criteria:** no new failures against a run on the base commit.

## Regression checks

Things that worked before and must still work:

- **PDU session establishment** — the Establishment Accept uses the same
  `SessionAmbr`/`QosRules` classes but as *mandatory*, IEI-less IEs, via a
  different message class. Unchanged by design, and covered by
  `ModificationCommand_CreateCase_Encodes` only indirectly; confirm with a plain
  session establishment in L1 before touching QoS at all.
- **QoS flow creation** — `NasModificationCommandTest.ModificationCommand_CreateCase_Encodes`
  plus the UE's `CREATE new QoS rule` in L1.
- **The QFI reuse fix this follows** — `test_upf_graph.cpp` QFI allocation tests,
  all still passing in T1.
- **AMF and UPF builds** — they vendor the same `common-src`. The macro change is
  library-wide; build both after bumping their submodule, and see OPEN_ISSUES.md
  item 5 for the scan to run first.
