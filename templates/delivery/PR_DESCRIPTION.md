# PR description — <SLUG>

Draft text for the pull request. Review it before posting; it is written from the
cloud run and may need the local test results added.

---

**Title:** <imperative, in the repo's style, e.g. "NR_RRC: add MCCH change notification">

---

## Summary

<2–4 sentences: what this adds, and why. Written for a maintainer who did not
read the task description.>

## Spec basis

| TS | Version | Clause | What it mandates |
|---|---|---|---|
| 38.331 | V<x.y.z> | <§> | <one line> |

## What changed

- <one bullet per commit, in order>

## Configuration

| Key | Default | Effect on existing deployments |
|---|---|---|
| `<key>` | <default> | <none — existing configs behave as before> |

## Testing done

- Build: <result>
- Unit tests: <n> tests, <m> new — <result>
- Integration: <result, or which tier and why not>
- Testbed / hardware: <what was run locally, with the result>

<Fill in the local results from TESTING.md before posting.>

## Notes for reviewers

- <the parts worth the closest look, and why>
- <anything deliberately left out, with the reason>

## Open points

- <from OPEN_ISSUES.md: anything a reviewer should weigh in on>
