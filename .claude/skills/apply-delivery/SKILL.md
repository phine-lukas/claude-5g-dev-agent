---
name: apply-delivery
description: Apply a delivery package produced by the implement-feature workflow to a local OpenAirInterface checkout. Fetches the delivery from the 5g-dev-agent repo, applies the patch series as commits with git am, builds, guides through the local test steps in TESTING.md, and helps debug and fix. Use when the user says apply/test/review a delivery, gives a delivery slug, or pastes a cloud session result.
---

# Apply Delivery (local workflow)

Never push a target or test repo, never open PRs — the user does that
manually. The one exception is the toolkit repo itself: if the user asks for
a toolkit fix to be published, commit it on `main` and use
`scripts/push_toolkit.sh`.

## 1. Locate the delivery
1. Find the toolkit repo: `$DEV_AGENT_HOME`, else `~/5g-dev-agent`, else ask.
2. Deliveries live in `deliveries/<slug>` on `main`, so just update `main`:
   ```bash
   git pull --ff-only origin main
   ls deliveries/<slug>
   ```
   The slug comes from the user or from pasted cloud output.
   Older deliveries made before this change still sit on their own branch
   `claude/delivery-<slug>`; fetch one of those without switching with
   `git fetch origin claude/delivery-<slug> && git checkout FETCH_HEAD -- deliveries/<slug>`.
   Read `README.md`, `CHANGES.md`, `OPEN_ISSUES.md`, `APPLY.md` of the delivery.
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
1. Update the delivery's `PR_DESCRIPTION.md` locally with test results and
   fixes (push the toolkit repo only if the user asks, and then only with
   `scripts/push_toolkit.sh`).
2. Tell the user the branch is ready, show `git log --oneline <base>..HEAD`,
   and remind them to squash fixups, push, and open the PR themselves.
