---
name: open5gs-mbs
description: Reference knowledge for the 5G-MAG MBS-enabled Open5GS core (github.com/5G-MAG/open5gs, branches 5mbs and 5mbs-development) — that MB-SMF and MB-UPF are the ordinary smfd/upfd daemons with MBS built in rather than separate NFs, where MBS session handling, Nmbsmf SBI, N4mb/PFCP and the multicast router live, the meson/ninja build, the test suites and the fact that none of them cover MBS, how it is deployed end-to-end with an OAI gNB, and the ABI divergence from upstream Open5GS that forces one set of binaries. Load this before changing anything in the 5G-MAG Open5GS fork or planning an MBS core change.
---

# 5G-MAG MBS-enabled Open5GS (`5G-MAG/open5gs`)

Verified on 2026-11-05 against commit `05adfc4f` (`v1.0.0-5mbs-v2.7.2-o5gs-15-g05adfc4f`)
— the commit the `frq-adsat-phine` testbed pins as its `5g-mag-open5gs` submodule.

- Repo: `https://github.com/5G-MAG/open5gs` — a fork of `open5gs/open5gs`.
- MBS branches: **`5mbs`** (release) and **`5mbs-development`**. `main` tracks upstream
  and has no MBS.
- Project docs: <https://5g-mag.github.io/Getting-Started/pages/5g-multicast-broadcast-services/>
- The MBS work was funded through the EU 6G-SANDBOX project (per the repo README).

## 1. Which version to work on

This is a real decision, and the task must settle it. Three cases:

| Situation | Base to use |
|---|---|
| Reproducing or extending **the testbed** | the commit the testbed's `5g-mag-open5gs` submodule pins — read it with `git -C <testbed> submodule status` |
| A **core fix meant to go upstream** to 5G-MAG | `5mbs-development` (or `5mbs` if the task says so) — a patch against an old pin is not upstreamable |
| **Checking whether a newer 5G-MAG release still works** with the testbed | the tag or branch tip named in the task |

Default to the **submodule pin** when the task does not say, and raise the choice as a
question in Phase 2 — it changes what the patch applies to.

## 2. There is no separate MB-SMF or MB-UPF binary

This is the single most important thing about this fork. From the repo README:

> Network functions relevant to MBS include NRF (`open5gs-nrfd`), SCP (`open5gs-scpd`),
> AMF (`open5gs-amfd`), **MB-SMF (`open5gs-smfd`)** and **MB-UPF (`open5gs-upfd`)**.

MBS is implemented *inside* the existing daemons, not alongside them. `src/` contains the
same NF directories as upstream (`amf bsf nrf nssf pcf scp smf upf …`) with MBS code added.
Do not go looking for an `mbsmf/` directory; there isn't one.

## 3. Where the MBS code lives

| Path | Role |
|---|---|
| `src/smf/nmbsmf-handler.[ch]` | **Nmbsmf** service (TS 29.532): MBS session create/update/release from the MBSF/AF |
| `src/smf/n4mb-build.[ch]`, `src/smf/n4mb-handler.[ch]` | **N4mb** — the MB-SMF side of PFCP towards the MB-UPF |
| `src/smf/context.[ch]`, `src/smf/smf-sm.c` | MBS session context and the state machine entry points |
| `src/smf/namf-build.c`, `src/smf/namf-handler.c`, `src/smf/ngap-build.c` | towards the AMF, and the NGAP transfer containers for MBS distribution |
| `src/smf/sbi-path.c`, `src/smf/pfcp-path.c` | request routing for the above |
| `src/upf/n4mb-build.[ch]`, `src/upf/n4mb-handler.[ch]` | **MB-UPF** side of N4mb |
| `src/upf/multicastrouter-path.h`, `lib/multicastrouter/multicastrouter.[ch]` | programming the Linux multicast forwarding cache for the downstream multicast |
| `src/upf/rule-match.c`, `src/upf/gtp-path.h`, `src/upf/init.c` | matching and forwarding MBS traffic on the user plane |
| `src/amf/namf-handler.c`, `src/amf/ngap-build.c`, `src/amf/amf-sm.c`, `src/amf/sbi-path.c` | AMF side: MBS distribution setup towards the NG-RAN |
| `lib/pfcp/types.[ch]`, `lib/pfcp/build.c`, `lib/pfcp/message.h` | the MBS-related PFCP IEs (TS 29.244) |
| `lib/asn1c/ngap/NGAP_MBS-*.{c,h}` | generated NGAP MBS IEs (TS 38.413): `MBS-DistributionSetupRequestTransfer`, `MBS-QoSFlowsToBeSetupItem`, `MBS-AreaSessionID`, … |
| `lib/sbi/openapi/model/mbs_*.{c,h}` | generated OpenAPI models for the MBS SBI data types |

Start a search with:

```bash
git grep -lni "mbs\|tmgi\|n4mb\|multicast" -- src lib | grep -v "lib/asn1c\|lib/sbi/openapi"
```

Excluding `lib/asn1c` and `lib/sbi/openapi` matters — they are generated and would drown
the result.

## 4. Configuration

MBS keys are in the shipped configs:

- `configs/open5gs/upf.yaml.in` — an `mbs:` section: the UDP tunnel port scheme for MBS
  (ephemeral / a single fixed port for testing / a range / an explicit pool), and a
  `multicast_router:` block (`activate`, `input_interface`) that drives the Linux
  Multicast Forwarding Cache so multicast routes are created automatically. The
  `input_interface` is the interface that receives multicast from the AF.
- `configs/open5gs/smf.yaml.in`, `amf.yaml.in`, `pcf.yaml.in` — the rest.

Any new key needs a default that preserves current behavior, and the testbed's own
`container/open5gs/core.yaml` has to be updated too, or the deployment will not see it.

## 5. Build

Standard Open5GS meson/ninja. No special MBS flag — the MBS code is compiled in on the
`5mbs*` branches.

```bash
git clone --recurse-submodules -b 5mbs https://github.com/5G-MAG/open5gs.git open5gs-mbs
cd open5gs-mbs
meson setup --prefix=$PWD/install build
ninja -C build
ninja -C build install
export LD_LIBRARY_PATH="$PWD/install/lib64:$PWD/install/lib"
```

Incremental rebuild after a change is just `ninja -C build` — keep the build directory.
Dependencies are the upstream Open5GS set (meson, ninja, libgnutls, libgcrypt, libsctp,
libyaml, libmicrohttpd, libnghttp2, mongodb …); `meson setup` names what is missing.

In the testbed, the same build is wrapped:

```bash
./core/build.sh --install-deps --skip-tests      # first time
./core/build.sh --skip-tests --only 5g-mag-open5gs
MAG_OPEN5GS_DIR=/path/to/fork ./core/build.sh --skip-tests
```

## 6. Tests

The upstream Open5GS test tree is present and runs with meson:

```bash
ninja -C build                 # tests build with the project
meson test -C build -v         # everything
meson test -C build --suite unit -v
```

| Suite | What |
|---|---|
| `tests/unit/` | message encode/decode: `ngap-message-test.c`, `nas-message-test.c`, `sbi-message-test.c`, `gtp-message-test.c`, `proto-message-test.c`, `s1ap-message-test.c`, `security-test.c` |
| `tests/core/`, `tests/crypt/`, `tests/sctp/` | library-level |
| `tests/registration/`, `attach/`, `vonr/`, `volte/`, `slice/`, `handover/`, `transfer/`, `non3gpp/`, `csfb/`, `310014/` | scenario tests that drive the NFs through simulated procedures |
| `tests/af/`, `tests/app/`, `tests/common/` | harness |

Tests are registered with `test('unit', …, suite: 'unit')` in each `meson.build`
(`is_parallel: false` — they bind real ports).

> **There are no MBS tests.** `grep -rli "mbs\|tmgi" tests/` returns nothing at the pinned
> commit. Any MBS change therefore has **no existing unit test to extend**. Say this
> explicitly in the plan: either propose a new test under `tests/unit/` following
> `sbi-message-test.c` / `ngap-message-test.c` (the realistic target is encode/decode of
> the Nmbsmf models and the N4mb/NGAP MBS IEs — pure functions, no NF startup needed), or
> record it in OPEN_ISSUES.md as untested. Do not add a new framework.

## 7. End-to-end with an OAI gNB (T3 / T4)

The deployment lives in the `frq-adsat-phine` testbed, not in this repo. Shape of it:

- `compose.yaml` services: `mongo`, `core` (all NFs in **one** container), `core_ui`,
  `gnb1`, `ue1`…`ue5`, on networks `net_5g_core` and `net_5g_rf`.
- Images: `frq_open5gs_core`, `frq_oai_gnb`, `frq_oai_ue`, all built from the repo root
  so the build context spans every component directory.
- The AF/AS role is simulated from inside the `core` container (there is no separate AF),
  so `AF_IP` resolves to that container's own `eth0`, and `smcroutectl` / `smcrouted`
  work on `eth0`.
- `./scripts/test-mbs.sh` runs the full flow: resolve the AF IP, create the broadcast
  session, add the multicast forwarding entry, inject a multicast packet
  (`--multicast 239.0.0.26` to override the group).
- `tests/mbs-tn.md` is the runbook/acceptance test (`runme run --all --filename tests/mbs-tn.md`).
- `docs/mbs-performance-testing.md` covers throughput, jitter, loss and latency.

Needs: Docker + compose, `/dev/net/tun`, multicast on the bridge, and for the
PTM-to-PTP eBPF program a recent kernel and privileges. In a cloud VM this is T3 at best
and usually T4 — check `scripts/probe_env.sh` before promising it.

## 8. Divergence from upstream Open5GS — the ABI trap

**You cannot mix upstream Open5GS daemons with 5G-MAG shared libraries in one runtime.**
The testbed's `core/README.md` documents the failure in detail; the short version:

- The fork makes ABI-breaking changes in shared libraries. For example
  `libogsdiameter-common.so` dropped `ogs_diam_logger_self` and
  `ogs_diam_logger_stats_start` in favour of `ogs_diam_stats_self`.
- Because every daemon in the testbed's single container shares one `LD_LIBRARY_PATH`,
  an upstream binary that needs the old symbols dies before `main()`:
  `./open5gs-hssd: symbol lookup error: … undefined symbol: ogs_diam_logger_self`.
- The testbed's resolution: **use the 5G-MAG binaries for all daemons**, not just the
  MBS ones. The repo keeps an `open5gs` submodule as well, but the image is built from
  the fork throughout.

Consequences for any change here:

- Touching a shared library in `lib/` affects every daemon — that is "shared
  infrastructure beyond the plan" and a reason to stop and ask.
- Never propose "just use the upstream NF for X" as a fix.
- When the task is a fix destined for upstream 5G-MAG, base it on `5mbs-development`,
  not on the testbed's pin (see §1).

## 9. Conventions

- **Language:** C, upstream Open5GS style — 4-space indent, `ogs_` prefixes for the
  library, `smf_`/`upf_`/`amf_` for NF-local symbols.
- **Logging:** `ogs_info()`, `ogs_error()`, `ogs_debug()`, `ogs_fatal()`.
- **Structure:** NFs are state machines (`*-sm.c`) fed by events (`event.h`); a new
  procedure usually means a new event plus handlers in `*-handler.c` and builders in
  `*-build.c`. Follow the `n4mb-build.c` / `n4mb-handler.c` pairing.
- **Licence:** AGPL-3.0. 5G-MAG-authored files carry a `5G-MAG Reference Tools` header
  (e.g. `src/smf/nmbsmf-handler.c`, © iTEAM UPV). Keep the header style of the file you
  are editing; new 5G-MAG files take the 5G-MAG header.
- **Commits:** read `git log` on the branch. Upstream Open5GS style is a plain imperative
  sentence (`Check datagram socket was actually created when finding the MTU`).

## 10. Specs that matter here

| TS | What |
|---|---|
| 23.247 | 5G MBS architecture — the stage 2 that defines MB-SMF, MB-UPF, MBSF |
| 29.532 | Nmbsmf MBS session management — the SBI this fork implements in `src/smf/nmbsmf-*` |
| 29.244 | PFCP, including the MBS IEs used over N4mb |
| 38.413 | NGAP, including the `MBS-Distribution*` transfer containers |
| 23.501 / 23.502 | the surrounding system architecture and procedures |

All are in `specs/manifest.yaml` under the `mbs` tag:
`python3 scripts/ensure_specs.py --tags mbs`.
