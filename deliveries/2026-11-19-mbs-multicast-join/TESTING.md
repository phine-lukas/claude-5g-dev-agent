# Testing — 2026-11-19-mbs-multicast-join

## Tier table

| Tier | What | Command | Result |
|---|---|---|---|
| T0 | core build | `meson setup --prefix=$PWD/install build && ninja -C build` | **PASSED** — no errors, no new warnings |
| T0 | RAN build | `cmake .. -GNinja -DENABLE_TESTS=ON && ninja nr-softmodem nr-uesoftmodem` | **PASSED** — no errors, no new warnings |
| T1 | core unit | `./build/tests/unit/smf-mbs` | **PASSED** — 2103 checks, 0 failed (2054 on the base commit, so 49 new) |
| T1 | core unit suite | `meson test -C build --suite unit` | **PASSED with pre-existing failures** — `crypt`, `unit`, `amf-mbs`, `amf-mbs-context` pass; `core` and `smf-mbs` die under meson's `MALLOC_PERTURB_`, on the base commit too (see below) |
| T1 | RAN unit | `ctest -R 'nas_lib_test\|ngap_lib_test'` | **PASSED** — 2/2 |
| T1 | RAN suite | `ctest -E '^physim\.\|^benchmark_'` | **79/87 passed**; the 8 failures are environmental or pre-existing, none in what changed (see below) |
| T1 | the runbook's decoder | `python3 tests/tools/test_decode_ngap.py` | **PASSED** — 9 checks, 0 failed |
| T2 | core scenario suites | — | n/a: none of them cover MBS |
| T3 | containers | — | **SKIPPED: this VM has no docker daemon** (`probe_env.sh`: "daemon reachable no") |
| T4 | testbed | `runme run --all --filename tests/mbs-tn.md` | **LOCAL ONLY — this is the important one, see below** |

### The pre-existing failures, and how that was established

**`open5gs`** — `meson test` sets `MALLOC_PERTURB_`, under which `core` and
`smf-mbs` crash. Established by stashing this change, rebuilding the base
commit's binary and running it the same way:

```bash
cd open5gs && git stash && ninja -C build
MALLOC_PERTURB_=140 ./build/tests/unit/smf-mbs   # SIGSEGV on 19149433f too
git stash pop
```

Run without `MALLOC_PERTURB_` the suite reports 0 failures, which is how the
2054 / 2103 numbers above were taken.

**`openairinterface5g`** — the 8 ctest failures:

| Test | Why |
|---|---|
| `test_nr_mac_gnb_NOT_BUILT` | **pre-existing link failure**: `undefined reference to e1_bc_bearer_context_release` from `openair2/RRC/NR/cucp_cuup_direct.c`. Reproduced on `a29db1e91` with this change stashed. |
| `test_thread-pool` | environmental: `pthread_create()` returns `EINVAL` in this sandbox |
| `nr_cuup_functional_test`, `nr_dlbench_um_functional_test`, `nr_dlbench_am_functional_test` | environmental: `SCTP Socket creation failed: Protocol not supported` — `probe_env.sh` reports "SCTP sockets: no" |
| `test_rfsimulator`, `test_vrtsim`, `test_vrtsim_cirdb` | environmental: the rfsimulator's `trx_start_func()` cannot listen here |

## What has to be run locally

### 1. Build the images

Tag them something of your own — **do not overwrite `:mbs`**, which is the
known-good broadcast baseline.

```bash
cd ~/Projects/projects/frq-adsat-phine
```

```bash
MBS_CORE_IMAGE=open5gs_core:mc-dev ./core/build.sh
```

```bash
MBS_GNB_IMAGE=oai-gnb:mc-dev ./gnb/build.sh
```

```bash
MBS_UE_IMAGE=oai-nr-ue:mc-dev ./ue/build.sh
```

(Check `core/README.md` and the OAI broadcast tutorial for the exact invocation
each build script wants; the point is the tag.)

**Rebuild the images after every code change.** Docker layer caching will
otherwise serve a stale binary from the final stage and the run means nothing.

### 2. Run the whole runbook

This is the real acceptance of this delivery: the broadcast checks must still be
green, and MBS-MC-02 must now pass.

```bash
MBS_CORE_IMAGE=open5gs_core:mc-dev MBS_GNB_IMAGE=oai-gnb:mc-dev MBS_UE_IMAGE=oai-nr-ue:mc-dev runme run --all --filename tests/mbs-tn.md
```

Expected tally at the end:

```
  Broadcast
    MBS-BC-07    passed
    MBS-BC-00    passed
    MBS-BC-04    passed
    MBS-BC-05    not implemented
    MBS-BC-03    passed
    MBS-BC-02    passed
    MBS-BC-06    not implemented
    MBS-BC-08    passed
    MBS-BC-01    not implemented
  Multicast
    MBS-MC-02         passed
    MBS-MC-02-radio   not implemented
    MBS-MC-04    not implemented
    MBS-MC-03    not implemented
    MBS-MC-01    not implemented
```

A broadcast check turning red is a regression from this delivery and matters
more than MBS-MC-02 passing.

### 3. Just MBS-MC-02, while iterating

The runbook's blocks are named, so a single section can be replayed once Setup A
is up:

```bash
runme run --filename tests/mbs-tn.md mc02-capture-start mc02-session mc02-tmgi mc02-join mc02-wait mc02-verify
```

What it should print:

```
the core allocated TMGI <12 hex chars> (service id <6 hex chars>)
ok: the AMF asked the gNB to activate TMGI <...>
ok: the gNB answered the activation successfully
UEs the core associated with the session: 1
2
UEs the gNB confirmed:                    1
2
ok: exactly two UEs were associated with the MBS session
ok: the gNB accepted both of them
ok: the gNB confirmed the same two UEs the core named
MBS-MC-02 passed (signalling; the radio part is below)
```

The two RAN UE NGAP IDs are whatever the gNB assigned; what matters is that
there are exactly two and that both lists hold the same two.

### 4. What to look at by hand, the first time

These are not assertions — the runbook deliberately does not depend on our own
log lines — but they are what to read when a step fails.

**The UE asked.** In `docker logs ue1`:

```
[NAS]   MBS: asked to join multicast session TMGI <tmgi> on PDU session 1
```

**The core accepted.** In `docker logs core`, from the SMF:

```
[smf] INFO: [<supi>:1] joined multicast MBS session TMGI <tmgi> (1 member(s))
```

and for ue2, `(2 member(s))`.

**The UE was told.** Back in `docker logs ue1`:

```
[NAS]   MBS: PDU session 1, multicast session TMGI <tmgi>: MBS join is accepted
```

A rejection prints the cause in brackets, e.g.
`MBS join is rejected (session context not found)` — which is what a TMGI the
core does not know gives.

**The gNB understood.** In `docker logs gnb`:

```
[NGAP]   [SCTP <n>] Multicast session activation: TMGI <tmgi> is active
[NR_RRC] UE <id>: PDU session 1 joined MBS session <tmgi>
```

**The capture itself**, which is what the check actually decides on:

```bash
python3 tests/tools/decode_ngap.py "$MBS_MC_N2DIR/n2.pcap" --summary
```

### 5. If it fails

| Symptom | Where to look first |
|---|---|
| no Multicast Session Activation (code 71) in the capture at all | the SMF never called the AMF: look for "Failed to send the Multicast Session Activation" in the core log, and for whether the AMF advertises `namf-mbs-comm` to the NRF |
| the activation is there but the gNB does not answer | the gNB dropped the procedure: check that the gNB image is the rebuilt one (`docker exec gnb nr-softmodem --version` or the build date), since the old binary has no handler for code 71 |
| no per-UE modify carrying the TMGI | the join never reached the SMF, or was rejected: check the UE log for "MBS join is rejected" and the core log for "no multicast session with that TMGI" |
| the TMGI in the capture differs from the one `--mbs-join` was given | the TMGI assembly in the `mc02-tmgi` block; the PLMN nibble order of TS 24.008 is the thing to suspect |
| exactly one UE instead of two | ue2 did not finish attaching before the capture stopped — raise the `sleep 8` in `mc02-wait` |
| ue3 appears with a TMGI | the core is sending the association to every UE rather than to the ones that joined; that is the bug this check exists to catch |

### 6. Beyond the runbook

Things worth trying by hand that no check covers yet:

- **a join of a TMGI nothing has**: start a UE with
  `--mbs-join 000000999f07`; expect
  `MBS join is rejected (session context not found)` in its log and **no** MBS
  procedure for it in the capture.
- **two UEs joining the same session**: already covered, but watch that the
  activation is sent **once** — `ran_activated` should keep the second join
  from re-activating.
- **releasing the UE's PDU session** while it is a member: the membership should
  be dropped (`smf_mbs_member_remove_by_sess()`); nothing checks this.
