# Plan — <SLUG>

Date: <DATE> · Profile: <profile or "none"> · Mode: <default | AUTOPILOT | E2E[:min]>

Written at the start of Phase 3 of /implement-feature, i.e. only after the
user approved the plan. In Phase 2 the plan exists as a chat message and
nothing else — this file is the approved version, with the answers folded in,
and it is the record that travels with the delivery.

---

## 1. Understanding

<3–5 sentences: what the task asks for, in your own words. What exists after
this work that doesn't today. If the task is ambiguous, say so here and raise
it under Questions — do not silently pick an interpretation.>

## 2. Repos and base commits

| Repo | Role | Branch | Base SHA |
|---|---|---|---|
| `<name>` | target / test | `<base branch>` | `<full sha>` |

## 3. Spec basis

| TS | Version | Clause | What it mandates |
|---|---|---|---|
| 38.331 | V<x.y.z> | 5.8.1.3 | <one line, from the converted spec — not from memory> |

> Every row must come from `scripts/spec_lookup.py`. If a clause could not be
> found, write "NOT FOUND" and raise it as a question.

## 4. Current state in the repo(s)

- Exists: <files/functions that already implement part of this>
- Missing: <the gap this task closes>
- Related prior work: <commits on the feature branch, earlier deliveries>

## 5. Design decisions

<For each real choice: the options, the trade-off, what you propose and why.
Anything where the spec allows more than one behavior belongs here.>

## 6. Commit plan

### `<repo-name>`

| # | Title | Files | Spec refs |
|---|---|---|---|
| 1 | <commit subject in the repo's style> | `path/a.c`, `path/b.h` | 38.331 §5.8.1.3 |
| 2 | <test commit, if tests are separate> | `tests/…` | — |

## 7. Configuration changes

| Key | Type | Default | Compatibility |
|---|---|---|---|
| `<config key>` | int | <value> | existing configs keep current behavior |

## 8. Test plan

### Unit tests to add or extend

| Module | Framework | What is asserted |
|---|---|---|
| `<file>` | <ctest / meson test / …> | <behavior, not implementation> |

### Tier table

| Tier | Command | Verdict | Note |
|---|---|---|---|
| T0 build | `<command>` | CAN RUN / MAYBE / LOCAL ONLY | from `scripts/probe_env.sh` |
| T1 unit | `<command>` | | |
| T2 integration (no RF) | `<command>` | | |
| T3 container E2E | `<command>` | NOT RUN (opt-in) unless `E2E` | time-box <n> min |
| T4 testbed / hardware | `<command>` | LOCAL ONLY | always |

### Testbed scripts and new test cases

- <which scripts/runbooks in the test repo cover this, and whether they need changes>
- <new test cases to add there — these are part of the delivery as a separate patch series>

## 9. Risks and assumptions

- <what could go wrong, what you are assuming that nobody confirmed>

## 10. Questions

1. <numbered, each answerable in one line; design choices with real trade-offs,
   scope boundaries, spec ambiguities>

> If there are no questions, write "None." — and if the task says `AUTOPILOT`,
> implementation may start right after posting the plan.

## 11. Approval log

| Date | Who | Answers / decision |
|---|---|---|
| <DATE> | <user> | <"go", plus the answers to the questions above> |
