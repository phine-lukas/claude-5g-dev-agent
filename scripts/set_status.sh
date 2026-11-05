#!/usr/bin/env bash
# Write the agent status line that drives notifications (.claude/hooks/notify.sh).
#
#   set_status.sh <STATE> "<short message>"
#
# STATE is one of: PLAN_READY QUESTION BLOCKED DELIVERED FAILED RUNNING
# The file <toolkit-root>/.agent-status is gitignored and holds one line:
#   <STATE>|<message>|<ISO-8601 timestamp>

set -euo pipefail

STATES="PLAN_READY QUESTION BLOCKED DELIVERED FAILED RUNNING"

usage() {
  echo "usage: set_status.sh <STATE> \"<message>\"" >&2
  echo "       STATE: ${STATES}" >&2
  exit 2
}

[ $# -ge 1 ] || usage
STATE="$1"
shift
MESSAGE="${*:-}"

case " $STATES " in
  *" $STATE "*) ;;
  *) echo "set_status.sh: unknown state '$STATE' (expected one of: $STATES)" >&2; exit 2 ;;
esac

# Toolkit root = nearest ancestor of this script holding .toolkit-root.
dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
root=""
while [ "$dir" != "/" ]; do
  if [ -f "$dir/.toolkit-root" ]; then root="$dir"; break; fi
  dir="$(dirname "$dir")"
done
if [ -z "$root" ]; then
  echo "set_status.sh: no .toolkit-root found above $(dirname "${BASH_SOURCE[0]}")" >&2
  exit 1
fi

# Keep it to one line: newlines and pipes would break the hook's parsing.
MESSAGE="$(printf '%s' "$MESSAGE" | tr '\n|' '  ')"

printf '%s|%s|%s\n' "$STATE" "$MESSAGE" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" >"$root/.agent-status"
echo "status: $STATE — $MESSAGE"
