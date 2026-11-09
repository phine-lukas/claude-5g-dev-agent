# Open issues — 2026-11-09-smf-qfi-reuse

Everything a reviewer should know that is not visible in the diff.

## Assumptions

| # | Assumption | Why it was needed | What breaks if it's wrong |
|---|---|---|---|
| 1 | QFI 0 is the SMF's "no QFI assigned" sentinel, so the pool is 1..63 and `generate_qfi()` returning 0 keeps meaning "none available" | the allocator needs a lower bound and a failure value | if 0 were a usable QFI the pool would be one short; every caller (`smf_context.cpp`, `smf_procedure.cpp`, `select_upf_nodes()`) compares `qfi` against 0, so this is how the codebase already treats it |
| 2 | `upf_graph::generate_qfi()` / `release_qfi()` are the only way QFIs are allocated for a session | the allocator state lives in `upf_graph` | a second allocation path would hand out duplicates; `grep -rn "generate_qfi\|release_qfi" src/` shows only `smf_context.cpp`, `smf_procedure.cpp`, `smf_pfcp_association.cpp` and the test file |
| 3 | The default QoS flow's QFI is never released during the session | its bit must stay set so no other flow takes it | a release would let a PCC rule land on the default flow's QFI; `commit_staged_flow_removals()` explicitly refuses to release the default flow, and `remove_qos_flow_edge()` keeps it |
| 4 | Wrap-around ordering (a released QFI comes back last) is preferable to lowest-free | the spec constrains uniqueness, not ordering | nothing breaks either way; wrap-around is the safer choice while removals are not signalled on N2 (see "Known limitations") |

## Spec ambiguities and the interpretation chosen

| TS / clause | What is ambiguous | Interpretation used | Why |
|---|---|---|---|
| TS 23.501 V18.12.0 §5.7.1.1 | "The QFI shall be unique within a PDU Session" does not say when a QFI may be reused after its flow is gone | a QFI may be reused as soon as no flow of the session holds it, but the allocator defers reuse until it has wrapped the range | uniqueness among *active* flows is the only stated constraint; deferring is a safety margin, not a requirement |
| TS 29.244 V18.10.0 §8.2.89 | the figure shows a 6 bit QFI field but does not enumerate reserved values; it defers the encoding to TS 38.415 §5.5.3.3 | 1..63 usable, 0 treated as "unassigned" by the SMF | matches what the code already assumed (`qfi_to_use == 0 \|\| qfi_to_use > 63`). TS 38.415 was not available in this toolkit's spec set, so the 6 bit width is cited from the 29.244 figure rather than from 38.415 |

Version note: the issue cites TS 29.244 V17.10.0 §8.2.89 and TS 23.501 V17.15.0
§5.7.1.1. The converted specs in this toolkit are the Rel-18 ones (V18.10.0 and
V18.12.0). The clause numbers and the sentences relied on are the same; the code
comments and commit messages cite the Rel-18 versions that were actually read.

## Untested parts

| What | Why it wasn't tested | How to test it |
|---|---|---|
| The end-to-end AF add/remove loop from the issue | needs a PCF + AF driving Npcf_PolicyAuthorization against a live deployment | TESTING.md, L2 |
| The QoS Robot suites | no docker daemon, no compose plugin, `robot` not installed in this VM | TESTING.md, L1 |
| The "QFI pool exhausted" log line and the resulting `RULE_PERMANENT_ERROR` towards the PCF | the branch is reachable in a unit test only by driving `smf_context::handle_pdu_session_update_sm_context_request()`, which needs a full SMF context, ITTI and an SBI peer | TESTING.md, L2 — the pass criterion is that neither line appears |
| Concurrent `generate_qfi()`/`release_qfi()` from several threads | the suite is single-threaded, as the pre-existing `upf_graph` tests are | the allocator serialises every allocation and release on `m_qfi_allocator`, doing the probe, the bit set and the `qfi_last_` update under that one lock — the same serialisation the previous `uint_generator` gave via its own two mutexes |
| The scale run (29 UEs, 100 requests/s) | needs the AF load generator | TESTING.md, L3 |

## Pre-existing failures

None. The suite is 46/46 on this branch, so no base-commit comparison run was
needed.

Pre-existing **warnings**, all in `src/common-src`, none in a file this delivery
touches (so T0's "no new warnings" criterion holds):

| Warning | Where | Fails on base? |
|---|---|---|
| `integer constant is so large that it is unsigned` | `ngap/libngap_ies/Ngap_VolumeTimedReport-Item.c` (generated) | yes |
| `'std::not1' is deprecated` | `utils/string.cpp` | yes |
| `'std::ptr_fun' is deprecated` | `utils/string.cpp` | yes |

## Known limitations

- **A reused QFI can still meet a stale flow at the gNB and the UE.** On
  `develop` the SMF builds no N2 Modify Request for a PCF-initiated flow
  removal, so neither the RAN nor the UE is told the flow is gone. Wrap-around
  ordering gives them a full lap of the range before the QFI returns, which is a
  mitigation, not a fix. Named in the issue; a separate defect.
- **The allocator is per `upf_graph`, not per PDU session by construction.** It
  is correct because each session has its own graph, and the copy constructor now
  carries the state; but nothing in the type system enforces that a graph belongs
  to exactly one session.
- **No fairness or ageing guarantee.** With 63 flows active and churn, which QFI
  comes back depends on where `qfi_last_` happens to sit. Only uniqueness is
  required.
- `clang-format` here is 18.1.3 while CI pins 19. `git clang-format 7bfe3220`
  reported no changes, but re-check with 19 before pushing.

## Follow-up suggestions

1. **Send an N2 PDU Session Resource Modify Request for a PCF-initiated flow
   removal.** The SMF already marks flows for release
   (`session_handler::mark_qfi_for_release()`, `m_qos_flows_to_be_released`) but
   nothing builds the N2 message for that path, so the gNB and the UE keep the
   flow. This is the defect that forced wrap-around ordering; fixing it would
   make reuse order irrelevant. The message is the N2 PDU Session Resource
   Modify Request of the PDU Session Modification procedure; the exact clauses in
   TS 23.502 and TS 38.413 were **not looked up** in this run (neither spec is in
   this toolkit's converted set), so verify them before writing the issue.
2. **Release the QFI on the graph that allocated it in
   `upf_graph::select_upf_nodes()`.** `smf_pfcp_association.cpp:1251` allocates
   from `sub_graph_ptr`; the unqualified `release_qfi(criteria.qfi)` at `:1263`
   then runs on `this`, the global association graph, not that subgraph. It is
   harmless today — the rejected subgraph is discarded, and the global graph's
   allocator is never used to hand out session QFIs — and it stays harmless with
   the bounded allocator, but it reads as a bug and will become one if the
   global graph ever allocates. Left out of this delivery by the approved plan.
3. **Fix or remove `uint_range_generator`.** In
   `common-src/utils/uint_generator.hpp`, `get_uid()` writes
   `uid_generator == MIN;` — a discarded comparison where an assignment was
   meant — so the template never wraps and runs past `MAX`. It has no users
   today, which is why nothing has noticed. Out of scope here because this
   delivery deliberately contains no `common-src` patch.
4. **Drop the unused `session_handler::m_qfi_generator`**
   (`src/smf_app/session_handler.hpp:217`), declared and never read; the
   surrounding `TODO` already notes that block is out of sync with the UPF-graph
   QoS handling.
5. **Add a Robot case for the add/remove loop to `oai-cn5g-fed`.** Deliberately
   not part of this delivery (it could not be executed here and needs an AF-side
   loop the fed repo lacks); TESTING.md L2/L3 describe what it would have to do.
