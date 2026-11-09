# Build Instructions: `5g-dev-agent` Toolkit Repository

> **How to use this file:** Create an empty **private** GitHub repo named `5g-dev-agent`, clone it locally, open Claude Code in it, and say:
> *"Read `SETUP_INSTRUCTIONS.md` and build this repository exactly as specified. Ask me before deviating from the spec."*
> (Save this file as `SETUP_INSTRUCTIONS.md` in the repo root first.)

---

## 0. Instructions for the builder (Claude Code)

You are building a private toolkit repository that lets a developer delegate 3GPP feature implementations to Claude Code running in the cloud. It is **not limited to OpenAirInterface**: it works with any set of repos — public OAI repos (RAN and 5G Core), private forks on custom base branches, other 5G stacks (e.g. the 5G-MAG Open5GS-based MBS core), and private testbed repos containing test scripts. The combination of repos, base branches, build commands and test tiers for a given project is described in a **project profile** (§5.4).

The cloud agent **never pushes to target repositories**. Instead it produces a *delivery package* (patch series per repo + documentation) and pushes that package to this toolkit repo only. The developer later applies the package locally with a second skill.

The cloud agent must test as much as the cloud VM allows: always build, always extend and run unit tests where a test framework exists, and run integration tests (e.g. robot tests, docker-compose based setups, rfsimulator) when the environment supports them. Only what truly can't run in the VM (hardware testbeds, RF, lab networks) is deferred to local testing.

Rules while building:

- Follow the structure in §2 exactly. Where this document gives full file contents, use them verbatim (fix only obvious errors and tell the user what you changed).
- Where this document gives only requirements (scripts), implement them in Python 3 (standard library + `pyyaml` + `requests` only) or Bash, and **test them** before finishing.
- 3GPP FTP URLs and file naming must be verified live (fetch the directory listing) rather than assumed. If anything doesn't match this spec, stop and ask.
- Do not commit any downloaded 3GPP zip/docx files. Converted Markdown is committed (see §5).
- At the end, run the self-check in §10 and report results.

---

## 1. Concept overview

```
┌────────────────────────── CLOUD (claude.ai/code) ──────────────────────────┐
│ Session repos: 5g-dev-agent + target repo(s) + test repo(s)                │
│   e.g. private OAI fork @ mbs-phase-a  +  private testbed repo             │
│                                                                            │
│ /implement-feature [profile] <task>                                        │
│   Phase 0  ensure specs (fetch + convert missing ones)                     │
│   Phase 1  recon: specs, code, test repo, probe VM capabilities            │
│   Phase 2  PLAN + QUESTIONS in chat  ──► STOP, wait for "go"               │
│   Phase 3  implement + extend unit tests (stop + ask if blocked)           │
│   Phase 4  test tiers: build → unit → integration/robot/docker → as far    │
│            as the VM allows; the rest documented for local testing         │
│   Phase 5  export delivery package ──► push to 5g-dev-agent ONLY, notify   │
└────────────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌────────────────────────────── LOCAL (IDE) ─────────────────────────────────┐
│ /apply-delivery <slug>                                                     │
│   git am patches (per repo) → build → remaining tests from TESTING.md      │
│   (testbed scripts, hardware, RF) → debug/fix                              │
│   developer pushes + opens PR manually                                     │
└────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Repository structure

```
5g-dev-agent/
├── README.md                         # §9 – deployment & usage guide
├── SETUP_INSTRUCTIONS.md             # this file
├── CLAUDE.md                         # §3 – always-loaded working rules
├── .gitignore
├── .toolkit-root                     # marker file (empty), used by scripts
├── .claude/
│   ├── settings.json                 # §7 – hooks
│   ├── hooks/
│   │   └── push_guard.py             # §7.1
│   └── skills/
│       ├── implement-feature/
│       │   └── SKILL.md              # §4.1
│       ├── apply-delivery/
│       │   └── SKILL.md              # §4.2
│       ├── oai-ran/
│       │   └── SKILL.md              # §4.3 – OAI RAN repo knowledge
│       ├── oai-cn/
│       │   └── SKILL.md              # §4.4 – OAI 5G Core repo knowledge
│       └── open5gs-mbs/
│           └── SKILL.md              # §4.5 – 5G-MAG Open5GS MBS core knowledge
├── profiles/
│   ├── README.md                     # how to write a profile
│   ├── oai-public.yaml               # §5.4 – public OAI RAN + CN + fed repo
│   └── mbs-testbed.yaml              # §5.4 – private fork + 5G-MAG CN + testbed repo
├── specs/
│   ├── manifest.yaml                 # §5.1
│   ├── INDEX.md                      # generated: all converted specs
│   └── <spec>/<version>/...          # generated: converted Markdown (§5.3)
├── scripts/
│   ├── ensure_specs.py               # §6.1
│   ├── spec_lookup.py                # §6.2
│   ├── make_delivery.sh              # §6.3
│   ├── push_delivery.sh              # §6.4
│   ├── push_toolkit.sh               # §6.4b – toolkit changes to main
│   ├── cloud_setup.sh                # §6.5 – pasted into cloud environment
│   └── probe_env.sh                  # §6.6 – what can this VM run?
├── templates/
│   ├── TASK_TEMPLATE.md              # §8.1 – how to write a task
│   ├── PLAN.md                       # §8.2
│   └── delivery/
│       ├── README.md                 # §8.3
│       ├── APPLY.md
│       ├── CHANGES.md
│       ├── TESTING.md
│       ├── OPEN_ISSUES.md
│       └── PR_DESCRIPTION.md
└── deliveries/
    └── .gitkeep                      # deliveries land here (§8.3)
```

`.gitignore` must contain at least:

```
specs/**/raw/
*.zip
*.docx
*.doc
__pycache__/
```

---

## 3. `CLAUDE.md` (full content)

````markdown
# 5g-dev-agent – working rules

This repo is a toolkit for implementing 3GPP features in 5G software stacks
(OpenAirInterface RAN/CN, 5G-MAG Open5GS MBS core, private forks) and testing
them with existing test suites and private testbed repos. It is opened
together with target repos (code to change) and test repos (test scripts)
in the same session. Project profiles in `profiles/` describe which repos,
base branches, build commands and test tiers belong together.

## Hard rules
1. NEVER run `git push` directly. NEVER push to any target or test repo.
   The only allowed push is `scripts/push_delivery.sh`, which pushes this
   toolkit repo's delivery branch. A hook enforces this.
2. NEVER open PRs/MRs, create releases, or modify remote branches of other repos.
3. Test repos may contain lab IPs, hostnames or credentials: never copy
   them into deliveries, logs or chat beyond what is needed; never try to
   reach lab infrastructure from the cloud.
4. Always plan before coding and wait for explicit approval (see the
   implement-feature skill). Questions go into the chat, then STOP.
5. New or changed behavior gets tests: extend the existing unit/integration
   tests of the target repo wherever a framework exists.
6. Spec claims must cite TS number, version and clause. If you cannot find
   the clause, say so; do not paraphrase from memory.
7. Notify only when a run is over: once the delivery is pushed, or once you
   stop for good, send ONE `PushNotification` (one line, e.g. "mbs-mcch:
   delivery pushed, 6 patches" / "mbs-mcch: stopped, build broken"). No
   notification for plans, questions or progress — those are chat only.

## Locating things
- Toolkit root: the directory containing `.toolkit-root`.
- Specs: `specs/INDEX.md`, search with `scripts/spec_lookup.py`.
- Profiles: `profiles/*.yaml`.
- Target and test repos: sibling directories of the toolkit root, or ask.

## Skills
- /implement-feature – cloud workflow: specs → plan → ask → implement → test → deliver
- /apply-delivery    – local workflow: apply patches, build, test, fix
- oai-ran, oai-cn, open5gs-mbs – reference knowledge about the stacks
````

---

## 4. Skills

### 4.1 `.claude/skills/implement-feature/SKILL.md` (full content)

````markdown
---
name: implement-feature
description: Implement a 3GPP feature or change in a 5G software repository (OpenAirInterface RAN/CN, 5G-MAG Open5GS MBS core, private forks on custom branches) from a task description, testing with the repos' own test suites and private testbed repos. Ensures required 3GPP specs are available, produces a plan with questions and waits for approval, implements as a clean commit series with extended tests, runs every test tier the cloud VM supports, and exports a delivery package (patch files per repo + apply/test/change docs) instead of pushing. Use whenever the user asks to implement, extend or fix a standards-based feature.
---

# Implement Feature (cloud workflow)

You work in phases. Never skip Phase 2. Never push to target or test repos.
Notifications: one `PushNotification` when the run is over (delivered, or
stopped for good) — never for plans, questions or progress.

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
This phase writes nothing to disk and commits nothing. The plan is a chat
message, so the user can read it and decide whether the run starts at all; if
it doesn't, no repo has been touched.

1. Post the plan IN THE CHAT, complete — this is its only copy. Follow the
   section order of `templates/PLAN.md`, kept compact (tables stay tables,
   prose stays short):
   - Your understanding of the task in 3–5 sentences
   - Repos and base commits (repo, role, branch, base SHA)
   - Spec basis: TS, version, clause, what it mandates — every row from
     `scripts/spec_lookup.py`, never from memory
   - Current state in the repo(s): what exists, what's missing
   - Design decisions: for each real choice, the options and what you propose
   - Proposed commit series per repo: one line per commit, with files touched
   - Configuration changes (new config keys, defaults, compatibility)
   - Test plan: which unit tests you will add/extend; the test-tier table
     (tier → command → CAN RUN / MAYBE / LOCAL ONLY); which testbed scripts
     from the test repo apply locally, and whether they need changes
     (new test cases for the feature are part of the delivery)
   - Risks and assumptions
   - **Numbered questions** — anything ambiguous in the task or spec,
     design choices with real trade-offs, scope boundaries
2. Then END YOUR TURN — no file, no branch, no notification. Do not write code.
3. Continue only after the user replies with approval ("go", "approved",
   answers + "go", etc.). If the answer is "no" or the plan needs rework, the
   run stops or replans here, with nothing to clean up.
4. Exception: if the task contains `AUTOPILOT` AND you have zero questions,
   post the plan and continue directly. If you have any question, stop anyway.

## Phase 3 – Implementation
1. First, record the approved plan: write `deliveries/<slug>/PLAN.md` from
   `templates/PLAN.md` — the plan as posted in the chat, with the user's
   answers folded in and the approval log filled in. `<slug>` =
   `YYYY-MM-DD-<component>-<short-feature-name>`, kebab-case. This is the
   first thing the run writes to disk; it travels with the delivery and is
   committed only in Phase 5.
2. In every repo you change (targets, and the test repo if you add test
   cases), create a local branch `agent/<slug>` from its base commit.
   These branches are never pushed.
3. Implement commit by commit as planned. Each commit must build on its own
   where reasonably possible, have a focused scope, and a message that
   follows the repo's existing conventions (inspect `git log`),
   referencing spec clauses in the body.
4. Tests are part of the work, not an afterthought:
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
5. Follow repo style. If the repo has `.clang-format`, format changed lines
   (`git clang-format <base>` or equivalent).
6. Prefer extending existing structures over parallel new ones. Do not
   refactor unrelated code.
7. STOP and ask in the chat (then end turn, no notification) when:
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
6. Send one `PushNotification`: `<slug>: N patches ready, <branch>` — then
   end. On unrecoverable failure: still deliver what exists (marked partial),
   and notify with what went wrong instead (`<slug>: stopped, <reason>`).
````

### 4.2 `.claude/skills/apply-delivery/SKILL.md` (full content)

````markdown
---
name: apply-delivery
description: Apply a delivery package produced by the implement-feature workflow to a local OpenAirInterface checkout. Fetches the delivery from the 5g-dev-agent repo, applies the patch series as commits with git am, builds, guides through the local test steps in TESTING.md, and helps debug and fix. Use when the user says apply/test/review a delivery, gives a delivery slug, or pastes a cloud session result.
---

# Apply Delivery (local workflow)

Never push. Never open PRs. The user does that manually.

## 1. Locate the delivery
1. Find the toolkit repo: `$DEV_AGENT_HOME`, else `~/5g-dev-agent`, else ask.
2. In the toolkit repo: `git fetch origin` and check out or read
   `claude/delivery-<slug>` (the user gives the slug, the branch name, or
   pasted cloud output from which you extract it). Read `README.md`,
   `CHANGES.md`, `OPEN_ISSUES.md`, `APPLY.md` of the delivery.
3. Summarize to the user in a few lines: what it does, number of patches,
   base commit, open issues. Ask before proceeding if open issues look
   blocking.

## 2. Apply
The delivery has one patch series per repo in `patches/<repo-name>/`.
APPLY.md lists each repo with its base branch and base SHA. For each repo:
1. Find the local checkout (current directory, a sibling directory, the
   path in the profile's `local_path`, or ask). Ensure a clean working
   tree; if not, ask the user (stash or abort).
2. Check whether the base commit exists locally (`git cat-file -e <sha>`);
   fetch if needed (it may be on a private branch like `mbs-phase-a`).
3. Create `feature/<slug>` at the base commit and run
   `git am -3 <delivery>/patches/<repo-name>/*.patch`.
4. If the user wants it on the current upstream instead: apply on base
   first, then `git rebase` onto the requested branch.
5. On conflicts: stop, show the conflict, propose a resolution, and wait
   for confirmation before continuing (`git am --continue`).

## 3. Build
Use the build commands from TESTING.md (fall back to the oai-ran / oai-cn
skill). Report warnings/errors related to changed files.

## 4. Test
Start with the tiers marked SKIPPED or NOT RUN (opt-in) in the cloud, then T4 (testbed scripts
from the test repo). Re-run T1 locally as a sanity check. Before starting
anything that launches containers, network namespaces, USRPs, touches lab
hosts, or needs sudo, show the command and ask for confirmation. Collect
logs, check the expected log lines/messages, and report pass/fail per step.

## 5. Fix
- Fixes for a specific patch: create `fixup!` commits targeting that commit
  so the user can `git rebase -i --autosquash` later. New functionality goes
  in new commits.
- Keep a running list of fixes.

## 6. Wrap up
1. Update the delivery's `PR_DESCRIPTION.md` locally (do not push the toolkit
   repo unless asked) with test results and fixes.
2. Tell the user the branch is ready, show `git log --oneline <base>..HEAD`,
   and remind them to squash fixups, push, and open the PR themselves.
````

### 4.3 `.claude/skills/oai-ran/SKILL.md` (requirements)

Write this skill by **inspecting the actual `openairinterface5g` repository** (clone it to a temp dir if not present; the user can point you to it). It must contain, with real paths verified in the repo:

- `description`: reference knowledge for the openairinterface5g repo (gNB, nrUE, CU/DU split, RRC/MAC/RLC/PDCP/PHY layout, build, test).
- Directory map of the relevant layers (RRC, MAC scheduler, PHY, F1AP, NGAP, config files) with one line each.
- Where ASN.1 definitions (RRC, F1AP, NGAP) live and how code is generated from them; which 38.331 / 38.473 / 38.413 version the repo's ASN.1 corresponds to (find it; this decides which spec version to use).
- Build: dependency install and build commands from the repo's build documentation (e.g. `doc/BUILD.md`), including the rfsimulator build variant and the fastest incremental rebuild. Mark which steps are realistic in a cloud VM.
- Unit tests: how to enable and run them (CMake option / ctest), where existing tests live per layer, and the pattern for adding a new one.
- Test tiers (T0–T4 as defined in implement-feature Phase 4) with concrete commands: e.g. which PHY/MAC simulators and unit-level simulators exist (T2), rfsimulator gNB+nrUE tutorials and CI docker-compose setups incl. how to attach a core network (T3), and their resource needs.
- What the CI pipelines run (from the CI configuration in the repo) — use it as the reference for "how tests are really run".
- Coding conventions: formatting (`.clang-format`), logging macros, config parameter definition pattern, commit message style (from `git log`).
- MBS-specific: existing MBS-related code (search for MBS, MCCH, MTCH, G-RNTI, G-CS-RNTI, multicast, broadcast), current state, and gaps.

### 4.4 `.claude/skills/oai-cn/SKILL.md` (requirements)

Same approach for the OAI 5G Core repos (at minimum `oai-cn5g-smf`, `oai-cn5g-amf`, `oai-cn5g-upf`, and the federation/umbrella repo with docker-compose tutorials). Verify real paths. Include:

- Repo list with purpose and where each lives on GitHub.
- Per NF: source layout (SBI handlers, PFCP, NAS, state machines, config), build commands (native and Docker image build), unit tests if any.
- How the federated deployment tutorials work (docker-compose files, how to swap in a locally built NF image).
- Test tiers T0–T4 with concrete commands: unit tests per NF (T1); robot framework or other automated test suites in the federation repo, how to run them against locally built images, and what they need (docker, privileges, resources) (T2/T3).
- Conventions: C++ style, formatting, logging, commit style.
- MBS-related state (search for MBS, MB-SMF, multicast, TMGI) and gaps.

### 4.5 `.claude/skills/open5gs-mbs/SKILL.md` (requirements)

Knowledge skill for the 5G-MAG MBS-enabled Open5GS core. Ask the user for the exact repository URL(s) and branch they use, then inspect:

- Repo layout: which NFs exist for MBS (e.g. MB-SMF, MB-UPF, NEF/MBSF or equivalents as implemented), where MBS session handling, N4mb/PFCP and SBI code live, config files.
- Build (meson/ninja as used by the repo) and how MBS components are enabled.
- Tests: the repo's test programs/suites (T1/T2), how to run them, and how they're organised; pattern for adding a test.
- How the repo deploys for E2E (docker, scripts) together with an OAI gNB (T3).
- Conventions: code style, logging, commit style. Differences from upstream Open5GS that matter for changes.

If repos cannot be accessed, write the skills with clearly marked `TODO(verify)` placeholders and tell the user.

### 4.6 Private forks and testbed repos

Don't write a skill per private repo. Private forks reuse the stack skill of their upstream; project-specific facts (branch, extra build flags, test scripts, lab constraints) go into a profile (§5.4). If a private repo contains its own `CLAUDE.md` or `.claude/skills/`, those are loaded too and take precedence for that repo.

---

## 5. Specifications

### 5.1 `specs/manifest.yaml` (full content)

```yaml
# Spec manifest. ensure_specs.py makes sure every entry selected by tag/id
# is downloaded and converted. `release` picks the latest version of that
# release unless `version` pins one (x.y.z).
#
# IMPORTANT: align RAN specs with the ASN.1 version used in OAI
# (see oai-ran skill). Override per entry with `version:`.
defaults:
  release: 18

specs:
  # --- Architecture / stage 2 ---
  - { id: "23.247", title: "5G MBS architecture",                 tags: [mbs, cn, ran] }
  - { id: "23.501", title: "5GS system architecture",             tags: [cn] }
  - { id: "23.502", title: "5GS procedures",                      tags: [cn] }
  - { id: "38.300", title: "NR overall description",              tags: [ran, mbs] }
  - { id: "38.401", title: "NG-RAN architecture",                 tags: [ran] }

  # --- RAN stage 3 ---
  - { id: "38.331", title: "NR RRC",                              tags: [ran, mbs], asn1: true }
  - { id: "38.321", title: "NR MAC",                              tags: [ran, mbs] }
  - { id: "38.322", title: "NR RLC",                              tags: [ran, mbs] }
  - { id: "38.323", title: "NR PDCP",                             tags: [ran, mbs] }
  - { id: "38.211", title: "NR physical channels and modulation", tags: [ran, mbs, phy] }
  - { id: "38.212", title: "NR multiplexing and channel coding",  tags: [ran, mbs, phy] }
  - { id: "38.213", title: "NR physical layer procedures for control", tags: [ran, mbs, phy] }
  - { id: "38.214", title: "NR physical layer procedures for data",    tags: [ran, mbs, phy] }
  - { id: "38.306", title: "NR UE radio access capabilities",     tags: [ran] }
  - { id: "38.473", title: "F1AP",                                tags: [ran, mbs, f1], asn1: true }
  - { id: "38.413", title: "NGAP",                                tags: [ran, cn, mbs, ng], asn1: true }

  # --- Core stage 3 ---
  - { id: "24.501", title: "5GS NAS",                             tags: [cn] }
  - { id: "29.244", title: "PFCP (N4)",                           tags: [cn, mbs] }
  - { id: "29.502", title: "Nsmf PDU session",                    tags: [cn] }
  - { id: "29.532", title: "Nmbsmf MBS session management",       tags: [cn, mbs] }
  - { id: "29.518", title: "Namf communication",                  tags: [cn] }
```

The builder must verify each spec number/title against the 3GPP site and flag mismatches to the user rather than silently fixing.

### 5.2 Source of specs

- Archive: `https://www.3gpp.org/ftp/Specs/archive/<series>_series/<id>/` (e.g. `38_series/38.331/`), files like `38331-i50.zip`.
- Version code: 3 characters = major, minor, patch; each is `0-9` or `a-z` (a=10 … z=35). Example `i50` = 18.5.0, `h70` = 17.7.0. Verify this against the live listing.
- Selection: for `release: N`, pick the highest version with major == N; if `version` is set, use exactly that.

### 5.3 Converted layout (committed)

```
specs/<id>/<x.y.z>/
├── meta.yaml          # id, title, version, source URL, sha256 of zip, conversion date
├── toc.md             # clause number → title → file, generated
├── clauses/
│   ├── 5.md           # one file per top-level clause …
│   ├── 6.3.2.md       # … split deeper wherever a file would exceed ~150 KB
│   └── annex-A.md
└── asn1/              # only if asn1: true
    └── <id>.asn       # all text between "-- ASN1START" and "-- ASN1STOP"
```

`specs/INDEX.md` lists every converted spec/version with a link to its `toc.md`.

### 5.4 Project profiles (`profiles/*.yaml`)

A profile bundles repos, base branches, build and test commands for one project so tasks stay short ("use profile mbs-testbed"). Task text always overrides profile values. Write `profiles/README.md` explaining the schema, and these two profiles.

`profiles/mbs-testbed.yaml` (fill `TODO` values by asking the user; repo names below are placeholders the user confirms):

```yaml
name: mbs-testbed
description: MBS development – private OAI RAN fork + 5G-MAG Open5GS MBS core + private testbed
spec_tags: [mbs, ran, cn]
stack_skills: [oai-ran, open5gs-mbs]

repos:
  - name: oai-ran-fork
    role: target                     # code is changed here
    github: TODO/openairinterface5g-private
    base_branch: mbs-phase-a
    upstream: https://github.com/OPENAIRINTERFACE/openairinterface5g  # for git log comparisons; verify URL
    local_path: ~/src/oai-ran-fork   # used by apply-delivery
  - name: open5gs-mbs
    role: target                     # only included if the task touches the core
    github: TODO
    base_branch: TODO
    local_path: TODO
  - name: frq-adsat-phine
    role: test                       # test scripts; may receive new test cases
    github: TODO/frq-adsat-phine
    base_branch: main
    local_path: ~/src/frq-adsat-phine

tests:
  T0: { cloud: yes,   notes: "build gNB + nrUE (rfsim); see oai-ran skill" }
  T1: { cloud: yes,   notes: "ctest in RAN fork; open5gs-mbs unit tests if CN changed" }
  T2: { cloud: maybe, notes: "PHY/MAC simulators relevant to MBS" }
  T3: { cloud: opt-in, timebox_min: 45, notes: "open5gs-mbs + gNB/nrUE rfsim via docker; runs only with E2E in the task" }
  T4: { cloud: no,    notes: "testbed scripts in frq-adsat-phine: TODO list entry points" }

constraints:
  - "Never contact lab hosts from the cloud."
  - TODO
```

`profiles/oai-public.yaml`: same schema for public OAI RAN (`develop`) + OAI CN NFs + the federation repo, with robot/docker tests as T2/T3. Fill from the oai-ran/oai-cn skills.

`implement-feature` must validate a profile on load (missing repos in session, `TODO` values relevant to the task) and ask about gaps in Phase 2.

---

## 6. Scripts (requirements)

All scripts locate the toolkit root via the `.toolkit-root` marker (walk up from the script's own directory) and must work from any cwd.

### 6.1 `scripts/ensure_specs.py`

```
ensure_specs.py [--tags mbs,ran] [--spec 38.331 ...] [--all] [--release N] [--dry-run]
```

- Reads the manifest, selects entries (union of `--tags` and `--spec`; `--all` for everything).
- For each: resolve the version (§5.2) from the live directory listing; if `specs/<id>/<version>/meta.yaml` exists → skip ("present").
- Otherwise: download zip into `specs/<id>/<version>/raw/` (gitignored), verify it's a valid zip, extract, convert the `.docx` with `pandoc -f docx -t gfm --wrap=none` (if only a `.doc` exists, convert to `.docx` with `soffice --headless --convert-to docx` first; if soffice is missing, report clearly).
- Split into clause files by heading level (§5.3), generate `toc.md`, extract ASN.1 if flagged, write `meta.yaml`, regenerate `specs/INDEX.md`.
- Output a final summary table: spec, version, status (present/added/failed), and exit non-zero if any requested spec failed.
- Retries with backoff on network errors; a clear message if 3gpp.org is unreachable (likely network policy).

### 6.2 `scripts/spec_lookup.py`

```
spec_lookup.py clause 38.331 5.9.1          # print clause (and subclauses with --deep)
spec_lookup.py grep 38.321 "G-RNTI"         # matching lines with clause context
spec_lookup.py asn1 38.331 MBS-BroadcastConfiguration   # print ASN.1 type definition
spec_lookup.py list                          # what's available
```

Uses the latest converted version unless `--version` is given. Output stays compact (cap with `--max-lines`, default 200).

### 6.3 `scripts/make_delivery.sh <slug> <repo-path>:<base-sha> [<repo-path>:<base-sha> ...]`

- Creates `deliveries/<slug>/` (keeps existing PLAN.md). For each repo: `git -C <repo> format-patch --base=<base-sha> -o deliveries/<slug>/patches/<repo-name>/ <base-sha>..HEAD`, where `<repo-name>` is the directory name of the checkout.
- Copies templates from `templates/delivery/` if not already present, pre-filling per repo: name, remote URL, base branch, base SHA, commit list (`git log --oneline`), diffstat; plus slug and date.
- Fails clearly if a repo has no commits or uncommitted changes.

### 6.4 `scripts/push_delivery.sh <slug>`

- Must run inside the toolkit repo (verify `.toolkit-root` and that `origin` is the toolkit repo; refuse otherwise).
- Creates/switches to branch `claude/delivery-<slug>`, stages `deliveries/<slug>/`, `specs/` and `specs/manifest.yaml`, commits (`delivery: <slug>`), pushes to `origin`.
- One of exactly two sanctioned push paths; the hook in §7.1 allows it.

### 6.4b `scripts/push_toolkit.sh [--dry-run]`

- Publishes changes to the toolkit repo itself (skills, scripts, templates, profiles, docs) on the current branch, normally `main`.
- Same location and origin guards as §6.4. Refuses: a detached HEAD, a `claude/delivery-*` branch (that is §6.4's job), any force/mirror/delete flag, and a non-fast-forward (it fetches first and tells the agent to rebase).
- Commits nothing — the agent commits, the script only pushes. Uncommitted changes are listed as a warning so nothing half-finished is pushed silently.
- `--dry-run` reports the branch and the commits that would go out, and changes nothing.

### 6.5 `scripts/cloud_setup.sh`

This script's content is pasted into the cloud environment's **Setup script** field (see README). Requirements:

- Install: `pandoc`, `python3-yaml`, `python3-requests`, `jq`, `curl`, `clang-format`; optionally `libreoffice-writer-nogui` (skip gracefully if unavailable). Use `apt-get` non-interactively; be idempotent.
- Must not depend on environment variables (they may not be available during setup).
- Must not depend on knowing where repos are cloned. Optionally pre-install OAI RAN build dependencies by locating `cmake_targets/build_oai` with a bounded `find` from `/` (maxdepth ~5); if not found, skip with a message (the skill installs deps at task time instead).
- Fallback for skill discovery: if a directory containing `.toolkit-root` is found, copy its `.claude/skills/*` to `~/.claude/skills/` and its hooks into `~/.claude/` with a matching `~/.claude/settings.json`, so skills and hooks work even if the session starts in the target repo.
- If Docker is present, pre-pull base images listed in the profiles' T3 notes only if they are public and small enough to be worth caching; otherwise skip.
- Print a short summary of what was installed.

### 6.6 `scripts/probe_env.sh`

Prints a compact capability report (also as JSON with `--json`) used to decide which test tiers can run:

- CPU cores, RAM, free disk in the work directory and `/tmp`.
- Whether running as root / passwordless sudo is available.
- Docker: client present, daemon reachable (`docker info`), compose plugin, ability to run a container (`docker run --rm hello-world` or an already cached tiny image), privileged mode (`--privileged` test), host networking.
- Kernel features relevant to 5G stacks: `/dev/net/tun` usable, SCTP available (`modprobe sctp` / `checksctp` or creating an SCTP socket in Python), ability to create network namespaces, sysctl writes (ip_forward).
- Network reachability: github.com, www.3gpp.org, docker registry (short timeouts).
- Tools: cmake, ninja, meson, gcc/clang versions, python3, robot (Robot Framework).
- Ends with a suggested tier verdict (T0–T3: CAN RUN / MAYBE / NO) with one-line reasons.

---

## 7. Hooks

### 7.1 `.claude/settings.json` (full content)

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          { "type": "command", "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/push_guard.py\"" }
        ]
      }
    ]
  }
}
```

Verify the schema against the current Claude Code hooks documentation and adjust if it changed.

**`push_guard.py` requirements:**
- Reads the hook JSON from stdin; inspects `tool_input.command`.
- Blocks (exit code 2, explanation on stderr) any command that contains a `git push` (including `git -C x push`, pushes inside `&&`/`;` chains, `git push` via `sh -c`), `gh pr create`, `gh pr merge`, `gh repo`, `gh release`, or `git remote set-url`/`git remote add` targeting a push.
- Allows commands that invoke `scripts/push_delivery.sh` or `scripts/push_toolkit.sh` — and only in the segment that invokes them, so a sanctioned script chained with a raw push of another repo is still blocked.
- Error message tells Claude: "Direct pushes are blocked. Use scripts/push_delivery.sh <slug> for delivery branches, or scripts/push_toolkit.sh for changes to the toolkit repo itself. Never push to target or test repos."
- Include a small self-test (`push_guard.py --self-test`) with allowed/blocked examples.

### 7.2 Notifications (no hook)

- There is no notifier hook and no status file. The agent itself sends one `PushNotification` at the end of a run — Claude's own channel, so it lands in the Claude app and as a desktop notification, with no third-party service and nothing to configure.
- Exactly two occasions: delivery pushed (`<slug>: N patches ready, <branch>`) and stopped for good (`<slug>: stopped, <reason>`). Plans, questions and progress are chat-only — Phase 2's stop is announced by the session's own "finished" notification.

---

## 8. Templates

### 8.1 `templates/TASK_TEMPLATE.md`

Sections with short guidance comments:
`Profile` (optional) · `Target repo(s) + base branch each` · `Test repo(s) + scripts to use` · `Component` · `Goal` (2–5 sentences) · `Scope – in` · `Scope – out` · `Spec references` (TS + clause, release) · `Existing work to build on` (branches, files, previous deliveries) · `Acceptance criteria` · `Test expectations` (unit tests to add, which tiers should pass in the cloud, which testbed scripts locally) · `Constraints` (config compatibility, no API breaks…) · `Mode` (keywords, combinable: `AUTOPILOT` to skip plan approval when there are no questions; `E2E` or `E2E:<minutes>` to run T3 container end-to-end tests in the cloud; default is plan approval and no T3).

Include one filled example (marked as example), e.g.:

```markdown
/implement-feature
Profile: mbs-testbed
Target: oai-ran-fork @ mbs-phase-a
Test repo: frq-adsat-phine — use the MBS broadcast test script(s); add a test case for the new behavior
Component: gNB (RRC + MAC)
Goal: Implement MCCH change notification for MBS broadcast ...
Spec references: TS 38.331 (MCCH procedures), TS 38.321 (MBS MAC), TS 38.212/38.213 (DCI 4_0) – Rel-17
Acceptance criteria: ...
Test expectations: extend unit tests for MCCH encoding/scheduling; T0–T1 must pass in the cloud; T4 via testbed script locally
Mode: (default — add E2E to also run the rfsim end-to-end test in the cloud)
```

### 8.2 `templates/PLAN.md`

Not written in Phase 2 — the Phase 2 plan is a chat message only. This template is
filled in at the start of Phase 3, once the user has approved, as the record that
travels with the delivery.

Sections: Understanding · Repos & base commits (table: repo, role, branch, SHA) · Spec basis (table: TS, version, clause, what it mandates) · Current state in repo(s) · Design decisions · Commit plan per repo (table: #, title, files, spec refs) · Config changes · Test plan (unit tests to add/extend; tier table T0–T4 with command and CAN RUN / MAYBE / LOCAL ONLY from probe_env; testbed scripts and new test cases) · Risks & assumptions · Questions (numbered) · Approval log (date, user's answers).

### 8.3 Delivery templates (`templates/delivery/`)

- **README.md**: slug, date, profile, table of repos (role, base branch, base SHA, number of patches), one-paragraph summary, test tier summary (passed / skipped / local only), links to the other files, status (complete/partial).
- **APPLY.md**: prerequisites; per repo:
  ```bash
  cd <repo-checkout>
  git fetch origin && git cat-file -e <BASE_SHA>
  git switch -c feature/<slug> <BASE_SHA>
  git am -3 <path-to>/deliveries/<slug>/patches/<repo-name>/*.patch
  ```
  plus conflict handling, how to rebase onto the current base branch, and how to abort (`git am --abort`).
- **CHANGES.md**: per repo and commit: purpose, files, spec clauses, notable design decisions; tests added/extended; requirement traceability table (requirement → clause → code location → test).
- **TESTING.md**: tier table T0–T4 (command, where run, result: PASSED / FAILED-preexisting / SKIPPED + reason / NOT RUN (opt-in) / LOCAL ONLY); cloud results with commands, durations and short log excerpts; local steps for every SKIPPED, NOT RUN and T4 item (testbed script invocations from the test repo, config changes, launch order, which logs/PCAPs to check, expected messages and log lines); pass/fail criteria; regression checks.
- **OPEN_ISSUES.md**: assumptions, spec ambiguities and chosen interpretation, untested parts, known limitations, follow-up suggestions.
- **PR_DESCRIPTION.md**: title, summary, spec references, testing done, notes for reviewers.

---

## 9. `README.md` (content requirements)

Write a clear, practical README in English with these sections. Use the user-facing tone of an internal team guide.

1. **What this is** — one paragraph + the diagram from §1.
2. **Repository layout** — short tree with one line per item.
3. **One-time setup: GitHub** — this repo is private; never contains OAI code; 3GPP content is copyrighted, keep the repo private.
4. **One-time setup: Claude Code in the cloud**
   - Sign in at claude.ai/code, connect GitHub (install the Claude GitHub App, or from the CLI run `/web-setup`). Grant access to `5g-dev-agent` and every repo you'll work on, including private forks and testbed repos.
   - If a private repo needs credentials for submodules or private dependencies, note how to handle that (no secrets in environment variables; prefer making the dependency accessible to the GitHub account).
   - Create a cloud environment named e.g. `oai-dev`:
     - **Network access:** must reach `www.3gpp.org` (spec downloads), package mirrors and GitHub. If the default/trusted level blocks 3gpp.org, use a custom allowlist or full access.
     - **Environment variables:** none needed. Note: values are visible to anyone who can edit the environment; there is no secret store. Don't put tokens here.
     - **Setup script:** paste the contents of `scripts/cloud_setup.sh`. It is cached between sessions; after changing it, expect the next session to rebuild.
5. **Notifications** — nothing to install or configure: the agent sends one notification through Claude when a run ends (delivered / stopped), which reaches the Claude app and the desktop. Say that plans and questions deliberately do not notify, and that you can always check the session manually.
6. **First-run verification checklist** — start a cloud session with `5g-dev-agent` + a target repo and ask Claude to run: `/implement-feature` is listed? (`/skills` or ask "which skills do you have?"); `python3 .claude/hooks/push_guard.py --self-test`; `python3 scripts/ensure_specs.py --spec 38.321 --dry-run` resolves a version?; a test `git push` is blocked. If skills/hooks aren't picked up because the session starts in the target repo, explain the setup-script fallback (§6.5).
7. **Profiles** — what a profile is, the two shipped profiles, how to create one for a new project (copy, fill repos/branches/test tiers), and that task text overrides profile values.
8. **Running a task in the cloud** — select repos (`5g-dev-agent` + target repo(s) + test repo(s)), select environment, paste a task based on `templates/TASK_TEMPLATE.md` starting with `/implement-feature`. Describe what happens: spec check → recon + environment probe → plan + questions → you answer in the chat (from browser or mobile) → implementation with tests → test tiers as far as the VM allows → delivery pushed to `claude/delivery-<slug>`. Mention plan mode as an extra safety option. Mention multiple tasks can run in parallel.
9. **What gets tested where** — explain tiers T0–T4, that the agent extends unit tests and adds test cases to the test repo, that T3 is opt-in (add `E2E` or `E2E:<minutes>` to the task, or say so when approving the plan) because it is long, and when enabled depends on the cloud VM (docker, TUN, SCTP, resources) and is time-boxed, and that T4 (testbed, hardware) is always local. Show how to read the tier table in TESTING.md.
10. **Local setup** — clone `5g-dev-agent`; `export DEV_AGENT_HOME=~/5g-dev-agent`; symlink skills into personal skills:
   ```bash
   mkdir -p ~/.claude/skills
   ln -s "$DEV_AGENT_HOME/.claude/skills/apply-delivery" ~/.claude/skills/
   ln -s "$DEV_AGENT_HOME/.claude/skills/oai-ran"        ~/.claude/skills/
   ln -s "$DEV_AGENT_HOME/.claude/skills/oai-cn"         ~/.claude/skills/
   ln -s "$DEV_AGENT_HOME/.claude/skills/open5gs-mbs"    ~/.claude/skills/
   ```
   Optionally also the push guard in `~/.claude/settings.json` for local sessions.
11. **Applying a delivery locally** — open Claude Code in the target repo (the skill also finds the other repos of the delivery via the profile's `local_path`), `/apply-delivery <slug>`; describe the flow; then squash fixups, push, open the PR manually.
12. **Maintaining the toolkit** — adding specs (manifest entry + `ensure_specs.py`), merging delivery branches back to `main` periodically (so newly converted specs land on main), cleaning old deliveries, adding new skills, updating stack skills and profiles when repos change.
13. **Limitations & troubleshooting** — cloud VM never runs RF/hardware/testbed tests; T3 docker setups may fail for lack of privileges, TUN/SCTP or resources (check `probe_env.sh` output); long builds; network policy blocking 3gpp.org; patches not applying because the base moved (rebase instructions); notifications not arriving (notifications off for the account, or Remote Control not connected for a local session).

---

## 10. Builder self-check (run before finishing)

Report each item as ✅/❌ with details:

1. Tree matches §2; `.gitignore` correct; `.toolkit-root` exists.
2. `python3 .claude/hooks/push_guard.py --self-test` passes.
3. `python3 scripts/ensure_specs.py --spec 38.321` downloads, converts and splits successfully; `spec_lookup.py grep 38.321 "RNTI"` returns results; INDEX.md updated. (Then ask the user whether to keep this spec committed.)
4. `python3 scripts/ensure_specs.py --tags mbs --dry-run` resolves versions for all MBS specs and reports any manifest mismatches.
5. `ensure_specs.py --spec 38.331` extracts ASN.1 into `asn1/38.331.asn` (if run; this one is large — ask first).
6. `make_delivery.sh` tested against two throwaway git repos (2 commits each) in one call; both patch series land in `patches/<repo-name>/` and apply with `git am` on their bases.
7. `push_delivery.sh` refuses to run outside the toolkit repo (test with a throwaway repo; do not actually push unless the user agrees).
8. No notifier hook or status file exists; the only notification path is the agent's own `PushNotification` at the end of a run.
9. `oai-ran`, `oai-cn` and `open5gs-mbs` skills written from real repo inspection, or `TODO(verify)` markers listed.
10. `probe_env.sh` runs locally and prints a tier verdict; `--json` output parses.
11. Both profiles exist and validate; the `TODO` values of `mbs-testbed.yaml` are listed for the user to fill in (repo URLs, branches, testbed script entry points).
12. README complete per §9.

Finally, commit everything to `main` with message `Initial 5g-dev-agent toolkit` and ask the user before pushing.
