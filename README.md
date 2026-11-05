# 5g-dev-agent

A private toolkit for handing 3GPP feature work to Claude Code running in the cloud, and
getting back something you can actually review: a patch series per repo, documentation
tying each change to the spec clause behind it, and an honest account of what was tested
and what was not. It works with any set of 5G repos — public OpenAirInterface RAN and 5G
Core, private forks on custom branches, the 5G-MAG Open5GS MBS core, and private testbed
repos full of lab scripts. Which repos belong together is described by a **profile**.

The cloud agent **never pushes to a target repo**. It builds a *delivery package* and
pushes that to this toolkit repo only. You apply it locally, finish the testing that needs
real hardware, and open the PR yourself.

```
┌────────────────────────── CLOUD (claude.ai/code) ──────────────────────────┐
│ Session repos: 5g-dev-agent + target repo(s) + test repo(s)                │
│   e.g. private OAI fork @ mbs-phase-a  +  private testbed repo             │
│                                                                            │
│ /implement-feature [profile] <task>                                        │
│   Phase 0  ensure specs (fetch + convert missing ones)                     │
│   Phase 1  recon: specs, code, test repo, probe VM capabilities            │
│   Phase 2  PLAN + QUESTIONS in chat  ──► STOP, notify, wait for "go"       │
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

## Repository layout

| Path | What it is |
|---|---|
| `CLAUDE.md` | always-loaded working rules — the hard "never push" rules live here |
| `SETUP_INSTRUCTIONS.md` | the specification this repo was built from |
| `.toolkit-root` | empty marker; every script finds the repo by walking up to it |
| `.claude/settings.json` | hook wiring (push guard, notifications) |
| `.claude/hooks/push_guard.py` | blocks every push path except `push_delivery.sh` |
| `.claude/hooks/notify.sh` | sends the status line to ntfy |
| `.claude/skills/implement-feature/` | the cloud workflow |
| `.claude/skills/apply-delivery/` | the local workflow |
| `.claude/skills/oai-ran/` | OAI RAN repo knowledge (layout, ASN.1 versions, build, tests, MBS state) |
| `.claude/skills/oai-cn/` | OAI 5G Core repo knowledge |
| `.claude/skills/open5gs-mbs/` | 5G-MAG MBS-enabled Open5GS knowledge |
| `profiles/` | per-project repo/branch/test-tier bundles (`README.md` has the schema) |
| `specs/manifest.yaml` | which 3GPP specs exist, their tags, and pinned versions |
| `specs/INDEX.md` | generated index of everything converted |
| `specs/<id>/<version>/` | converted Markdown: `clauses/`, `toc.md`, `asn1/`, `meta.yaml` |
| `scripts/ensure_specs.py` | download + convert the specs a task needs |
| `scripts/spec_lookup.py` | search clauses, grep spec text, print ASN.1 types |
| `scripts/make_delivery.sh` | export one patch series per repo into a delivery |
| `scripts/push_delivery.sh` | the only sanctioned push |
| `scripts/set_status.sh` | write the status line that drives notifications |
| `scripts/probe_env.sh` | what can this VM run? (decides the test tiers) |
| `scripts/cloud_setup.sh` | paste into the cloud environment's Setup script field |
| `templates/` | task, plan and delivery document templates |
| `deliveries/` | where delivery packages land |

## One-time setup: GitHub

**Keep this repository private.** Two reasons:

1. 3GPP specification text is copyrighted. The converted Markdown under `specs/` is
   committed here for the agent to search — that is fine for internal use, and not fine
   in public.
2. Deliveries quote code and test output from private forks and testbed repos.

This repo contains no OAI source of its own — only patches against it, inside deliveries.

## One-time setup: Claude Code in the cloud

1. **Sign in** at [claude.ai/code](https://claude.ai/code) and connect GitHub (install the
   Claude GitHub App, or run `/web-setup` from the CLI). Grant access to `5g-dev-agent`
   **and every repo you will work on**, including private forks and testbed repos.

2. **Private dependencies.** If a repo pulls private submodules (the `frq-adsat-phine`
   testbed carries three), make sure the same GitHub account can read them — the session
   clones with the app's credentials. Do **not** put tokens in environment variables:
   there is no secret store, and anyone who can edit the environment can read them.

3. **Create an environment**, e.g. `oai-dev`:

   - **Network access.** It must reach `www.3gpp.org` (spec downloads), the package
     mirrors, `github.com`, and `ntfy.sh` if you use notifications. Development also pulls
     from `gitlab.eurecom.fr` (OAI RAN) and the Docker registry. If the default or trusted
     level blocks 3gpp.org, switch to a custom allowlist (tick "also include default list
     of common package managers") or full access.

   - **Environment variables.** `NTFY_TOPIC=<a long random string>` (optional).
     Optionally `NTFY_SERVER` for a self-hosted ntfy. Nothing secret belongs here.

   - **Setup script.** Paste the contents of [`scripts/cloud_setup.sh`](scripts/cloud_setup.sh).
     It installs pandoc, PyYAML, requests, jq, clang-format and (if available) LibreOffice,
     and copies the skills and hooks into `~/.claude/` so they work even when the session
     starts in a target repo rather than here. It is cached between sessions — after
     editing it, expect the next session to rebuild.

## Notifications

The agent writes a status line at the end of every turn, and a hook forwards it to
[ntfy](https://ntfy.sh). Install the ntfy app (iOS / Android / desktop) and subscribe to
your topic. Anyone who knows the topic can read it — use something long and random.

| State | Meaning |
|---|---|
| `PLAN_READY` | the plan is posted and waiting for your "go" |
| `QUESTION` | the agent needs an answer before it can continue |
| `BLOCKED` | something it cannot resolve (no network, missing access, a dependency) |
| `DELIVERED` | a delivery package is pushed and ready to apply |
| `FAILED` | it stopped without a complete delivery; a partial one may still exist |

`QUESTION`, `BLOCKED`, `FAILED` and "waiting for input" are sent with `Priority: high`.
Identical consecutive statuses are only sent once, so a long run doesn't buzz every turn.

Notifications are optional — with `NTFY_TOPIC` unset the hook exits silently. The Claude
app's own notifications work too, and you can always just open the session.

## First-run verification checklist

Start a cloud session with `5g-dev-agent` plus one target repo, and ask Claude to run:

```bash
# 1. Are the skills visible?  (/skills, or just ask "which skills do you have?")
#    Expect: implement-feature, apply-delivery, oai-ran, oai-cn, open5gs-mbs

# 2. The push guard works
python3 .claude/hooks/push_guard.py --self-test        # expect "44/44 ... passed"

# 3. A real push is blocked
git push origin main                                   # expect the hook to refuse it

# 4. Notifications arrive
scripts/set_status.sh QUESTION "first-run test"        # then end the turn

# 5. Spec download works through the environment's network policy
python3 scripts/ensure_specs.py --spec 38.321 --dry-run   # expect a resolved version

# 6. What can this VM do?
scripts/probe_env.sh                                   # read the tier verdict at the end
```

If the skills or hooks are not picked up because the session started in the target repo
rather than here, that is what the setup script's fallback is for: it copies
`.claude/skills/*` and the hooks into `~/.claude/` with a matching `settings.json`.
Re-run it, or check its output in the environment build log.

## Profiles

A profile bundles the repos, base branches, build commands and test tiers of one project,
so a task can say `Profile: mbs-testbed` instead of repeating all of it.

| Profile | Project |
|---|---|
| [`oai-public.yaml`](profiles/oai-public.yaml) | public OAI RAN `develop` + the OAI 5G Core NFs + `oai-cn5g-fed` |
| [`mbs-testbed.yaml`](profiles/mbs-testbed.yaml) | private OAI RAN fork + 5G-MAG Open5GS MBS core + the `frq-adsat-phine` testbed |

**Task text always overrides the profile.** The profile is the default, never the
authority. To make one for a new project, copy the closest existing file and fill it in —
[`profiles/README.md`](profiles/README.md) documents every field, including how to express
a repo whose base is a submodule pin rather than a branch.

## Running a task in the cloud

1. Start a session and select the repos: `5g-dev-agent` **plus** the target repo(s)
   **plus** the test repo(s). The agent can only see what the session attaches.
2. Select your environment.
3. Paste a task based on [`templates/TASK_TEMPLATE.md`](templates/TASK_TEMPLATE.md),
   starting with `/implement-feature`. That file has a fully worked example.

What then happens:

- **Phase 0** — the specs your task needs are downloaded and converted if missing.
- **Phase 1** — recon: the spec clauses, the code, the test repo's scripts, and
  `probe_env.sh` to see what this VM can run.
- **Phase 2** — a plan and numbered questions land in the chat, and **the agent stops.**
  Answer from the browser or your phone and say "go". This is the point where a vague
  task costs you a round trip, which is why the template is worth filling in.
- **Phase 3** — implementation, commit by commit, with unit tests as part of the work.
- **Phase 4** — the test tiers, as far as the VM allows.
- **Phase 5** — the delivery is pushed to `claude/delivery-<slug>` of this repo.

Two things worth knowing: plan mode is available as an extra safety net, and several tasks
can run in parallel in separate sessions — they only ever write to their own delivery branch.

`AUTOPILOT` in the task skips the Phase 2 stop, **but only when the agent has zero
questions.** Any question and it stops anyway.

## What gets tested where

| Tier | What | Where |
|---|---|---|
| **T0** | Build every affected target in every changed repo | cloud |
| **T1** | Unit tests, including the ones added for this change | cloud |
| **T2** | Component/integration without RF — PHY/MAC simulators, robot suites | cloud when it fits |
| **T3** | End-to-end in containers — core + gNB/nrUE in rfsimulator | cloud, **opt-in** |
| **T4** | Testbed, RF, hardware, lab hosts | **always local** |

The agent extends the repos' own unit tests rather than inventing a framework, and adds
test cases to the test repo where one exists for related features.

**T3 is opt-in** because it is slow and fragile. Add `E2E` to the task (or `E2E:<minutes>`
for a time-box, default 45), or say so when you approve the plan. Even then it only runs
if `probe_env.sh` finds docker, compose, a usable `/dev/net/tun` and enough RAM and disk —
a cloud VM often has no usable TUN, in which case the UPF and the nrUE tunnel cannot come
up. Without opt-in, T3 is recorded as `NOT RUN (opt-in)` and the full steps are written
into `TESTING.md` for you.

**Reading the tier table in `TESTING.md`:** each row ends in one of

- `PASSED` — it ran here and passed
- `FAILED-preexisting` — it also fails on the base commit, so it is not this change's fault
- `SKIPPED (<reason>)` — the VM could not run it; the reason is the environment, not the code
- `NOT RUN (opt-in)` — T3 without `E2E`
- `LOCAL ONLY` — T4

A tier that could not run is never marked passed. Everything that is `SKIPPED`, `NOT RUN`
or `LOCAL ONLY` has a copy-pasteable local recipe further down the same file, with the log
lines to watch for and the pass criteria.

## Local setup

```bash
git clone git@github.com:phine-lukas/claude-5g-dev-agent.git ~/5g-dev-agent
echo 'export DEV_AGENT_HOME=~/5g-dev-agent' >> ~/.bashrc   # or ~/.zshrc
export DEV_AGENT_HOME=~/5g-dev-agent

mkdir -p ~/.claude/skills
ln -s "$DEV_AGENT_HOME/.claude/skills/apply-delivery" ~/.claude/skills/
ln -s "$DEV_AGENT_HOME/.claude/skills/oai-ran"        ~/.claude/skills/
ln -s "$DEV_AGENT_HOME/.claude/skills/oai-cn"         ~/.claude/skills/
ln -s "$DEV_AGENT_HOME/.claude/skills/open5gs-mbs"    ~/.claude/skills/
```

Optionally wire the push guard into local sessions too, by adding the `PreToolUse` block
from [`.claude/settings.json`](.claude/settings.json) to your `~/.claude/settings.json`
with an absolute path to `push_guard.py`. Worth it if you also run agents against the
target repos locally.

## Applying a delivery locally

Open Claude Code in the target repo and run `/apply-delivery <slug>` (the slug, the branch
name, or just paste the cloud session's final message). The skill will:

1. Fetch `claude/delivery-<slug>` from this repo and summarize what is in it.
2. For each repo in the delivery: find your checkout (the profile's `local_path` helps),
   check the base commit is present, create `feature/<slug>` at it, and `git am -3` the
   series. On a conflict it stops and shows you the conflict rather than forcing it.
3. Build, using the commands in `TESTING.md`.
4. Walk the remaining test steps — everything marked `SKIPPED`, `NOT RUN` or `LOCAL ONLY`,
   then T4. It asks before anything that launches containers, touches lab hosts or needs
   sudo.
5. Write fixes as `fixup!` commits so the series stays reviewable.

Then: `git rebase -i --autosquash <base>` to squash the fixups, push, and open the PR
yourself. The agent does none of those three.

## Maintaining the toolkit

- **Adding a spec:** add an entry to `specs/manifest.yaml` (id, title, tags, optionally
  `version:` to pin and `asn1: true` to extract ASN.1), then
  `python3 scripts/ensure_specs.py --spec <id>`.
- **Keeping RAN specs aligned with the code:** `38.331`, `38.473` and `38.413` are pinned
  to the versions OAI's ASN.1 grammars actually compile (V17.3.0, V17.0.0, V17.10.0).
  Those are set in each protocol's `MESSAGES/CMakeLists.txt` in the RAN repo and **do
  move** — re-check them when a fork bumps a grammar, and update the manifest pin to match.
  Citing a clause from a version the code doesn't implement is how wrong IE names get in.
- **Merging deliveries back:** periodically merge `claude/delivery-*` branches into `main`
  so newly converted specs land on main and the next session doesn't re-download them.
- **Cleaning up:** delete old delivery branches and `deliveries/<slug>` folders once the
  PR is merged. The patches are reproducible from the PR.
- **Updating the stack skills:** `oai-ran`, `oai-cn` and `open5gs-mbs` record real paths
  and versions. When a repo reorganises, fix the skill — a skill that points at a path
  that no longer exists is worse than no skill.
- **Adding a skill:** a directory under `.claude/skills/<name>/SKILL.md` with `name` and
  `description` frontmatter. The description is what makes Claude load it, so write it for
  that job.

## Limitations and troubleshooting

**The cloud VM never runs RF, hardware or testbed tests.** That is by design, not a bug.
T4 always comes home.

| Symptom | Likely cause and fix |
|---|---|
| `ensure_specs.py` cannot reach 3gpp.org | The environment's network policy. Add `www.3gpp.org` to the allowlist. The script retries with backoff and says so explicitly before giving up. |
| `pandoc is required to convert specs` | The setup script could not install it — check the environment build log and the allowed package-manager domains. |
| A spec is only published as legacy `.doc` | Needs LibreOffice; the setup script installs it when available, and the error names it if not. |
| T3 fails immediately, UPF or nrUE won't start | Almost always `/dev/net/tun` unusable or missing privileges. Check `probe_env.sh` — if it says `T3 NO`, that is the answer; mark it SKIPPED and run it locally. |
| T3 runs but proves nothing | Containers were built from public images instead of your branch. Rebuild the images from the agent branch first; Docker layer caching will otherwise serve a stale binary. |
| The build takes forever | A cold OAI RAN build is 20–40 minutes. Keep `build/` between fix cycles — ASN.1 regeneration alone is minutes. |
| `git am` fails locally | The base moved. Apply on the recorded base SHA first, then `git rebase origin/<branch>`. Applying directly onto a moved tip produces much worse conflicts. |
| No notification arrives | `NTFY_TOPIC` unset, `ntfy.sh` not in the network allowlist, or the agent never called `set_status.sh` (check `.agent-status` in the toolkit root). |
| Skills not listed in the session | The session started in a target repo. Re-run the setup script, or check `~/.claude/skills/`. |
| The agent says a push was blocked | Working as intended. Deliveries go out through `scripts/push_delivery.sh`; `gh repo` and `gh release` are blocked wholesale, so use `gh api` or `git ls-remote` for read-only lookups. |
