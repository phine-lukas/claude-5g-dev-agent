# Night report — multicast join, UE to gNB over the core

2026-11-19, overnight. Delivery `deliveries/2026-11-19-mbs-multicast-join`.

## Read this first

**The signalling path is built and compiles; nothing was run end to end.** This
VM has no docker daemon (`probe_env.sh`: "daemon reachable no", "can run a
container no"), so no image could be built, no testbed could come up, and
MBS-MC-02 has never been executed against the stack. Everything below T3 was run
and passed. The first thing to do this morning is build the images and run the
runbook — TESTING.md has the commands.

I could not verify the broadcast checks are still green, for the same reason. I
believe they are: nothing in the broadcast path was touched, and the only shared
file either side of it is `decode_ngap.py`, whose existing behaviour is covered
by the new self-test. But "I believe" is not "I ran it".

## What works, and how far that was shown

| | Built | Compiles | Unit-tested | Run on the testbed |
|---|---|---|---|---|
| UE sends the join (NAS, `--mbs-join`) | yes | yes | yes | **no** |
| UE reads the answer and logs it | yes | yes | yes | **no** |
| Core accepts the join, answers the UE | yes | yes | yes | **no** |
| Core tells the gNB per UE (N2 modify + MBS list) | yes | yes | yes | **no** |
| Core asks the AMF to activate the session | yes | yes | yes (the transfer) | **no** |
| gNB decodes and answers the modify | yes | yes | — | **no** |
| gNB decodes and answers the activation | yes | yes | — | **no** |
| gNB keeps the membership in the CU | yes | yes | — | **no** |
| MBS-MC-02 check | written | — | its decoder is tested | **no** |
| Multicast MRB / radio | **no — out of scope tonight** | | | |
| Distribution Setup | **no — see below** | | | |

### Test results actually obtained

```
open5gs   meson setup + ninja                         PASSED, no new warnings
open5gs   ./build/tests/unit/smf-mbs                   2103 checks, 0 failed
                                                       (2054 on the base commit: 49 new)
open5gs   meson test --suite unit                      4 of 6 pass; `core` and `smf-mbs`
                                                       crash under MALLOC_PERTURB_ on the
                                                       BASE COMMIT too (verified by stashing)
OAI       cmake -DENABLE_TESTS=ON + ninja              PASSED, no new warnings
OAI       ctest -R 'nas_lib_test|ngap_lib_test'        2/2 passed
OAI       ctest -E '^physim\.|^benchmark_'             79/87; the 8 failures are
                                                       environmental (no SCTP, no threads,
                                                       no listening sockets) or pre-existing
                                                       (test_nr_mac_gnb does not link on the
                                                       base commit either — verified)
testbed   python3 tests/tools/test_decode_ngap.py      9 checks, 0 failed
testbed   runme run --all --filename tests/mbs-tn.md   NOT RUN — no docker
```

## Branches, commits, images

Branches are **local only and were not pushed** — CLAUDE.md rule 1. The work is
delivered as patches in `deliveries/2026-11-19-mbs-multicast-join/patches/`,
verified to apply cleanly on their base commits in a throwaway worktree.

| Repo | Base | Local branch | Commits |
|---|---|---|---|
| `5G-MAG/open5gs` | `5mbs-development` @ `19149433f` | `agent/2026-11-19-mbs-multicast-join` | `3d4a155f` smf: handle the NAS join of a UE into a multicast MBS session |
| `phinetech/openairinterface5g` | `mbs-ptm` @ `a29db1e91` | same | `ebe4e243e` NGAP: decode and answer the multicast MBS procedures of a join · `96f6cfcf5` RRC: keep a UE's multicast MBS membership in the CU · `205c3a07c` NAS: let the nrUE join a multicast MBS session |
| `phinetech/frq-adsat-phine` | `tests/acceptance-runbooks` @ `b6403ecd6` | same | `00ac767` Check the multicast join over N2 in MBS-MC-02 |

**Image tags: none were built**, because there is no docker here. TESTING.md
tells you to build `:mc-dev` tags and leaves `:mbs` alone, as the task asked.

**Submodule pointers in `frq-adsat-phine` are not bumped** — they can only move
once these commits exist in the target repos, which this delivery does not push.

## Stubbed or missing

### Distribution Setup — the one that matters

Not implemented on either side, and nothing fakes it. TS 38.413 V17.10.0 clause
8.18.1.2 makes it **gNB-initiated** ("The NG-RAN node initiates the procedure by
sending a DISTRIBUTION SETUP REQUEST message to the AMF", procedure code 69),
and the AMF answers with the shared NG-U TNL information — the (S,G) pair and
C-TEID the payload arrives on.

Exactly what is missing:

- **gNB**: the ASN.1 types compile; the dispatcher has `{0, 0, 0}` for code 69.
  Nothing sends the request, nothing handles the response or the failure.
- **AMF (5G-MAG)**: nothing at all. The OpenAPI model has
  `MBS_DIS_SETUP_REQ/RSP/FAIL` as `ngapIeType` values and no code uses them.
- **MB-SMF**: no Nmbsmf operation answers a Distribution Setup, and nothing
  allocates the shared NG-U transport for a *multicast* session. The broadcast
  equivalent exists (`MBS-SessionTNLInfo5GC`, `smf_mbs_dl_tunnel_t`).

It did not block the night's work because the task scoped the gNB to
understanding and acknowledging, which it does. It blocks *delivery*, so it is
the first thing the radio work needs. The broadcast path's
`decodeMBSSessionSetup()` in `openair3/NGAP/ngap_common.c` already takes the
same information out of a different message; that is where to start.

### Everything else that is absent

1. Multicast MRB, RRC reconfiguration to the UE, DCI 4_2 — out of scope tonight.
2. Leave and release (MBS-MC-03 / MBS-MC-04). The core *parses* a leave and
   refuses it with a log line rather than answering a false success; the UE has
   no way to ask for one.
3. Deactivation: `ran_activated` is set and never cleared, so a session that
   loses its last member stays active in the gNB. The AMF's deactivation builder
   exists and is still uncalled.
4. Joining by source-specific IP multicast address — the NAS container allows
   it, the MB-SMF indexes multicast sessions by TMGI, so it is warned about and
   skipped.

## Decisions I took without asking, and why

1. **I did not stop for approval.** CLAUDE.md rule 4 and the skill's Phase 2
   require a plan and an explicit go. The task overrode that in its first line.
   The plan is written down in PLAN.md and DESIGN_NOTE.md instead, with every
   question it would have contained.
2. **The SMF and the MB-SMF are one process**, so clause 7.2.1.3 steps 2–3 (NRF
   discovery of the MB-SMF, `Nmbsmf_MBSSession_ContextStatusSubscribe`) are a
   lookup in this process's own context. The testbed runs one `open5gs-smfd` for
   both roles and the profile says so. Writing the SBI round trip would have been
   code with no caller in any deployment we have. It is behind one function,
   `find_multicast_session()`, named in a comment as the place to change.
3. **Authorisation accepts any UE** whose TMGI the MB-SMF knows, and rejects an
   unknown TMGI with "Session context not found". Clause 7.2.1.3 step 4 wants MBS
   subscription data from the UDM; the testbed's Mongo provisioning has none and
   inventing a schema is a bigger change than this task. One commented block to
   replace.
4. **No PFCP exchange for a join**, per clause 7.2.1.3 NOTE 8 — shared delivery
   needs no UPF interaction. This is why the join answers the UpdateSMContext
   stream directly instead of going through `smf_5gc_pfcp_send_*`.
5. **The gNB answers an MBS-only modify in a branch of its own.** The ordinary
   `rrc_gNB_process_NGAP_PDUSESSION_MODIFY_REQ()` path ends in
   `init_delayed_action()` and answers the AMF only once an RRC reconfiguration
   has completed. A join starts no reconfiguration — that is tomorrow — so going
   through it would have left the procedure unanswered and MBS-MC-02 red for a
   reason that had nothing to do with MBS. The branch triggers only when no QoS
   flow is added, modified or released.
6. **The N1 container reaches the UE by DL information transfer**, since there is
   no reconfiguration to attach it to. Clause 7.2.1.3 step 8 says "as part of the
   AN specific signalling exchange"; with no radio to configure, that is the
   exchange.
7. **No `associatedMBSQosFlowSetuporModifyRequestList`** in the N2 item. It is
   for 5GC Individual MBS traffic delivery, and step 6 says that with shared
   delivery the associated unicast QoS flow information "is not used to allocate
   the radio resource". There are no multicast QoS flows to map yet either.
8. **The test restarts ue1 and ue2 with `--mbs-join <tmgi>`** rather than using a
   telnet command, because the TMGI is only known once the session exists.
   `MBS_UE1_EXTRA`/`MBS_UE2_EXTRA`/`MBS_UE3_EXTRA` in the compose file carry it;
   they default to empty, so an existing run's command line is unchanged.
9. **MBS-MC-02 is split into a passing signalling check and a `NOTIMPL` radio
   section** rather than left as one stub or declared passed. The runbook's own
   convention is that a gap stays visible; asserting only what is true and naming
   what is not seemed better than either extreme. If you would rather it stayed a
   single NOTIMPL until the radio works, that is a one-block revert.
10. **`decode_ngap.py` reports the RAN UE NGAP ID.** Without it, nothing in a
    capture distinguishes ue1's procedures from ue3's, and "ue3 got nothing"
    could not be asserted at all.

## What I would do next

**In order:**

1. **Run the runbook.** Build `:mc-dev` images, `runme run --all --filename
   tests/mbs-tn.md`. Expect the broadcast checks green and MBS-MC-02 passing. If
   MBS-MC-02 fails, TESTING.md §5 has a symptom-to-cause table — I wrote it
   from the code paths, so it should point at the right file even though I never
   saw it fail.
2. **Distribution Setup**, gNB side first: send a DISTRIBUTION SETUP REQUEST once
   the first UE joins a session, and handle the response. Then the AMF relay and
   the MB-SMF's answer with the shared NG-U TNL information. Until this exists
   there is no tunnel for a multicast MRB to deliver into, so it gates everything
   below.
3. **The multicast MRB and the RRC reconfiguration**, reading the membership this
   delivery puts in `rrc_pdu_session_param_t.mbs_sessions`. The broadcast path's
   G-RNTI and MTCH handling is the template.
4. **Deactivation**, so a session whose last member leaves is turned off — the
   AMF builder is already there, and it is a small piece next to leave handling.

**If I had another night**, I would spend it on 2, because it is the only item
whose shape I am still unsure of: the gNB has to decide *when* to ask for the
tunnel, and clause 7.2.1.4 leaves that to the implementation.
