# Open issues — 2026-11-19-mbs-multicast-join

Everything a reviewer should know that is not visible in the diff.

## The big one: nothing was run end to end

This VM has **no docker daemon** (`probe_env.sh`: "daemon reachable no", "can run
a container no"), so no image could be built and no testbed could be brought up.
The join has therefore never crossed a real N2. Every tier below T3 passed; T3
and T4 are untouched. MBS-MC-02 is written and its decoder is tested against
synthetic PDUs built from the same ASN.1 grammar, but the check itself has never
been executed against the stack. **Run it first thing** — TESTING.md has the
exact commands.

## Distribution Setup is missing, on both sides

TS 23.247 V18.8.0 clause 7.2.1.3 step 7: "If shared tunnel has not been
established for the multicast MBS session towards the NG-RAN node, the
procedures in clause 7.2.1.4 for the establishment of shared delivery toward
NG-RAN node are executed."

That procedure is **gNB-initiated**: TS 38.413 V17.10.0 clause 8.18.1.2, "The
NG-RAN node initiates the procedure by sending a DISTRIBUTION SETUP REQUEST
message to the AMF" (procedure code 69), and the AMF answers with the shared
NG-U TNL information — the (S,G) pair and C-TEID the payload will arrive on.

What is missing, exactly:

| Side | What exists | What is missing |
|---|---|---|
| gNB | the ASN.1 types are compiled; `{0, 0, 0}` in `ngap_messages_callback[]` for procedure code 69 | nothing sends a DISTRIBUTION SETUP REQUEST, and nothing handles its response or failure |
| AMF (5G-MAG) | nothing | no handler for the request; `OpenAPI_mbs_ngap_ie_type_MBS_DIS_SETUP_REQ/RSP/FAIL` exist in the OpenAPI model but no code uses them |
| MB-SMF | the broadcast path has `MBS-SessionTNLInfo5GC` and a DL tunnel list (`smf_mbs_dl_tunnel_t`) | no Nmbsmf operation that answers a Distribution Setup; nothing allocates the shared NG-U transport for a *multicast* session |

**Why it did not block the night's work:** the task's scope is the gNB
understanding and acknowledging the join, which it does. The shared tunnel only
matters once there is a multicast MRB to deliver into, which is tomorrow's
radio work. Nothing is stubbed in the sense of a fake success being reported:
no Distribution Setup is attempted and none is claimed. The MBS-MC-02 radio
section names it as the first thing that work needs.

**Where to start:** the broadcast path already receives
`MBS-SessionTNLInfo5GC` in `decodeMBSSessionSetup()`
(`openair3/NGAP/ngap_common.c`) and hands the (S,G) and C-TEID to the user
plane; the multicast equivalent is the same information arriving in a
`MBS-DistributionSetupResponseTransfer` instead, after the gNB asks for it.

## Assumptions

| # | Assumption | Why it was needed | What breaks if it's wrong |
|---|---|---|---|
| 1 | The SMF and the MB-SMF are one `open5gs-smfd`, so the MBS session context for a TMGI is in this process. | Steps 2–3 of clause 7.2.1.3 are NRF discovery plus `Nmbsmf_MBSSession_ContextStatusSubscribe`; implementing them for a co-located pair would be code with no caller. | A split deployment finds no session and rejects every join with "Session context not found". `find_multicast_session()` in `src/smf/mbs-join.c` is the one place to change. |
| 2 | Any UE that reaches the SMF may join any multicast session the MB-SMF knows. | Clause 7.2.1.3 step 4 wants MBS subscription data from the UDM; the testbed's Mongo provisioning has none, and inventing a schema is a larger change than this task. | Nothing in the testbed; in a real deployment it is an authorisation hole. The check is one commented block in `smf_mbs_handle_join()`. |
| 3 | A join carries no QoS flow change, so the gNB can tell it apart by that. | The gNB needs to know when to take the branch that answers without a reconfiguration. | A core that sent QoS changes *and* an MBS list in one modify would take the ordinary path: the MBS list is still decoded and stored, but it would not be reported in the response, and the response would wait for the reconfiguration. |
| 4 | One MBS session per join request is enough. | The container allows several; the testbed has one. | Nothing breaks — up to `SMF_MBS_MAX_REQUESTS` (8) entries are handled — but only the first few were ever exercised. |
| 5 | The TMGI encodings of NAS (TS 24.008 10.5.6.13 from octet 2) and NGAP (`TMGI ::= OCTET STRING (SIZE(6))`) are byte for byte the same. | It lets a TMGI read off a NAS container be compared with a session's without converting either. | A unit test asserts it (`test_tmgi_octets_match_ngap`), so it would fail loudly rather than mis-match silently. |

## Spec ambiguities and the interpretation chosen

| TS / clause | What is ambiguous | Interpretation used | Why |
|---|---|---|---|
| 24.501 V18.14.0 9.11.4.30 | The IE is said to have "a minimum length of 8 octets", but the smallest entry it can describe is 1 + 6 = 7 octets of contents, i.e. 10 with IEI and length. | The stated minimum is not enforced; entries are parsed by their ID type's own length. | The per-entry figures and the TS 24.008 reference are unambiguous; the stated minimum is not reachable by any encoding the clause defines. |
| 24.501 V18.14.0 9.11.4.31 | The MBS service area may be an "MBS TAI list", which is "coded as octet 2 and above of the 5GS tracking area identity list IE" — that list carries no length of its own inside the container. | The UE's decoder stops after the entry carrying a TAI list, with a warning, instead of guessing where the next entry starts. | Guessing would silently mis-parse. The SMF never sends one (MSAI = 00), so this is a decoder robustness path, not a live one. |
| 23.247 V18.8.0 7.2.1.3 step 5 | "NOTE 5: Detailed information included in N2 SM information will be aligned with by RAN WG3." | `MBSSessionSetuporModifyRequestItem` with only the MBS Session ID; no `associatedMBSQosFlowSetuporModifyRequestList`. | That list is for 5GC Individual MBS traffic delivery, and step 6 says that with shared delivery "the associated unicast QoS flow information, if provided, is not used to allocate the radio resource". There are no multicast QoS flows to map yet either. |

## Untested parts

| What | Why it wasn't tested | How to test it |
|---|---|---|
| The whole join, end to end | no docker daemon in this VM | `runme run --all --filename tests/mbs-tn.md` — see TESTING.md |
| The gNB's MULTICAST SESSION ACTIVATION FAILURE arm | needs more than `NGAP_MAX_MULTICAST_SESSIONS` (8) sessions | create nine multicast sessions and watch the ninth activation be refused |
| Rejection of a join for an unknown TMGI | needs a live UE | start a UE with `--mbs-join 000000999f07` (a TMGI no session has) and look for "MBS join is rejected (session context not found)" in its log |
| A leave | not implemented — MBS-MC-03/04 | — |
| More than one MBS session per UE | the testbed has one | — |
| `MBS_UE3_EXTRA` | nothing uses it yet | it is there so a later check can give ue3 something |

## Known gaps, in the order they matter

1. **Distribution Setup** — above. Nothing can be delivered without it.
2. **The multicast MRB and its RRC reconfiguration** — the gNB knows which UEs
   joined and does nothing with that knowledge yet.
3. **Leave and release** (MBS-MC-03, MBS-MC-04). The core parses a leave and
   refuses it explicitly; the UE has no way to ask for one.
4. **Deactivation.** `ran_activated` is set and never cleared, so a session that
   loses its last member stays active in the gNB. The AMF builder for
   MULTICAST SESSION DEACTIVATION exists and is still uncalled.
5. **The AMF relays an N2MessageTransfer to every connected gNB**, which is a
   pre-existing simplification documented in
   `amf_namf_mbs_comm_handle_n2_message_transfer()`'s own comment, not something
   this change introduced. Correct for a single-gNB testbed only.
6. **The submodule pointers in `frq-adsat-phine` are not bumped.** They can only
   be moved once these commits exist in the target repos, which this delivery
   does not push.

## Pre-existing failures seen while testing

Both reproduced on the base commits, not caused by this change:

- `open5gs`, `meson test -C build --suite unit`: `core` and `smf-mbs` both die
  on a SIGSEGV/SIGABRT under meson's `MALLOC_PERTURB_`. Run directly without it,
  `smf-mbs` reports **0 failures** over its whole suite. Verified by stashing
  this change and running the base commit's binary the same way.
- `openairinterface5g`, `ninja tests`: `test_nr_mac_gnb` fails to link —
  `undefined reference to e1_bc_bearer_context_release` from
  `openair2/RRC/NR/cucp_cuup_direct.c`. Reproduced on `a29db1e91` with this
  change stashed.
