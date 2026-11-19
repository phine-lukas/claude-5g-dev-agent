# Plan — 2026-11-19-mbs-multicast-join

Date: 2026-11-19 · Profile: `mbs-testbed` · Approval: **none — the task said to
decide and keep going** ("Start developing right away. Do not present a plan and
wait for a go: nobody is there to answer until tomorrow morning. Decide for
yourself, write the decisions down"). CLAUDE.md rule 4 and the skill's Phase 2
stop are overridden by that instruction for this run only; every decision that
would have been a question is written down here and in OPEN_ISSUES.md instead.

## Understanding of the task

A UE asks to join an MBS **multicast** session over NAS, the core accepts the
join and tells the gNB over N2, and the gNB decodes those messages and answers
them correctly. An acceptance check in `tests/mbs-tn.md` (MBS-MC-02) proves it
from an N2 capture. Out of scope: the multicast MRB and the RRC reconfiguration
to the UE, DCI 4_2 scheduling and the radio, and leaving/release (MBS-MC-03 and
MBS-MC-04). The gNB only has to understand and acknowledge. The broadcast checks
must stay green.

## Repos and base commits

| Repo | Role | Base branch | Base SHA |
|---|---|---|---|
| `openairinterface5g` (phinetech) | target | `mbs-ptm` | `a29db1e9180aaa075407fa7a287029c58a35088b` |
| `open5gs` (5G-MAG) | target | `5mbs-development` | `19149433f08f48d1d04bb62d5b5f9be1dcfd6c58` |
| `frq-adsat-phine` | test | `tests/acceptance-runbooks` | `b6403ecd657fae6eaba35bed64ae87d36a61405c` |

Work branches, local only, never pushed: `agent/2026-11-19-mbs-multicast-join`
in each.

## Spec basis

| TS | Version | Clause | What it mandates |
|---|---|---|---|
| 23.247 | V18.8.0 | 7.2.1.3 | The join procedure end to end: the UE's Modification Request with the MBS Session ID (step 1), the SMF's lookup and authorisation (2–4), the N1+N2 answer (5–6), the shared delivery (7), the gNB's response (9). |
| 23.247 | V18.8.0 | 7.2.1.4 | Establishment of shared delivery toward the NG-RAN node. |
| 24.501 | V18.14.0 | 9.11.4.30 | Requested MBS container: IEI `0x70`, type 6; per entry an octet of ID type (bits 1–2) and MBS operation (bits 3–4), then the session ID. |
| 24.501 | V18.14.0 | 9.11.4.31 | Received MBS container: IEI `0x71`, type 6; per entry MBS decision (bits 1–3 of octet 4), MSAI (4–5), rejection cause (6–8), then a flags octet and the TMGI. |
| 24.501 | V18.14.0 | 6.3.2.2 | What the SMF puts in the Received MBS container for accepted and rejected joins. |
| 24.501 | V18.14.0 | 6.3.2.3 | What the UE does with it. |
| 38.413 | V17.10.0 | 9.3.4.3 / IE list | `id-MBSSessionSetuporModifyRequestList` (319) is an optional IE of `PDUSessionResourceModifyRequestTransfer`; `id-MBSSessionSetuporModifyResponseList` (313) and `id-MBS-SupportIndicator` are extensions of the response transfer. |
| 38.413 | V17.10.0 | 8.18.3 | Multicast Session Activation (procedure code 71): the AMF asks, the gNB activates and reports for which session the request was fulfilled, or answers a failure with a cause. |
| 38.413 | V17.10.0 | 8.18.1 | Distribution Setup (69) is **gNB-initiated**: "The NG-RAN node initiates the procedure by sending a DISTRIBUTION SETUP REQUEST message to the AMF." |
| 29.518 | V17.8.0 | 5.7.2.2 | Namf_MBSCommunication N2MessageTransfer: how the MB-SMF asks the AMF to put an MBS N2 message on N2, with `ngapIeType` choosing the procedure. |

## Current state, verified before building (see DESIGN_NOTE.md for the evidence)

- **Core**: multicast session *creation* works (`src/smf/context.c:4484`). No NAS
  join (`gsm_handle_pdu_session_modification_request()` ignores the container and
  then rejects the message for having no QoS flow to modify), no per-UE N2 MBS,
  no membership state, no Distribution Setup. The AMF's
  `amf_namf_mbs_comm_handle_n2_message_transfer()` and its activation builder
  already exist and nothing calls them.
- **gNB**: handlers for BroadcastSessionSetup/Release only; `{0,0,0}` for
  DistributionSetup and the three Multicast procedures.
  `decodePDUSessionResourceModify()` logs "Unhandled optional IE" for the MBS
  list.
- **nrUE**: no PDU Session Modification Request encoder at all, and no MBS
  containers in either direction.

## Design decisions (would have been questions)

1. **SMF and MB-SMF are one process**, so steps 2–3 of clause 7.2.1.3 (NRF
   discovery of the MB-SMF, `Nmbsmf_MBSSession_ContextStatusSubscribe`) are a
   lookup in this process's own context, behind one function.
2. **No PFCP round trip for a join** — clause 7.2.1.3 NOTE 8.
3. **Authorisation accepts anything whose TMGI the MB-SMF knows**; there is no
   MBS subscription data in the testbed's provisioning.
4. **Distribution Setup is stubbed**, documented in OPEN_ISSUES.md.
5. **The gNB answers an MBS-only modify without an RRC reconfiguration**, in a
   branch of its own, because the ordinary path answers the AMF only after a
   reconfiguration that this change deliberately does not start.
6. **The test restarts ue1 and ue2 with `--mbs-join <tmgi>`** rather than using a
   telnet command, because the TMGI is only known once the session exists.

## Commit series

`open5gs`

1. `smf: handle the NAS join of a UE into a multicast MBS session` —
   `src/smf/mbs-join.{c,h}` (new), `context.{c,h}`, `gsm-handler.c`,
   `ngap-build.{c,h}`, `namf-build.{c,h}`, `sbi-path.{c,h}`, `meson.build`,
   `tests/unit/smf-mbs-test.c`.

`openairinterface5g`

1. `NGAP: decode and answer the multicast MBS procedures of a join` —
   `openair2/COMMON/ngap_messages_types.h`, `openair3/NGAP/*`.
2. `RRC: keep a UE's multicast MBS membership in the CU` —
   `openair2/RRC/NR/*`.
3. `NAS: let the nrUE join a multicast MBS session` —
   `openair3/NAS/NR_UE/*`, `executables/nr-uesoftmodem.{c,h}`,
   `openair3/NAS/NR_UE/5GS/tests/nas_lib_test.c`.

`frq-adsat-phine`

1. `Check the multicast join over N2 in MBS-MC-02` — `tests/mbs-tn.md`,
   `tests/tools/decode_ngap.py`, `tests/tools/test_decode_ngap.py` (new),
   `tests/README.md`, `testbed/mbs-mono/compose.yaml`.

## Configuration changes

- nrUE: new option `--mbs-join <tmgi hex>` (12 hex characters), default unset.
- testbed: `MBS_UE1_EXTRA` / `MBS_UE2_EXTRA` / `MBS_UE3_EXTRA` append options to
  one UE's command line; empty by default, so an existing run is unchanged.
- No core configuration change. `smf.serving`, `upf.mbs.udptunnel` and
  `upf.mbs.multicast_router` are already in `testbed/mbs-mono/running/open5gs/core.yaml`.

## Test plan

| Tier | Command | Cloud |
|---|---|---|
| T0 core | `meson setup build && ninja -C build` | CAN RUN |
| T0 RAN | `cmake .. -GNinja -DENABLE_TESTS=ON && ninja nr-softmodem nr-uesoftmodem` | CAN RUN |
| T1 core | `meson test -C build --suite unit` | CAN RUN |
| T1 RAN | `ctest -R 'nas_lib_test|ngap_lib_test'` | CAN RUN |
| T2 | the core's scenario suites — none cover MBS | n/a |
| T3 | containers | **SKIPPED: no docker daemon in this VM** |
| T4 | `runme run --all --filename tests/mbs-tn.md` | LOCAL ONLY |

New tests: `tests/unit/smf-mbs-test.c` (both NAS container codecs, the TMGI
encodings, the two new NGAP transfers decoded back),
`openair3/NAS/NR_UE/5GS/tests/nas_lib_test.c` (the UE's side of both containers
and the whole Modification Request), `tests/tools/test_decode_ngap.py` (the
decoder the runbook check depends on).

## Risks

- Nothing was run end to end: this VM has no docker daemon, so the join has
  never crossed a real N2. Everything below T3 passed.
- The gNB's MBS-only branch is reached only when a modify carries no QoS flow
  change; a core that sent both would take the ordinary path and the MBS list
  would be stored but not reported. Noted in OPEN_ISSUES.md.
