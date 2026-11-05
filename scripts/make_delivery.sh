#!/usr/bin/env bash
# Export one patch series per repo into a delivery package.
#
#   make_delivery.sh <slug> <repo-path>:<base-sha> [<repo-path>:<base-sha> ...]
#
# For each repo it runs `git format-patch --base=<base-sha> <base-sha>..HEAD` into
#   deliveries/<slug>/patches/<repo-name>/
# and copies the delivery doc templates (never overwriting files that already
# exist, so a PLAN.md written in Phase 2 survives).
#
# Fails if a repo has uncommitted changes or no commits above its base.

set -euo pipefail

die() { echo "make_delivery.sh: $*" >&2; exit 1; }

[ $# -ge 2 ] || die "usage: make_delivery.sh <slug> <repo-path>:<base-sha> [...]"

SLUG="$1"; shift
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
[ -n "$ROOT" ] || die "no .toolkit-root found above $(dirname "${BASH_SOURCE[0]}")"

DELIVERY="$ROOT/deliveries/$SLUG"
mkdir -p "$DELIVERY/patches"

DATE="$(date -u +%Y-%m-%d)"
REPO_ROWS=""
REPO_SECTIONS=""
TOTAL_PATCHES=0

for arg in "$@"; do
  case "$arg" in
    *:*) ;;
    *) die "expected <repo-path>:<base-sha>, got '$arg'" ;;
  esac
  REPO_PATH="${arg%:*}"
  BASE="${arg##*:}"
  [ -d "$REPO_PATH" ] || die "no such directory: $REPO_PATH"
  REPO_PATH="$(cd "$REPO_PATH" && pwd)"
  NAME="$(basename "$REPO_PATH")"

  git -C "$REPO_PATH" rev-parse --is-inside-work-tree >/dev/null 2>&1 \
    || die "$REPO_PATH is not a git repository"
  git -C "$REPO_PATH" cat-file -e "${BASE}^{commit}" 2>/dev/null \
    || die "$NAME: base commit $BASE does not exist"

  if ! git -C "$REPO_PATH" diff --quiet || ! git -C "$REPO_PATH" diff --cached --quiet; then
    die "$NAME has uncommitted changes — commit or stash them first"
  fi

  COUNT="$(git -C "$REPO_PATH" rev-list --count "${BASE}..HEAD")"
  [ "$COUNT" -gt 0 ] || die "$NAME has no commits above $BASE"

  OUT="$DELIVERY/patches/$NAME"
  rm -rf "$OUT"
  mkdir -p "$OUT"
  git -C "$REPO_PATH" format-patch --base="$BASE" --no-signature -o "$OUT" "${BASE}..HEAD" >/dev/null

  BRANCH="$(git -C "$REPO_PATH" rev-parse --abbrev-ref HEAD)"
  REMOTE="$(git -C "$REPO_PATH" remote get-url origin 2>/dev/null || echo '(no origin)')"
  HEAD_SHA="$(git -C "$REPO_PATH" rev-parse HEAD)"
  SHORT_BASE="$(git -C "$REPO_PATH" rev-parse --short "$BASE")"
  LOG="$(git -C "$REPO_PATH" log --oneline --no-decorate "${BASE}..HEAD" | sed 's/^/    /')"
  STAT="$(git -C "$REPO_PATH" diff --stat "${BASE}..HEAD" | sed 's/^/    /')"

  TOTAL_PATCHES=$((TOTAL_PATCHES + COUNT))
  REPO_ROWS="${REPO_ROWS}| \`${NAME}\` | TODO(role) | TODO(base branch) | \`${SHORT_BASE}\` | ${COUNT} |
"
  REPO_SECTIONS="${REPO_SECTIONS}
### ${NAME}

- Remote: ${REMOTE}
- Agent branch: \`${BRANCH}\` (local only, never pushed) — HEAD \`${HEAD_SHA}\`
- Base commit: \`${BASE}\`
- Patches: \`patches/${NAME}/\` (${COUNT})

Commits:

\`\`\`
${LOG}
\`\`\`

Diffstat:

\`\`\`
${STAT}
\`\`\`
"
  echo "  ${NAME}: ${COUNT} patch(es) from ${SHORT_BASE} -> ${OUT#$ROOT/}"
done

# Copy templates, never clobbering what is already there.
for tpl in "$ROOT"/templates/delivery/*.md; do
  [ -e "$tpl" ] || continue
  target="$DELIVERY/$(basename "$tpl")"
  [ -e "$target" ] || cp "$tpl" "$target"
done

# Pre-fill the placeholders the script actually knows.
for f in "$DELIVERY"/*.md; do
  [ -e "$f" ] || continue
  python3 - "$f" "$SLUG" "$DATE" "$TOTAL_PATCHES" "$REPO_ROWS" "$REPO_SECTIONS" <<'PY'
import sys, pathlib
path, slug, date, total, rows, sections = sys.argv[1:7]
p = pathlib.Path(path)
text = p.read_text()
text = (text.replace("<SLUG>", slug)
            .replace("<DATE>", date)
            .replace("<N_PATCHES>", total)
            .replace("<REPO_TABLE_ROWS>", rows.rstrip("\n"))
            .replace("<REPO_SECTIONS>", sections.rstrip("\n")))
p.write_text(text)
PY
done

echo "delivery: ${DELIVERY#$ROOT/}  (${TOTAL_PATCHES} patch(es) total)"
echo "next: fill in README.md, APPLY.md, CHANGES.md, TESTING.md, OPEN_ISSUES.md, PR_DESCRIPTION.md"
