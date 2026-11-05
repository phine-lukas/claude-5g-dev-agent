# Task template

Paste a filled-in copy of this into a cloud session, starting with
`/implement-feature`. Leave out sections that don't apply — but the more
precise the task, the fewer questions come back in Phase 2.

Anything you write here **overrides** the profile.

---

```markdown
/implement-feature

Profile: <name from profiles/, e.g. mbs-testbed — optional, bundles repos/branches/test tiers>

Target: <repo> @ <base branch>          # repeat per repo whose code changes
Test repo: <repo> @ <branch> — <which scripts/runbooks to use; whether to add test cases>

Component: <gNB, nrUE, CU, DU, AMF, SMF, MB-SMF, UPF, MB-UPF, …>

Goal:
<2–5 sentences. What should exist afterwards that doesn't today, and why.>

Scope – in:
- <the parts you want touched>

Scope – out:
- <explicitly not now; this is what stops scope creep>

Spec references:
- TS <number> clause <x.y.z> — <what it mandates>, Rel-<n>
# If you don't know the clause, name the spec and the procedure; Phase 0/1 will find it.

Existing work to build on:
- <branches, earlier deliveries, files, prior commits on the feature branch>

Acceptance criteria:
- <observable, checkable statements: a message is sent, an IE is encoded, a log line appears>

Test expectations:
- Unit tests: <which modules should get new/extended tests>
- Cloud: <which tiers must pass, e.g. T0–T1 mandatory, T2 if possible>
- Local: <which testbed scripts/runbooks you will run yourself>

Constraints:
- <config backwards compatibility, no API breaks, no new dependencies, …>

Mode: <empty = plan approval, no T3>
# Keywords, combinable:
#   AUTOPILOT      skip plan approval *only* when the agent has zero questions
#   E2E            run T3 container end-to-end tests in the cloud
#   E2E:<minutes>  same, with an explicit time-box (default: profile's timebox_min, else 45)
```

---

## Example (filled in)

```markdown
/implement-feature

Profile: mbs-testbed

Target: openairinterface5g-private @ mbs-phase-a
Test repo: frq-adsat-phine @ main — use tests/mbs-tn.md and scripts/test-mbs.sh;
add a runbook step for the new behavior

Component: gNB (RRC + MAC)

Goal:
Implement MCCH change notification for MBS broadcast. Today the gNB sends a static
MCCH and never signals changes, so a UE that joins after a configuration change keeps
stale MTCH parameters. The gNB should signal MCCH changes on PDCCH with the MCCH-RNTI
and apply the new configuration at the next modification period boundary.

Scope – in:
- MCCH change notification DCI and its scheduling in the MAC
- MCCH modification period bookkeeping in the RRC
- Config keys for the modification/repetition period

Scope – out:
- nrUE-side reception of the notification (separate task)
- Any change to unicast scheduling

Spec references:
- TS 38.331 clause 5.8.1.3 — MCCH change notification, Rel-17
- TS 38.321 clause 5.x — MBS MAC handling, Rel-17
- TS 38.212 / 38.213 — DCI format 4_0 on MCCH-RNTI, Rel-17

Existing work to build on:
- mbs-phase-a already carries the MCCH construction and MTCH scheduling commits

Acceptance criteria:
- The gNB transmits a change-notification DCI in each repetition period after an MCCH change
- The new MCCH content is applied exactly at the next modification period boundary
- Periods are configurable, with the current behavior as the default

Test expectations:
- Unit tests: extend the MCCH encoding tests and add scheduling-decision tests for the period boundary
- Cloud: T0 and T1 must pass; T2 if a relevant simulator exists
- Local: tests/mbs-tn.md end-to-end on the testbed

Constraints:
- Existing gNB configuration files must keep working unchanged
- No new external dependencies

Mode:
```
