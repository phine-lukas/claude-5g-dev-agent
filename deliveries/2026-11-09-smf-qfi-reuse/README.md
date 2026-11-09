# Delivery 2026-11-09-smf-qfi-reuse

Date: 2026-11-09 · Profile: oai-public · Status: **complete**

Each PDU session's `upf_graph` drew QFIs from a monotonic counter that never
handed a freed value back until it had wrapped through 256 values. Since the SMF
rejects a QFI above 63, the 63rd QoS flow *ever added* to a session failed with
"QFI pool exhausted" and so did the next ~190 attempts — even when only the
default flow was active, so an AF that adds and removes one flow on a UE
succeeded 62 times and then failed for the rest of the wrap. The patches replace
that counter with a bounded per-session allocator over 1..63 (a 64 bit in-use
mask plus the QFI handed out last) that reuses released values, wrapping 63 -> 1
so a released QFI is the last to come back rather than the first. Expect two
patches: the allocator itself, and six GoogleTest cases over allocation, reuse,
wrap-around and genuine exhaustion. `oai::utils::uint_generator` in `common-src`
is deliberately untouched, so there is no `common-src` patch.

## Repos

| Repo | Role | Base branch | Base SHA | Patches |
|---|---|---|---|---|
| `oai-cn5g-smf` | target | `claude/jolly-rubin-p7b75o` (session branch off `develop`) | `7bfe322` | 2 |

Total: **2** patch(es).

## Test summary

| Tier | Result |
|---|---|
| T0 build | **PASSED** — `smf compiled`, no new warnings |
| T1 unit | **PASSED** — 46 tests, 6 new, 0 failures |
| T2 integration | **SKIPPED** — no docker daemon, no compose plugin, `robot` absent |
| T3 container E2E | **NOT RUN (opt-in)** — no `E2E` in the task, and no docker in this VM |
| T4 testbed / hardware | **LOCAL ONLY** — the issue's AF add/remove loop, see TESTING.md L2 |

Details, including everything still to run locally, are in [TESTING.md](TESTING.md).

## Files

- [APPLY.md](APPLY.md) — how to apply the patch series, per repo
- [CHANGES.md](CHANGES.md) — what changed, mapped to spec clauses, with the traceability table
- [TESTING.md](TESTING.md) — tier table, cloud results, and the local steps that remain
- [OPEN_ISSUES.md](OPEN_ISSUES.md) — assumptions, untested parts, known gaps
- [PR_DESCRIPTION.md](PR_DESCRIPTION.md) — draft PR text for when you push
- [PLAN.md](PLAN.md) — the approved plan this was built from

## Repo details


### oai-cn5g-smf

- Remote: https://github.com/openairinterface/oai-cn5g-smf
- Agent branch: `claude/jolly-rubin-p7b75o` (local only, never pushed) — HEAD `967b9260fa6f295eca81d3065e5f6d62fe4bbe22`
- Base commit: `7bfe3220bc12ec52655ca355096a979b162ad260`
- Patches: `patches/oai-cn5g-smf/` (2)

Commits:

```
    967b926 test(smf): cover QFI allocation, reuse and exhaustion in upf_graph
    1ea6ace fix(smf): reuse released QFIs within the 1-63 range per PDU session
```

Diffstat:

```
     src/smf_app/smf_context.cpp          |   8 +--
     src/smf_app/smf_pfcp_association.cpp |  25 ++++++-
     src/smf_app/smf_pfcp_association.hpp |  45 +++++++++++-
     src/smf_app/test/test_upf_graph.cpp  | 130 +++++++++++++++++++++++++++++++++++
     4 files changed, 201 insertions(+), 7 deletions(-)
```
