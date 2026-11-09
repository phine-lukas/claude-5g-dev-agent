# PR description — 2026-11-09-smf-qfi-reuse

Draft text for the pull request. Review it before posting; it is written from the
cloud run and may need the local test results added.

---

**Title:** fix(smf): reuse released QFIs within the 1-63 range per PDU session

---

## Summary

A PDU session's `upf_graph` allocated QFIs from a monotonic
`oai::utils::uint_generator<uint8_t>`. The SMF already freed the QFI of a removed
QoS flow, but that generator only ever counts up, so a freed value came back only
after its 8 bit counter had wrapped through 256 values. Since a QFI above 63 is
rejected (it is a 6 bit field), the 63rd flow *ever added* to a session failed
with "QFI pool exhausted" and so did the next ~190 attempts, even when only the
default flow was active. An AF that adds and removes one flow on a UE therefore
succeeded 62 times, then failed for the rest of the wrap. This replaces the
generator with a bounded per-session allocator over 1..63 that reuses released
QFIs, so the pool is exhausted only when 63 flows really are active at once.

## Spec basis

| TS | Version | Clause | What it mandates |
|---|---|---|---|
| 29.244 | V18.10.0 | 8.2.89 | The QFI IE carries the value in bits 1–6 of octet 5, bits 7–8 spare — a 6 bit range. |
| 23.501 | V18.12.0 | 5.7.1.1 | "The QFI shall be unique within a PDU Session" — uniqueness is session-scoped, so a QFI held by no flow may be reused. |
| 23.501 | V18.12.0 | 5.7.1.1 | The QoS Flow of the default QoS rule "remains established throughout the lifetime of the PDU Session" — its QFI stays reserved. |

## What changed

- `fix(smf): reuse released QFIs within the 1-63 range per PDU session` —
  `upf_graph`'s QFI generator becomes a 64 bit in-use mask plus the QFI handed
  out last, under its own mutex. `generate_qfi()` walks one lap forward from
  that value, wrapping 63 → 1, and returns the first free QFI or 0 after a full
  lap. `release_qfi()` clears the bit and leaves the last-handed-out value alone.
  The copy constructor now carries the allocator state (it could not copy the
  non-copyable generator, so a copied graph used to restart from scratch while
  serving the same session). The now-unreachable `> 63` branch in
  `smf_context.cpp` and its out-of-range release are removed.
- `test(smf): cover QFI allocation, reuse and exhaustion in upf_graph` — six
  GoogleTest cases; nothing previously called `generate_qfi()`.

## Configuration

None. No new key, no changed default; existing deployments behave as before
except that flow additions past the 62nd now succeed.

## Testing done

- Build: **PASSED** — `build_smf --clean --build-type Release --jobs`, no new
  warnings (the three in the log are pre-existing, all in `common-src`).
- Unit tests: **PASSED** — `build_smf --tests`, 46 tests, 6 new, 0 failures.
  The reported scenario is pinned by
  `GenerateQfi_ReusesReleasedQfiAcrossManyAddRemoveCycles`: 200 add/remove
  cycles, every allocation succeeds and every QFI lands in 2..63.
- Integration (Robot suites from `oai-cn5g-fed`): **not run** — the cloud VM had
  no docker daemon, no compose plugin and no `robot`.
- Testbed / hardware: **not run** — needs a PCF + AF driving
  Npcf_PolicyAuthorization.

<Fill in the local results from TESTING.md before posting — at minimum the
`docker build --target checks` run and the QoS Robot suite.>

## Notes for reviewers

- **Why wrap-around rather than lowest-free.** A released QFI is deliberately
  the last to come back. On `develop` a PCF-initiated flow removal produces no
  N2 Modify Request, so the gNB and the UE may still have the old flow
  configured under that QFI; a full lap of the range gives them the most time to
  let go of it. It also preserves the 1, 2, 3, … order existing traces show.
- **Why `uint_generator` itself is not changed.** TEIDs, SEIDs and the
  PDR/FAR/QER/URR id generators share it, and there not handing a just-freed
  value straight back can be intended — a packet still in flight for a deleted
  TEID should not match a new session. A QFI only has to be unique among one
  session's active flows, and its range is too small for a counter.
- The copy-constructor change is load-bearing, not cosmetic: without it a copied
  `upf_graph` reissues QFIs the original already gave away.
- The first allocation is still 1, so the default flow's QFI is unchanged.

## Open points

- A reused QFI can still meet a stale flow at the gNB and the UE, because the
  SMF builds no N2 PDU Session Resource Modify Request for a PCF-initiated
  removal. Wrap-around mitigates this; it does not fix it. Worth a separate
  issue — the relevant clauses of TS 23.502 and TS 38.413 were not verified in
  this run, so look them up before filing it.
- `upf_graph::select_upf_nodes()` allocates the QFI from the subgraph but
  releases it on the global association graph when `verify()` fails. Harmless
  today and unchanged here, but it reads as a bug.
- `uint_range_generator::get_uid()` in `common-src` writes `uid_generator == MIN;`
  where an assignment was meant, so that template never wraps. It has no users.
