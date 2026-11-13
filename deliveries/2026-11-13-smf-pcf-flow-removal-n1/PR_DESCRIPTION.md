# PR description — 2026-11-13-smf-pcf-flow-removal-n1

Draft text for the pull request. Review it before posting; the local
end-to-end results (TESTING.md L1) still need to be added — nothing above T1
ran in the cloud.

These are two PRs: one against `oai-cn5g-common-src`, one against
`oai-cn5g-smf` on top of `fix/qfi-reuse`. The SMF one depends on the other.

---

## PR 1 — `oai-cn5g-common-src`

**Title:** `fix(nas): correct the encoding of the PDU Session Modification Command`

### Summary

Three bugs that together made the PDU Session Modification Command unusable: it
was encoded without the IEIs of its optional IEs, so a UE could not parse it,
and the removal case could not be encoded at all. The second of those traces to
`ENCODE_U8`/`U16`/`U32` being multi-statement macros without a
`do { } while (0)` wrapper — at an unbraced conditional call site the store was
guarded but the `size +=` was not, so the encoder reported octets it never
wrote and left them uninitialised in the buffer.

### Spec basis

| TS | Version | Clause | What it mandates |
|---|---|---|---|
| 24.501 | V18.14.0 | 8.3.7 | Session-AMBR, authorized QoS rules and authorized QoS flow descriptions are optional IEs of the Modification Command, each preceded by its IEI (0x2a, 0x7a, 0x79). |
| 24.501 | V18.14.0 | 9.11.4.13, Table 9.11.4.13.1 | For "delete existing QoS rule": the length of QoS rule field is set to one, the packet filter list is empty, and neither the precedence nor the QFI value field is included. NOTE 1 forbids the QFI octet without the precedence octet. |

### What changed

- `fix(nas): make the ENCODE macros single statements` — wrap
  `ENCODE_U8`/`U16`/`U32` in `do { } while (0)` and brace the three unbraced
  conditional call sites in the tree (`QosRule::Encode()` twice,
  `_5gsNetworkFeatureSupport::Encode()` once). A scan of the whole `src/` tree
  found exactly those three.
- `fix(nas): keep the QoS rule length indicator in sync` —
  `SetRuleOperationCode()` and `SetNumberOfPacketFilters()` now recompute the
  indicator, the constructor initialises every member, the create/modify packet
  filter list is counted once in total rather than once per filter (it was
  quadratic in the filter count), and `Encode()` validates the buffer against
  `GetIeLength()` instead of the content length — it was writing 3 octets more
  than it checked for.
- `fix(nas): set the IEI of the Modification Command's optional IEs` — in the
  three setters, matching `Set5gsmCause()` beside them. The class's own
  `Decode()` already dispatched on these IEIs, so encoder and decoder
  contradicted each other.

### Compatibility

The same IE classes are mandatory and IEI-less in the PDU Session Establishment
Accept; that is a different message class and is untouched. The macro change is
library-wide — see the note in the SMF PR about re-scanning the AMF and UPF
trees before bumping their submodule.

### Testing

Covered by 11 new unit tests in the companion SMF PR (this repo has no test
target of its own beyond `main.cpp`).

---

## PR 2 — `oai-cn5g-smf` (on top of `fix/qfi-reuse`)

**Title:** `fix(smf): make PCF-initiated QoS flow removal reach the gNB and the UE`

### Summary

Follow-up to the QFI reuse work. An AF create/delete cycle left the gNB holding
its DRBs and the UE holding its QoS rules. The N2 side was fixed in `f086910`;
this completes the N1 side. The SMF built a DELETE QoS rule carrying a QFI,
which TS 24.501 forbids, and it ignored both N1/N2 builder return values, so a
failed N1 encode declared an empty container and the AMF silently dropped the
whole transfer — including the valid N2 release list.

### Spec basis

| TS | Version | Clause | What it mandates |
|---|---|---|---|
| 24.501 | V18.14.0 | 9.11.4.13, Table 9.11.4.13.1 | For "delete existing QoS rule" the QoS flow identifier value field shall not be included; the network shall not set the QoS rule identifier to 0. |
| 23.502 | V18.14.0 | 4.3.3.2 step 3b | SMF-requested modification sends the N2 SM information and the N1 SM container via `Namf_Communication_N1N2MessageTransfer`. |
| 38.413 | V17.10.0 | 9.3.4.3, 9.3.1.13 | The QoS Flow to Release List is a *QoS Flow List with Cause* (9.3.1.13); every IE of the Modify Request Transfer is optional, so a release-only transfer is valid. |

### What changed

- `fix(smf): build spec-compliant delete QoS rules` — drop the QFI from the
  DELETE rule (the UE still gets it in the DELETE flow description beside it);
  release the flow without an N1 rule when no edge supplies a rule identifier,
  instead of emitting identifier 0; have `mark_qfi_for_release()` call
  `build_release_flow()`, which duplicated it verbatim and had no caller; and
  correct the QoS Flow To Release List citation from §9.3.1.8 (*Global ng-eNB
  ID*) to §9.3.1.13.
- `fix(smf): do not send an N1N2 transfer with a failed container` — replaces
  the `TODO: handle encode N1, N2 failure`. Check both builders, declare only
  the containers that were built, and send nothing when neither succeeded.
- `test(smf): cover the NAS encoding of the Modification Command` — 11 new
  cases.
- `build(smf): bump common-src for the NAS encoding fixes` — requires PR 1.

### Testing

Clean `build_smf --clean --build-type Release --jobs --tests`: **57/57 tests
pass, no compiler warnings**. 11 of those are new.

The tests were written first and run against the unmodified base to pin down
the root cause: 7 failed, showing a delete rule reporting `GetIeLength() == 7`,
encoding 6 octets, and needing 4. That reproduces the reported failure exactly —
`GetLength()` returned 33 while encoding needed 35, so the QoS flow
descriptions IE no longer fitted and `Encoding QoS Flow Descriptions error`
followed.

**Not verified here:** nothing above T1 could run (no `oai-cn5g-fed` in the
session, no docker daemon). The end-to-end check — gNB releases the DRBs, UE
logs `DELETE QoS rule` and no `Unknown IEI` — still has to be run on the
testbed. Steps and expected log lines are in the delivery's TESTING.md.

### Known gaps

- The AMF answers 200 `N1_N2_TRANSFER_INITIATED` and forwards nothing when a
  declared container is empty, with no log line. The SMF no longer triggers it,
  but the silent drop should be fixed in the AMF separately.
- UEs in CM-IDLE still get nothing (already marked TODO in `smf_procedure.cpp`).
- `common-src` is vendored by the AMF and UPF too. Before bumping their
  submodule, re-run the unbraced-macro scan in those trees; see the delivery's
  OPEN_ISSUES.md item 5 for the exact command.
