# Changes — 2026-11-09-smf-qfi-reuse

What changed and why, commit by commit, with the spec clause behind each decision.

## Summary

Each PDU session's `upf_graph` drew QFIs from a monotonic
`oai::utils::uint_generator<uint8_t>`. The SMF already freed the QFI of a removed
QoS flow, but that generator's counter only ever counts up — `free_uid()` removes
the value from the in-use set and leaves the counter alone — so a released QFI
only came back after the 8 bit counter had wrapped through 256 values. Because a
QFI above 63 is rejected (it is a 6 bit field), the 63rd flow *ever added* to a
session failed with "QFI pool exhausted" and so did the next ~190 attempts, even
while only the default flow was active. This delivery replaces that generator
with a bounded per-session allocator over 1..63 that reuses released values, and
adds unit coverage for allocation, reuse, wrap-around and genuine exhaustion.
`oai::utils::uint_generator` itself is deliberately untouched.

## Per repo

### `oai-cn5g-smf`

#### 1. `fix(smf): reuse released QFIs within the 1-63 range per PDU session`

- **Purpose:** a released QFI becomes available to the session's next QoS flow,
  so "QFI pool exhausted" only happens when 63 flows are active at once.
- **Files:** `src/smf_app/smf_pfcp_association.hpp`,
  `src/smf_app/smf_pfcp_association.cpp`, `src/smf_app/smf_context.cpp`
- **Spec:**
  - TS 29.244 V18.10.0 §8.2.89 — the QFI IE carries the QFI value in bits 1–6 of
    octet 5 with bits 7–8 spare, so the value range is 6 bits (0–63).
  - TS 23.501 V18.12.0 §5.7.1.1 — "The QFI shall be unique within a PDU
    Session". Uniqueness is scoped to the session, so a QFI that belongs to none
    of its flows may be handed out again.
  - TS 23.501 V18.12.0 §5.7.1.1 — the QoS Flow of the default QoS rule "remains
    established throughout the lifetime of the PDU Session", so its QFI stays
    reserved for as long as the session lives.
- **Design notes:**
  - `upf_graph`'s `uint_generator<uint8_t> qfi_generator` is replaced by
    `QFI_MIN = 1`, `QFI_MAX = 63`, a `uint64_t qfi_in_use_` bitmask (bit
    `qfi - QFI_MIN`), a `uint8_t qfi_last_` initialised to `QFI_MAX`, and a
    dedicated `m_qfi_allocator` mutex. The old generator guarded itself with
    mutexes, so the replacement keeps its own rather than leaning on
    `graph_mutex` (which `release_qfi()` does not take today either).
  - `generate_qfi()` walks one lap of 63 candidates forward from `qfi_last_`,
    wrapping `QFI_MAX -> QFI_MIN`, and returns the first QFI whose bit is clear,
    or 0 when the lap finds all 63 in use.
  - `release_qfi()` clears the bit and **deliberately leaves `qfi_last_`
    alone**, so a released QFI is the last to come back rather than the first.
    Wrap-around was chosen over "lowest free QFI" because on `develop` a
    PCF-initiated flow removal produces no N2 Modify Request, so the gNB and the
    UE may still have the old flow configured under that QFI; a full lap gives
    them the most time to let go of it. It also preserves the 1, 2, 3, … order
    that existing traces show.
  - Because `qfi_last_` starts at `QFI_MAX`, the first allocation still returns
    1 — the default flow keeps the QFI it gets on `develop`, and nothing
    releases it (`commit_staged_flow_removals()` explicitly refuses to release
    the default flow), so its bit stays set for the session's lifetime.
  - The copy constructor now carries `qfi_in_use_` and `qfi_last_` under the
    source's lock. It could not copy the non-copyable `uint_generator`, so a
    copied graph used to begin allocating from scratch while serving the same
    PDU session — it would have reissued QFIs the original had already given
    away. This is needed for the allocator to be correct, not a drive-by change.
  - `generate_qfi()` can no longer return a value outside the QFI's range, so
    the `qfi_to_use > 63` branch in `smf_context.cpp` and its "out of range"
    `release_qfi()` are removed; the check is now just `== 0`. The operator-
    visible message "QFI pool exhausted, cannot add flow for rule '%s'" is kept
    verbatim and now means what it says.
  - **Not** changed: `oai::utils::uint_generator` in `common-src`. TEIDs, SEIDs
    and the PDR/FAR/QER/URR id generators share it, and there not handing a
    just-freed value straight back can be intended — a packet still in flight
    for a deleted TEID should not match a new session. A QFI only has to be
    unique among one session's active flows, and its range is too small for a
    counter.

#### 2. `test(smf): cover QFI allocation, reuse and exhaustion in upf_graph`

- **Purpose:** `test_upf_graph.cpp` exercised the PCC-rule-to-QFI map and the
  edge removal that accompany a release, but nothing ever called
  `generate_qfi()`, so the pool could run dry without a test noticing.
- **Files:** `src/smf_app/test/test_upf_graph.cpp`
- **Spec:** TS 23.501 V18.12.0 §5.7.1.1, TS 29.244 V18.10.0 §8.2.89
- **Design notes:** uses the file's existing GoogleTest style and its
  `make_test_graph()` helper; no new framework or helper was introduced.

## Tests added or extended

| Repo | File | Framework | What it asserts | Commit |
|---|---|---|---|---|
| `oai-cn5g-smf` | `src/smf_app/test/test_upf_graph.cpp` | GoogleTest + ctest (`-L unit`) | first allocation is 1 — the default flow's QFI | #2 |
| `oai-cn5g-smf` | same | same | 200 add/remove cycles all succeed with every QFI in 2..63, then 62 QFIs are free and the 63rd allocation fails | #2 |
| `oai-cn5g-smf` | same | same | 63 allocations yield 1..63 once each, the 64th returns 0, one release frees exactly one | #2 |
| `oai-cn5g-smf` | same | same | a released QFI returns only after a full lap, not immediately | #2 |
| `oai-cn5g-smf` | same | same | `release_qfi(0)`, `(64)`, `(255)` are no-ops; both range ends are releasable | #2 |
| `oai-cn5g-smf` | same | same | a copied graph does not reissue the original's QFIs | #2 |

Suite result: 46/46 passed, 6 of them new. See TESTING.md.

## Requirement traceability

| Requirement (from the issue's "Expected") | Spec clause | Code | Test |
|---|---|---|---|
| A released QFI can be used again for the session's next QoS flow | TS 23.501 §5.7.1.1 | `smf_pfcp_association.cpp:upf_graph::release_qfi()` / `generate_qfi()` | `test_upf_graph.cpp:GenerateQfi_ReusesReleasedQfiAcrossManyAddRemoveCycles` |
| A session only runs out of QFIs when 63 flows are active at once | TS 29.244 §8.2.89 | `smf_pfcp_association.cpp:upf_graph::generate_qfi()` (returns 0 only after a full lap) | `test_upf_graph.cpp:GenerateQfi_ExhaustsOnlyWhenAll63FlowsAreActive` |
| The QFI counter wraps within 1–63, not 1–255 | TS 29.244 §8.2.89 | `QFI_MIN`/`QFI_MAX` and the wrap in `generate_qfi()` | `test_upf_graph.cpp:GenerateQfi_WrapsRatherThanReturningAReleasedQfiAtOnce` |
| The default flow's QFI stays set for the session's lifetime | TS 23.501 §5.7.1.1 | `qfi_last_` initialised to `QFI_MAX` so the first allocation is 1; nothing releases the default flow | `test_upf_graph.cpp:GenerateQfi_FirstAllocationIsTheDefaultFlowQfi`, and the 200-cycle test's `ASSERT_GE(qfi, 2)` |
| "QFI pool exhausted" means what it says | — | `smf_context.cpp` check reduced to `== 0` | covered indirectly by the exhaustion test; the log line itself is not unit-testable — see OPEN_ISSUES.md |
| A released QFI is not handed back at once (RAN/UE still hold the old flow) | TS 23.501 §5.7.1.1 (uniqueness is the only constraint, so ordering is an implementation choice) | `release_qfi()` leaves `qfi_last_` alone | `test_upf_graph.cpp:GenerateQfi_WrapsRatherThanReturningAReleasedQfiAtOnce` |

## Configuration

None. No new config key, no change to any existing default, no change to any
`etc/*.conf` or Helm/compose value. Existing deployments behave as before except
that flow additions past the 62nd now succeed.

## Not changed on purpose

- `oai::utils::uint_generator` (`common-src/utils/uint_generator.hpp`) — shared
  with TEIDs, SEIDs and the PDR/FAR/QER/URR id generators; see the design note
  under commit 1. This delivery contains no `common-src` patch at all.
- The misdirected `release_qfi()` in `upf_graph::select_upf_nodes()`
  (`smf_pfcp_association.cpp:1263`) — allocation happens on `sub_graph_ptr`, the
  release on `this`. Harmless before and after this change; reported in
  OPEN_ISSUES.md rather than fixed here, per the approved plan.
- The absent N2 Modify Request for a PCF-initiated flow removal — the reason
  wrap-around ordering was chosen, but a separate defect. See OPEN_ISSUES.md.
- `session_handler::m_qfi_generator` — declared, never used. Left alone.
- No Robot test case was added to `oai-cn5g-fed`, per the approved plan: it
  could not be executed in this VM and needs an AF-side loop the fed repo does
  not have. The manual procedure is in TESTING.md (L2/L3) instead.
