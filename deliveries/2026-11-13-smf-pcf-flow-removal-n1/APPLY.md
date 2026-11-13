# Apply — 2026-11-13-smf-pcf-flow-removal-n1

Nothing here pushes. You apply the patches, build, test, and open the PR yourself.
`/apply-delivery 2026-11-13-smf-pcf-flow-removal-n1` walks through all of this interactively.

## Prerequisites

- A local checkout of every repo listed below, with a clean working tree.
- Each base commit must be reachable locally. If `git cat-file -e <BASE_SHA>`
  fails, `git fetch origin` first — base commits often live on private feature
  branches that your clone has not seen yet.
- This delivery lives in `deliveries/2026-11-13-smf-pcf-flow-removal-n1` on `main` of the toolkit repo:

```bash
cd "$DEV_AGENT_HOME"
git switch main && git pull --ff-only origin main
DELIVERY="$DEV_AGENT_HOME/deliveries/2026-11-13-smf-pcf-flow-removal-n1"
```

## Per repo

| Repo | Role | Base branch | Base SHA | Patches |
|---|---|---|---|---|
| `oai-cn5g-common-src` | target (submodule `src/common-src`) | pinned by the SMF at `f725043c` | `f725043c` | 3 |
| `oai-cn5g-smf` | target | `fix/qfi-reuse` | `f086910` | 4 |

**Apply `common-src` first.** The SMF's fourth patch bumps the submodule to the
commit the third `common-src` patch creates, so the SMF series only builds once
that series is in place. The SHAs the bump records are the ones `git am`
produces from these patches in this order — if you rebase or reorder them, the
submodule pointer has to be updated to match (see "If the submodule bump does
not match" below).

For each repo:

```bash
cd <repo-checkout>
git fetch origin
git cat-file -e <BASE_SHA>                       # must succeed before continuing
git switch -c feature/2026-11-13-smf-pcf-flow-removal-n1 <BASE_SHA>
git am -3 "$DELIVERY"/patches/<repo-name>/*.patch
```

Apply the repos in the order listed above when one depends on another.

## If the submodule bump does not match

The SMF's `build(smf): bump common-src ...` patch records the exact SHA that
applying the three `common-src` patches onto `f725043c` produces. If your
`common-src` history differs — you rebased, reordered, or already carry some of
these fixes — that pointer will be wrong. Fix it in place rather than dropping
the patch:

```bash
cd <smf-checkout>/src/common-src
git log --oneline -4                   # confirm the three fixes are on top
cd <smf-checkout>
git add src/common-src
git commit --amend --no-edit           # re-record the pointer you actually have
```

Check it with `git submodule status src/common-src` before building.

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
git branch -D feature/2026-11-13-smf-pcf-flow-removal-n1
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
