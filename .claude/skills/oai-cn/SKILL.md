---
name: oai-cn
description: Reference knowledge for the OpenAirInterface 5G Core repositories (oai-cn5g-amf, oai-cn5g-smf, oai-cn5g-upf, the other NFs, and the oai-cn5g-fed federation/umbrella repo) — which repo holds what, the per-NF source layout for SBI handlers, PFCP, NAS and state machines, native and Docker image builds, the GoogleTest/ctest unit tests and how to run them, the Robot Framework suites in the federation repo, the docker-compose tutorials and how to swap in a locally built NF image, C++ conventions, and the current MBS/MB-SMF state. Load this before changing anything in an OAI 5G Core repository.
---

# OpenAirInterface 5G Core (`oai-cn5g-*`)

Verified against local clones of the `openairinterface` GitHub repositories on 2026-11-05
(`oai-cn5g-amf` @ `b2f19d1a`, `oai-cn5g-smf` @ `5d6c732f`, `oai-cn5g-upf` @ `84131ca`,
`oai-cn5g-fed` @ `69d91e0`).

> Each repo carries its own `README.md`, `docs/`, `CONTRIBUTING.md` and `CHANGELOG.md`.
> Read those first; this skill is the map between them.

## 1. The repositories

All live at `https://github.com/openairinterface/<name>`.

| Repo | NF / purpose |
|---|---|
| `oai-cn5g-amf` | AMF — NAS, NGAP, N1/N2, SBI (Namf) |
| `oai-cn5g-smf` | SMF — session management, PFCP/N4 towards the UPF, Nsmf, policy towards the PCF |
| `oai-cn5g-upf` | UPF — user plane, GTP-U, PFCP agent, simple-switch and eBPF datapaths |
| `oai-cn5g-nrf` | NRF — NF registration and discovery |
| `oai-cn5g-ausf`, `oai-cn5g-udm`, `oai-cn5g-udr`, `oai-cn5g-udsf` | authentication and data management |
| `oai-cn5g-pcf` | PCF — policy |
| `oai-cn5g-nssf` | NSSF — slice selection |
| `oai-cn5g-nef` | NEF — northbound exposure |
| `oai-cn5g-lmf` | LMF — location |
| `oai-cn5g-common-src` | shared sources, vendored into each NF as `src/common-src/` |
| **`oai-cn5g-fed`** | **the umbrella**: docker-compose deployments, CI scripts, Robot Framework suites, the tutorials in `docs/` |

`oai-cn5g-fed` is where integration happens — if a task says "test the core", it almost
always means a compose file plus a Robot suite from this repo.

## 2. Per-NF source layout

The NFs share a structure. Using `oai-cn5g-smf` as the example:

| Path | Contents |
|---|---|
| `src/smf_app/` | the NF's own logic: session handler, policy manager, UPF graph, message types |
| `src/api-server/` | generated + hand-written SBI (HTTP/2 REST) handlers |
| `src/pfcp/` | PFCP (N4) message encoding and the PFCP association/session layer |
| `src/itti/` | the inter-task interface — the message bus every NF is built around |
| `src/ngap/`, `src/nas/` | NGAP / NAS where the NF needs them |
| `src/common/`, `src/common-src/` | shared types; `common-src` is the vendored `oai-cn5g-common-src` |
| `src/oai_smf/` | `main()` and startup |
| `etc/` | shipped configuration (`*.conf` / YAML) |
| `build/scripts/build_smf` | the build entry point |
| `docker/Dockerfile.smf.ubuntu` | multi-stage image build, including a `checks` stage that runs the tests |
| `ci-scripts/` | per-repo CI helpers |
| `docs/` | per-repo documentation, incl. `docs/testing/README.md` |

AMF adds `src/amf-app/`, `src/contexts/`, `src/sbi/`, `src/sctp/`, `src/secu_algorithms/`.
UPF adds `src/upf_app/` (with `control/`, `simpleswitch/`, `bpf/` datapaths) and `src/gtpv1u/`.

## 3. Build

### Native

A fresh clone has **empty submodules** — `src/common-src` (the vendored NAS /
PFCP / NGAP library), `build/common-build` and `ci-scripts/common`. `build_<nf>`
syncs them itself, but anything that reads the sources first (grep, a review,
a patch) sees nothing until you run:

```bash
git submodule update --init --recursive
```

Each NF has a build script with the same shape:

```bash
cd oai-cn5g-smf/build/scripts
./build_smf --install-deps          # once per machine (needs sudo and network)
./build_smf --clean --Verbose --build-type Release --jobs
./build_smf --tests                 # build AND run the GoogleTest unit tests
```

`build_amf` and `build_upf` take the same options (`build/scripts/build_<nf>`).
Run `./build_<nf> --help` for the authoritative list — options drift between repos.

### Docker image

```bash
cd oai-cn5g-smf
docker build --target oai-smf -f docker/Dockerfile.smf.ubuntu -t oai-smf:my-change .
```

Image builds are the realistic path for integration testing, because the compose files
in `oai-cn5g-fed` consume images, not binaries.

## 4. Unit tests (T1)

Tests are GoogleTest, driven by ctest. They live in `test/` directories inside `src/`:

| Repo | Test directories |
|---|---|
| `oai-cn5g-smf` | `src/smf_app/test/` (`test_session_handler.cpp`, `test_smf_msg.cpp`, `test_upf_graph.cpp`, `test_smf_policy_manager.cpp`, `test_pcf_qod_workflow.cpp`), `src/common-src/test/`, `src/common-src/ngap/test/` |
| `oai-cn5g-amf` | `src/common-src/test/`, `src/common-src/ngap/test/`, `src/common-src/nas/test/` |
| `oai-cn5g-upf` | `src/common-src/test/`, `src/common-src/ngap/test/`, `src/common-src/nas/test/` |

Two ways to run them — **the Docker one is what CI does and needs no host dependencies**:

**`--install-deps` does NOT install GoogleTest**, so a native `--tests` run on a
fresh machine fails at `#include <gtest/gtest.h>`. Install it first (the
Dockerfile's `checks` stage also asks for `googletest-tools`, which no longer
exists on Ubuntu 24.04 — skip it):

```bash
sudo apt-get install -y libgtest-dev libgmock-dev
```

```bash
# Native: builds the smf_unit_tests binary and runs it
cd oai-cn5g-smf/build/scripts && ./build_smf --tests

# Docker: the `checks` stage runs ctest during the image build
docker build --progress=plain --target checks -f docker/Dockerfile.smf.ubuntu -t oai-smf-checks .
# read the run's log back out of the image without rebuilding:
docker run --rm oai-smf-checks cat /openair-smf/build/smf/build/Testing/Temporary/LastTest.log
```

See `oai-cn5g-smf/docs/testing/README.md` for the full description of this workflow.

**Adding a test:** drop a `test_<thing>.cpp` beside the existing ones and register it in
that directory's `CMakeLists.txt`. Note `smf_globals_stub.cpp` — the app's globals are
stubbed so handlers can be tested without starting the NF. Follow that pattern rather
than standing up a whole NF in a test.

Coverage is uneven: the SMF has real unit tests around session handling, policy and the
UPF graph; the AMF and UPF have little beyond `common-src`. If the code you are changing
has no test neighbours, say so in the plan and propose a minimal addition — do not
introduce a new framework unasked.

## 5. Integration tests (T2 / T3) — `oai-cn5g-fed`

### Robot Framework suites

In `oai-cn5g-fed/test/`:

| Suite | Covers |
|---|---|
| `all_nfs.robot` | every NF comes up and registers with the NRF |
| `smf_tests.robot`, `smf_upf_tests.robot` | session management, N4 |
| `qos_tests.robot`, `policy_api_tests.robot` | QoS and PCF policy |
| `Northbound.robot` | NEF northbound APIs |
| `lmf_tests.robot` | location |
| `packetrusher_tests.robot`, `omec_gnbsim_tests.robot` | with a simulated gNB/UE |
| `ebpf_tests.robot` | the eBPF UPF datapath |
| `common.robot`, `CNTestLib.py`, `docker_api.py` | shared keywords and helpers |

They are driven with the `robot` CLI against a running compose deployment; the repo ships
a virtualenv (`.rfvenv`) and `ci-scripts/checkRobotFrameworkHtmlReport.py` parses the
result. Read the suite's own `Suite Setup` to see which compose file it expects —
**the suite assumes a deployment is already up; it will not start one for you.**

### Compose deployments

`oai-cn5g-fed/docker-compose/` holds ~25 `docker-compose-basic-*.yaml` variants
(`-nrf`, `-nrf-pcf`, `-nrf-qos`, `-nrf-ebpf`, `-mongodb`, `-vpp-upf`, …), plus
`core-network.py` as the start/stop driver and `conf/` for the NF configuration.
`docs/DEPLOY_SA5G_*.md` is one tutorial per scenario; `docs/BUILD_IMAGES.md` covers
building the images these compose files use.

**Swapping in a locally built NF image** — this is the step that makes an integration
test mean anything:

1. Build the NF image from your branch with a distinctive tag (§3).
2. Edit the `image:` line for that NF in the compose file you are using, or override it
   with the tag the file already expects.
3. Bring the deployment up and confirm from `docker image inspect` / the NF's startup
   banner that the container is really running your build, not a pulled `:develop`.

Testing against a public image instead of your own is the most common way an integration
test silently proves nothing.

### Resource needs

A basic compose deployment is roughly 8 containers; the UPF needs `/dev/net/tun`,
and the eBPF datapath additionally needs privileges and a recent kernel. Expect
~6–8 GB RAM and a few GB of disk for images. In a cloud VM, check `scripts/probe_env.sh`
first — without TUN, the UPF will not come up and T3 must be marked SKIPPED, not failed.

## 6. Test tiers (T0–T4)

| Tier | What | Command | Cloud VM |
|---|---|---|---|
| **T0** build | affected NFs, native or image | `./build_<nf> --clean --build-type Release --jobs` or `docker build --target oai-<nf> …` | CAN RUN |
| **T1** unit | GoogleTest per NF | `./build_<nf> --tests`, or the `checks` Docker stage | CAN RUN |
| **T2** component | one NF against stubs / a minimal compose subset | compose subset + the narrow Robot suite | MAYBE |
| **T3** container E2E (**opt-in**) | full compose deployment + Robot suite | `docker-compose/core-network.py` + `robot test/<suite>.robot` | needs docker, TUN, ~8 GB; **only with `E2E` in the task** |
| **T4** testbed / hardware | real gNB, lab hosts | — | NEVER in the cloud |

## 7. Conventions

- **Language:** C++17. The NFs are heavily ITTI-message-driven — new cross-component
  behavior usually means a new ITTI message type, not a direct call.
- **Formatting:** each repo has a `.clang-format`; the UPF pins **clang-format 19**
  (commit `84131ca` was a reformat for exactly that). Check the repo's CI script for the
  version before reformatting, and format only the lines you touched:
  `git clang-format <base-sha>`.
- **Logging:** spdlog-based per-NF loggers (`Logger::smf_app().info(...)` and friends).
- **Config:** YAML under `etc/`, mirrored by `oai-cn5g-fed/docker-compose/conf/`. A new
  key needs a default that keeps existing deployments working **and** a matching entry in
  the fed repo's conf, or the compose deployment will not pick it up.
- **Commits:** conventional-commit style is in use — `fix(smf): never install a PDR
  without an SDF filter`, `docs(qos): add mini QoS-on-demand scenario`,
  `fix: fix the clang formatting to version 19`. Check `git log` on the repo you are in.

## 8. MBS state in the OAI core

**There is essentially no MBS in the OAI 5G Core.** A search for `mbs`/`tmgi` across
`src/` in the AMF and SMF returns nothing; the only hits in the UPF
(`src/upf_app/control/SessionManager.cpp`, `src/upf_app/simpleswitch/pfcp_far.*`) are
ordinary PFCP FAR fields that happen to contain the substring, not MBS support.

Concretely missing: MB-SMF and MB-UPF as such, Nmbsmf (TS 29.532), MBS session contexts,
TMGI allocation, N4mb, and the MBS-specific NGAP procedures on the AMF side.

**Consequence for planning:** an MBS task that needs a core is a task for the 5G-MAG
Open5GS fork (see the `open5gs-mbs` skill), not for the OAI core. If a task asks for MBS
in an OAI NF, treat it as a large new feature, say so in the plan, and raise it as a
question before writing code.

Verify before relying on this — the core moves:

```bash
for r in oai-cn5g-amf oai-cn5g-smf oai-cn5g-upf; do
  echo "== $r"; git -C "$r" grep -ni "mbs\|tmgi\|mb-smf\|n4mb\|multicast" -- src | head
done
```
