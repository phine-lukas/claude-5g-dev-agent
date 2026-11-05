---
name: oai-ran
description: Reference knowledge for the openairinterface5g repository (OAI RAN) — gNB, nrUE, CU/DU and CU-CP/CU-UP split, the RRC/MAC/RLC/PDCP/PHY directory layout, where the RRC/F1AP/NGAP/E1AP ASN.1 grammars live and which 3GPP versions they correspond to, how to build (cmake/ninja, rfsimulator), how to run and extend the ctest unit tests, the T0-T4 test tiers with concrete commands, coding and commit conventions, and the current state of MBS (MCCH, MTCH, G-RNTI, SIB20) support. Load this before changing anything in an openairinterface5g checkout or a private fork of it.
---

# OpenAirInterface RAN (`openairinterface5g`)

Verified against the private fork `phinetech/openairinterface5g-private` @ `mbs-phase-a`
(upstream `OPENAIRINTERFACE/openairinterface5g`, GitLab `gitlab.eurecom.fr/oai/openairinterface5g`)
on 2026-11-05. Paths below exist in that tree.

> **The repo documents itself.** `AGENTS.md` at the repo root is written for agents and
> takes precedence over this skill wherever the two disagree — read it first. Also read
> `doc/BUILD.md`, `doc/code-style-contrib.md`, `CONTRIBUTING.md`, and on a feature branch
> `MBS-REBASE-NOTES.md`. This skill is the map; the repo is the territory.

## 1. Directory map

| Path | What lives there |
|---|---|
| `openair1/PHY/` | PHY: coding (LDPC/polar), modulation, channel estimation, transport channels |
| `openair1/SIMULATION/NR_PHY/` | PHY unit simulators: `dlsim`, `ulsim`, `pbchsim`, `prachsim`, `pucchsim`, `dlschsim`, `ulschsim` |
| `openair2/LAYER2/NR_MAC_gNB/` | gNB MAC and the DL/UL schedulers; `nr_radio_config.c` builds the RRC config |
| `openair2/LAYER2/NR_MAC_UE/` | nrUE MAC, DCI handling, DL assignment processing |
| `openair2/LAYER2/NR_MAC_COMMON/` | shared MAC structures and helpers used by both sides |
| `openair2/LAYER2/nr_rlc/` | NR RLC (`nr_rlc_oai_api.[ch]` is the layer boundary) |
| `openair2/LAYER2/nr_pdcp/` | NR PDCP (`nr_pdcp_oai_api.[ch]` is the layer boundary) |
| `openair2/RRC/NR/` | gNB RRC: `rrc_gNB*.c`, `nr_rrc_defs.h`, `mac_rrc_dl*.c` (direct vs F1AP dispatch) |
| `openair2/RRC/NR_UE/` | nrUE RRC (`rrc_UE.c`) |
| `openair2/F1AP/` | F1 between CU and DU |
| `openair2/E1AP/` | E1 between CU-CP and CU-UP |
| `openair3/NGAP/` | NGAP towards the AMF |
| `openair3/ocp-gtpu/` | GTP-U user plane (`gtp_itf.cpp`) |
| `openair3/NAS/` | NAS |
| `radio/` | radio drivers: `rfsimulator/`, `USRP/`, `zmq/`, `vrtsim/` |
| `fronthaul/` | native 7.2x fronthaul split |
| `executables/` | `main()` for gNB, nrUE, CU, DU |
| `ci-scripts/` | the real CI harness: `run_locally.sh`, `xml_files/*.xml`, `conf_files/*.yaml` |
| `cmake_targets/` | `build_oai` wrapper and build plumbing |
| `doc/` | build, style, tutorials (`NR_SA_Tutorial_OAI_CN5G.md`, `handover-tutorial.md`, …) |

## 2. ASN.1 — which spec version the code actually speaks

**This decides which spec version to cite and which IE names exist.** Each protocol
pins its grammar in its own `MESSAGES/CMakeLists.txt`; `asn1c` generates the C from it
at build time (`run_asn1c(...)`, prefix `NR_`, `-gen-UPER -gen-APER`).

| Protocol | Spec | Version compiled | Pin site | Grammar file |
|---|---|---|---|---|
| NR RRC | TS 38.331 | **V17.3.0** | `openair2/RRC/NR/MESSAGES/CMakeLists.txt` → `set(NR_RRC_VERSION 17 3 0)` | `ASN.1/nr-rrc-17.3.0.asn1` |
| F1AP | TS 38.473 | **V17.0.0** | `openair2/F1AP/MESSAGES/CMakeLists.txt` → `set(F1AP_VERSION 17 0 0)` | `ASN1/f1ap-17.0.0.asn1` |
| NGAP | TS 38.413 | **V17.10.0** | `openair3/NGAP/MESSAGES/CMakeLists.txt` → `set(NGAP_VERSION 17 10 0)` | `ASN1/ngap-17.10.0.asn1` |
| E1AP | TS 37.483 | **V17.0.0** | `openair2/E1AP/MESSAGES/CMakeLists.txt` → `set(E1AP_VERSION 17 0 0)` | `ASN.1/e1ap-17.0.0.asn1` |

`specs/manifest.yaml` in the toolkit pins 38.331, 38.473 and 38.413 to exactly these
versions for that reason. **Re-check the `set(..._VERSION ...)` lines at the start of
every task** — a fork may have bumped one (this fork bumped NGAP and F1AP to Rel-17 in
commits `2a9ebe4a6f` and `26b9e73e67`).

If a feature needs an IE that only exists in a newer release, that is a grammar upgrade,
not a code change: say so in the plan and stop — it touches every generated file.

## 3. Build

Prefer plain cmake over the `build_oai` wrapper (`AGENTS.md` says so):

```bash
# once, on a fresh machine — installs system dependencies (needs sudo)
./cmake_targets/build_oai -I

mkdir -p build && cd build
cmake .. -GNinja
ninja                                   # everything
ninja nr-softmodem nr-uesoftmodem       # just gNB + nrUE
ninja nr-cuup                           # CU-UP
```

- **rfsimulator** builds as part of the default target (`radio/rfsimulator`); no separate
  build variant is needed. Run with `--rfsim`.
- **Fastest incremental rebuild:** keep the `build/` directory and run `ninja <target>`.
  Never delete `build/` between fix cycles — the ASN.1 regeneration alone is minutes.
- **Realistic in a cloud VM:** the cmake+ninja build (T0) is fine on 4+ cores; budget
  20–40 min cold, seconds to a couple of minutes incremental. `build_oai -I` needs sudo
  and network — run it once at the start, and report it as BLOCKED if sudo is unavailable.
- `asn1c` must be present; if not, configure with `-DAUTO_DOWNLOAD_ASN1C=ON` (it clones
  `github.com/mouse07410/asn1c` and builds it — adds several minutes).

## 4. Unit tests (ctest)

Tests live in `tests/` directories next to the code. They build with the normal target
and are registered with `add_test(...)`. There are ~45 such directories; the ones that
matter most for RAN feature work:

| Area | Test directory |
|---|---|
| gNB/UE MAC common | `openair2/LAYER2/NR_MAC_COMMON/tests/` |
| nrUE MAC | `openair2/LAYER2/NR_MAC_UE/tests/` |
| RLC / PDCP | `openair2/LAYER2/nr_rlc/tests/`, `openair2/LAYER2/nr_pdcp/tests/` |
| RRC and RRC messages | `openair2/RRC/NR/tests/`, `openair2/RRC/NR/MESSAGES/tests/` |
| F1AP / E1AP / XNAP / NGAP | `openair2/F1AP/tests/`, `openair2/E1AP/tests/`, `openair2/XNAP/tests/`, `openair3/NGAP/tests/` |
| GTP-U | `openair3/ocp-gtpu/tests/` |
| NR-UP | `openair2/NRUP/tests/` |
| config framework | `common/config/tests/`, `common/config/yaml/tests/` |
| PHY | `openair1/PHY/INIT/tests/`, `openair1/PHY/TOOLS/tests/`, `openair1/PHY/MODULATION/tests/` |

Running them, from `build/`:

```bash
ctest -E '^physim\.|^benchmark_'      # the functional unit tests — this is T1
ctest -R f1ap_lib_test                # one test
ctest -R '^benchmark_'                # perf benchmarks; only for perf-sensitive changes
ctest -L quick_physim                 # fast pass over the physim executables (< 3 min)
ctest -R '^physim\.'                  # full physim; needs -DENABLE_PHYSIM_TESTS=ON
```

> `ENABLE_PHYSIM_TESTS=ON` is required for `physim.*` to be registered at all. The
> executables build either way, so **0 matched tests means the flag is missing** —
> reconfigure and rerun; never record 0 tests as a pass.

**Adding a test** — follow `openair2/F1AP/tests/` as the pattern: a `tests/` directory
beside the code, a `CMakeLists.txt` with an executable plus `add_test(NAME x COMMAND x)`,
and `add_subdirectory(tests)` from the parent. From `AGENTS.md`: an equivalence or
regression test must call the real production functions, not re-derive the expected
value independently — a self-consistent but wrong test passes for years.

## 5. Test tiers (T0–T4)

| Tier | What | Command | Cloud VM |
|---|---|---|---|
| **T0** build | gNB, nrUE, CU-UP as affected | `cd build && cmake .. -GNinja && ninja nr-softmodem nr-uesoftmodem` | CAN RUN |
| **T1** unit | the ctest functional suite | `ctest -E '^physim\.\|^benchmark_'` | CAN RUN |
| **T2** component, no RF | PHY/MAC unit simulators | `ctest -L quick_physim`, or run `nr_dlsim`/`nr_ulsim`/`nr_pbchsim` directly from `build/` | CAN RUN (CPU-bound; the full physim set is slow) |
| **T3** container E2E (**opt-in**) | rfsimulator gNB+nrUE against a core, via the CI harness | build the images, then `cd ci-scripts && ./run_locally.sh xml_files/container_5g_rfsim.xml` | needs docker + `/dev/net/tun` + ≥8 GB; **only with `E2E` in the task** |
| **T4** testbed / RF | USRP, lab hosts, the `frq-adsat-phine` testbed | — | NEVER in the cloud |

T3 image build (from `AGENTS.md` — build in this order, and **rebuild after every code
change**: Docker layer caching will otherwise serve a stale binary from the final stage):

```bash
docker build . -f docker/Dockerfile.base.ubuntu    -t ran-base
docker build . -f docker/Dockerfile.build.ubuntu   -t ran-build
docker build . -f docker/Dockerfile.gNB.ubuntu     -t oai-gnb
docker build . -f docker/Dockerfile.nrUE.ubuntu    -t oai-nr-ue
docker build . -f docker/Dockerfile.nr-cuup.ubuntu -t oai-nr-cuup
```

Relevant `ci-scripts/xml_files/` testcases: `container_5g_rfsim.xml` (baseline SA),
`container_5g_f1_rfsim.xml` (CU/DU split), `container_5g_e1_rfsim.xml` (CU-CP/CU-UP),
`container_5g_rfsim_multiue.xml`, `container_5g_rfsim_ntn_leo.xml`.
`container_4g_rfsim_mbms.xml` and `container_4g_rfsim_fembms.xml` exist but are **LTE**
eMBMS, not NR MBS — do not treat them as NR MBS coverage.

Manual rfsim run without containers (useful for a quick look; needs sudo for the TUN):

```bash
cd build
sudo ./nr-softmodem -O ../ci-scripts/conf_files/gnb.sa.band78.106prb.rfsim.yaml -E --rfsim
sudo ./nr-uesoftmodem -O ../ci-scripts/conf_files/nrue.uicc.yaml -E --rfsim -r 106 --numerology 1 -C 3319680000
```

**What CI really runs** is `ci-scripts/` driven from `.github/workflows/jenkins-dispatch.yml`
→ Jenkins. `ci-scripts/run_locally.sh <xml>` is the same harness, locally. When in doubt
about how a test is "supposed" to run, read the XML testcase, not the tutorial.

## 6. Conventions

- **Formatting:** `.clang-format` at the repo root. 2-space indent, no tabs, 132-column
  limit. Format only the lines you touched: `git clang-format <base-sha>`.
  `ci-scripts/checkCodingFormattingRules.sh` is what CI runs.
- **Style** (`doc/code-style-contrib.md`): strong types (`c16_t`, not `uint32_t`, for IQ
  samples). `AssertFatal()` / `DevAssert()` are for invariants — **not** error handling.
- **Logging:** `LOG_E/W/I/D(COMPONENT, ...)`. Per-component levels come from the config
  (`nr_mac_log_level`, `nr_phy_dci_log_level`, …). Remember that a testbed shipping
  `error` as the default will silently hide `info`-level traces.
- **Config:** parameters are declared in `paramdef_t` arrays near their component and read
  through the common config framework (`common/config/`); YAML and `.conf` are both
  supported. A new key needs a default that preserves existing behavior.
- **Commits:** read `git log` on the branch you are on. The prevailing style here is a
  short area prefix and an imperative sentence, e.g.
  `MBS: schedule and fill a group transmission from the MRB`,
  `NGAP: update the ASN.1 schema to Rel-17 (TS 38.413 v17.10.0)`,
  `F1AP: carry a broadcast session to the DU`. Put spec clause references in the body.
- `AGENTS.md`: no WIP/TODO markers and no leftover debug logging in finished code.
- `AGENTS.md`: never push, never open PRs — which is also rule 1 of this toolkit.

## 7. MBS state in this fork

Upstream `develop` has essentially **no NR MBS**: the `*mbsfn*` and `m2ap`/`m3ap` files
under `openair1/PHY/LTE_*` and `openair3/` are **LTE eMBMS**, a different feature.

The `mbs-phase-a` branch of the private fork carries the NR MBS work (25 commits above
`upstream/develop`, 74 files). Read `MBS-REBASE-NOTES.md` first — it records what is
implemented, what was verified on air, and what is explicitly unmeasured.

Where the NR MBS code lives:

| File | Role |
|---|---|
| `openair2/LAYER2/NR_MAC_gNB/nr_mac_mbs.[ch]` | gNB-side MBS session state and the PTM transmit path |
| `openair2/LAYER2/NR_MAC_UE/nr_ue_mbs.[ch]` | nrUE-side group-RNTI monitoring and DL assignment acceptance |
| `openair2/F1AP/f1ap_mbs.[ch]` | carrying a broadcast session over F1 to the DU |
| `openair3/NGAP/ngap_gNB_handlers.c` | `BroadcastSessionSetup` from the AMF |
| `openair3/ocp-gtpu/gtp_itf.cpp` | source-specific multicast group reception |
| `openair2/LAYER2/NR_MAC_gNB/nr_radio_config.c` | SIB20 / group-RNTI configuration |

Implemented as of `26531a1f64`: PTM transmit on a group RNTI, UE reception of it, MCS
capped to the weakest group member, HARQ feedback suppressed for group transmissions,
SIB20 broadcast with the G-RNTI, NGAP `BroadcastSessionSetup`, E1/F1 carriage of the
session, and a broadcast MRB terminating at the CU-UP.

**Gaps to expect** (verify with `grep`, do not assume): MCCH and its change notification,
MTCH scheduling driven by an MCCH-signalled configuration, MBS multicast (as opposed to
broadcast) with G-CS-RNTI, multicast DRX (`drx-*PTM`), and the UE-side RRC reception of
`MBS-BroadcastConfiguration`.

Useful searches when starting an MBS task:

```bash
git grep -ni "mbs\|mcch\|mtch\|g-rnti\|g_rnti\|tmgi\|sib20\|multicast" -- openair2 openair3
git log --oneline upstream/develop..HEAD          # what this branch already did
python3 scripts/spec_lookup.py grep 38.321 "G-RNTI"
python3 scripts/spec_lookup.py asn1 38.331 --list --filter MBS
```

## 8. Working on a private fork

The fork keeps three remotes: `origin` (GitHub private), `private`, and `upstream`.
Use `upstream/develop` as the comparison base for `git log` and `git diff --stat`, and
the branch named in the task (`mbs-phase-a`) as the base commit for the delivery.
A fork's own `AGENTS.md`, `docs/` and CI files always win over this skill.
