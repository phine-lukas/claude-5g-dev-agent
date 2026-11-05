#!/usr/bin/env bash
# Stop / Notification hook: push the agent's status line to ntfy.
#
#   notify.sh stop           # end of a turn: send only when the status changed
#   notify.sh notification   # Claude is waiting for input: always send
#
# Notifications are optional. With NTFY_TOPIC unset this exits silently, and it
# never fails the session: every path ends in `exit 0`.
#
# Env: NTFY_TOPIC (required to send), NTFY_SERVER (default https://ntfy.sh)

set -u

MODE="${1:-stop}"
TOPIC="${NTFY_TOPIC:-}"
[ -n "$TOPIC" ] || exit 0

SERVER="${NTFY_SERVER:-https://ntfy.sh}"
command -v curl >/dev/null 2>&1 || exit 0

# Toolkit root = nearest ancestor holding .toolkit-root, else this hook's grandparent.
root="${CLAUDE_PROJECT_DIR:-$PWD}"
dir="$root"
while [ "$dir" != "/" ]; do
  [ -f "$dir/.toolkit-root" ] && { root="$dir"; break; }
  dir="$(dirname "$dir")"
done
[ -f "$root/.toolkit-root" ] || root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." 2>/dev/null && pwd)" || exit 0

STATE="RUNNING"
MESSAGE="(no status set)"
if [ -r "$root/.agent-status" ]; then
  line="$(head -n1 "$root/.agent-status")"
  STATE="${line%%|*}"
  rest="${line#*|}"
  MESSAGE="${rest%%|*}"
fi

if [ "$MODE" = "notification" ]; then
  STATE="WAITING"
  MESSAGE="Claude is waiting for input — ${MESSAGE}"
else
  # Only ping when something actually changed since the last notification.
  stamp_file="/tmp/.5g-dev-agent-notify-$(id -u)-$(printf '%s' "$root" | cksum | cut -d' ' -f1)"
  current="$(printf '%s|%s' "$STATE" "$MESSAGE" | cksum | cut -d' ' -f1)"
  if [ -r "$stamp_file" ] && [ "$(cat "$stamp_file" 2>/dev/null)" = "$current" ]; then
    exit 0
  fi
  printf '%s' "$current" >"$stamp_file" 2>/dev/null || true
fi

PRIORITY_HEADER=()
case "$STATE" in
  QUESTION|BLOCKED|FAILED|WAITING) PRIORITY_HEADER=(-H "Priority: high") ;;
esac

curl -s -m 10 \
  -H "Title: 5g-dev-agent ${STATE}" \
  "${PRIORITY_HEADER[@]}" \
  -d "${MESSAGE}" \
  "${SERVER}/${TOPIC}" >/dev/null 2>&1 || true

exit 0
