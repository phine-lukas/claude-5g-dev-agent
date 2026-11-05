#!/usr/bin/env bash
# Setup script for the Claude cloud environment used by 5g-dev-agent.
#
# Paste the contents of this file into:
#   claude.ai/code -> environment settings -> Setup script
#
# Network access for the environment must reach, at minimum:
#   - the distro package mirrors (tick "default list of common package managers")
#   - www.3gpp.org        (spec downloads)
#   - github.com          (repos)
#   - ntfy.sh             (only if notifications are used)
# Development also pulls from gitlab.eurecom.fr (OAI RAN) and the Docker registry.
#
# Rules this script obeys:
#   - no environment variables are read (they may not exist during setup)
#   - nothing assumes where repos are cloned
#   - every step is idempotent and tolerant of failure; the session must start
#     even if a package is unavailable
# It is cached between sessions: after editing it, expect the next session to rebuild.

set -u
export DEBIAN_FRONTEND=noninteractive

say() { echo "[5g-dev-agent setup] $*"; }

INSTALLED=""
MISSING=""

# ------------------------------------------------------------------ packages --
# pandoc            spec conversion (ensure_specs.py)
# python3-yaml      manifest + profile parsing
# python3-requests  spec downloads (urllib fallback exists, but requests retries better)
# jq, curl          scripts and notifications
# clang-format      formatting changed lines in the C/C++ repos
CORE_PKGS="pandoc python3-yaml python3-requests jq curl clang-format git"
# Only needed for the handful of specs still published as legacy .doc.
OPTIONAL_PKGS="libreoffice-writer-nogui"

apt-get update -qq || say "apt-get update failed; continuing with whatever is cached"

for pkg in $CORE_PKGS; do
  if dpkg -s "$pkg" >/dev/null 2>&1; then
    INSTALLED="$INSTALLED $pkg(already)"
  elif apt-get install -y -qq --no-install-recommends "$pkg" >/dev/null 2>&1; then
    INSTALLED="$INSTALLED $pkg"
  else
    MISSING="$MISSING $pkg"
  fi
done

for pkg in $OPTIONAL_PKGS; do
  if dpkg -s "$pkg" >/dev/null 2>&1; then
    INSTALLED="$INSTALLED $pkg(already)"
  elif apt-get install -y -qq --no-install-recommends "$pkg" >/dev/null 2>&1; then
    INSTALLED="$INSTALLED $pkg"
  else
    say "optional package $pkg unavailable — legacy .doc specs will need conversion elsewhere"
  fi
done

# ------------------------------------------------------- find the toolkit repo --
# The session may start in any of the attached repos, so locate the toolkit by its
# marker file rather than by name. Bounded depth: these checkouts are large.
TOOLKIT=""
for base in /home /workspace /repo /root /srv /mnt; do
  [ -d "$base" ] || continue
  found="$(find "$base" -maxdepth 5 -name .toolkit-root -type f 2>/dev/null | head -1)"
  if [ -n "$found" ]; then TOOLKIT="$(dirname "$found")"; break; fi
done

if [ -n "$TOOLKIT" ]; then
  say "toolkit repo: $TOOLKIT"

  # Fallback for skill and hook discovery: if the session starts in a target repo
  # rather than the toolkit, project-scoped skills and hooks are not picked up.
  # Copying them into the personal config makes them work either way.
  HOME_DIR="${HOME:-/root}"
  mkdir -p "$HOME_DIR/.claude/skills" "$HOME_DIR/.claude/hooks" 2>/dev/null

  if [ -d "$TOOLKIT/.claude/skills" ]; then
    cp -r "$TOOLKIT/.claude/skills/." "$HOME_DIR/.claude/skills/" 2>/dev/null \
      && say "skills copied to ~/.claude/skills/" \
      || say "could not copy skills"
  fi

  if [ -d "$TOOLKIT/.claude/hooks" ]; then
    cp -r "$TOOLKIT/.claude/hooks/." "$HOME_DIR/.claude/hooks/" 2>/dev/null
    chmod +x "$HOME_DIR/.claude/hooks/"* 2>/dev/null
    # A personal settings.json pointing at the copied hooks, using absolute paths
    # ($CLAUDE_PROJECT_DIR would resolve to the wrong repo here).
    if [ ! -f "$HOME_DIR/.claude/settings.json" ]; then
      cat > "$HOME_DIR/.claude/settings.json" <<EOF
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          { "type": "command", "command": "python3 \"$HOME_DIR/.claude/hooks/push_guard.py\"" }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          { "type": "command", "command": "bash \"$HOME_DIR/.claude/hooks/notify.sh\" stop" }
        ]
      }
    ],
    "Notification": [
      {
        "hooks": [
          { "type": "command", "command": "bash \"$HOME_DIR/.claude/hooks/notify.sh\" notification" }
        ]
      }
    ]
  }
}
EOF
      say "hooks installed in ~/.claude/ (push guard active session-wide)"
    else
      say "~/.claude/settings.json already exists — left untouched; check it wires up push_guard.py"
    fi
  fi

  # Sanity check the guard actually runs here.
  if [ -f "$TOOLKIT/.claude/hooks/push_guard.py" ]; then
    if python3 "$TOOLKIT/.claude/hooks/push_guard.py" --self-test >/dev/null 2>&1; then
      say "push_guard self-test: passed"
    else
      say "WARN: push_guard self-test FAILED — pushes may not be blocked"
    fi
  fi
else
  say "no .toolkit-root found — skills and hooks will be used from the project directory"
fi

# ------------------------------------------- optional: OAI RAN build dependencies --
# Installing these at setup time saves ~10 minutes on the first build, but only works
# if the RAN repo is already cloned. If it isn't, the implement-feature skill installs
# them at task time instead.
OAI_BUILD=""
for base in /home /workspace /repo /root; do
  [ -d "$base" ] || continue
  found="$(find "$base" -maxdepth 5 -path "*/cmake_targets/build_oai" -type f 2>/dev/null | head -1)"
  if [ -n "$found" ]; then OAI_BUILD="$found"; break; fi
done

if [ -n "$OAI_BUILD" ]; then
  say "OAI RAN found at $(dirname "$(dirname "$OAI_BUILD")") — installing build dependencies"
  ( cd "$(dirname "$(dirname "$OAI_BUILD")")" && timeout 1800 ./cmake_targets/build_oai -I --ninja ) >/dev/null 2>&1 \
    && say "OAI build dependencies installed" \
    || say "build_oai -I did not complete; the skill will install deps at task time"
else
  say "OAI RAN not cloned yet — skipping build dependency pre-install"
fi

# Docker images are deliberately NOT pre-pulled: the T3 images in both profiles are
# built from the session's own branch, so a cached public image would only mislead.

# ------------------------------------------------------------------- summary --
say "---"
say "installed:$INSTALLED"
[ -n "$MISSING" ] && say "MISSING (check the environment's allowed domains):$MISSING"
say "pandoc: $(pandoc --version 2>/dev/null | head -1 || echo 'NOT AVAILABLE — spec conversion will fail')"
say "python3: $(python3 --version 2>&1)"
say "ready"

exit 0
