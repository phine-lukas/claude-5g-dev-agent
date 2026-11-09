# Apply — 2026-11-09-smf-qfi-reuse

Nothing here pushes. You apply the patches, build, test, and open the PR yourself.
`/apply-delivery 2026-11-09-smf-qfi-reuse` walks through all of this interactively.

## Prerequisites

- A local checkout of every repo listed below, with a clean working tree.
- Each base commit must be reachable locally. If `git cat-file -e 7bfe3220`
  fails, `git fetch origin` first — base commits often live on private feature
  branches that your clone has not seen yet.
- This delivery lives on branch `claude/delivery-2026-11-09-smf-qfi-reuse` of the toolkit repo:

```bash
cd "$DEV_AGENT_HOME"
git fetch origin && git switch claude/delivery-2026-11-09-smf-qfi-reuse
DELIVERY="$DEV_AGENT_HOME/deliveries/2026-11-09-smf-qfi-reuse"
```

## Per repo

| Repo | Role | Base branch | Base SHA | Patches |
|---|---|---|---|---|
| `oai-cn5g-smf` | target | `claude/jolly-rubin-p7b75o` (session branch off `develop`) | `7bfe322` | 2 |

For each repo:

```bash
cd <your oai-cn5g-smf checkout>
git fetch origin
git cat-file -e 7bfe3220bc12ec52655ca355096a979b162ad260  # must succeed before continuing
git switch -c feature/2026-11-09-smf-qfi-reuse 7bfe3220bc12ec52655ca355096a979b162ad260
git am -3 "$DELIVERY"/patches/oai-cn5g-smf/*.patch
```

Only one repo is touched, so there is no ordering to respect. The series needs
the `src/common-src` submodule populated to build; it is pinned to
`f725043cc3694f29c5ea91b0d244a868f5d4179a` and this delivery does not change it:

```bash
git submodule update --init src/common-src
```

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
git branch -D feature/2026-11-09-smf-qfi-reuse
```

## Rebasing onto the current base branch

The series is cut against `7bfe3220bc12ec52655ca355096a979b162ad260`. To move it onto the branch's current tip,
apply on the base first (above), then:

```bash
git fetch origin
git rebase origin/develop
```

Rebasing first and applying second tends to produce worse conflicts — apply on the
recorded base, then rebase.

## Then

1. Build — see [TESTING.md](TESTING.md).
2. Run the tiers marked SKIPPED, NOT RUN or LOCAL ONLY there.
3. Squash any `fixup!` commits: `git rebase -i --autosquash 7bfe3220bc12ec52655ca355096a979b162ad260`.
4. Push and open the PR yourself, using [PR_DESCRIPTION.md](PR_DESCRIPTION.md).
