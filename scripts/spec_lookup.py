#!/usr/bin/env python3
"""Search the converted 3GPP specs under specs/ (built by ensure_specs.py).

  spec_lookup.py list                                    # what is converted
  spec_lookup.py list 38.331                             # clause index of one spec
  spec_lookup.py clause 38.331 5.9.1                     # one clause's own text
  spec_lookup.py clause 38.331 5.9.1 --deep              # that clause and all subclauses
  spec_lookup.py grep 38.321 "G-RNTI"                    # matching lines, with their clause
  spec_lookup.py grep --all "MBS session"                # across every converted spec
  spec_lookup.py asn1 38.331 MBS-BroadcastConfiguration  # one ASN.1 type definition
  spec_lookup.py asn1 38.331 --list                      # every ASN.1 type name

Uses the newest converted version of a spec unless --version is given.
Output is capped by --max-lines (default 200) so a clause never floods the context.

Cite anything this prints as: TS <id> V<version> clause <n>.
"""

import argparse
import re
import sys
from pathlib import Path

TOC_ROW = re.compile(r"^\|\s*(.+?)\s*\|\s*(.*?)\s*\|\s*(\S+)\s*\|\s*(\d+)-(\d+)\s*\|$")


def toolkit_root() -> Path:
    here = Path(__file__).resolve().parent
    for candidate in [here, *here.parents]:
        if (candidate / ".toolkit-root").is_file():
            return candidate
    sys.exit(f"spec_lookup.py: no .toolkit-root found above {here}")


ROOT = toolkit_root()
SPECS = ROOT / "specs"


def version_key(name: str) -> tuple:
    try:
        return tuple(int(p) for p in name.split("."))
    except ValueError:
        return (0,)


def available() -> list[tuple[str, str, Path]]:
    out = []
    for meta in sorted(SPECS.glob("*/*/meta.yaml")):
        out.append((meta.parent.parent.name, meta.parent.name, meta.parent))
    return out


def resolve(spec_id: str, version: str | None) -> tuple[str, Path]:
    base = SPECS / spec_id
    if not base.is_dir():
        have = sorted({s for s, _, _ in available()})
        sys.exit(
            f"TS {spec_id} is not converted yet.\n"
            f"Run: python3 scripts/ensure_specs.py --spec {spec_id}\n"
            + (f"Converted so far: {', '.join(have)}" if have else "Nothing is converted yet.")
        )
    versions = sorted((d.name for d in base.iterdir() if (d / "toc.md").exists()), key=version_key)
    if not versions:
        sys.exit(f"TS {spec_id} has no converted version (run ensure_specs.py --spec {spec_id})")
    if version:
        if version not in versions:
            sys.exit(f"TS {spec_id} V{version} not converted; available: {', '.join(versions)}")
        return version, base / version
    return versions[-1], base / versions[-1]


def read_toc(directory: Path) -> list[tuple[str, str, str, int, int]]:
    rows = []
    for line in (directory / "toc.md").read_text().splitlines():
        m = TOC_ROW.match(line)
        if m and m.group(1) not in ("Clause", "---"):
            rows.append((m.group(1), m.group(2), m.group(3), int(m.group(4)), int(m.group(5))))
    return rows


def emit(lines: list[str], max_lines: int) -> None:
    for line in lines[:max_lines]:
        print(line)
    if len(lines) > max_lines:
        print(f"... truncated after {max_lines} of {len(lines)} lines (raise with --max-lines)")


def is_child(clause: str, parent: str) -> bool:
    return clause != parent and clause.startswith(parent) and clause[len(parent)] in ".."


# ------------------------------------------------------------------ list ----

def cmd_list(args) -> int:
    if not args.spec:
        entries = available()
        if not entries:
            print("Nothing converted yet. Run: python3 scripts/ensure_specs.py --tags mbs")
            return 0
        print(f"{'TS':<9} {'VERSION':<9} ASN.1  PATH")
        for spec_id, version, directory in entries:
            asn1 = "yes" if (directory / "asn1").is_dir() else "—"
            print(f"{spec_id:<9} {version:<9} {asn1:<6} {directory.relative_to(ROOT)}")
        return 0

    version, directory = resolve(args.spec, args.version)
    rows = read_toc(directory)
    print(f"=== TS {args.spec} V{version} — {len(rows)} clauses")
    pattern = re.compile(args.filter, re.I) if args.filter else None
    shown = [f"{clause:<12} {title}" for clause, title, _, _, _ in rows
             if not pattern or pattern.search(clause) or pattern.search(title)]
    emit(shown, args.max_lines)
    return 0


# ---------------------------------------------------------------- clause ----

def cmd_clause(args) -> int:
    version, directory = resolve(args.spec, args.version)
    rows = read_toc(directory)
    match = next((r for r in rows if r[0] == args.clause), None)
    if not match:
        near = [f"{c}  {t}" for c, t, _, _, _ in rows if c.startswith(args.clause)][:15]
        print(f"clause {args.clause} not found in TS {args.spec} V{version}", file=sys.stderr)
        if near:
            print("Did you mean:\n  " + "\n  ".join(near), file=sys.stderr)
        else:
            print(f"Try: spec_lookup.py grep {args.spec} '<keyword>'", file=sys.stderr)
        return 1

    clause, title, rel, start, end = match
    text = (directory / rel).read_text().splitlines()

    if not args.deep:
        # Stop at the first subclause that lives in the same file.
        child_starts = [s for c, _, r, s, _ in rows if r == rel and is_child(c, clause) and s > start]
        if child_starts:
            end = min(min(child_starts) - 1, end)

    print(f"=== TS {args.spec} V{version} clause {clause} — {title}")
    print(f"=== {rel} lines {start}-{end}" + ("" if args.deep else "  (add --deep for subclauses)"))
    emit(text[start - 1:end], args.max_lines)
    return 0


# ------------------------------------------------------------------ grep ----

def owner(rows, rel: str, line_no: int) -> str:
    """Deepest clause in `rel` that contains this line."""
    best = ""
    best_depth = -1
    for clause, _, r, start, end in rows:
        if r == rel and start <= line_no <= end:
            depth = clause.count(".")
            if depth > best_depth:
                best, best_depth = clause, depth
    return best or "?"


def grep_spec(spec_id: str, version: str, directory: Path, pattern, args, budget: list[int]) -> None:
    rows = read_toc(directory)
    for path in sorted((directory / "clauses").glob("*.md")):
        rel = f"clauses/{path.name}"
        for n, line in enumerate(path.read_text().splitlines(), 1):
            if not pattern.search(line):
                continue
            if budget[0] <= 0:
                return
            budget[0] -= 1
            text = line.strip()
            if len(text) > args.width:
                text = text[:args.width] + "…"
            print(f"TS {spec_id} V{version}  {owner(rows, rel, n):<12} {rel}:{n}  {text}")


def cmd_grep(args) -> int:
    try:
        pattern = re.compile(args.pattern, 0 if args.case else re.I)
    except re.error as exc:
        sys.exit(f"bad regex: {exc}")
    budget = [args.max_lines]
    if args.all:
        targets = [(s, v, d) for s, v, d in available()]
        # Newest version of each spec only.
        newest: dict[str, tuple[str, str, Path]] = {}
        for spec_id, version, directory in targets:
            if spec_id not in newest or version_key(version) > version_key(newest[spec_id][1]):
                newest[spec_id] = (spec_id, version, directory)
        targets = sorted(newest.values())
    else:
        if not args.spec:
            sys.exit("grep needs a spec id, or --all")
        version, directory = resolve(args.spec, args.version)
        targets = [(args.spec, version, directory)]

    for spec_id, version, directory in targets:
        grep_spec(spec_id, version, directory, pattern, args, budget)
        if budget[0] <= 0:
            print(f"... stopped at {args.max_lines} hits (raise with --max-lines)")
            break
    return 0


# ------------------------------------------------------------------ asn1 ----

DEF_START = re.compile(r"^([A-Za-z][\w-]*)\s*::=")


def cmd_asn1(args) -> int:
    version, directory = resolve(args.spec, args.version)
    path = directory / "asn1" / f"{args.spec}.asn"
    if not path.exists():
        sys.exit(
            f"No ASN.1 extracted for TS {args.spec} V{version}.\n"
            f"Mark the manifest entry with `asn1: true` and rerun "
            f"ensure_specs.py --spec {args.spec}."
        )
    lines = path.read_text().splitlines()
    starts = [(n, m.group(1)) for n, line in enumerate(lines) if (m := DEF_START.match(line))]

    if args.list or not args.type:
        names = [name for _, name in starts]
        print(f"=== TS {args.spec} V{version} — {len(names)} ASN.1 definitions")
        if args.filter:
            pattern = re.compile(args.filter, re.I)
            names = [n for n in names if pattern.search(n)]
        emit(names, args.max_lines)
        return 0

    wanted = args.type
    exact = [i for i, (_, name) in enumerate(starts) if name == wanted]
    if not exact:   # the spec suffixes release tags: Foo -> Foo-r17
        exact = [i for i, (_, name) in enumerate(starts) if re.fullmatch(rf"{re.escape(wanted)}-r\d+\w*", name)]
    if not exact:
        candidates = [name for _, name in starts if wanted.lower() in name.lower()]
        print(f"ASN.1 type '{wanted}' not found in TS {args.spec} V{version}", file=sys.stderr)
        if candidates:
            print("Close matches:\n  " + "\n  ".join(candidates[:20]), file=sys.stderr)
        else:
            print(f"List them all: spec_lookup.py asn1 {args.spec} --list", file=sys.stderr)
        return 1

    index = exact[0]
    start = starts[index][0]
    end = starts[index + 1][0] if index + 1 < len(starts) else len(lines)
    body = lines[start:end]
    while body and not body[-1].strip():
        body.pop()
    print(f"=== TS {args.spec} V{version} ASN.1 — {starts[index][1]}")
    emit(body, args.max_lines)
    return 0


def main() -> int:
    # Shared options, accepted both before and after the subcommand.
    # SUPPRESS keeps the subparser from overwriting a value given before the
    # subcommand (argparse re-applies `parents` defaults otherwise).
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--version", default=argparse.SUPPRESS,
                        help="use this spec version instead of the newest converted one")
    common.add_argument("--max-lines", type=int, default=argparse.SUPPRESS,
                        help="output cap (default 200)")

    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter,
        parents=[common],
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("list", parents=[common], help="what is converted, or one spec's clause index")
    p.add_argument("spec", nargs="?")
    p.add_argument("--filter", help="only clauses whose number or title match this regex")

    p = sub.add_parser("clause", parents=[common], help="print a clause")
    p.add_argument("spec")
    p.add_argument("clause")
    p.add_argument("--deep", action="store_true", help="include all subclauses")

    p = sub.add_parser("grep", parents=[common], help="search clause text")
    p.add_argument("spec", nargs="?")
    p.add_argument("pattern")
    p.add_argument("--all", action="store_true", help="search every converted spec")
    p.add_argument("--case", action="store_true", help="case-sensitive")
    p.add_argument("--width", type=int, default=200, help="truncate each hit at N characters")

    p = sub.add_parser("asn1", parents=[common], help="print an ASN.1 type definition")
    p.add_argument("spec")
    p.add_argument("type", nargs="?")
    p.add_argument("--list", action="store_true", help="list every type name")
    p.add_argument("--filter", help="with --list: only names matching this regex")

    args = parser.parse_args()
    args.max_lines = getattr(args, "max_lines", 200)
    args.version = getattr(args, "version", None)
    return {"list": cmd_list, "clause": cmd_clause, "grep": cmd_grep, "asn1": cmd_asn1}[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
