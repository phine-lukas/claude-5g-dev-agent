#!/usr/bin/env bash
# Publish a delivery package as a folder on the toolkit repo's main branch, so
# reviewers never have to check out a branch to read one.
#
#   push_delivery.sh <slug> [--dry-run]
#
# It refuses to run anywhere but inside the toolkit repo, so it can never be
# pointed at a target or test repo. .claude/hooks/push_guard.py allows commands
# that invoke this script and blocks every other push.

set -euo pipefail

die() { echo "push_delivery.sh: $*" >&2; exit 1; }

DRY=0
ARGS=()
for a in "$@"; do
  case "$a" in
    --dry-run) DRY=1 ;;
    *) ARGS+=("$a") ;;
  esac
done
[ "${#ARGS[@]}" -eq 1 ] || die "usage: push_delivery.sh <slug> [--dry-run]"
SLUG="${ARGS[0]}"
case "$SLUG" in
  */*|.*|"") die "invalid slug '$SLUG'" ;;
esac

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

# Guard 3: the delivery must exist.
[ -d "deliveries/$SLUG" ] || die "deliveries/$SLUG does not exist (run make_delivery.sh first)"

# Deliveries land on the main branch as a folder, so a reviewer only has to
# pull main to see every delivery. Override for a repo whose default differs.
BRANCH="${DELIVERY_BRANCH:-main}"

# --dry-run reports and changes nothing: no branch, no commit, no push.
if [ "$DRY" -eq 1 ]; then
  echo "--dry-run: all guards passed."
  echo "  toolkit root : $ROOT"
  echo "  origin       : $ORIGIN"
  echo "  delivery     : deliveries/$SLUG ($(find "deliveries/$SLUG" -name '*.patch' | wc -l) patch file(s))"
  echo "  would branch : $BRANCH"
  echo "  would stage  : deliveries/$SLUG specs"
  echo "  would run    : git commit -m 'delivery: $SLUG' && git push origin $BRANCH"
  exit 0
fi

# Guard 4: anything staged that is not part of this delivery would be swept
# into the delivery commit. Report it and stop instead.
STAGED="$(git diff --cached --name-only | grep -v -e "^deliveries/$SLUG/" -e '^specs/' || true)"
if [ -n "$STAGED" ]; then
  echo "push_delivery.sh: staged changes outside deliveries/$SLUG and specs/:" >&2
  echo "$STAGED" | sed 's/^/    /' >&2
  die "unstage them (git restore --staged <path>) or commit them with push_toolkit.sh first"
fi

# Move onto the delivery branch. Untracked delivery files follow the switch.
CURRENT="$(git symbolic-ref --quiet --short HEAD || true)"
if [ "$CURRENT" != "$BRANCH" ]; then
  if git show-ref --verify --quiet "refs/heads/$BRANCH"; then
    git switch "$BRANCH"
  elif git rev-parse --quiet --verify "refs/remotes/origin/$BRANCH" >/dev/null; then
    git switch -c "$BRANCH" --track "origin/$BRANCH"
  else
    die "no branch '$BRANCH' here or on origin — create it first"
  fi
fi

# Guard 5: must fast-forward. Fetch first so a stale cloud checkout is caught
# here with a clear message instead of as a rejected push.
git fetch --quiet origin "$BRANCH" 2>/dev/null || true
if git rev-parse --quiet --verify "refs/remotes/origin/$BRANCH" >/dev/null; then
  BEHIND="$(git rev-list --count "HEAD..origin/$BRANCH")"
  if [ "$BEHIND" -gt 0 ]; then
    die "origin/$BRANCH has $BEHIND commit(s) you don't have — rebase first: git pull --rebase origin $BRANCH"
  fi
fi

git add -A "deliveries/$SLUG" specs
# specs/manifest.yaml is inside specs/, but add it explicitly in case it moved.
[ -f specs/manifest.yaml ] && git add specs/manifest.yaml

if git diff --cached --quiet; then
  echo "nothing to commit — deliveries/$SLUG is already on $BRANCH"
else
  git commit -q -m "delivery: $SLUG"
  echo "committed delivery: $SLUG on $BRANCH"
fi

git push origin "$BRANCH"
echo "pushed $BRANCH to $ORIGIN"
echo "it is in deliveries/$SLUG on $BRANCH — apply it locally with: /apply-delivery $SLUG"
