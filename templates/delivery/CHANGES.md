# Changes — <SLUG>

What changed and why, commit by commit, with the spec clause behind each decision.

## Summary

<One paragraph for a reviewer deciding whether to read on.>

## Per repo

### `<repo-name>`

#### 1. `<commit subject>`

- **Purpose:** <what this commit makes possible>
- **Files:** `path/a.c`, `path/b.h`
- **Spec:** TS 38.331 V<x.y.z> §5.8.1.3 — <what the clause requires>
- **Design notes:** <why it was done this way; alternatives rejected and why>

#### 2. `<commit subject>`

…

## Tests added or extended

| Repo | File | Framework | What it asserts | Commit |
|---|---|---|---|---|
| `<repo>` | `<test file>` | <ctest / meson / runme> | <behavior> | #<n> |

## Requirement traceability

Every acceptance criterion from the task, mapped to the clause that mandates it,
the code that implements it, and the test that proves it.

| Requirement | Spec clause | Code | Test |
|---|---|---|---|
| <from the task's acceptance criteria> | TS 38.331 §5.8.1.3 | `file.c:function()` | `test_file.c:case` |

> A row with no test needs a reason, in [OPEN_ISSUES.md](OPEN_ISSUES.md).

## Configuration

| Key | Type | Default | Effect on existing configs |
|---|---|---|---|
| `<key>` | int | <default> | <none — default preserves current behavior> |

## Not changed on purpose

- <things a reviewer might expect to see here and won't, with the reason>
