#!/usr/bin/env python3
"""PreToolUse(Bash) hook: block every push path except scripts/push_delivery.sh.

The cloud agent works in target and test repos it must never write to remotely.
This hook reads the hook JSON on stdin, looks at `tool_input.command`, and exits
2 (with the reason on stderr) when the command would push, open a PR, or change a
remote. Exit 0 lets the command through.

  push_guard.py              # hook mode (JSON on stdin)
  push_guard.py --self-test  # run the built-in allow/block cases
"""

import json
import re
import shlex
import sys

MESSAGE = (
    "Direct pushes are blocked. Use scripts/push_delivery.sh <slug> for delivery "
    "branches. Never push to target or test repos."
)

ALLOWED_SCRIPT = "push_delivery.sh"

# Wrappers that take the real command as their trailing arguments.
WRAPPERS = {"sudo", "env", "nohup", "time", "command", "builtin", "exec", "stdbuf", "ionice", "nice"}
SHELLS = {"sh", "bash", "zsh", "dash", "ksh", "busybox"}
OPERATORS = {"&&", "||", ";", "|", "&", "\n", ";;", "|&"}

# git global options that take a separate value argument.
GIT_VALUE_OPTS = {"-C", "-c", "--git-dir", "--work-tree", "--namespace", "--exec-path", "--config-env"}

# Mutating gh api methods.
WRITE_METHODS = {"POST", "PATCH", "PUT", "DELETE"}

# Last-resort textual patterns, applied to the raw command string so that pushes
# hidden in command substitutions or unparseable quoting are still caught.
RAW_PATTERNS = [
    re.compile(r"\bgit\b(?:\s+(?:-[A-Za-z-]+(?:=\S+)?|\S+=\S+|[^\s;|&]+))*?\s+push\b"),
    re.compile(r"\bgh\s+pr\s+(create|merge|ready|edit|close|reopen|comment|review)\b"),
    re.compile(r"\bgh\s+(repo|release)\b"),
    re.compile(r"\bgit\s+remote\s+(set-url|add)\b"),
]


def basename(token: str) -> str:
    return token.rsplit("/", 1)[-1]


def strip_prefixes(tokens: list[str]) -> list[str]:
    """Drop leading VAR=value assignments and wrapper commands."""
    i = 0
    while i < len(tokens):
        tok = tokens[i]
        if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*=.*", tok):
            i += 1
        elif basename(tok) in WRAPPERS:
            i += 1
            # `env`/`sudo` may carry their own flags before the command.
            while i < len(tokens) and tokens[i].startswith("-"):
                i += 1
        elif basename(tok) == "timeout":
            i += 1
            while i < len(tokens) and (tokens[i].startswith("-") or re.fullmatch(r"[0-9.]+[smhd]?", tokens[i])):
                i += 1
        else:
            break
    return tokens[i:]


def git_subcommand(args: list[str]) -> list[str]:
    """Remaining words after git's global options."""
    i = 0
    while i < len(args):
        tok = args[i]
        if tok in GIT_VALUE_OPTS:
            i += 2
        elif tok.startswith("-"):
            i += 1
        else:
            return args[i:]
    return []


def check_segment(tokens: list[str], depth: int = 0) -> str | None:
    """Reason to block this one command, or None."""
    tokens = strip_prefixes(tokens)
    if not tokens:
        return None
    cmd, args = basename(tokens[0]), tokens[1:]

    if any(ALLOWED_SCRIPT in t for t in tokens):
        return None  # the one sanctioned push path

    if cmd in SHELLS and depth < 4:
        for i, tok in enumerate(args):
            if tok in ("-c", "-lc", "-cl") and i + 1 < len(args):
                return check_command(args[i + 1], depth + 1)
        return None

    if cmd in ("xargs", "parallel") and depth < 4:
        rest = [a for a in args if not a.startswith("-")]
        return check_segment(rest, depth + 1) if rest else None

    if cmd == "git":
        sub = git_subcommand(args)
        if not sub:
            return None
        if sub[0] == "push":
            return "`git push` to any repository is blocked."
        if sub[0] == "remote" and len(sub) > 1 and sub[1] in ("set-url", "add"):
            return f"`git remote {sub[1]}` is blocked (it can redirect a push target)."
        if sub[0] == "send-email":
            return "`git send-email` is blocked."
        if sub[0] == "config":
            # Writing remote.<name>.url has the same effect as `git remote set-url`.
            # Reading it (`git config --get remote.origin.url`) is harmless: a write is
            # one where a value follows the key.
            for i, token in enumerate(sub[1:], start=1):
                if re.fullmatch(r"remote\..+\.(push)?url", token) and i + 1 < len(sub):
                    return f"`git config {token} <value>` is blocked (same effect as `git remote set-url`)."
        return None

    if cmd == "gh":
        sub = [a for a in args if not a.startswith("-")]
        if not sub:
            return None
        if sub[0] == "pr" and len(sub) > 1 and sub[1] in (
            "create", "merge", "ready", "edit", "close", "reopen", "comment", "review",
        ):
            return f"`gh pr {sub[1]}` is blocked. The user opens PRs manually."
        if sub[0] in ("repo", "release"):
            return f"`gh {sub[0]}` is blocked. For read-only lookups use `gh api` or `git ls-remote`."
        if sub[0] == "api":
            for i, tok in enumerate(args):
                if tok in ("-X", "--method") or tok.startswith("--method="):
                    value = tok.split("=", 1)[1] if "=" in tok else (args[i + 1] if i + 1 < len(args) else "")
                    if value.upper() in WRITE_METHODS:
                        return f"`gh api -X {value.upper()}` writes to GitHub and is blocked."
        return None

    return None


def check_command(command: str, depth: int = 0) -> str | None:
    """Reason to block this command line, or None."""
    if not command or not command.strip():
        return None

    try:
        lexer = shlex.shlex(command, posix=True, punctuation_chars=True)
        lexer.whitespace_split = True
        tokens = list(lexer)
        parsed = True
    except ValueError:
        tokens, parsed = [], False

    if parsed:
        segment: list[str] = []
        for tok in tokens:
            if tok in OPERATORS or (tok and set(tok) <= {"&", "|", ";"}):
                if reason := check_segment(segment, depth):
                    return reason
                segment = []
            else:
                segment.append(tok)
        if reason := check_segment(segment, depth):
            return reason

    # Belt and braces: catch pushes inside $(...), backticks, or unparseable quoting.
    if ALLOWED_SCRIPT not in command:
        for pattern in RAW_PATTERNS:
            if pattern.search(command):
                return f"This command contains a blocked push/remote operation (/{pattern.pattern}/)."
    return None


CASES: list[tuple[str, bool]] = [
    # (command, should_be_blocked)
    ("git push origin main", True),
    ("git push", True),
    ("git -C /src/oai push origin HEAD:develop", True),
    ("git --git-dir=/x/.git --work-tree=/x push -f", True),
    ("cd /repo && make && git push origin feature", True),
    ("make; git push", True),
    ("sh -c 'git push origin main'", True),
    ('bash -c "cd /tmp && git push"', True),
    ("sudo git push origin main", True),
    ("GIT_SSH_COMMAND='ssh -i k' git push origin main", True),
    ("timeout 60 git push origin main", True),
    ("echo $(git push origin main)", True),
    ("git remote set-url origin git@github.com:x/y.git", True),
    ("git remote add upstream https://github.com/a/b", True),
    ("gh pr create --title x --body y", True),
    ("gh pr merge 42 --squash", True),
    ("gh repo clone OPENAIRINTERFACE/openairinterface5g", True),
    ("gh release create v1.0", True),
    ("gh api -X POST repos/a/b/issues", True),
    ("git send-email --to a@b patches/0001.patch", True),
    ("git config remote.origin.url https://x/y.git", True),
    ("git -C /src config remote.origin.pushurl git@h:a/b.git", True),
    # Allowed
    ("scripts/push_delivery.sh 2026-11-05-gnb-mcch", False),
    ("bash scripts/push_delivery.sh 2026-11-05-gnb-mcch", False),
    ("./scripts/push_delivery.sh my-slug && echo done", False),
    ("git status", False),
    ("git log --oneline develop..HEAD", False),
    ("git format-patch --base=abc123 -o out/ abc123..HEAD", False),
    ("git fetch origin", False),
    ("git am -3 patches/0001.patch", False),
    ("git remote -v", False),
    ("git remote get-url origin", False),
    ("git config user.email t@t", False),
    ("git config --get remote.origin.url", False),
    ("git -C /src/oai rev-parse HEAD", False),
    ("gh pr view 42", False),
    ("gh pr list", False),
    ("gh api repos/a/b/branches", False),
    ("gh api -X GET repos/a/b/branches", False),
    ("ls -la && make -j8", False),
    ("grep -rn 'push' src/", False),
    ("python3 scripts/ensure_specs.py --tags mbs", False),
    ("docker compose up -d core", False),
    ("", False),
]


def self_test() -> int:
    failures = 0
    for command, should_block in CASES:
        reason = check_command(command)
        blocked = reason is not None
        if blocked != should_block:
            failures += 1
            want = "BLOCK" if should_block else "ALLOW"
            got = "BLOCK" if blocked else "ALLOW"
            print(f"FAIL  want {want}, got {got}: {command!r}" + (f"  [{reason}]" if reason else ""))
    total = len(CASES)
    print(f"{total - failures}/{total} push_guard cases passed")
    return 1 if failures else 0


def main() -> int:
    if "--self-test" in sys.argv:
        return self_test()
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0  # never break the session on a malformed hook payload
    command = (payload.get("tool_input") or {}).get("command", "")
    if reason := check_command(command):
        print(f"{reason}\n{MESSAGE}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
