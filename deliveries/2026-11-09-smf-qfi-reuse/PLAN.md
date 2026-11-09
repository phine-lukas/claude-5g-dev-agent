# Plan — 2026-11-09-smf-qfi-reuse

Date: 2026-11-09 · Profile: oai-public · Mode: default (no AUTOPILOT, no E2E)

---

## 1. Understanding

Each PDU session's `upf_graph` hands out QFIs from a monotonic
`oai::utils::uint_generator<uint8_t>`. The SMF does free the QFI of a removed
QoS flow, but the generator's counter only ever counts up, so a freed value
does not come back until the 8-bit counter wraps after 256 allocations. Since
the SMF rejects any QFI above 63 (a QFI is 6 bits), the 63rd flow ever added to
a session fails and so do the next ~190 attempts, even when only the default
flow is active. This work replaces the per-session QFI source with a bounded
allocator over 1–63 that reuses released values, so "QFI pool exhausted" only
happens when 63 flows really are active at once.

## 2. Repos and base commits

| Repo | Role | Branch | Base SHA |
|---|---|---|---|
| `oai-cn5g-smf` | target | `claude/jolly-rubin-p7b75o` | `7bfe3220bc12ec52655ca355096a979b162ad260` |
| `oai-cn5g-common-src` | build dependency (pinned submodule, **not changed**) | `claude/jolly-rubin-p7b75o` | `f725043cc3694f29c5ea91b0d244a868f5d4179a` |

`oai-cn5g-pcf`, `oai-cn5g-amf`, `oai-cn5g-fed` are in the session but are not
touched: the fix is entirely inside the SMF's per-session QFI bookkeeping.

## 3. Spec basis

| TS | Version | Clause | What it mandates |
|---|---|---|---|
| 29.244 | V18.10.0 | 8.2.89 | The QFI IE carries the QFI value in bits 1–6 of octet 5, bits 7–8 are spare — i.e. the value range is 6 bits wide (0–63). |
| 23.501 | V18.12.0 | 5.7.1.1 | "The QFI shall be unique within a PDU Session." Uniqueness is scoped to the session, so a QFI no longer bound to any flow of that session may be used again. |
| 23.501 | V18.12.0 | 5.7.1.1 | "a QoS Flow associated with the default QoS rule is required to be established for a PDU Session and remains established throughout the lifetime of the PDU Session" — the default flow's QFI must stay reserved for the session's whole life. |

Note on versions: the issue cites TS 29.244 V17.10.0 §8.2.89 and TS 23.501
V17.15.0 §5.7.1.1. The converted copies in this toolkit are the Rel-18 ones
(V18.10.0 / V18.12.0); the clause numbers and the wording relied on here are
the same in both.

## 4. Current state in the repo(s)

- Exists:
  - `upf_graph::generate_qfi()` / `release_qfi()` —
    `src/smf_app/smf_pfcp_association.cpp:1536-1554`, backed by the private
    member `oai::utils::uint_generator<uint8_t> qfi_generator`
    (`src/smf_app/smf_pfcp_association.hpp:241`).
  - Release on flow removal already works:
    `session_update_sm_context_procedure::commit_staged_flow_removals()`
    (`src/smf_app/smf_procedure.cpp:2102-2138`) and the N4-reject path
    (`:1805-1813`) both call `release_qfi()`.
  - The range check and the "QFI pool exhausted" error:
    `src/smf_app/smf_context.cpp:2894-2908`.
  - Allocation for the default flow at session setup:
    `upf_graph::select_upf_nodes()`, `smf_pfcp_association.cpp:1250-1253`.
  - GoogleTest suite `src/smf_app/test/test_upf_graph.cpp` (195 lines) already
    covers `register_pcc_rule_qfi` / `release_qfi` / `remove_qos_flow_edge`,
    but nothing calls `generate_qfi()`.
- Missing: any reuse of a released QFI, and any bound on the generator that
  matches the QFI's own 6-bit range.
- `oai::utils::uint_generator` is shared with TEIDs, SEIDs and the PDR/FAR/QER/
  URR id generators, so it is **not** changed (per the issue: delaying reuse is
  wanted there).

## 5. Design decisions

**Bounded allocator inside `upf_graph`, wrap-around order.** Replace the
`uint_generator<uint8_t>` member with two plain members plus a mutex:

```cpp
static constexpr uint8_t QFI_MIN = 1;   // 0 is the SMF's "unassigned" sentinel
static constexpr uint8_t QFI_MAX = 63;  // TS 29.244 §8.2.89: QFI is 6 bits
uint64_t qfi_in_use_ = 0;               // bit (qfi - QFI_MIN) set == in use
uint8_t  last_qfi_   = QFI_MAX;         // so the first allocation returns 1
mutable std::mutex qfi_mutex_;
```

- `generate_qfi()` walks forward from `last_qfi_`, wrapping 63 → 1, and returns
  the first QFI whose bit is clear; after a full lap of 63 candidates it
  returns 0. `release_qfi()` clears the bit and deliberately leaves `last_qfi_`
  alone.
- Options considered: (a) lowest free QFI — simplest, but hands a released QFI
  straight back; (b) wrap-around from the last value — chosen. On `develop` a
  PCF-initiated removal produces no N2 Modify Request, so the gNB and the UE
  may still have the old flow configured under that QFI; wrapping gives them a
  full lap before the value returns. It also preserves today's 1, 2, 3, …
  ordering, which keeps existing traces readable.
- First allocation stays 1, so the default flow keeps the QFI it gets today,
  and its bit stays set for the session's lifetime (nothing releases it —
  `commit_staged_flow_removals()` explicitly refuses to release the default
  flow).
- Thread safety: the current `uint_generator` guards itself with mutexes, so
  the replacement keeps its own `std::mutex` rather than relying on
  `graph_mutex` (which `release_qfi()` does not take today either).
- **Copy constructor.** `upf_graph`'s copy ctor (`smf_pfcp_association.hpp:250`)
  copies `pcc_rule_id_to_qfi_` but cannot copy `qfi_generator` (non-copyable),
  so a copied graph starts allocating from scratch. The new members *are*
  copyable and the copy ctor will carry them, so a copy no longer hands out
  QFIs that the original already gave away. This is required for the allocator
  to be correct, not a drive-by change.
- **Caller cleanup.** With a bounded allocator `generate_qfi()` can no longer
  return a value above 63, so the `qfi_to_use > 63` branch in
  `smf_context.cpp:2899-2903` (and its "out of range" `release_qfi`) becomes
  dead and is reduced to `if (qfi_to_use == 0)`. The user-visible
  "QFI pool exhausted, cannot add flow for rule '%s'" message is kept verbatim;
  it now only fires on genuine exhaustion.

## 6. Commit plan

### `oai-cn5g-smf`

| # | Title | Files | Spec refs |
|---|---|---|---|
| 1 | `fix(smf): reuse released QFIs within the 1-63 range per PDU session` | `src/smf_app/smf_pfcp_association.hpp`, `src/smf_app/smf_pfcp_association.cpp`, `src/smf_app/smf_context.cpp` | 29.244 §8.2.89, 23.501 §5.7.1.1 |
| 2 | `test(smf): cover QFI allocation, reuse and exhaustion in upf_graph` | `src/smf_app/test/test_upf_graph.cpp` | 23.501 §5.7.1.1 |

Commit 1 builds and passes the existing suite on its own; commit 2 adds the new
assertions. (Repo convention from `git log`: Conventional Commits, `fix(smf):` /
`test(smf):`, spec clauses in the body.)

## 7. Configuration changes

None. No new config keys, no change to any existing default.

## 8. Test plan

### Unit tests to add or extend

`src/smf_app/test/test_upf_graph.cpp` (GoogleTest, built with
`build/scripts/build_smf --tests`):

| What is asserted | Why |
|---|---|
| First `generate_qfi()` on a fresh graph returns 1 | the default flow keeps today's QFI |
| Add and remove one flow 200 times: every allocation succeeds and every QFI is in 2–63 | the exact scenario in the issue (the default flow holds 1) |
| 63 flows active → the 64th `generate_qfi()` returns 0; after one `release_qfi()` the next call succeeds and returns the released QFI | "QFI pool exhausted" means what it says |
| A QFI released while a higher QFI was the last handed out is not returned immediately | the wrap-around preference over lowest-free |
| `release_qfi(0)` and `release_qfi(64)` are no-ops and do not disturb allocation | out-of-range robustness |
| A copy of a graph with 1–3 in use allocates 4, not 1 | copy ctor carries the in-use set |
| Existing `register_pcc_rule_qfi` / `remove_qos_flow_edge` tests keep passing | no regression in the PCC-rule map cleanup that shares `release_qfi()` |

### Tier table

| Tier | Command | Verdict | Note |
|---|---|---|---|
| T0 build | `build/scripts/build_smf --clean --build-type Release --jobs` | CAN RUN | `src/common-src` submodule is not checked out; it is pinned to `f725043`, which is exactly the HEAD of the sibling `oai-cn5g-common-src` checkout, so it is populated from there for the build |
| T1 unit | `build/scripts/build_smf --tests` (GoogleTest + ctest, `smf_unit_tests`) | CAN RUN | full suite, plus a base-commit run if anything fails |
| T2 integration (no RF) | Robot suites from `oai-cn5g-fed/test/` (`qos_tests`, `smf_tests`) against a compose subset | SKIPPED | `probe_env.sh`: no docker daemon, no compose plugin, `robot` not installed |
| T3 container E2E | `oai-cn5g-fed/docker-compose/core-network.py` + `robot test/qos_tests.robot` with a locally built SMF image | NOT RUN (opt-in) | no `E2E` in the task, and no docker in this VM either way; full steps go into TESTING.md |
| T4 testbed / hardware | the issue's repro: PCF + AF (Npcf_PolicyAuthorization), one UE, 70 create/delete cycles, watching QFIs in the PFCP Session Modification Requests | LOCAL ONLY | always |

### Testbed scripts and new test cases

- `oai-cn5g-fed/test/qos_tests.robot` and the QoS tutorial referenced by the
  issue (oai-cn5g-fed PR 4, "tutorial A") are the natural home for an
  add/remove-loop case. Writing it needs the AF-side loop the issue describes,
  which is not in the fed repo today — see question 2.
- TESTING.md will carry the exact local T3/T4 steps, the expected QFI sequence
  in the PFCP traces, and the log lines that must *not* appear
  ("QFI pool exhausted", "RULE_PERMANENT_ERROR").

## 9. Risks and assumptions

- **Assumption:** QFI 0 stays the SMF's "unassigned" sentinel (it is compared
  against 0 in `smf_context.cpp`, `smf_procedure.cpp` and
  `select_upf_nodes()`), so the pool is 1–63 and `generate_qfi()` returning 0
  keeps meaning "none available".
- **Assumption:** nothing outside `upf_graph` reads the QFI generator; grep
  confirms `generate_qfi`/`release_qfi` are the only entry points.
- **Risk (named in the issue, not fixed here):** a reused QFI can still find a
  stale flow configured at the gNB/UE, because `develop` sends no N2 Modify
  Request for a PCF-initiated removal. Wrap-around ordering mitigates it but
  does not fix it; it goes into OPEN_ISSUES.md as a separate defect.
- Pre-existing, out of scope, to be listed in OPEN_ISSUES.md:
  - `uint_range_generator::get_uid()` in common-src writes
    `uid_generator == MIN;` (a discarded comparison) where it means `=`, so
    that template never wraps. It has no users today.
  - `session_handler::m_qfi_generator` is declared and never used.

## 10. Questions

1. **Scope — misdirected release in `select_upf_nodes()`.** At
   `smf_pfcp_association.cpp:1251` the QFI is allocated from `sub_graph_ptr`,
   but when `verify()` fails the unqualified `release_qfi(criteria.qfi)` at
   `:1263` runs on `this` — the global association graph — instead of the
   subgraph that allocated it. Today this is harmless (the subgraph is
   discarded, and the global graph's generator is never used for anything), and
   it stays harmless with the bounded allocator. Fix it as a third commit for
   clarity, or leave it and note it in OPEN_ISSUES.md?
   *Recommendation: leave it out of this fix and note it* — it is a different
   defect and the file is shared with the UPF-selection logic.
2. **Integration test case.** Should a `qos_tests.robot` case for the
   add/remove loop be part of this delivery as a second patch series against
   `oai-cn5g-fed`? It cannot be run in this VM (no docker, no robot), so it
   would ship unexecuted, and it needs an AF-side loop the fed repo does not
   have today. *Recommendation: no — keep the delivery to the SMF, and put the
   manual T3/T4 procedure in TESTING.md instead.*

## 11. Approval log

| Date | Who | Answers / decision |
|---|---|---|
| | | |
