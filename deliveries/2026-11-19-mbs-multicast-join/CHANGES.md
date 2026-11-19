# Changes — 2026-11-19-mbs-multicast-join

## Summary

A UE can now ask to join a multicast MBS session over NAS; the core accepts the
join, tells the gNB about it over N2 both per-UE and for the session as a whole,
and the gNB decodes both and answers them. Five commits across three repos: one
in the 5G-MAG core, three in OAI (NGAP, RRC, UE NAS), one in the testbed repo
that turns the MBS-MC-02 stub into a real check. Nothing in the broadcast path
is touched.

What this does **not** do: no multicast MRB, no RRC reconfiguration to the UE,
no DCI 4_2 scheduling, no Distribution Setup, no leave or release. The gNB
understands and acknowledges; it does not yet transmit.

## Per repo

### `open5gs` (5G-MAG, base `19149433f`)

#### 1. `smf: handle the NAS join of a UE into a multicast MBS session`

- **Purpose:** everything the core does for a join.
- **Files:** `src/smf/mbs-join.{c,h}` (new), `src/smf/context.{c,h}`,
  `src/smf/gsm-handler.c`, `src/smf/ngap-build.{c,h}`,
  `src/smf/namf-build.{c,h}`, `src/smf/sbi-path.{c,h}`, `src/smf/meson.build`,
  `tests/unit/smf-mbs-test.c`.
- **Spec:**
  - TS 23.247 V18.8.0 clause 7.2.1.3 steps 1–6 — the join procedure. Step 5 is
    the shape of the answer: "N2 SM information (PDU Session ID, MBS Session ID,
    …), N1 SM container (PDU Session Modification Command …)". NOTE 8 is why
    there is no PFCP exchange: "If the shared tunnel is used, no interaction
    with UPF is needed for the indicated multicast MBS session".
  - TS 24.501 V18.14.0 clause 9.11.4.30 — the Requested MBS container the UE
    sends, parsed in `smf_mbs_parse_requested_container()`.
  - TS 24.501 V18.14.0 clause 9.11.4.31 and clause 6.3.2.2 — the Received MBS
    container of the answer, built in `smf_mbs_build_received_container()`:
    "MBS join is accepted" for each session the UE may join, "MBS join is
    rejected" with a cause for the others.
  - TS 38.413 V17.10.0, `PDUSessionResourceModifyRequestTransferIEs` —
    `id-MBSSessionSetuporModifyRequestList` (ProtocolIE-ID 319), built by
    `ngap_build_pdu_session_resource_modify_request_transfer_mbs()`.
  - TS 38.413 V17.10.0 clause 8.18.3 and TS 29.518 V17.8.0 clause 5.7.2.2 —
    the activation, asked of the AMF with Namf_MBSCommunication N2MessageTransfer
    and `ngapIeType` `MBS_SES_ACT_REQ`. The AMF's builder and handler already
    existed; `smf_sbi_send_mbs_comm_n2_message_transfer()` is what finally calls
    them, and `ngap_build_multicast_session_activation_request_transfer()`
    encodes the transfer they take as an opaque octet string.
- **Design notes:**
  - The join is recognised in `gsm_handle_pdu_session_modification_request()`
    and handled before the QoS-flow logic, which requires exactly one flow to
    modify and would otherwise answer a Modification Reject.
  - Membership is a list of `smf_mbs_member_t` on `smf_mbs_sess_t`, each holding
    the associated PDU session by pool id rather than by pointer, so a session
    released behind the MB-SMF's back is noticed instead of dereferenced; a
    released PDU session leaves every MBS session it joined
    (`smf_mbs_member_remove_by_sess()`, called from `smf_sess_remove()`).
  - Finding the MBS session is a lookup in this process's own context, because
    the SMF and the MB-SMF are the same `open5gs-smfd` here. The function is
    named and commented so a split deployment has one place to change.
  - Activation is sent once, when the first member joins (`ran_activated`).
  - A leave is parsed and refused rather than silently accepted: answering
    "Remove UE from multicast MBS session" without doing it would be a lie.

### `openairinterface5g` (base `a29db1e91`, branch `mbs-ptm`)

#### 2. `NGAP: decode and answer the multicast MBS procedures of a join`

- **Purpose:** the gNB understands both N2 messages a join produces, and
  answers them.
- **Files:** `openair2/COMMON/ngap_messages_types.h`,
  `openair3/NGAP/ngap_gNB_handlers.c`,
  `openair3/NGAP/ngap_gNB_pdu_session_management.c`,
  `openair3/NGAP/ngap_msg_includes.h`.
- **Spec:**
  - TS 38.413 V17.10.0, ProtocolIE-ID 319 decoded in
    `decodePDUSessionResourceModify()`; 313
    (`id-MBSSessionSetuporModifyResponseList`) and `id-MBS-SupportIndicator`
    written into the response transfer's extension container. Clause 7.2.1.3
    step 9 of TS 23.247: "If the MBS is supported by NG-RAN, the N2 SM
    information further includes the indication of supporting MBS."
  - TS 38.413 V17.10.0 clause 8.18.3 — Multicast Session Activation, procedure
    code 71, handled by `ngap_gNB_handle_multicast_session_activation()`:
    successful outcome naming the session, or, per clause 8.18.3.3, a
    MULTICAST SESSION ACTIVATION FAILURE "with an appropriate cause value".
- **Design notes:**
  - The transfer of a modify item is now decoded whether or not a NAS PDU came
    with it: clause 9.2.1.5 makes the NAS-PDU optional and the transfer
    mandatory, and the old code skipped the whole item when the NAS PDU was
    absent.
  - The activation transfer is decoded even though it only repeats the MBS
    Session ID, and a mismatch is warned about — a core that puts a different
    session in it is a bug worth seeing.
  - The gNB's table of multicast sessions is read and written only by the NGAP
    task, so it needs no locking; the per-UE membership that the radio work
    needs lives in RRC instead.

#### 3. `RRC: keep a UE's multicast MBS membership in the CU`

- **Purpose:** remember which UE joined which session, where the radio
  configuration will look for it.
- **Files:** `openair2/RRC/NR/nr_rrc_defs.h`, `openair2/RRC/NR/rrc_gNB_NGAP.c`.
- **Spec:** TS 23.247 V18.8.0 clause 7.2.1.3 step 6 ("the NG-RAN uses the MBS
  Session ID to determine that the PDU Session … is associated with the
  indicated multicast MBS session") and step 8 (the N1 container reaches the UE
  "as part of the AN specific signalling exchange"); TS 38.413 clause 8.2.3.2
  for what the response reports.
- **Design notes:** an MBS-only modification takes a branch of its own because
  the ordinary path answers the AMF only after an RRC reconfiguration that a
  join does not start. The branch stores the membership, forwards the N1
  container by DL information transfer, and answers immediately.

#### 4. `NAS: let the nrUE join a multicast MBS session`

- **Purpose:** the UE can ask, and can read the answer.
- **Files:** `openair3/NAS/NR_UE/5GS/5GSM/MSG/MbsContainers.{c,h}` (new),
  `.../PduSessionModificationRequest.{c,h}` (new),
  `.../PduSessionModificationCommand.{c,h}`, `.../CMakeLists.txt`,
  `openair3/NAS/NR_UE/nr_nas_msg.{c,h}`, `executables/nr-uesoftmodem.{c,h}`,
  `openair3/NAS/NR_UE/5GS/tests/nas_lib_test.c`.
- **Spec:** TS 24.501 V18.14.0 clauses 9.11.4.30, 9.11.4.31, 8.3.7 and 6.3.2.3;
  TS 23.247 V18.8.0 clause 7.2.1.3 step 1 for when the join may be sent.
- **Design notes:** `--mbs-join <tmgi hex>` fires once a PDU session is up and
  only once. The Received MBS container's optional fields are skipped rather
  than kept, but sized correctly, because an entry after them cannot otherwise
  be found; an MBS TAI list ends the decode with a warning, since only the NR
  CGI list carries its own length.

### `frq-adsat-phine` (base `b6403ecd6`, branch `tests/acceptance-runbooks`)

#### 5. `Check the multicast join over N2 in MBS-MC-02`

- **Purpose:** prove the above from a capture.
- **Files:** `tests/mbs-tn.md`, `tests/tools/decode_ngap.py`,
  `tests/tools/test_decode_ngap.py` (new), `tests/README.md`,
  `testbed/mbs-mono/compose.yaml`.
- **Design notes:** the check asserts the activation and its successful answer,
  exactly two distinct RAN UE NGAP IDs associated with the session and
  confirmed by the gNB, and that the third UE carries no MBS procedure. The
  radio half is a separate `NOTIMPL` section with a "needs:" line.
  `decode_ngap.py` had to learn two things: to look inside the nested
  `*Transfer` octet strings, and to report the RAN UE NGAP ID — which meant
  teaching its search about pycrate's CHOICE pairs, since an open-type IE value
  is a CHOICE and `RAN-UE-NGAP-ID` is its name rather than a dict key.

## Tests added or extended

| Repo | File | Framework | What it asserts | Commit |
|---|---|---|---|---|
| `open5gs` | `tests/unit/smf-mbs-test.c` | meson (`smf-mbs`) | Requested MBS container parsing (TMGI, leave, the SSM forms skipped by length, truncated and reserved values refused); Received MBS container building (accepted, rejected with cause, two entries, buffer bound); the NAS and NGAP TMGI encodings agree; the modify request transfer and the activation transfer decoded back and checked for IE id, criticality and TMGI | 1 |
| `openairinterface5g` | `openair3/NAS/NR_UE/5GS/tests/nas_lib_test.c` | ctest (`nas_lib_test`) | the Requested MBS container's octets against the clause, the whole PDU Session Modification Request, the Received MBS container including optional-field skipping and the malformed cases, the decode of the IE inside its message, and `--mbs-join`'s argument parsing | 4 |
| `frq-adsat-phine` | `tests/tools/test_decode_ngap.py` | standalone (`python3 …`) | the decoder the runbook check rests on: activation request and response, the TMGI inside both nested transfers, per-UE attribution, the negative case of a UE with no MBS procedure, `--ran-ue`, `--summary` | 5 |
| `frq-adsat-phine` | `tests/mbs-tn.md` | runme | MBS-MC-02 itself | 5 |

## Requirement traceability

| Requirement | Where it is met | How it is shown |
|---|---|---|
| R-SYS-5011 (membership) | `smf_mbs_member_*` in the core, `rrc_pdu_session_param_t.mbs_sessions` in the CU | MBS-MC-02: exactly two UEs associated, confirmed by the gNB |
| R-SYS-5031 (multicast delivery to members) | not met — no multicast MRB | MBS-MC-02 radio section, `NOTIMPL` |
| R-SYS-5034 / R-SYS-5036 (reception by members) | not met | same |
| The core accepts a join and answers the UE | `smf_mbs_handle_join()` | unit tests of both containers; the UE logs the decision |
| The core tells the gNB, per UE and for the session | `ngap_build_pdu_session_resource_modify_request_transfer_mbs()`, `smf_sbi_send_mbs_comm_n2_message_transfer()` | MBS-MC-02, from the capture |
| The gNB decodes and answers both | `ngap_gNB_handle_multicast_session_activation()`, `decodePDUSessionResourceModify()` + the response extension | MBS-MC-02, from the capture |
