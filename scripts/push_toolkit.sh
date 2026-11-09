#!/usr/bin/env bash
# Push changes to the toolkit repo itself (skills, scripts, templates, docs,
# profiles) — the second and last sanctioned push in this toolkit.
#
#   push_toolkit.sh [--dry-run]
#
# It pushes the CURRENT branch of the toolkit repo (normally `main`) to origin.
# It never commits for you: commit first, then run this. Delivery packages go
# out through push_delivery.sh instead.
#
# Guards: only inside the toolkit repo, only to an origin that looks like the
# 5g-dev-agent repo, never a force push, never a non-fast-forward.
# .claude/hooks/push_guard.py allows commands that invoke this script or
# push_delivery.sh and blocks every other push.

set -euo pipefail

die() { echo "push_toolkit.sh: $*" >&2; exit 1; }

DRY=0
for a in "$@"; do
  case "$a" in
    --dry-run) DRY=1 ;;
    -f|--force|--force-with-lease|--mirror|--delete)
      die "'$a' is never allowed — this script only fast-forwards origin" ;;
    *) die "usage: push_toolkit.sh [--dry-run]" ;;
  esac
done

# Toolkit root = nearest ancestor of this script holding .toolkit-root.
dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT=""
while [ "$dir" != "/" ]; do
  if [ -f "$dir/.toolkit-root" ]; then ROOT="$dir"; break; fi
  dir="$(dirname "$dir")"
done
[ -n "$ROOT" ] || die "no .toolkit-root found above $(dirname "${BASH_SOURCE[0]}") — this is not the toolkit repo"

cd "$ROOT"

# Guard 1: we are in a git repo whose top level is the toolkit root.
TOP="$(git rev-parse --show-toplevel 2>/dev/null)" || die "$ROOT is not a git repository"
[ "$TOP" = "$ROOT" ] || die "git top level ($TOP) is not the toolkit root ($ROOT) — refusing to push"

# Guard 2: origin must be this toolkit repo, not a target or test repo.
ORIGIN="$(git remote get-url origin 2>/dev/null)" || die "no 'origin' remote configured"
case "$ORIGIN" in
  *5g-dev-agent*) ;;
  *) die "origin is '$ORIGIN', which does not look like the 5g-dev-agent toolkit repo — refusing to push" ;;
esac

# Guard 3: on a real branch, and not a delivery branch.
BRANCH="$(git symbolic-ref --quiet --short HEAD)" \
  || die "HEAD is detached — switch to a branch first"
case "$BRANCH" in
  claude/delivery-*) die "'$BRANCH' is a delivery branch — use push_delivery.sh <slug> for those" ;;
esac

# Guard 4: nothing half-finished. Uncommitted work is reported, not pushed.
DIRTY="$(git status --porcelain --untracked-files=normal | grep -v '^?? deliveries/' || true)"
if [ -n "$DIRTY" ]; then
  echo "push_toolkit.sh: uncommitted changes — these are NOT part of the push:" >&2
  echo "$DIRTY" | sed 's/^/    /' >&2
fi

# Guard 5: must fast-forward. Fetch first so a stale cloud checkout is caught
# here with a clear message instead of as a rejected push.
git fetch --quiet origin "$BRANCH" 2>/dev/null || true
AHEAD=0
BEHIND=0
if git rev-parse --quiet --verify "refs/remotes/origin/$BRANCH" >/dev/null; then
  read -r BEHIND AHEAD < <(git rev-list --left-right --count "origin/$BRANCH...HEAD")
  if [ "$BEHIND" -gt 0 ]; then
    die "origin/$BRANCH has $BEHIND commit(s) you don't have — rebase first: git pull --rebase origin $BRANCH"
  fi
  if [ "$AHEAD" -eq 0 ]; then
    echo "nothing to push — $BRANCH is already up to date with origin"
    exit 0
  fi
else
  AHEAD="$(git rev-list --count HEAD)"
  echo "note: origin has no '$BRANCH' yet — it will be created"
fi

COMMITS="$(git log --oneline --no-decorate -n "$AHEAD" HEAD | sed 's/^/    /')"

if [ "$DRY" -eq 1 ]; then
  echo "--dry-run: all guards passed."
  echo "  toolkit root : $ROOT"
  echo "  origin       : $ORIGIN"
  echo "  branch       : $BRANCH"
  echo "  would push   : $AHEAD commit(s)"
  echo "$COMMITS"
  echo "  would run    : git push origin $BRANCH"
  exit 0
fi

echo "pushing $AHEAD commit(s) on $BRANCH:"
echo "$COMMITS"
git push origin "$BRANCH"
echo "pushed $BRANCH to $ORIGIN"
