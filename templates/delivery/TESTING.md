# Testing — <SLUG>

What was verified in the cloud, and exactly what remains to run locally.

Result values: `PASSED` · `FAILED-preexisting` (also fails on the base commit)
· `SKIPPED (<reason>)` (the VM could not run it) · `NOT RUN (opt-in)` (T3 without
`E2E` in the task) · `LOCAL ONLY` (testbed, RF, hardware — never run in the cloud).

A tier that could not run is never marked passed.

## Tier table

| Tier | Command | Where | Result | Duration |
|---|---|---|---|---|
| T0 build | `<command>` | cloud | <result> | <mm:ss> |
| T1 unit | `<command>` | cloud | <result> | <mm:ss> |
| T2 integration (no RF) | `<command>` | cloud | <result> | <mm:ss> |
| T3 container E2E | `<command>` | cloud | NOT RUN (opt-in) | — |
| T4 testbed / hardware | `<command>` | local | LOCAL ONLY | — |

VM capabilities behind the SKIPPED entries (from `scripts/probe_env.sh`):

```
<the relevant lines: docker, TUN, SCTP, privileges, cores/RAM/disk>
```

## Cloud results

### T0 — build

```
<command>
```

<Result, plus any new warnings. Short log excerpt only — the lines that matter.>

### T1 — unit tests

```
<command>
```

- Total: <n> tests, <m> of them new in this delivery
- New tests: `<test name>` — <what it asserts>
- <If anything failed: the same suite on the base commit, to separate regressions
  from pre-existing failures.>

### T2 — integration without RF

…

### T3 — container end-to-end

<Either the run, or: "NOT RUN (opt-in) — the task did not contain E2E. Full steps
to run it locally are below.">

## Fix log

Every failure that was caused by this change, and what happened to it.

| # | Tier | Failure | Root cause | Fix | Re-test |
|---|---|---|---|---|---|
| 1 | T1 | `<test>` asserted X, got Y | <one or two sentences> | `fixup!` into commit #<n> | T0–T1 green |

> Pre-existing and environmental failures do not belong here — they go in the
> tier table and in [OPEN_ISSUES.md](OPEN_ISSUES.md).

## Still to run locally

Copy-pasteable, in order. Each step says what to watch for and what counts as a pass.

### L1 — <name, e.g. "T3 container end-to-end">

**Why it is local:** <VM lacked TUN / not opted in / needs hardware>

**Prerequisites:** <built images, applied patches, config>

```bash
<exact commands, from the test repo's scripts and the repos' compose files>
```

**Watch for:**

- `<expected log line>` in `<which log>`
- `<expected message>` in the PCAP / on the interface

**Pass criteria:** <observable, checkable>

**If it fails:** <where to look first — which log, which counter, which PCAP filter>

### L2 — <testbed script>

…

## Regression checks

Things that worked before and must still work, with the command that shows it:

- <e.g. unicast PDU session establishment still completes> — `<command>`
