# Changes — 2026-11-13-smf-pcf-flow-removal-n1

## Summary

A PCF-initiated QoS flow removal never reached the gNB or the UE. Four defects
were reported; the first was already fixed on the base branch (`f086910`), so
this delivery closes the remaining three. The N1 PDU Session Modification
Command was being encoded without the IEIs of its optional IEs, so the UE
could not parse it; the removal case failed to encode at all; and an N1 encode
failure was ignored and took the valid N2 release list down with it.

The encode failure turned out not to be where the task description suspected.
`ENCODE_U8`/`ENCODE_U16`/`ENCODE_U32` are multi-statement macros with no
`do { } while (0)` wrapper, so at an unbraced conditional call site only the
store was guarded while the `size +=` ran unconditionally. `QosRule::Encode()`
hit this twice, reporting 6 octets for a 4-octet delete rule and leaving two
uninitialised octets in the buffer. Three further length bugs in the same
class were found alongside it. Seven commits across two repos, plus 10 new
unit tests.

## Per repo

### `oai-cn5g-common-src` (submodule `src/common-src`, base `f725043c`)

#### 1. `fix(nas): make the ENCODE macros single statements`

- **Purpose:** the root cause of the delete-case encode failure.
- **Files:** `common/common_defs.h`, `nas/ies/QosRule.cpp`,
  `nas/ies/_5gsNetworkFeatureSupport.cpp`
- **Spec:** TS 24.501 V18.14.0 §9.11.4.13 — a "delete existing QoS rule" has no
  precedence and no QFI octet, so neither must be counted.
- **Design notes:** the macros now expand to `do { } while (0)`, and the three
  unbraced conditional call sites in the tree are braced as well, so the fix
  holds regardless of macro form. A scan of the whole `src/` tree found exactly
  those three sites, which bounds the blast radius: two in `QosRule::Encode()`
  (this bug) and one in `_5gsNetworkFeatureSupport::Encode()`, which had the
  same defect for its octet 4 and is fixed by the same change.

#### 2. `fix(nas): keep the QoS rule length indicator in sync`

- **Purpose:** make `GetIeLength()` agree with what `Encode()` writes.
- **Files:** `nas/ies/QosRule.cpp`
- **Spec:** TS 24.501 V18.14.0 §9.11.4.13, Table 9.11.4.13.1 — "For the 'delete
  existing QoS rule' operation, the length of QoS rule field is set to one."
- **Design notes:** three distinct problems in one class.
  `SetRuleOperationCode()` and `SetNumberOfPacketFilters()` never recomputed the
  length indicator, and the constructor left `qos_rule_id_`,
  `rule_operation_code_` and `number_of_packet_filters_` uninitialised, so a
  rule built only from those setters kept the constructor's placeholder of 4 and
  reported `GetIeLength() == 7` while encoding 4 octets. Separately,
  `SetLengthIndicator()` walked the create/modify packet filter list once per
  packet filter instead of once in total, making the claimed length quadratic in
  the filter count — harmless at one filter, wrong at two. Finally `Encode()`
  validated the buffer against the content length while writing
  `content + 3` octets, a 3-octet overrun on an exactly-sized buffer; it now
  validates against `GetIeLength()`.

#### 3. `fix(nas): set the IEI of the Modification Command's optional IEs`

- **Purpose:** make the message decodable by the UE.
- **Files:** `nas/5gsm-msgs/PduSessionModificationCommand.cpp`
- **Spec:** TS 24.501 V18.14.0 §8.3.7 — Session-AMBR, authorized QoS rules and
  authorized QoS flow descriptions are optional IEs of this message, so each is
  preceded by its IEI (0x2a, 0x7a, 0x79).
- **Design notes:** fixed in the three setters rather than at the SMF call
  sites, matching `Set5gsmCause()` immediately beside them and making it
  impossible for a caller to forget. The class's own `Decode()` already
  dispatches on these IEIs, so encoder and decoder were contradicting each
  other. The same IE classes are mandatory and IEI-less in the PDU Session
  Establishment Accept, which is a different message class and is untouched.

### `oai-cn5g-smf` (base `f086910b`, branch `fix/qfi-reuse`)

#### 1. `fix(smf): build spec-compliant delete QoS rules`

- **Purpose:** stop putting a QFI on a delete rule.
- **Files:** `src/smf_app/session_handler.cpp`
- **Spec:** TS 24.501 V18.14.0 §9.11.4.13, Table 9.11.4.13.1 — for "delete
  existing QoS rule" the QoS flow identifier value field "shall not be
  included"; NOTE 1 forbids that octet without the precedence octet, which a
  delete rule must not carry either. Also TS 38.413 V17.10.0 §9.3.1.13.
- **Design notes:** the QFI still reaches the UE in the DELETE QoS flow
  description beside the rule, so nothing is lost. A flow whose edge lookup
  fails produced rule identifier 0, which the same table forbids the network
  from sending; the flow is now released without an N1 rule and the condition is
  logged, rather than emitting a rule the UE would reject. `build_release_flow()`
  duplicated `mark_qfi_for_release()` verbatim and had no caller — the latter now
  calls the former. The code's citation for the QoS Flow To Release List pointed
  at §9.3.1.8, which is *Global ng-eNB ID*; corrected to §9.3.1.13.

#### 2. `fix(smf): do not send an N1N2 transfer with a failed container`

- **Purpose:** stop a failed N1 encode from discarding a valid N2 part.
- **Files:** `src/smf_app/smf_context.cpp`
- **Spec:** TS 23.502 V18.14.0 §4.3.3.2 step 3b.
- **Design notes:** replaces the `TODO: handle encode N1, N2 failure`. Both
  builders' return values are checked, only containers that were built are
  declared in the `N1N2MessageTransfer`, and nothing is sent when neither
  succeeded. Confirmed against the AMF (`src/sbi/amf_http2_server.cpp`): an
  empty declared MIME part makes it answer 200 `N1_N2_TRANSFER_INITIATED` and
  return without forwarding. The AMF's silent drop is a separate AMF issue and
  is deliberately not addressed here.

#### 3. `test(smf): cover the NAS encoding of the Modification Command`

- **Files:** `src/smf_app/test/test_nas_modification_command.cpp` (new),
  `src/smf_app/test/test_session_handler.cpp`, `src/smf_app/test/CMakeLists.txt`

#### 4. `build(smf): bump common-src for the NAS encoding fixes`

- **Files:** `src/common-src` — `f725043c` → the three commits above.
- **Note:** this submodule is vendored by the AMF and UPF too. The IEI change is
  confined to `PduSessionModificationCommand`'s own setters, but the macro
  change is library-wide; see OPEN_ISSUES.md.

## Tests added or extended

| Repo | File | Framework | What it asserts | Commit |
|---|---|---|---|---|
| `oai-cn5g-smf` | `test_nas_modification_command.cpp` | GoogleTest/ctest | A DELETE QoS rule is 4 octets with length indicator 1 and octets `id,00,01,40` | #3 |
| `oai-cn5g-smf` | `test_nas_modification_command.cpp` | GoogleTest/ctest | A DELETE rule carries neither QFI nor precedence | #3 |
| `oai-cn5g-smf` | `test_nas_modification_command.cpp` | GoogleTest/ctest | `Encode()` returns exactly `GetIeLength()` for create and delete rules | #3 |
| `oai-cn5g-smf` | `test_nas_modification_command.cpp` | GoogleTest/ctest | `Encode()` rejects a buffer smaller than the IE instead of overrunning it | #3 |
| `oai-cn5g-smf` | `test_nas_modification_command.cpp` | GoogleTest/ctest | The QoS rules IE encodes exactly the length it reports | #3 |
| `oai-cn5g-smf` | `test_nas_modification_command.cpp` | GoogleTest/ctest | The removal-case Modification Command encodes to exactly `GetLength()` | #3 |
| `oai-cn5g-smf` | `test_nas_modification_command.cpp` | GoogleTest/ctest | The creation case still encodes to exactly `GetLength()` | #3 |
| `oai-cn5g-smf` | `test_nas_modification_command.cpp` | GoogleTest/ctest | IEIs 0x2a, 0x7a, 0x79 appear at the expected offsets | #3 |
| `oai-cn5g-smf` | `test_nas_modification_command.cpp` | GoogleTest/ctest | An encoded command decodes again and yields both QoS rules | #3 |
| `oai-cn5g-smf` | `test_session_handler.cpp` | GoogleTest/ctest | The rule `mark_qfi_for_release()` builds is spec-compliant and encodes to 4 octets | #3 |
| `oai-cn5g-smf` | `test_session_handler.cpp` | GoogleTest/ctest | With no edge, no N1 rule is emitted but the flow description still deletes the flow | #3 |

## Requirement traceability

| Requirement | Spec clause | Code | Test |
|---|---|---|---|
| The UE installs the new QoS rules on create (no `Unknown IEI`) | TS 24.501 §8.3.7 | `PduSessionModificationCommand::SetSessionAmbr/SetAuthorizedQosRules/SetAuthorizedQosFlowDescriptions` | `ModificationCommand_OptionalIesCarryTheirIei`, `ModificationCommand_RoundTripsThroughDecode` |
| The delete-case command encodes and is sent | TS 24.501 §9.11.4.13 | `common_defs.h` ENCODE macros, `QosRule::SetLengthIndicator/Encode`, `session_handler::build_release_flow` | `ModificationCommand_DeleteCase_Encodes`, `DeleteQosRule_IsFourOctetsWithLengthOne`, `MarkQfiForRelease_BuildsASpecCompliantDeleteRule` |
| The UE removes the QoS rules on delete | TS 24.501 §9.11.4.13 | `session_handler::build_release_flow` | `MarkQfiForRelease_BuildsASpecCompliantDeleteRule` |
| The gNB releases the DRBs of the removed QFIs | TS 38.413 §9.3.4.3 / §9.3.1.13 | `smf_n2` (base commit `f086910`), `smf_context` container handling | **No unit test** — see OPEN_ISSUES.md; verified by L1 locally |
| A failed N1 encode does not drop the N2 part | TS 23.502 §4.3.3.2 | `smf_context::handle_pdu_session_modification_network_requested` | **No unit test** — see OPEN_ISSUES.md |

## Configuration

None. No new keys, no changed defaults, no compose/conf changes.

## Not changed on purpose

- **The AMF's silent drop.** When a declared N1 or N2 MIME part is empty the AMF
  answers 200 `N1_N2_TRANSFER_INITIATED` and forwards nothing, with no log. The
  SMF no longer triggers it, but any other NF that does gets the same silence.
  Out of scope here; worth an AMF issue.
- **UEs in CM-IDLE.** The SMF only logs a warning and sends nothing
  (`src/smf_app/smf_procedure.cpp`, already marked TODO).
- **The UPF update step after a release-only modify.** See OPEN_ISSUES.md.
