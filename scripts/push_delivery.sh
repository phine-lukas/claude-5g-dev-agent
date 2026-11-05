#!/usr/bin/env bash
# The ONLY sanctioned push in this toolkit: publish a delivery package on
# branch claude/delivery-<slug> of the toolkit repo itself.
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

BRANCH="claude/delivery-$SLUG"

# --dry-run reports and changes nothing: no branch, no commit, no push.
if [ "$DRY" -eq 1 ]; then
  echo "--dry-run: all guards passed."
  echo "  toolkit root : $ROOT"
  echo "  origin       : $ORIGIN"
  echo "  delivery     : deliveries/$SLUG ($(find "deliveries/$SLUG" -name '*.patch' | wc -l) patch file(s))"
  echo "  would branch : $BRANCH"
  echo "  would stage  : deliveries/$SLUG specs"
  echo "  would run    : git commit -m 'delivery: $SLUG' && git push -u origin $BRANCH"
  exit 0
fi

if git show-ref --verify --quiet "refs/heads/$BRANCH"; then
  git switch "$BRANCH"
else
  git switch -c "$BRANCH"
fi

git add -A "deliveries/$SLUG" specs
# specs/manifest.yaml is inside specs/, but add it explicitly in case it moved.
[ -f specs/manifest.yaml ] && git add specs/manifest.yaml

if git diff --cached --quiet; then
  echo "nothing to commit — $BRANCH is already up to date"
else
  git commit -q -m "delivery: $SLUG"
  echo "committed delivery: $SLUG on $BRANCH"
fi

git push -u origin "$BRANCH"
echo "pushed $BRANCH to $ORIGIN"
echo "apply it locally with: /apply-delivery $SLUG"
