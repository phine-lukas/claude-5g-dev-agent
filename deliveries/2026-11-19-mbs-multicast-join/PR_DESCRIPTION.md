# PR description — 2026-11-19-mbs-multicast-join

Draft text for the pull requests. Three repos, so three drafts. Review before
posting, and **add the local test results from TESTING.md first** — nothing in
this delivery has been run end to end.

---

## `5G-MAG/open5gs` ← `5mbs-development`

**Title:** `smf: handle the NAS join of a UE into a multicast MBS session`

### Summary

The MB-SMF could create a multicast MBS session but no UE could join one: a PDU
Session Modification Request carrying a Requested MBS container fell through to
the QoS-flow handling, which needs exactly one flow to modify and answered a
Modification Reject. This adds the join — the NAS containers in both
directions, the membership, the per-UE N2 information, and the Multicast Session
Activation that the AMF already knew how to build and nothing ever asked for.

### Spec basis

| TS | Version | Clause | What it mandates |
|---|---|---|---|
| 23.247 | V18.8.0 | 7.2.1.3 | The join: the UE's request (step 1), the MBS session lookup and authorisation (2–4), the N1+N2 answer (5–6). NOTE 8: with shared delivery "no interaction with UPF is needed". |
| 24.501 | V18.14.0 | 9.11.4.30 / 9.11.4.31 | The Requested and Received MBS containers. |
| 24.501 | V18.14.0 | 6.3.2.2 | What the SMF puts in the answer for accepted and rejected joins. |
| 38.413 | V17.10.0 | 9.3.4.3 | `id-MBSSessionSetuporModifyRequestList` (319) in the PDU Session Resource Modify Request Transfer. |
| 29.518 | V17.8.0 | 5.7.2.2 | Namf_MBSCommunication N2MessageTransfer, `ngapIeType` `MBS_SES_ACT_REQ`. |

### What changed

- `src/smf/mbs-join.{c,h}`: the Requested MBS container is parsed, the
  multicast session found by TMGI, the UE's PDU session added to its membership,
  and the UpdateSMContext answered with a Modification Command carrying the
  Received MBS container plus the N2 SM information.
- `src/smf/ngap-build.c`: the MBS list inside the modify request transfer, and
  the Multicast Session Activation Request Transfer.
- `src/smf/namf-build.c`, `src/smf/sbi-path.c`: the Namf_MBSCommunication
  N2MessageTransfer client.
- `src/smf/context.{c,h}`: membership on `smf_mbs_sess_t`, dropped when the PDU
  session is released.
- `tests/unit/smf-mbs-test.c`: 49 new checks.

### Known limitations

The SMF finds the MBS session in its own context because this deployment runs
the SMF and the MB-SMF as one `open5gs-smfd`; a split deployment needs the NRF
discovery and `Nmbsmf_MBSSession_ContextStatusSubscribe` of clause 7.2.1.3 steps
2–3 in `find_multicast_session()`'s place. Authorisation (step 4) accepts any UE
because there is no MBS subscription data to check against. Distribution Setup,
leave and deactivation are not implemented.

### Configuration

| Key | Default | Effect on existing deployments |
|---|---|---|
| — | — | none; no new configuration, and the broadcast path is untouched |

---

## `phinetech/openairinterface5g` ← `mbs-ptm`

**Title:** `MBS: decode and answer a multicast join, and let the nrUE ask for one`

### Summary

Three commits: the gNB decodes and answers the two N2 messages a multicast join
produces, the CU remembers which UE joined which session, and the nrUE can ask
to join one with `--mbs-join <tmgi>`. The gNB understands and acknowledges; it
does not yet transmit — no multicast MRB, no scheduling.

### Spec basis

| TS | Version | Clause | What it mandates |
|---|---|---|---|
| 38.413 | V17.10.0 | 8.18.3 | Multicast Session Activation (code 71): activate, then report for which session the request was fulfilled, or answer a failure with a cause. |
| 38.413 | V17.10.0 | 9.3.4.3 / 8.2.3.2 | The MBS list in the modify request transfer (319) and the response list (313) with `id-MBS-SupportIndicator` in the response transfer's extensions. |
| 23.247 | V18.8.0 | 7.2.1.3 steps 6, 8, 9 | The NG-RAN associates the PDU session with the MBS session, passes the N1 container to the UE, and answers the modify. |
| 24.501 | V18.14.0 | 9.11.4.30 / 9.11.4.31 / 8.3.7 / 6.3.2.3 | The UE's side of both containers, and the message around them. |

### What changed

1. `NGAP: decode and answer the multicast MBS procedures of a join`
2. `RRC: keep a UE's multicast MBS membership in the CU`
3. `NAS: let the nrUE join a multicast MBS session`

### Configuration

| Key | Default | Effect on existing deployments |
|---|---|---|
| `--mbs-join <tmgi hex>` (nrUE) | unset | none — with no TMGI given, the UE behaves exactly as before |

### Testing done

- Build: nr-softmodem and nr-uesoftmodem, no errors, no new warnings.
- Unit tests: `nas_lib_test` and `ngap_lib_test` pass, with new cases for both
  MBS containers and the Modification Request.
- Testbed: **not run** — see TESTING.md.

---

## `phinetech/frq-adsat-phine` ← `tests/acceptance-runbooks`

**Title:** `Check the multicast join over N2 in MBS-MC-02`

### Summary

Replaces the MBS-MC-02 stub with a check of the signalling half of the
requirement, decided from an N2 capture: the AMF activated the session and the
gNB accepted it; the two joining UEs' PDU sessions were associated with it and
the gNB accepted that too; the third UE got none of it. The radio half stays
reported as not implemented, with what it needs. `decode_ngap.py` gains the
ability to find a TMGI inside the nested transfer octet strings and to report
the RAN UE NGAP ID, and a self-test that needs no testbed.

### Configuration

| Key | Default | Effect on existing deployments |
|---|---|---|
| `MBS_UE1_EXTRA` / `MBS_UE2_EXTRA` / `MBS_UE3_EXTRA` | empty | none — an existing run is byte-for-byte the same command line |
