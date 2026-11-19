# Delivery 2026-11-19-mbs-multicast-join

Date: 2026-11-19 · Profile: `mbs-testbed` · Status: **partial — see below**

A UE can ask to join an MBS **multicast** session over NAS; the core accepts the
join, tells the gNB about it over N2 — per UE, and once for the session as a
whole — and the gNB decodes both messages and answers them correctly. Expect to
read: a new `src/smf/mbs-join.c` in the 5G-MAG core that parses the Requested
MBS container and answers with the Received one; the two N2 builders that were
missing (the MBS list inside a PDU Session Resource Modify, and the Multicast
Session Activation transfer the AMF's existing builder has been waiting for a
caller to supply); an NGAP handler and a response extension in the gNB; the CU
remembering which UE joined which session; and the nrUE's first PDU Session
Modification Request, behind `--mbs-join <tmgi>`.

**Partial, deliberately**: the radio half is out of scope and absent — no
multicast MRB, no RRC reconfiguration to the UE, no DCI 4_2. The shared NG-U
tunnel (Distribution Setup) is also missing on both sides; OPEN_ISSUES.md says
exactly what of it is missing and where to start. And **nothing was run end to
end** — this VM has no docker daemon — so MBS-MC-02 is written and its decoder
is tested, but the check itself has never run against the stack.

## Repos

| Repo | Role | Base branch | Base SHA | Patches |
|---|---|---|---|---|
| `open5gs` (5G-MAG) | target | `5mbs-development` | `19149433` | 1 |
| `openairinterface5g` (phinetech) | target | `mbs-ptm` | `a29db1e91` | 3 |
| `frq-adsat-phine` | test | `tests/acceptance-runbooks` | `b6403ec` | 1 |

Total: **5** patch(es).

## Test summary

| Tier | Result |
|---|---|
| T0 build | **PASSED** — core and RAN, no errors, no new warnings |
| T1 unit | **PASSED** — core `smf-mbs` 2103 checks (49 new), 0 failed; RAN `nas_lib_test` and `ngap_lib_test` pass; the runbook's own decoder test passes (9 checks). 8 of 87 RAN ctest cases fail, all environmental or pre-existing — TESTING.md shows how that was established |
| T2 integration | n/a — no MBS coverage exists in either repo's integration suites |
| T3 container E2E | **SKIPPED: no docker daemon in this VM** |
| T4 testbed / hardware | LOCAL ONLY — `runme run --all --filename tests/mbs-tn.md` |

Details, including everything still to run locally, are in [TESTING.md](TESTING.md).

## Files

- [APPLY.md](APPLY.md) — how to apply the patch series, per repo
- [CHANGES.md](CHANGES.md) — what changed, mapped to spec clauses, with the traceability table
- [TESTING.md](TESTING.md) — tier table, cloud results, and the local steps that remain
- [OPEN_ISSUES.md](OPEN_ISSUES.md) — assumptions, untested parts, known gaps
- [PR_DESCRIPTION.md](PR_DESCRIPTION.md) — draft PR text for when you push
- [PLAN.md](PLAN.md) — the plan this was built from (not approved: the task said to decide and keep going)
- [DESIGN_NOTE.md](DESIGN_NOTE.md) — the spec and code reading the plan rests on, written before any code
- [REPORT.md](REPORT.md) — the short report for the morning

## Repo details


### open5gs

- Remote: https://github.com/5G-MAG/open5gs
- Agent branch: `agent/2026-11-19-mbs-multicast-join` (local only, never pushed) — HEAD `3d4a155f32638364987f90b73c061cd65059f037`
- Base commit: `19149433f08f48d1d04bb62d5b5f9be1dcfd6c58`
- Patches: `patches/open5gs/` (1)

Commits:

```
    3d4a155f smf: handle the NAS join of a UE into a multicast MBS session
```

Diffstat:

```
     src/smf/context.c         | 103 ++++++++++++
     src/smf/context.h         |  27 +++
     src/smf/gsm-handler.c     |  15 ++
     src/smf/mbs-join.c        | 417 ++++++++++++++++++++++++++++++++++++++++++++++
     src/smf/mbs-join.h        | 114 +++++++++++++
     src/smf/meson.build       |   2 +
     src/smf/namf-build.c      |  85 ++++++++++
     src/smf/namf-build.h      |   2 +
     src/smf/ngap-build.c      |  84 ++++++++++
     src/smf/ngap-build.h      |   5 +
     src/smf/sbi-path.c        |  23 +++
     src/smf/sbi-path.h        |   2 +
     tests/unit/smf-mbs-test.c | 244 +++++++++++++++++++++++++++
     13 files changed, 1123 insertions(+)
```

### openairinterface5g

- Remote: https://github.com/phinetech/openairinterface5g
- Agent branch: `agent/2026-11-19-mbs-multicast-join` (local only, never pushed) — HEAD `205c3a07c1c4b73dde99270597401ccb1e8ae204`
- Base commit: `a29db1e9180aaa075407fa7a287029c58a35088b`
- Patches: `patches/openairinterface5g/` (3)

Commits:

```
    205c3a07c NAS: let the nrUE join a multicast MBS session
    96f6cfcf5 RRC: keep a UE's multicast MBS membership in the CU
    ebe4e243e NGAP: decode and answer the multicast MBS procedures of a join
```

Diffstat:

```
     executables/nr-uesoftmodem.c                       |   5 +
     executables/nr-uesoftmodem.h                       |   5 +
     openair2/COMMON/ngap_messages_types.h              |  21 ++
     openair2/RRC/NR/nr_rrc_defs.h                      |   7 +
     openair2/RRC/NR/rrc_gNB_NGAP.c                     | 122 +++++++++++
     openair3/NAS/NR_UE/5GS/5GSM/MSG/CMakeLists.txt     |   4 +-
     openair3/NAS/NR_UE/5GS/5GSM/MSG/MbsContainers.c    | 174 +++++++++++++++
     openair3/NAS/NR_UE/5GS/5GSM/MSG/MbsContainers.h    |  92 ++++++++
     .../5GS/5GSM/MSG/PduSessionModificationCommand.c   |  18 ++
     .../5GS/5GSM/MSG/PduSessionModificationCommand.h   |   8 +-
     .../5GS/5GSM/MSG/PduSessionModificationRequest.c   |  49 +++++
     .../5GS/5GSM/MSG/PduSessionModificationRequest.h   |  44 ++++
     openair3/NAS/NR_UE/5GS/tests/nas_lib_test.c        | 141 ++++++++++++
     openair3/NAS/NR_UE/nr_nas_msg.c                    | 172 +++++++++++++++
     openair3/NAS/NR_UE/nr_nas_msg.h                    |   7 +
     openair3/NGAP/ngap_gNB_handlers.c                  | 240 ++++++++++++++++++++-
     openair3/NGAP/ngap_gNB_pdu_session_management.c    |  38 ++++
     openair3/NGAP/ngap_msg_includes.h                  |  15 ++
     18 files changed, 1149 insertions(+), 13 deletions(-)
```

### frq-adsat-phine

- Remote: https://github.com/phinetech/frq-adsat-phine
- Agent branch: `agent/2026-11-19-mbs-multicast-join` (local only, never pushed) — HEAD `00ac767a00e8c2dc2b3b478ce1961156b8df9ec9`
- Base commit: `b6403ecd657fae6eaba35bed64ae87d36a61405c`
- Patches: `patches/frq-adsat-phine/` (1)

Commits:

```
    00ac767 Check the multicast join over N2 in MBS-MC-02
```

Diffstat:

```
     testbed/mbs-mono/compose.yaml   |   8 ++
     tests/README.md                 |   7 ++
     tests/mbs-tn.md                 | 202 +++++++++++++++++++++++++++++++++++++---
     tests/tools/decode_ngap.py      | 115 +++++++++++++++++++++--
     tests/tools/test_decode_ngap.py | 186 ++++++++++++++++++++++++++++++++++++
     5 files changed, 496 insertions(+), 22 deletions(-)
```
