# Open issues — <SLUG>

Everything a reviewer should know that is not visible in the diff.

## Assumptions

Things that were decided without confirmation. If one of these is wrong, the
affected part of the change is wrong too.

| # | Assumption | Why it was needed | What breaks if it's wrong |
|---|---|---|---|
| 1 | <…> | <…> | <…> |

## Spec ambiguities and the interpretation chosen

| TS / clause | What is ambiguous | Interpretation used | Why |
|---|---|---|---|
| 38.331 §<x> | <…> | <…> | <…> |

## Untested parts

| What | Why it wasn't tested | How to test it |
|---|---|---|
| <…> | <no framework / needs hardware / VM limits> | <…> |

## Pre-existing failures

Failures that also occur on the base commit — not caused by this change, not
fixed here.

| Test / build target | Fails on base? | Note |
|---|---|---|
| <…> | yes | <…> |

## Known limitations

- <what this change deliberately does not do yet>

## Follow-up suggestions

- <the natural next task, with enough detail to turn into a task description>
