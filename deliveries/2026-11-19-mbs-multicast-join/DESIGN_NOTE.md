# Multicast join — which messages, which IEs, which clauses

Written before any code, as step 1 of the night task. Everything below was
read out of the converted specs in `specs/` and out of the ASN.1 grammar OAI
actually compiles (`openair3/NGAP/MESSAGES/ASN1/ngap-17.10.0.asn1`), not from
memory.

## The flow being built

TS 23.247 V18.8.0 clause 7.2.1.3 ("Multicast session join and session
establishment procedure"), steps 1, 4, 5, 6, 9 — and clause 7.2.1.4 for the
shared delivery tunnel, which is the part that gets stubbed.

```
UE                 gNB                 AMF              SMF/MB-SMF
 |  PDU Sess Mod Req (Requested MBS container: join, TMGI)       |   step 1
 |------------------ UL NAS transport ------------------------->|
 |                                                              | step 4: authorise
 |                    N1: PDU Sess Mod Command (Received MBS container)
 |                    N2: PDUSessionResourceModifyRequest        | step 5
 |                        + MBSSessionSetuporModifyRequestList   |
 |<-----------------------------------------------------------  |
 |                    MulticastSessionActivationRequest (non-UE) | first member
 |                 <---------------------------------------     |
 |                 --- MulticastSessionActivationResponse --->   |
 |                 --- PDUSessionResourceModifyResponse ----->   | step 9
 |<-- DL info transfer (the N1 container) --                     |
 |--- PDU Sess Mod Complete ------------------------------------>|
```

## NAS (TS 24.501 V18.14.0)

| What | Clause | Coding |
|---|---|---|
| Requested MBS container | 9.11.4.30 | IEI `0x70`, type 6 (TLV-E). Per entry: octet 4 = bits 1-2 *Type of multicast MBS session ID* (`01` = TMGI), bits 3-4 *MBS operation* (`01` = join, `10` = leave), bits 5-8 spare; then the session ID. For TMGI that is 6 octets, "coded as described in clause 10.5.6.13 in 3GPP TS 24.008 starting from octet 2" — 3 octets MBS Service ID then 3 octets MCC/MNC. So one TMGI entry is 7 octets. |
| Received MBS container | 9.11.4.31 | IEI `0x71`, type 6 (TLV-E). Per entry: octet 4 = bits 1-3 *MBS decision* (`010` accepted, `011` rejected, `100` remove), bits 4-5 *MSAI*, bits 6-8 *Rejection cause*; octet 5 = bit 1 IPAE, bits 2-3 MTI, bit 4 MSCI, bit 5 IPAT, bits 6-8 spare; octets 6..j TMGI. With MSAI=00, MTI=00, MSCI=0, IPAE=0 an entry is 8 octets. |
| Where they ride | 8.3.9.1 (Modification Request), 8.3.2.1 / 8.3.9.1 tables | Requested in PDU SESSION MODIFICATION REQUEST, Received in PDU SESSION MODIFICATION COMMAND. Both also exist on Establishment Request/Accept; not used tonight. |
| SMF behaviour | 6.3.2.2 | "shall include the TMGI for the multicast MBS session IDs that the UE is allowed to join … shall set the MBS decision to 'MBS join is accepted' for each of those", and the mirror for rejected. |
| UE behaviour | 6.3.2.3 | "If the PDU SESSION MODIFICATION COMMAND message includes the Received MBS container IE, for each of the Received MBS informations: …" |

Rejection causes (9.11.4.31 table 9.11.4.31.1, bits 6-8 of octet 4): `000` no
additional information, `001` insufficient resources, `010` not authorized,
`011` session has not started, `100` outside local MBS service area, `101`
session context not found, `110` session released.

Open5GS already carries both IEs as opaque `length + buffer` blobs
(`lib/nas/5gs/types.h` `ogs_nas_requested_mbs_container_t` /
`ogs_nas_received_mbs_container_t`, decoder/encoder in `lib/nas/5gs/ies.c`), so
only the *contents* have to be parsed and built. OAI's nrUE NAS has neither the
containers nor a PDU Session Modification Request encoder at all.

## N2 (TS 38.413 V17.10.0, ASN.1 as OAI compiles it)

Per-UE — the association of the UE's PDU session with the MBS session:

| IE / type | ID | Where |
|---|---|---|
| `MBSSessionSetuporModifyRequestList` | ProtocolIE-ID **319** | optional IE of `PDUSessionResourceModifyRequestTransfer` (procedure code 26, `id-PDUSessionResourceModify`), criticality ignore |
| `MBSSessionSetuporModifyRequestItem` | — | `{ mBS-SessionID, mBS-AreaSessionID OPTIONAL, associatedMBSQosFlowSetuporModifyRequestList OPTIONAL, mBS-QosFlowToReleaseList OPTIONAL }` |
| `MBSSessionSetuporModifyResponseList` | ProtocolIE-ID **313** | **extension** of `PDUSessionResourceModifyResponseTransfer` (type `MBSSessionSetupResponseList`), criticality ignore |
| `MBSSessionFailedtoSetuporModifyList` | ProtocolIE-ID **311** | extension of the same transfer |
| `MBS-SessionID` | — | `{ tMGI OCTET STRING (SIZE(6)), nID OPTIONAL }` |

Non-UE associated — turning the session on in the RAN:

| Procedure | Code | Messages |
|---|---|---|
| `id-MulticastSessionActivation` | **71** | Request / Response / Failure. Request IEs: `MBS-SessionID` (M) + `MulticastSessionActivationRequestTransfer` (M, OCTET STRING CONTAINING). Response IEs: `MBS-SessionID` (M), `CriticalityDiagnostics` (O). |
| `id-MulticastSessionDeactivation` | 72 | out of scope tonight (MBS-MC-03) |
| `id-DistributionSetup` | **69** | **NG-RAN → AMF** (TS 38.413 cl. 8.18.1.2: "The NG-RAN node initiates the procedure by sending a DISTRIBUTION SETUP REQUEST message to the AMF"). This is the shared NG-U tunnel. |
| `id-DistributionRelease` | 70 | out of scope |

`MulticastSessionActivationRequestTransfer ::= SEQUENCE { mBS-SessionID
MBS-SessionID, iE-Extensions OPTIONAL, ... }` — so the transfer carries the
TMGI a second time and nothing else. That matters: the AMF builder in Open5GS
takes the transfer as an opaque pkbuf from its caller, so the MB-SMF has to
encode it.

Procedure-code ordering check (ASN.1 lines 12227-12235): 66 BroadcastSession
Modification, 67 BroadcastSessionRelease, 68 BroadcastSessionSetup, 69
DistributionSetup, 70 DistributionRelease, 71 MulticastSessionActivation, 72
Deactivation, 73 Update, 74 MulticastGroupPaging, 75 BroadcastSession
ReleaseRequired. OAI's `ngap_messages_callback[]` is already sized through 75
with null handlers for 69-74.

## What the three stacks have today — verified, not assumed

**5G-MAG Open5GS @ `19149433f`**

* `src/smf/context.c:4484` creates a `MULTICAST` session and puts it in state
  `Configured`; `smf_mbs_sess_find_by_tmgi()` indexes it. So multicast session
  *creation* works — confirmed.
* No NAS join: `gsm_handle_pdu_session_modification_request()`
  (`src/smf/gsm-handler.c:190`) never looks at
  `OGS_NAS_5GS_PDU_SESSION_MODIFICATION_REQUEST_REQUESTED_MBS_CONTAINER_PRESENT`,
  and falls into `ogs_list_count(&sess->qos_flow_to_modify_list) != 1` →
  "Invalid modification request" → Modification Reject. Confirmed by reading
  the function top to bottom.
* No per-UE N2 MBS: `ngap_build_pdu_session_resource_modify_request_transfer()`
  (`src/smf/ngap-build.c:286`) only emits `QosFlowAddOrModifyRequestList`.
* No membership state: `smf_mbs_sess_t` (`src/smf/context.h:693`) has
  `dl_tunnel_list` and `amf_list` but no list of joined UEs.
* **The AMF side is already there**:
  `amf_namf_mbs_comm_handle_n2_message_transfer()`
  (`src/amf/namf-handler.c:4267`) handles Namf_MBSCommunication N2MessageTransfer
  and dispatches `MBS_SES_ACT_REQ` → `ngap_build_multicast_session_activation_
  request()`. Nothing in the SMF ever calls it — confirmed by grep: the only
  hits for `multicast_session_activation` outside `ngap-build.c` are that
  handler and the header.
* No Distribution Setup anywhere: no handler, no `DistributionSetupRequest`
  decode, no Nmbsmf operation for it.

**OAI gNB @ `mbs-ptm`**

* `ngap_messages_callback[]` (`openair3/NGAP/ngap_gNB_handlers.c:1790`) has
  handlers for BroadcastSessionSetup/Release only; `{0,0,0}` for
  DistributionSetup, MulticastSessionActivation/Deactivation/Update,
  MulticastGroupPaging. An unhandled procedure code is dropped with a log line
  at `ngap_gNB_handle_message()`.
* `decodePDUSessionResourceModify()` (`ngap_gNB_handlers.c:1178`) handles
  `QosFlowAddOrModifyRequestList` and `QosFlowToReleaseList`, and its `default:`
  arm logs "Unhandled optional IE" — so an `MBSSessionSetuporModifyRequestList`
  arrives and is thrown away today.
* `ngap_gNB_pdusession_modify_resp()`
  (`openair3/NGAP/ngap_gNB_pdu_session_management.c:153`) builds the response
  transfer with `qosFlowAddOrModifyResponseList` only.

**OAI nrUE @ `mbs-ptm`**

* `openair3/NAS/NR_UE/5GS/5GSM/MSG/` has Establish Request/Accept, Modification
  Command and Modification Complete. There is **no** Modification Request
  encoder — `FGS_PDU_SESSION_MODIFICATION_REQ (0xc9)` is only a message-type
  constant.
* `handle_pdu_session_modification_command()`
  (`openair3/NAS/NR_UE/nr_nas_msg.c:1974`) decodes 5GSM cause, Session-AMBR, QoS
  rules and flow descriptions; `FOREACH_MOD_IEI` has no `0x71`.

## Design decisions taken without asking

1. **SMF and MB-SMF are one process.** The testbed runs a single `open5gs-smfd`
   serving both roles (profile `mbs-testbed.yaml`: "MB-SMF is open5gs-smfd";
   `testbed/mbs-mono/running/open5gs/core.yaml` has one `smf:` section and the
   MB-SMF SBI is the same `127.0.0.4:7777`). So steps 2 and 3 of clause 7.2.1.3
   (NRF discovery of the MB-SMF, then `Nmbsmf_MBSSession_ContextStatusSubscribe`)
   collapse into a direct `smf_mbs_sess_find_by_tmgi()` in the same address
   space. Written that way deliberately, behind one function, with the SBI path
   named in a comment so a split deployment has one place to change.
2. **No PFCP round trip for a join.** 5GC *shared* delivery is used, and clause
   7.2.1.3 NOTE 8 says "If the shared tunnel is used, no interaction with UPF is
   needed for the indicated multicast MBS session". The join answers the
   `Nsmf_PDUSession_UpdateSMContext` stream directly with
   `smf_sbi_send_sm_context_updated_data_n1_n2_message()`.
3. **Authorisation is accept-by-default.** Clause 7.2.1.3 step 4 wants MBS
   subscription data from the UDM; there is no MBS subscription data in the
   testbed's Mongo provisioning and inventing a schema is a bigger change than
   tonight's scope. The SMF accepts a join for a TMGI it knows and rejects with
   "Session context not found" (`101`) for one it does not. Written as one
   function so a real check drops in.
4. **Distribution Setup is stubbed** — see OPEN_ISSUES.md.
5. **The gNB answers the MBS modify in NGAP/RRC without an RRC
   reconfiguration.** Radio is out of scope tonight, and the normal
   `rrc_gNB_process_NGAP_PDUSESSION_MODIFY_REQ()` path ends in
   `init_delayed_action()`, whose response is only sent once a reconfiguration
   completes. An MBS-only modification (no QoS flows added, modified or
   released) therefore takes a dedicated branch that stores the membership in
   the CU's UE context, delivers the N1 container by DL information transfer,
   and answers the modify immediately.
