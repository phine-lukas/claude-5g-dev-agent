# Apply — <SLUG>

Nothing here pushes. You apply the patches, build, test, and open the PR yourself.
`/apply-delivery <SLUG>` walks through all of this interactively.

## Prerequisites

- A local checkout of every repo listed below, with a clean working tree.
- Each base commit must be reachable locally. If `git cat-file -e <BASE_SHA>`
  fails, `git fetch origin` first — base commits often live on private feature
  branches that your clone has not seen yet.
- This delivery lives on branch `claude/delivery-<SLUG>` of the toolkit repo:

```bash
cd "$DEV_AGENT_HOME"
git fetch origin && git switch claude/delivery-<SLUG>
DELIVERY="$DEV_AGENT_HOME/deliveries/<SLUG>"
```

## Per repo

| Repo | Role | Base branch | Base SHA | Patches |
|---|---|---|---|---|
<REPO_TABLE_ROWS>

For each repo:

```bash
cd <repo-checkout>
git fetch origin
git cat-file -e <BASE_SHA>                       # must succeed before continuing
git switch -c feature/<SLUG> <BASE_SHA>
git am -3 "$DELIVERY"/patches/<repo-name>/*.patch
```

Apply the repos in the order listed above when one depends on another.

## If `git am` conflicts

```bash
git status                       # what collided
# resolve the files, then:
git add <resolved files>
git am --continue
```

Stop and look at the conflict rather than forcing it through — a conflict usually
means the base branch moved under the patch. To start over:

```bash
git am --abort
git switch -                     # back where you were
git branch -D feature/<SLUG>
```

## Rebasing onto the current base branch

The series is cut against `<BASE_SHA>`. To move it onto the branch's current tip,
apply on the base first (above), then:

```bash
git fetch origin
git rebase origin/<base-branch>
```

Rebasing first and applying second tends to produce worse conflicts — apply on the
recorded base, then rebase.

## Then

1. Build — see [TESTING.md](TESTING.md).
2. Run the tiers marked SKIPPED, NOT RUN or LOCAL ONLY there.
3. Squash any `fixup!` commits: `git rebase -i --autosquash <BASE_SHA>`.
4. Push and open the PR yourself, using [PR_DESCRIPTION.md](PR_DESCRIPTION.md).
