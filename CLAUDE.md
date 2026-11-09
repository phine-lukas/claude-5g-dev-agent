# 5g-dev-agent – working rules

This repo is a toolkit for implementing 3GPP features in 5G software stacks
(OpenAirInterface RAN/CN, 5G-MAG Open5GS MBS core, private forks) and testing
them with existing test suites and private testbed repos. It is opened
together with target repos (code to change) and test repos (test scripts)
in the same session. Project profiles in `profiles/` describe which repos,
base branches, build commands and test tiers belong together.

## Hard rules
1. NEVER run `git push` directly. NEVER push to any target or test repo.
   Exactly two pushes are sanctioned, and both only ever touch THIS toolkit
   repo (a hook enforces it):
   - `scripts/push_delivery.sh <slug>` — the delivery branch
     `claude/delivery-<slug>`.
   - `scripts/push_toolkit.sh` — the current branch (normally `main`) with
     changes to the toolkit itself: skills, scripts, templates, profiles,
     specs, docs. Commit first, the script only pushes, never force, never
     non-fast-forward. Fix the toolkit where it was wrong rather than
     working around it, keep those commits separate from delivery work,
     and push them before the delivery so the delivery branch carries them.
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
