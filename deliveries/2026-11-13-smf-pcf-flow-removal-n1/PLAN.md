# Plan — 2026-11-13-smf-pcf-flow-removal-n1

Date: 2026-11-13 · Profile: none (oai-public-like, repos given in the task) · Mode: default (no AUTOPILOT, no E2E)

Follow-up to the QFI-reuse work. Approved in chat on 2026-11-13; the answers
are folded in below and recorded in §11.

---

## 1. Understanding

An AF creates a QoD session and deletes it again. The PCF removes the PCC rule
and the SMF removes the flows on the UPF, but the gNB keeps its DRBs and the UE
keeps its QoS rules, because the PDU Session Modification Command never arrives
intact. Four defects were reported. Defect 1 (a removal-only PCF update built no
N2 transfer) is **already fixed and committed** on the base branch as `f086910`
— the task document describes it as an uncommitted local diff, which is stale;
`followup-n2-release-only.diff` was never needed. This work therefore closes
defects 2, 3 and 4: the optional N1 IEs are sent without their IEI so the UE
cannot decode the message; the delete-case command does not encode at all; and an
N1 encode failure is ignored and takes the valid N2 part down with it.

## 2. Repos and base commits

| Repo | Role | Branch | Base SHA |
|---|---|---|---|
| `oai-cn5g-smf` | target | `fix/qfi-reuse` | `f086910b62964497f6a38dc1e78489dc02348efe` |
| `oai-cn5g-common-src` | target (submodule `src/common-src`) | pinned by the SMF | `f725043cc3694f29c5ea91b0d244a868f5d4179a` |
| `oai-cn5g-amf` | read-only reference | `develop` | `b2f19d1a` |
| `claude-5g-dev-agent` | toolkit | `main` | `f1eb8395836ae3e09422578e2e0820cd2bb74d0a` |

`oai-cn5g-fed` (compose deployments and Robot suites) is not present in this
session, so no tier above T1 can run here.

## 3. Spec basis

| TS | Version | Clause | What it mandates |
|---|---|---|---|
| 24.501 | V18.14.0 | 9.11.4.13, Table 9.11.4.13.1 | "For the 'delete existing QoS rule' operation, the QoS flow identifier value field shall not be included." Likewise "the QoS rule precedence value field shall not be included", and "For the 'delete existing QoS rule' operation, the length of QoS rule field is set to one." NOTE 1: "Octet m+2 shall not be included without octet m+1." |
| 24.501 | V18.14.0 | 9.11.4.12, Figure 9.11.4.12.2 | A QoS flow description is QFI / operation code / E-bit + number of parameters; for "delete existing QoS flow description" the E bit is 0 and no parameters list follows — 3 octets. The existing code is already correct here. |
| 24.501 | V18.14.0 | 8.3.2 (Establishment Accept) vs 8.3.7 (Modification Command) | Session-AMBR, authorized QoS rules and authorized QoS flow descriptions are mandatory (no IEI) in the Establishment Accept but optional (type 4/6, with IEI) in the Modification Command. |
| 38.413 | V17.10.0 | 9.3.4.3 | Every IE of the PDU Session Resource Modify Request Transfer is Optional, so a release-only transfer carrying just the QoS Flow to Release List is valid. |
| 38.413 | V17.10.0 | 9.3.1.13 | "QoS Flow to Release List" is of type *QoS Flow List with Cause*, clause 9.3.1.13 — **not** 9.3.1.8, which is *Global ng-eNB ID*. The comment in `session_handler.cpp` cites the wrong clause. |
| 23.502 | V18.14.0 | 4.3.3.2 step 3b | For SMF-requested modification the SMF invokes `Namf_Communication_N1N2MessageTransfer` carrying the N2 SM information and the N1 SM container. |
| 29.512 | V18.13.0 | 4.2.3.2 | `Npcf_SMPolicyControl_UpdateNotify` — the PCC rule removal that triggers this path. Added to the toolkit spec manifest by this run. |

## 4. Current state in the repo(s)

**Exists / already fixed:** `f086910` makes the PCF-initiated N2 builder look up
released flows before its early return, so a removal-only decision now produces a
QoS Flow To Release List.

**Defect 2 — missing IEIs.** `PduSessionModificationCommand::Set5gsmCause` calls
`SetIei(kIei5gsmCause)`; `SetSessionAmbr`, `SetAuthorizedQosRules` and
`SetAuthorizedQosFlowDescriptions` do not. The same class's `Decode()` switches on
`kIeiSessionAmbr` (0x2a), `kIeiAuthorizedQosRules` (0x7a) and
`kIeiAuthorizedQosFlowDescriptions` (0x79), so the library cannot decode what it
encodes. `Type6NasIe::GetIeLength()` = `GetHeaderLength()` (3 with IEI, 2 without)
+ `li_`, so setting the IEI grows the IE and all length arithmetic follows.
`smf_context::get_session_ambr` only calls setters on the object it is passed, so
an IEI carried by that object is not lost.

**Defect 3 — the delete-case command does not encode.** The reported numbers
reproduce exactly from the code. With `QosRule::GetIeLength()` = 5 per delete rule:

    GetLength() = 4 (hdr) + 2 (cause+IEI) + 7 (AMBR) + 12 (rules) + 8 (flowdesc) = 33
    Encode()    = 4 + 2 + 7 + 14 (rules)  = 27 consumed
                  -> 33-27 = 6 < 8, Type6NasIe::Validate() logs
                     "Buffer length is less than the minimum length of this IE (8 octet)"

matching the reported `33` and the reported failure. The length side counts 5 per
rule while the encoder reportedly wrote 6; reading `QosRule::Encode()` statically
gives 5 (id 1 + length 2 + octet-7 1 + QFI 1), so one octet was unaccounted for.
Commit 1 pins this down empirically before anything is changed.

Independently of that, the spec settles the correct shape: `session_handler.cpp`
calls `rule.SetQfi()` on a "delete existing QoS rule", which 9.11.4.13 forbids
twice over (QFI present at all; QFI without precedence, against NOTE 1). A
spec-correct delete rule is 4 octets with length indicator 1.

**Also found:** `QosRule::Encode()` guards with `if (len < length_)` but writes
`length_ + 3` octets — a buffer sized exactly `length_` is overrun by 3.

**Defect 4.** `smf_context.cpp` (`handle_pdu_session_modification_network_requested`,
`TODO: handle encode N1, N2 failure`) ignores both builders' return values and sets
the N1 container unconditionally. On the AMF side `amf_http2_server.cpp` finds the
N1 MIME part empty, answers `200 N1_N2_TRANSFER_INITIATED` and returns, discarding
the already-parsed N2 part.

**Dead code:** `session_handler::build_release_flow` is byte-for-byte duplicated by
`mark_qfi_for_release` and has no callers.

## 5. Design decisions

**D1 — where to fix the missing IEIs.** Options: (a) construct the three IEs with
their IEI at the two `smf_n1.cpp` call sites; (b) set the IEI inside the three
setters of `PduSessionModificationCommand`, as `Set5gsmCause` already does.
**Chosen: (b)**, confirmed by the user. It matches the sibling setter, fixes every
caller at once, cannot be lost by a caller that forgets, and is symmetric with the
class's own `Decode()`. It is safe for the PDU Session Establishment Accept, which
uses a different message class whose setters are untouched. Cost: a `common-src`
commit plus a submodule bump in the SMF.

**D2 — delete-rule shape.** Remove the `SetQfi()` call per 24.501 §9.11.4.13 so the
rule is 4 octets with length indicator 1, and additionally fix the `QosRule::Encode()`
buffer guard to validate against `GetIeLength()`. The user confirmed that fixes
belong in the submodule as well as the SMF.

**D3 — N1/N2 failure handling.** Check both builders' return values; omit a container
whose builder failed; if both fail, send no transfer and log an error. The AMF's
silent drop is a separate AMF issue and stays out of scope.

**D4 — incidental cleanups.** Fold in the two small corrections in code already being
touched: the wrong `38.413 §9.3.1.8` citation, and the duplicated `build_release_flow`.

## 6. Commit plan

### `oai-cn5g-common-src` (submodule `src/common-src`)

| # | Title | Files | Spec refs |
|---|---|---|---|
| 1 | `fix(nas): set the IEI of the Modification Command's optional IEs` | `nas/5gsm-msgs/PduSessionModificationCommand.cpp` | 24.501 §8.3.7 |
| 2 | `fix(nas): validate the full IE length before encoding a QoS rule` | `nas/ies/QosRule.cpp` | 24.501 §9.11.4.13 |

### `oai-cn5g-smf`

| # | Title | Files | Spec refs |
|---|---|---|---|
| 1 | `test(smf): pin down delete QoS rule encoding` (characterisation, run before any fix) | `src/smf_app/test/test_nas_modification_command.cpp`, `src/smf_app/test/CMakeLists.txt` | 24.501 §9.11.4.13 |
| 2 | `fix(smf): build spec-compliant delete QoS rules` | `src/smf_app/session_handler.cpp`, `.hpp` | 24.501 §9.11.4.13; 38.413 §9.3.1.13 |
| 3 | `test(smf): assert delete rules encode to four octets` | `src/smf_app/test/*` | 24.501 §9.11.4.13 |
| 4 | `fix(smf): do not send an N1N2 transfer with a failed container` | `src/smf_app/smf_context.cpp` | 23.502 §4.3.3.2 |
| 5 | `build(smf): bump common-src for the NAS encoding fixes` | `src/common-src` | — |

## 7. Configuration changes

None. No new config keys, no defaults changed, no compose/conf changes needed.

## 8. Test plan

### Unit tests to add or extend

| Module | Framework | What is asserted |
|---|---|---|
| `src/smf_app/test/test_nas_modification_command.cpp` (new) | GoogleTest / ctest | A delete QoS rule encodes to 4 octets with length indicator 1 and no precedence/QFI octet; `Encode()` return equals `GetIeLength()` for create and delete rules; a full Modification Command with (a) one create rule + flow description and (b) two delete rules + flow descriptions encodes with `Encode() == GetLength()`; IEIs 0x2a/0x7a/0x79 appear at the expected offsets; `Encode()` → `Decode()` round-trips (impossible today). |
| `src/smf_app/test/test_session_handler.cpp` (extend `MarkQfiForRelease_*`) | GoogleTest / ctest | The rule the handler actually builds carries no QFI and encodes to 4 octets. |

`src/smf_app/test/CMakeLists.txt` already links `NAS` and includes `nas/ies`,
`nas/common` and `nas/5gsm-msgs`, so the new test needs one `add_executable` line
and no new framework. The `smf_n1` builders themselves depend on the global SMF
context and cannot be unit-tested directly; the tests mirror their IE assembly
instead. That gap is recorded in OPEN_ISSUES.md.

### Tier table

| Tier | Command | Verdict | Note |
|---|---|---|---|
| T0 build | `build/scripts/build_smf --clean --build-type Release --jobs` | CAN RUN | 4 cores, 30 GB free |
| T1 unit | `build/scripts/build_smf --tests` | CAN RUN | full `smf_unit_tests`; base-commit run too if anything fails |
| T2 integration (no RF) | Robot suites in `oai-cn5g-fed` | SKIPPED | repo not in this session; also needs a running deployment |
| T3 container E2E | `docker-compose/core-network.py` + Robot | NOT RUN (opt-in) | no docker daemon in this VM, and no `E2E` in the task |
| T4 testbed / hardware | mini QoS-with-AF scenario, OAI gNB + nrUE in rfsim | LOCAL ONLY | always |

### Testbed scripts and new test cases

- Local T4: mini QoS-with-AF scenario (`oai-cn5g-fed`, branch `feat-closed-loop-qos`)
  with a patched SMF image, one QoD create/delete cycle. Expected: on create the UE
  logs `CREATE new QoS rule` and no `Unknown IEI`; on delete the gNB logs a
  `PDUSESSIONModify initiating message` and releases the DRBs of the removed QFIs,
  and the UE logs `DELETE QoS rule`. Full steps go into TESTING.md.
- To watch in that run: after a release-only modify the SMF runs a UPF update step
  that copies the gNB tunnel ID from the response onto the downlink edges
  (`smf_procedure.cpp` around line 1608); a response without tunnel info would give
  zero there. Not addressed by this work.

## 9. Risks and assumptions

- The one octet unaccounted for in `QosRule::Encode()` is settled by commit 1 before
  behaviour changes. If it turns out to be a third distinct defect, stop and report
  rather than fold it in silently.
- The delete-rule shape changes bytes on the wire to the UE. Upstream OAI nrUE
  `develop` handles the delete operation, but a UE that tolerated the old
  non-compliant encoding is untested here.
- The `common-src` change is in a library vendored by the AMF and UPF too. The IEI
  change is confined to `PduSessionModificationCommand`'s own setters, so other
  messages are unaffected — but the submodule bump has to be carried downstream.
- Nothing above T1 can run in this VM, so the end-to-end claim in the task stays
  unverified by this run.

## 10. Questions

Answered in chat before implementation started — see §11. None outstanding.

## 11. Approval log

| Date | Who | Answers / decision |
|---|---|---|
| 2026-11-13 | user | Q1: fix it in `common-src`, not only in the SMF. Q2: likewise include the `QosRule::Encode` buffer-guard fix in the submodule. Q3: deliveries should from now on be pushed as a folder on `main` instead of a `claude/delivery-<slug>` branch, so no branch checkout is needed — `push_delivery.sh`, CLAUDE.md and the two skills are updated accordingly as a separate toolkit commit. Q4: fold in the incidental cleanups. Implementation approved. |

---

## 12. Deviations from this plan

Recorded after implementation. The plan above is the approved version; this
section says where the work diverged from it and why.

1. **The root cause of defect 3 was not the one this plan expected.** §4 noted
   that one octet was unaccounted for and that commit 1 would pin it down. It
   did: a delete rule reported `GetIeLength() == 7` and encoded 6 octets where
   the spec wants 4. The 7 is the stale constructor length, as suspected. The 6
   is a different bug the plan did not anticipate — `ENCODE_U8` expands to two
   statements with no `do { } while (0)`, so under the unbraced
   `if (precedence_.has_value())` and `if (segregation_ or qfi_.has_value())`
   the stores were skipped but `encoded_size` advanced for both anyway.

2. **One extra `common-src` commit.** That macro defect needed its own fix, so
   the planned 2-commit `common-src` series became 3:
   `fix(nas): make the ENCODE macros single statements` leads it. It also fixes
   `_5gsNetworkFeatureSupport::Encode()`, which had the same defect — the only
   other unbraced site in the tree, found by scanning all of `src/`.

3. **Two further `QosRule` length bugs fixed in the same commit** as the planned
   one: `SetLengthIndicator()` counted the create/modify packet filter list once
   per packet filter rather than once in total (quadratic, harmless at one
   filter), and the constructor left three members uninitialised. Both are in
   the function the plan already called for changing.

4. **No characterisation commit.** §6 planned commit 1 of the SMF series as a
   test that records current behaviour before any fix. The characterisation
   *run* happened as planned and is written up in TESTING.md, but committing a
   deliberately red test and then fixing it would have left a commit that does
   not build green. The tests are instead in `test(smf): cover the NAS encoding
   of the Modification Command`, after the fixes. The SMF series is 4 commits,
   not 5.

5. **A guard the plan left open.** §5 D-notes mentioned guarding `rule_id != 0`
   without settling the behaviour. Implemented as: release the flow without an
   N1 QoS rule and log an error, rather than emitting identifier 0, which
   Table 9.11.4.13.1 forbids the network from sending and which would make the
   UE reject the whole command. Covered by
   `MarkQfiForRelease_OmitsTheRuleWhenNoIdentifierExists`.

6. **Toolkit changes made along the way**, pushed to `main` ahead of this
   delivery: the delivery mechanism moved from `claude/delivery-<slug>` to a
   folder on `main` (user's request), TS 29.512 was added to the spec manifest,
   and the `oai-cn` skill gained the GoogleTest and submodule prerequisites that
   a native `build_smf --tests` needs.
