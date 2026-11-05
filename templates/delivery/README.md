# Delivery <SLUG>

Date: <DATE> · Profile: <profile or "none"> · Status: **<complete | partial>**

<One paragraph: what this delivery implements, in plain language. What a reviewer
should expect to see when they read the patches.>

## Repos

| Repo | Role | Base branch | Base SHA | Patches |
|---|---|---|---|---|
<REPO_TABLE_ROWS>

Total: **<N_PATCHES>** patch(es).

## Test summary

| Tier | Result |
|---|---|
| T0 build | <PASSED / FAILED / SKIPPED (reason)> |
| T1 unit | <PASSED (n tests, m new) / …> |
| T2 integration | <…> |
| T3 container E2E | <PASSED / NOT RUN (opt-in) / SKIPPED (reason)> |
| T4 testbed / hardware | LOCAL ONLY |

Details, including everything still to run locally, are in [TESTING.md](TESTING.md).

## Files

- [APPLY.md](APPLY.md) — how to apply the patch series, per repo
- [CHANGES.md](CHANGES.md) — what changed, mapped to spec clauses, with the traceability table
- [TESTING.md](TESTING.md) — tier table, cloud results, and the local steps that remain
- [OPEN_ISSUES.md](OPEN_ISSUES.md) — assumptions, untested parts, known gaps
- [PR_DESCRIPTION.md](PR_DESCRIPTION.md) — draft PR text for when you push
- [PLAN.md](PLAN.md) — the approved plan this was built from

## Repo details

<REPO_SECTIONS>
