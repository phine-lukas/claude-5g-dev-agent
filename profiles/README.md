# Project profiles

A profile bundles the repos, base branches, build commands and test tiers of one
project, so a task can say `Profile: mbs-testbed` instead of repeating all of it.

**Task text always wins.** Anything written in the task overrides the profile — a
different branch, an extra repo, a tier the profile marks `no`. The profile is the
default, never the authority.

## Using one

```markdown
/implement-feature
Profile: mbs-testbed
Target: openairinterface5g-private @ mbs-phase-a
...
```

`implement-feature` validates the profile when it loads it (Phase 1) and asks in
Phase 2 about anything relevant that is missing — a repo named here that isn't in the
session, or a `TODO` the task actually needs. A `TODO` nobody needs is not a problem.

## Shipped profiles

| Profile | Project |
|---|---|
| `oai-public.yaml` | public OpenAirInterface: RAN `develop` + the OAI 5G Core NFs + `oai-cn5g-fed` |
| `mbs-testbed.yaml` | MBS development: the private OAI RAN fork + the 5G-MAG Open5GS MBS core + the `frq-adsat-phine` testbed |

## Writing a new one

Copy the closest existing profile and fill it in. The schema:

```yaml
name: <profile name, matching the filename>
description: <one line>

spec_tags: [mbs, ran, cn]       # passed to ensure_specs.py in Phase 0
stack_skills: [oai-ran, open5gs-mbs]   # skills to load in Phase 1

repos:
  - name: <short name; also the directory name of the checkout>
    role: target | test         # target = code is changed; test = test scripts
    github: <org/repo>
    base_branch: <branch the work starts from>
    upstream: <URL>             # optional: for `git log upstream/x..HEAD` comparisons
    local_path: <path>          # used by /apply-delivery to find the local checkout
    optional: true              # optional: only included when the task touches it

tests:
  T0: { cloud: yes,     notes: "<build command, or where to find it>" }
  T1: { cloud: yes,     notes: "<unit test command>" }
  T2: { cloud: maybe,   notes: "<integration without RF>" }
  T3: { cloud: opt-in, timebox_min: 45, notes: "<container E2E>" }
  T4: { cloud: no,      notes: "<testbed scripts, hardware>" }

constraints:
  - "<rules that apply to every task in this project>"
```

### Field notes

- **`role`** decides what happens to the repo. `target` repos get an `agent/<slug>`
  branch and a patch series. `test` repos get one too, but only when the task adds or
  changes test cases there.
- **`base_branch`** is what the agent checks out *before anything else*. If it doesn't
  exist in the session's checkout, the agent stops and asks rather than guessing.
- **`base_ref`** may be used instead of `base_branch` when the base is not a branch —
  see "Submodule-pinned repos" below.
- **`local_path`** is only read locally, by `/apply-delivery`. Leave it `TODO` if the
  repo is never applied locally.
- **`cloud:`** values are `yes` (run it), `maybe` (run it if `probe_env.sh` allows),
  `opt-in` (T3: run only when the task says `E2E`), `no` (never in the cloud — write
  local steps into TESTING.md instead).
- **`timebox_min`** caps T3. `E2E:<minutes>` in the task overrides it; the fallback is
  45 minutes.
- **`notes`** should be concrete enough to act on. "see the oai-ran skill" is fine when
  the skill really has the command; a vague note is worse than none.

### Submodule-pinned repos

When a test repo pins a target repo as a git submodule, the right default base is that
pin, not a branch. Express it as:

```yaml
    base_ref: submodule-pin
    submodule: <test-repo-name>:<submodule path>
    alternatives: ["5mbs", "5mbs-development", "latest tag"]
```

The agent resolves it with `git -C <test repo> submodule status <path>` and uses the
commit it prints. `alternatives` lists what a task may name instead — use one of them
when the change is meant to go upstream, because a patch against an old pin is not
upstreamable. The agent raises this choice in Phase 2 whenever the task doesn't settle it.

### `TODO`

Leave `TODO` where you genuinely don't know yet. It is a marker for a human, and the
agent treats it as "ask before relying on this" — which is better than a wrong value
that looks confident.
