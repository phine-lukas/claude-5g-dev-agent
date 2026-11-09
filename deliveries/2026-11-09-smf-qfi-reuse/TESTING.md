# Testing — 2026-11-09-smf-qfi-reuse

What was verified in the cloud, and exactly what remains to run locally.

Result values: `PASSED` · `FAILED-preexisting` (also fails on the base commit)
· `SKIPPED (<reason>)` (the VM could not run it) · `NOT RUN (opt-in)` (T3 without
`E2E` in the task) · `LOCAL ONLY` (testbed, RF, hardware — never run in the cloud).

A tier that could not run is never marked passed.

## Tier table

| Tier | Command | Where | Result | Duration |
|---|---|---|---|---|
| T0 build | `build/scripts/build_smf --clean --build-type Release --jobs --force` | cloud | **PASSED** | 27:51 |
| T1 unit | `build/scripts/build_smf --build-type Release --jobs --force --tests` (GoogleTest + `ctest -L unit`) | cloud | **PASSED** — 46/46, 6 new | 11:23 (0.72 s for ctest itself) |
| T2 integration (no RF) | `robot test/qos_tests.robot` from `oai-cn5g-fed` against a compose subset | cloud | **SKIPPED** (no docker daemon, no compose plugin, `robot` not installed) | — |
| T3 container E2E | `oai-cn5g-fed/docker-compose/core-network.py` + `robot test/qos_tests.robot` with a locally built SMF image | cloud | **NOT RUN (opt-in)** — the task contained no `E2E`, and the VM has no docker daemon either way | — |
| T4 testbed / AF loop | the issue's reproduction, see L2 below | local | **LOCAL ONLY** | — |

VM capabilities behind the SKIPPED entries (from `scripts/probe_env.sh`):

```
=== Docker
  daemon reachable         no
  compose plugin           no
  can run a container      no
  --privileged works       no
=== Kernel features
  /dev/net/tun usable      yes
  SCTP sockets             no
=== Tools
  cmake 3.28.3 · ninja 1.11.1 · gcc 13.3.0 · clang 18.1.3 · clang-format 18.1.3
  robot                    -
=== Tier verdict
  T0 CAN RUN · T1 CAN RUN · T2 CAN RUN (RAM/cores only) · T3 NO (no usable docker daemon)
```

Note: `probe_env.sh` rates T2 as CAN RUN on resources alone (16 GB RAM, 4 cores).
The OAI CN T2 suites are Robot suites against a docker-compose subset, so the
missing docker daemon and the missing `robot` binary make T2 unrunnable here
regardless of resources.

## Environment preparation (not part of the change)

Two things the VM lacked. Neither is a code change; both are recorded so the
cloud result can be reproduced.

1. `src/common-src` was not checked out. It is a submodule pinned to
   `f725043cc3694f29c5ea91b0d244a868f5d4179a`, which is byte-for-byte the HEAD
   of the sibling `oai-cn5g-common-src` checkout in this session
   (`diff` of `utils/uint_generator.hpp` between the two: identical).

   ```bash
   git submodule update --init src/common-src
   ```

2. The SMF's from-source dependencies (fmt, spdlog, pistache, nlohmann,
   nghttp2, yaml-cpp, cpr) were absent, so `cmake` failed with
   `Could not find a package configuration file provided by "cpr"`.

   ```bash
   build/scripts/build_smf --install-deps --force
   ```

3. GoogleTest was absent, so the unit-test target failed to compile with
   `fatal error: gtest/gtest.h: No such file or directory`. CI builds the tests
   in the `checks` stage of `docker/Dockerfile.smf.ubuntu`, which installs them
   from apt. The same packages were installed here:

   ```bash
   apt-get install --yes libgtest-dev libgmock-dev
   ```

   (`googletest-tools`, the third package the Dockerfile lists, has no
   installation candidate on this Ubuntu release and is not needed to build or
   run the suite.)

## Cloud results

### T0 — build

```bash
build/scripts/build_smf --clean --build-type Release --jobs --force
```

`smf compiled`, exit 0.

No new warnings. The build log holds three warnings, all pre-existing and all in
`src/common-src`, none in a file this delivery touches:

```
src/common-src/ngap/libngap_ies/Ngap_VolumeTimedReport-Item.c: warning: integer constant is so large that it is unsigned
src/common-src/utils/string.cpp: warning: 'std::not1' is deprecated: use 'std::not_fn' instead [-Wdeprecated-declarations]
src/common-src/utils/string.cpp: warning: 'std::ptr_fun' is deprecated: use 'std::function' instead [-Wdeprecated-declarations]
```

`git clang-format 7bfe3220` reports "clang-format did not modify any files".
Note the VM has clang-format 18.1.3 while CI pins clang-format 19
(`ci-scripts/common/docker/Dockerfile.ci.clang-format`), so re-check formatting
locally with 19 before pushing.

### T1 — unit tests

```bash
build/scripts/build_smf --build-type Release --jobs --force --tests
```

- `100% tests passed, 0 tests failed out of 46` — total ctest time 0.72 s
- 6 of the 46 are new in this delivery; nothing failed, so no base-commit
  comparison run was needed.

```
25/46 Test #25: UpfGraphTest.GenerateQfi_FirstAllocationIsTheDefaultFlowQfi ............ Passed
26/46 Test #26: UpfGraphTest.GenerateQfi_ReusesReleasedQfiAcrossManyAddRemoveCycles .... Passed
27/46 Test #27: UpfGraphTest.GenerateQfi_ExhaustsOnlyWhenAll63FlowsAreActive ........... Passed
28/46 Test #28: UpfGraphTest.GenerateQfi_WrapsRatherThanReturningAReleasedQfiAtOnce .... Passed
29/46 Test #29: UpfGraphTest.ReleaseQfi_IgnoresValuesOutsideTheSixBitRange ............. Passed
30/46 Test #30: UpfGraphTest.CopiedGraphDoesNotReissueTheOriginalsQfis ................. Passed
```

What each one pins down:

| Test | Asserts |
|---|---|
| `GenerateQfi_FirstAllocationIsTheDefaultFlowQfi` | the first three allocations are 1, 2, 3 — the default QoS flow keeps the QFI it gets on `develop` |
| `GenerateQfi_ReusesReleasedQfiAcrossManyAddRemoveCycles` | the reported regression: 200 add/remove cycles with one flow at a time all succeed, every QFI in 2..63; afterwards exactly 62 QFIs are free and the 63rd allocation fails |
| `GenerateQfi_ExhaustsOnlyWhenAll63FlowsAreActive` | 63 allocations yield 1..63 each exactly once, the 64th returns 0, and one release frees exactly one QFI |
| `GenerateQfi_WrapsRatherThanReturningAReleasedQfiAtOnce` | a QFI released while a higher one was handed out last comes back only after a full lap of the range |
| `ReleaseQfi_IgnoresValuesOutsideTheSixBitRange` | `release_qfi(0)`, `(64)`, `(255)` are no-ops; both ends of the range are themselves releasable |
| `CopiedGraphDoesNotReissueTheOriginalsQfis` | a copied `upf_graph` continues at 4 rather than restarting at 1 |

The four existing `UpfGraphTest` cases that call `release_qfi()` on a QFI the
allocator never handed out (`ReleaseQfi_FreesQfiAndErasesMappedPccRules` and
friends) still pass: clearing an already-clear bit is a no-op, and the PCC-rule
map cleanup they exercise is unchanged.

### T2 — integration without RF

SKIPPED. `docker info` fails (`no docker daemon`), the compose plugin is absent
and `robot` is not installed, so the Robot suites in `oai-cn5g-fed/test/` cannot
run. Steps for a local run are under L1.

### T3 — container end-to-end

NOT RUN (opt-in) — the task did not contain `E2E`, and this VM has no docker
daemon. Full local steps are under L1.

## Fix log

No failure was caused by this change. Nothing to record.

The two build failures seen in the cloud run were environmental and are covered
above: a missing `cpr` (no dependencies installed) and a missing `gtest/gtest.h`
(no GoogleTest installed). Neither reached the changed code.

## Still to run locally

Copy-pasteable, in order. Each step says what to watch for and what counts as a pass.

### L1 — T2/T3: QoS Robot suite against a locally built SMF image

**Why it is local:** this VM has no docker daemon, no compose plugin and no
`robot`; T3 was also not opted into (`E2E` absent from the task).

**Prerequisites:** the patch series applied (see APPLY.md), docker + compose,
`/dev/net/tun`, ~8 GB RAM, a checkout of `oai-cn5g-fed`.

```bash
# 1. Build the SMF image from the patched tree
cd <oai-cn5g-smf checkout>
docker build --target oai-smf -f docker/Dockerfile.smf.ubuntu -t oai-smf:qfi-reuse .

# 2. Run the unit tests the way CI does, inside the image's checks stage
docker build --target checks -f docker/Dockerfile.smf.ubuntu .

# 3. Point the compose file at the local image, then deploy
cd <oai-cn5g-fed checkout>/docker-compose
#    edit the smf service's `image:` line to oai-smf:qfi-reuse
python3 core-network.py --type start-basic --scenario 1

# 4. Run the QoS and SMF suites
cd ..
robot test/qos_tests.robot
robot test/smf_tests.robot
```

**Watch for:**

- step 2 ends with `SMF unit tests passed` and `100% tests passed` (the image
  build fails the build if a test fails)
- no `QFI pool exhausted` line in the SMF log
- the suites report the same pass count as on the base commit

**Pass criteria:** both suites pass, and the SMF log carries no new error line.

**If it fails:** compare against a run of the same suites on an image built from
`7bfe3220` — this change touches only per-session QFI bookkeeping, so a suite
that fails on both is unrelated to it.

### L2 — T4: the reported AF add/remove loop

**Why it is local:** needs a PCF with an AF driving Npcf_PolicyAuthorization
against a live deployment.

**Prerequisites:** the deployment from the QoS tutorial the issue names
(oai-cn5g-fed PR 4, tutorial A), one UE with an established PDU session, and a
PFCP capture on N4.

```bash
# with the deployment up and one UE attached, from the AF side:
#   repeat 70 times:
#     create an app session with one media component on the UE's flow
#       (a GBR QoS reference)
#     delete that app session
# capture N4 throughout:
tshark -i <n4-iface> -f 'udp port 8805' -Y 'pfcp' -w qfi-loop.pcapng
```

**Watch for:**

- in each PFCP Session Modification Request, the QFI in the Create QER and
  Create PDR: on `develop` these climb 2, 3, 4, … and the run dies at 64; with
  this change they stay inside 2..63 and wrap
- SMF log: **no** `QFI pool exhausted, cannot add flow for rule 'PA-QOS-…'`
- SMF log: **no** `Could not allocate a QFI for … PCC rule(s), reporting them as
  inactive`
- PCF log: **no** `RULE_PERMANENT_ERROR`
- every create is answered `201`, none `500`

**Pass criteria:** all 70 create/delete cycles succeed, every QFI observed is in
2..63, and none of the four log lines above appears.

**If it fails:** the SMF log's `Allocated QFI=%d for PCC rule '%s'` debug line
shows what the allocator handed out; compare it with the QFI in the Create QER
of the same transaction in the PCAP.

### L3 — scale check from the issue's second table

**Why it is local:** needs the AF's load generator and 29 UEs.

Re-run the 100 requests/s step that produced 1,100 `500` responses out of 1,511
creates. Pass criterion: no `500` attributable to QFI allocation, and no
`QFI pool exhausted` in the SMF log, at any step rate.

## Regression checks

Things that worked before and must still work:

- a PDU session establishes and its default QoS flow gets a QFI —
  `robot test/smf_tests.robot`, and the default flow's QFI is 1 in the PFCP
  Session Establishment Request
- adding several flows at once still assigns distinct QFIs —
  `robot test/qos_tests.robot`
- the SMF unit suite — `build/scripts/build_smf --tests` (46 tests)
