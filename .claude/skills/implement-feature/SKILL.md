---
name: implement-feature
description: Implement a 3GPP feature or change in a 5G software repository (OpenAirInterface RAN/CN, 5G-MAG Open5GS MBS core, private forks on custom branches) from a task description, testing with the repos' own test suites and private testbed repos. Ensures required 3GPP specs are available, produces a plan with questions and waits for approval, implements as a clean commit series with extended tests, runs every test tier the cloud VM supports, and exports a delivery package (patch files per repo + apply/test/change docs) instead of pushing. Use whenever the user asks to implement, extend or fix a standards-based feature.
---

# Implement Feature (cloud workflow)

You work in phases. Never skip Phase 2. Never push to target or test repos.
Before ending ANY turn: `scripts/set_status.sh <STATE> "<short message>"`
States: PLAN_READY, QUESTION, BLOCKED, DELIVERED, FAILED.

## Inputs
The user message (ideally following `templates/TASK_TEMPLATE.md`). Identify:
- profile name, if given (`profiles/<name>.yaml`); task values override it
- target repo(s) and the **base branch per repo** (e.g. private OAI fork
  @ `mbs-phase-a`) — check out that branch before anything else; if it
  doesn't exist, STOP and ask
- test repo(s) and the test scripts/entry points to use
- component (gNB, nrUE, CU/DU, SMF, MB-SMF, AMF, UPF, MB-UPF…), feature
  scope, spec references, acceptance criteria
- whether the keyword `AUTOPILOT` is present (see Phase 2)
- whether the keyword `E2E` is present (optionally `E2E:<minutes>` as
  time-box) — this opts in to T3 container end-to-end tests (Phase 4).
  Without it, T3 is NOT run in the cloud, regardless of the profile
If repos named in the task aren't present in the session, say which are
missing and ask the user to add them to the session (or provide URLs).

## Phase 0 – Specs
1. Determine which specs the task needs: start from the user's references,
   then add from `specs/manifest.yaml` by tag (e.g. `mbs`, `ran`, `cn`).
2. Run `python3 scripts/ensure_specs.py --tags <tags> [--spec <id> ...]`.
   It downloads + converts anything missing and prints what it added.
3. If a needed spec is not in the manifest, add an entry to the manifest and
   rerun. If download fails (network), report it as BLOCKED with the exact
   error and ask the user how to proceed.
4. Newly converted specs become part of the delivery commit (Phase 5).

## Phase 1 – Recon
1. Read the relevant spec clauses (use `scripts/spec_lookup.py` for clause
   numbers, keywords, ASN.1 type names). Collect exact clause references.
2. Load the matching stack skill(s) (oai-ran, oai-cn, open5gs-mbs) and the
   profile. A private fork inherits the stack skill of its upstream, but
   always prefer what the fork itself documents (README, docs, CI files).
3. Inspect each target repo: record branch and base commit
   (`git rev-parse HEAD`). Find existing code related to the feature (grep
   for IE names, RNTI types, procedure names, config keys). Determine what
   already exists vs. what is missing. On feature branches like
   `mbs-phase-a`, read `git log <upstream-main>..HEAD` to understand prior
   work on the feature.
4. Inventory tests: the target repo's unit test framework and existing
   tests near the affected code; integration/robot tests; CI definitions
   (they reveal how tests are really run). Inspect the test repo: what each
   script does, what it needs (hardware, lab hosts, docker, root), and
   which parts could run in a VM.
5. Run `scripts/probe_env.sh` and record what this VM can do (docker,
   compose, privileged, TUN/SCTP, cores/RAM/disk, network). Map each test
   tier from the profile to: CAN RUN / MAYBE / LOCAL ONLY. Do not start
   long builds yet.

## Phase 2 – Plan and questions (MANDATORY STOP)
1. Write the plan to `deliveries/<slug>/PLAN.md` using `templates/PLAN.md`.
   `<slug>` = `YYYY-MM-DD-<component>-<short-feature-name>`, kebab-case.
2. Post the plan IN THE CHAT (condensed, but complete), containing:
   - Your understanding of the task in 3–5 sentences
   - Spec basis: list of TS/clause references
   - Current state in the repo (what exists, what's missing)
   - Proposed commit series: one line per commit, with files touched
   - Configuration changes (new config keys, defaults)
   - Test plan: which unit tests you will add/extend; the test-tier table
     (tier → command → CAN RUN / MAYBE / LOCAL ONLY); which testbed scripts
     from the test repo apply locally, and whether they need changes
     (new test cases for the feature are part of the delivery)
   - Risks and assumptions
   - **Numbered questions** — anything ambiguous in the task or spec,
     design choices with real trade-offs, scope boundaries
3. Then `scripts/set_status.sh PLAN_READY "<slug>: plan ready, N questions"`
   (or QUESTION if questions exist) and END YOUR TURN. Do not write code.
4. Continue only after the user replies with approval ("go", "approved",
   answers + "go", etc.). Incorporate answers into PLAN.md.
5. Exception: if the task contains `AUTOPILOT` AND you have zero questions,
   post the plan and continue directly. If you have any question, stop anyway.

## Phase 3 – Implementation
1. In every repo you change (targets, and the test repo if you add test
   cases), create a local branch `agent/<slug>` from its base commit.
   These branches are never pushed.
2. Implement commit by commit as planned. Each commit must build on its own
   where reasonably possible, have a focused scope, and a message that
   follows the repo's existing conventions (inspect `git log`),
   referencing spec clauses in the body.
3. Tests are part of the work, not an afterthought:
   - Extend existing unit tests for every changed function/module with
     testable logic (encoding/decoding, scheduling decisions, state
     machines, config parsing, message builders). Put them in the commit
     that introduces the behavior, or in a directly following test commit.
   - Use the repo's existing framework and patterns; don't introduce a new
     framework without asking.
   - If the repo has no unit tests around the affected code, say so in the
     plan and propose a minimal addition — don't add one unasked.
   - Where the test repo has test cases for related features, add or adapt
     test cases for the new behavior there (separate patch series).
4. Follow repo style. If the repo has `.clang-format`, format changed lines
   (`git clang-format <base>` or equivalent).
5. Prefer extending existing structures over parallel new ones. Do not
   refactor unrelated code.
6. STOP and ask (status QUESTION or BLOCKED, then end turn) when:
   - The spec is ambiguous or clauses conflict, and the choice matters
   - The change requires touching shared infrastructure beyond the plan
     (schedulers core, ITTI/messaging, config framework, common libs)
   - You deviate from the approved commit plan in a non-trivial way
   - The build or a test still fails after 3 genuine fix attempts
   - Something is missing (dependency, spec, access) that you can't resolve
   When asking, state what you've tried, the options, and your recommendation.

## Phase 4 – Verification in the cloud (go as far as the VM allows)
Work through the tiers in order. A tier failing because of YOUR change goes
back to implementation via the fix loop below. A tier that can't run
for environmental reasons is marked SKIPPED with the reason and moved to
local testing — never mark it passed.

- T0 Build: all affected targets in all changed repos. No new warnings.
- T1 Unit tests: the full relevant suite incl. your new tests. Also run
  the suite on the base commit if anything fails, to separate
  pre-existing failures from regressions.
- T2 Component/integration tests without RF: e.g. OAI CN robot tests or
  test suites from the federation repo, Open5GS test programs, PHY/MAC
  simulators and unit-level simulators of the RAN repo — whatever the
  profile and stack skills list as T2.
- T3 End-to-end in containers (**opt-in**): e.g. CN via docker-compose +
  gNB/nrUE in rfsimulator, incl. MBS session setup. Run it only if the
  task contains `E2E` (or the user enables it when answering the plan)
  AND probe_env says docker/compose, TUN and enough resources are
  available. Time-box: `E2E:<minutes>` from the task, else the profile's
  `timebox_min`, else 45 min. If it doesn't come up, record what happened
  and move on. Without opt-in, mark T3 as `NOT RUN (opt-in)` and write
  the full T3 steps into TESTING.md for local execution. If you think the
  feature really warrants T3 in the cloud, suggest it in the plan, but
  don't run it unasked.
- T4 Testbed/hardware: never in the cloud. Prepare exact steps with the
  test repo's scripts for TESTING.md, plus any new test cases.

Record every command, its duration and result, and keep relevant log
excerpts (short) for TESTING.md. Before T3, rebuild containers/images from
your branch, not from public images, or the test is meaningless.

### Fix loop (Phase 4 → Phase 3 → Phase 4)
When a tier fails, classify the failure first:
- **Pre-existing**: also fails on the base commit → don't fix, document it
  in TESTING.md and OPEN_ISSUES.md, continue.
- **Environmental**: VM limits (no privileges, TUN, SCTP, resources,
  network) → mark SKIPPED with the reason, continue.
- **Caused by the change** → go back to Phase 3:
  1. Diagnose from logs/core dumps/PCAPs; state the root cause in one or
     two sentences before changing code.
  2. Fix it in the commit that introduced the bug: make a
     `fixup! <commit title>` commit, and before delivery run
     `git rebase -i --autosquash <base>` so the series stays clean. Only
     genuinely new work gets a new commit.
  3. If the bug was found by T2/T3 but not caught by T1, add a unit test
     that reproduces it (where testable), so it can't come back silently.
  4. Re-run from T0 up to and including the failed tier; lower tiers must
     still pass after the fix.
  5. If the test itself seems wrong (its expectation contradicts the spec
     or the approved plan), don't change the test to make it pass: STOP and
     ask, citing the clause.

Limits: max 3 genuine fix attempts per distinct failure, and STOP and ask
whenever a fix would deviate from the approved plan (other design, other
files/modules, interface or config changes). Every fix cycle is logged in
TESTING.md (failure → root cause → fix commit → re-test result), so the
reviewer sees what went wrong along the way.

## Phase 5 – Delivery
1. `scripts/make_delivery.sh <slug> <repo-path>:<base-sha> [<repo-path>:<base-sha> ...]`
   generates `deliveries/<slug>/patches/<repo-name>/*.patch` for every
   changed repo (targets and test repo) via `git format-patch --base`,
   and copies the doc templates.
2. Fill in every doc in `deliveries/<slug>/` (see templates). TESTING.md
   holds the tier table with cloud results and concrete, copy-pasteable
   local steps for everything SKIPPED or T4 (using the test repo's scripts
   and the repos' tutorials/docker-compose files), expected log lines /
   messages, and pass criteria. CHANGES.md maps each change to spec
   clauses and lists the tests added. OPEN_ISSUES.md lists assumptions,
   untested parts, and known gaps.
3. Verify each patch series applies cleanly on its base commit in a
   temporary worktree: `git worktree add /tmp/verify-<repo> <base-sha>` →
   `git am` → remove the worktree.
4. `scripts/push_delivery.sh <slug>` commits the delivery folder (and any
   newly converted specs) on branch `claude/delivery-<slug>` of this toolkit
   repo and pushes it.
5. Post a final summary in chat: delivery path + branch, commit list, what
   was verified, what needs local testing, open issues.
6. `scripts/set_status.sh DELIVERED "<slug>: N patches ready"` and end.
   On unrecoverable failure: still deliver what exists (marked partial) and
   use FAILED.
