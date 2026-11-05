#!/usr/bin/env python3
"""Make sure the 3GPP specs a task needs are present as searchable Markdown.

  ensure_specs.py --tags mbs,ran            # everything tagged mbs or ran
  ensure_specs.py --spec 38.331 --spec 38.321
  ensure_specs.py --all
  ensure_specs.py --tags mbs --dry-run      # resolve versions, download nothing
  ensure_specs.py --spec 38.321 --release 17

Selection is the union of --tags and --spec (--all takes everything in
specs/manifest.yaml). For each selected spec it resolves the newest version of
the target release from the live 3GPP archive listing; if
specs/<id>/<version>/meta.yaml already exists the spec is reported as `present`
and nothing is downloaded.

Otherwise the archive is fetched into specs/<id>/<version>/raw/ (gitignored),
converted with pandoc, and written out as:

  specs/<id>/<version>/meta.yaml    id, title, version, source URL, sha256, date
  specs/<id>/<version>/toc.md       clause -> title -> file -> line range
  specs/<id>/<version>/clauses/*.md one file per top-level clause, split deeper
                                    wherever a file would exceed ~150 KB
  specs/<id>/<version>/asn1/<id>.asn  (only for entries flagged `asn1: true`)

Needs: pandoc. LibreOffice (`soffice`) only for the few specs still shipped as
legacy .doc. Downloaded archives are never committed; the Markdown is.

Exit status is non-zero if any requested spec failed.
"""

import argparse
import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import zipfile
from datetime import date, timezone, datetime
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("ensure_specs.py needs PyYAML: pip install pyyaml (or apt install python3-yaml)")

try:
    import requests
except ImportError:
    requests = None
    import urllib.error
    import urllib.request

ARCHIVE = "https://www.3gpp.org/ftp/Specs/archive/{series}_series/{spec}/"
# The 3GPP FTP mirror rejects non-browser user agents with 403.
BROWSER_UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/126.0 Safari/537.36"
)
MAX_CLAUSE_BYTES = 150 * 1024
RETRIES = 3

HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
# "5", "5.8.1.3", "6.3.2a"
NUMERIC_CLAUSE = re.compile(r"^(\d+(?:\.\d+)*[A-Za-z]?)(?:\s+(.*))?$")
# "Annex A (normative): ASN.1 definitions"
ANNEX_HEAD = re.compile(r"^Annex\s+([A-Z][0-9A-Za-z]*)\b\s*(.*)$", re.I)
# "A.2.1 Something" inside an annex
ANNEX_CLAUSE = re.compile(r"^([A-Z])((?:\.\d+)+[A-Za-z]?)(?:\s+(.*))?$")
ASN1_BLOCK = re.compile(r"--\s*ASN1START(.*?)--\s*ASN1STOP", re.S)


def toolkit_root() -> Path:
    here = Path(__file__).resolve().parent
    for candidate in [here, *here.parents]:
        if (candidate / ".toolkit-root").is_file():
            return candidate
    sys.exit(f"ensure_specs.py: no .toolkit-root found above {here}")


ROOT = toolkit_root()
SPECS = ROOT / "specs"


def log(msg: str) -> None:
    print(msg, file=sys.stderr, flush=True)


# ----------------------------------------------------------------- network --

class Unreachable(RuntimeError):
    pass


def fetch(url: str, binary: bool = False):
    """GET with retries and backoff. Raises Unreachable after the last attempt."""
    last = None
    for attempt in range(1, RETRIES + 1):
        try:
            if requests is not None:
                response = requests.get(url, headers={"User-Agent": BROWSER_UA}, timeout=300)
                response.raise_for_status()
                return response.content if binary else response.text
            req = urllib.request.Request(url, headers={"User-Agent": BROWSER_UA})
            with urllib.request.urlopen(req, timeout=300) as r:
                data = r.read()
            return data if binary else data.decode("utf-8", errors="replace")
        except Exception as exc:  # noqa: BLE001 - any transport error is retryable here
            last = exc
            if attempt < RETRIES:
                delay = 2 ** attempt
                log(f"    [retry {attempt}/{RETRIES - 1}] {type(exc).__name__}: {exc} — waiting {delay}s")
                time.sleep(delay)
    raise Unreachable(
        f"{url} unreachable after {RETRIES} attempts ({type(last).__name__}: {last}). "
        "If this is a cloud session, the environment's network policy probably blocks "
        "www.3gpp.org — allow it in the environment settings and retry."
    )


# ------------------------------------------------------- version resolution --

def code_char(n: int) -> str:
    """3GPP version-code digit: 0-9 then a=10 ... z=35."""
    if not 0 <= n <= 35:
        raise ValueError(f"version component {n} is out of range for a 3GPP version code")
    return str(n) if n < 10 else chr(ord("a") + n - 10)


def char_value(c: str) -> int:
    return int(c) if c.isdigit() else ord(c.lower()) - ord("a") + 10


def to_code(version: str) -> str:
    return "".join(code_char(int(part)) for part in version.split("."))


def from_code(code: str) -> str:
    return ".".join(str(char_value(c)) for c in code)


def resolve_version(spec_id: str, release: int, pinned: str | None) -> tuple[str, str]:
    """Return (version, zip name) for the newest `release` version in the archive."""
    series = spec_id.split(".")[0]
    listing = fetch(ARCHIVE.format(series=series, spec=spec_id))
    stem = spec_id.replace(".", "")
    codes = sorted(
        set(re.findall(rf"{stem}-([0-9a-z]{{3}})\.zip", listing, re.I)),
        key=lambda c: tuple(char_value(x) for x in c),
    )
    if not codes:
        raise RuntimeError(f"no versions of {spec_id} found in the archive listing")

    if pinned:
        want = to_code(pinned)
        if want.lower() in [c.lower() for c in codes]:
            return pinned, f"{stem}-{want}.zip"
        raise RuntimeError(
            f"pinned version {pinned} of {spec_id} is not in the archive "
            f"(available: {', '.join(from_code(c) for c in codes[-5:])})"
        )

    target = code_char(release)
    in_release = [c for c in codes if c[0].lower() == target.lower()]
    if not in_release:
        raise RuntimeError(
            f"no Rel-{release} version of {spec_id} in the archive "
            f"(newest available: {from_code(codes[-1])})"
        )
    best = in_release[-1]
    return from_code(best), f"{stem}-{best}.zip"


# ----------------------------------------------------------- doc conversion --

def soffice() -> str | None:
    for candidate in ("soffice", "libreoffice", "/snap/bin/libreoffice"):
        path = shutil.which(candidate)
        if path:
            try:
                if subprocess.run([path, "--version"], capture_output=True, timeout=120).returncode == 0:
                    return path
            except (subprocess.SubprocessError, OSError):
                continue
    return None


TABLE = re.compile(r"<table.*?</table>", re.S)
ROW = re.compile(r"<tr.*?</tr>", re.S)
CELL = re.compile(r"<t[hd]([^>]*)>(.*?)</t[hd]>", re.S)


def compact_tables(md: str) -> str:
    """Pandoc emits verbose HTML for merged-cell tables; flatten each row to one line.

    3GPP specs are full of merged-cell tables (IE tables, message formats). Left as
    HTML they are unreadable and unsearchable; flattened they grep cleanly.
    """
    def one_row(match: re.Match) -> str:
        cells = []
        for attrs, body in CELL.findall(match.group(0)):
            text = re.sub(r"<br\s*/?>", " / ", body)
            text = re.sub(r"<[^>]+>", " ", text)
            text = re.sub(r"\s+", " ", text).strip()
            span = re.search(r'colspan="(\d+)"', attrs)
            cells.append(text + (f" (x{span.group(1)})" if span and text else ""))
        return "| " + " | ".join(cells) + " |" if any(cells) else ""

    def one_table(match: re.Match) -> str:
        rows = [r for r in (one_row(x) for x in ROW.finditer(match.group(0))) if r]
        return "\n".join(["<!-- table -->", *rows, "<!-- /table -->"])

    return TABLE.sub(one_table, md)


def to_markdown(docs: list[Path], work: Path) -> str:
    parts = []
    for doc in docs:
        if doc.suffix.lower() == ".doc":
            binary = soffice()
            if not binary:
                raise RuntimeError(
                    f"{doc.name} is a legacy .doc file and LibreOffice is not installed. "
                    "Install libreoffice-writer-nogui (or soffice) and retry."
                )
            subprocess.run(
                [binary, "--headless", "--convert-to", "docx", "--outdir", str(work), str(doc)],
                check=True, capture_output=True, timeout=900,
            )
            doc = work / (doc.stem + ".docx")
            if not doc.exists():
                raise RuntimeError(f"LibreOffice did not produce {doc.name}")
        result = subprocess.run(
            ["pandoc", "-f", "docx", "-t", "gfm", "--wrap=none", str(doc)],
            capture_output=True, text=True, timeout=3600,
        )
        if result.returncode != 0:
            raise RuntimeError(f"pandoc failed on {doc.name}: {result.stderr.strip()[:400]}")
        # Figures are images we do not keep; leave a marker so clause text stays contiguous.
        parts.append(compact_tables(re.sub(r"!\[[^\]]*\]\([^)]*\)", "[figure]", result.stdout)))
    return "\n\n".join(parts)


# -------------------------------------------------------------- clause tree --

class Section:
    __slots__ = ("clause", "depth", "title", "start", "end", "children")

    def __init__(self, clause: str, depth: int, title: str, start: int):
        self.clause = clause
        self.depth = depth
        self.title = title
        self.start = start          # 0-based index of the heading line
        self.end = start            # exclusive; filled in later
        self.children: list["Section"] = []


def parse_heading(text: str) -> tuple[str, int, str] | None:
    """(clause, depth, title) for a 3GPP heading, or None if it isn't one.

    Depth comes from the clause number, not the Markdown heading level: pandoc's
    levels drift between specs, the numbering does not.
    """
    clean = re.sub(r"[*_`]|\\(?=.)", "", text).strip()
    if not clean:
        return None

    if m := ANNEX_HEAD.match(clean):
        letter, rest = m.group(1), (m.group(2) or "").strip()
        return f"Annex {letter}", 1, rest or f"Annex {letter}"

    if m := ANNEX_CLAUSE.match(clean):
        letter, tail, rest = m.group(1), m.group(2), (m.group(3) or "").strip()
        clause = f"{letter}{tail}"
        return clause, 1 + tail.count("."), rest or clause

    if m := NUMERIC_CLAUSE.match(clean):
        number, rest = m.group(1), (m.group(2) or "").strip()
        return number, number.count(".") + 1, rest or number

    return None


def build_tree(lines: list[str]) -> tuple[list[Section], int]:
    """Top-level sections plus the line where the first one starts (front matter end).

    3GPP documents open with a title page, foreword and a table of contents that
    repeats every clause heading. The real body starts at the *second* occurrence
    of clause 1, so the first heading that is followed by actual prose wins.
    """
    flat: list[Section] = []
    for index, line in enumerate(lines):
        m = HEADING.match(line)
        if not m:
            continue
        text = m.group(2)
        if not text.strip():
            # A soft line break inside a Word heading makes pandoc emit "#" on its
            # own line with the heading text underneath. Pull it back up.
            for follow in lines[index + 1:index + 3]:
                if follow.strip():
                    text = follow.strip()
                    break
        parsed = parse_heading(text)
        if not parsed:
            continue
        clause, depth, title = parsed
        flat.append(Section(clause, depth, title, index))

    if not flat:
        return [], 0

    # Drop the embedded table of contents: a run of headings at the top where the
    # same clause number appears again later in the document.
    seen: dict[str, list[int]] = {}
    for i, section in enumerate(flat):
        seen.setdefault(section.clause, []).append(i)
    first_body = 0
    for i, section in enumerate(flat):
        later = [j for j in seen[section.clause] if j > i]
        if not later:
            first_body = i
            break
    else:
        first_body = 0
    # Walk back to the first heading of the body run (the duplicate block is contiguous).
    while first_body > 0:
        previous = flat[first_body - 1]
        if [j for j in seen[previous.clause] if j >= first_body]:
            first_body -= 1
        else:
            break
    flat = flat[first_body:]

    for i, section in enumerate(flat):
        section.end = flat[i + 1].start if i + 1 < len(flat) else len(lines)

    # Nest by depth.
    roots: list[Section] = []
    stack: list[Section] = []
    for section in flat:
        while stack and stack[-1].depth >= section.depth:
            stack.pop()
        if stack:
            stack[-1].children.append(section)
        else:
            roots.append(section)
        stack.append(section)

    # A parent spans all of its children.
    def close(section: Section) -> None:
        for child in section.children:
            close(child)
        if section.children:
            section.end = max(section.end, section.children[-1].end)

    for root in roots:
        close(root)

    return roots, flat[0].start


def file_name(clause: str) -> str:
    if clause.startswith("Annex "):
        return f"annex-{clause.split()[1]}.md"
    if re.match(r"^[A-Z](\.\d+)+", clause):
        return f"annex-{clause}.md"
    return f"{clause}.md"


def write_clauses(lines: list[str], roots: list[Section], front_end: int, out: Path) -> list[tuple]:
    """Write clause files; return toc rows (clause, title, file, start, end)."""
    clauses_dir = out / "clauses"
    if clauses_dir.exists():
        shutil.rmtree(clauses_dir)
    clauses_dir.mkdir(parents=True)
    rows: list[tuple] = []

    if front_end > 0:
        body = "\n".join(lines[:front_end]).strip()
        if body:
            (clauses_dir / "front-matter.md").write_text(body + "\n")
            rows.append(("front-matter", "Title page, foreword and scope front matter",
                         "clauses/front-matter.md", 1, body.count("\n") + 1))

    def emit(section: Section) -> None:
        text = "\n".join(lines[section.start:section.end]).strip() + "\n"
        too_big = len(text.encode("utf-8")) > MAX_CLAUSE_BYTES
        if not too_big or not section.children:
            name = file_name(section.clause)
            (clauses_dir / name).write_text(text)
            index_rows(section, f"clauses/{name}", section.start)
            return
        # Split: the parent keeps its lead-in, each child gets its own file.
        lead_end = section.children[0].start
        lead = "\n".join(lines[section.start:lead_end]).strip()
        name = file_name(section.clause)
        (clauses_dir / name).write_text((lead or f"# {section.clause} {section.title}") + "\n")
        rows.append((section.clause, section.title, f"clauses/{name}", 1, max(1, lead.count("\n") + 1)))
        for child in section.children:
            emit(child)

    def index_rows(section: Section, rel: str, base: int) -> None:
        """One toc row per clause inside a file, with 1-based line numbers in that file."""
        rows.append((section.clause, section.title, rel,
                     section.start - base + 1, section.end - base))
        for child in section.children:
            index_rows(child, rel, base)

    for root in roots:
        emit(root)
    return rows


def write_toc(spec_id: str, version: str, title: str, rows: list[tuple], out: Path) -> None:
    lines = [
        f"# TS {spec_id} V{version} — {title}",
        "",
        "Clause index. `File` is relative to this directory; `Lines` is the 1-based",
        "line range of the clause inside that file.",
        "",
        "| Clause | Title | File | Lines |",
        "|---|---|---|---|",
    ]
    for clause, clause_title, rel, start, end in rows:
        safe = clause_title.replace("|", "\\|")
        lines.append(f"| {clause} | {safe} | {rel} | {start}-{end} |")
    (out / "toc.md").write_text("\n".join(lines) + "\n")


def official_title(lines: list[str], spec_id: str) -> str:
    """The spec's own title, from the cover page.

    3GPP cover pages read:
        3GPP TS 38.321 V18.10.0 (2026-06)
        Technical Specification
        3rd Generation Partnership Project;
        Technical Specification Group Radio Access Network;
        NR;
        Medium Access Control (MAC) protocol specification
        (Release 18)
    Everything between the TSG line and the "(Release N)" line is the title.
    """
    text = [re.sub(r"[*_`]|\\(?=.)", "", line).strip() for line in lines[:120]]
    start = next((i for i, line in enumerate(text)
                  if re.match(r"Technical Specification Group\b", line, re.I)), None)
    end = next((i for i, line in enumerate(text)
                if re.match(r"\(?Release\s+\d+\)?$", line, re.I)), None)
    if start is None or end is None or end <= start:
        return ""
    parts = [line.rstrip(";").strip() for line in text[start + 1:end] if line.strip()]
    return "; ".join(parts)


def write_asn1(spec_id: str, markdown: str, out: Path) -> int:
    blocks = [b.strip("\n") for b in ASN1_BLOCK.findall(markdown)]
    if not blocks:
        return 0
    asn1_dir = out / "asn1"
    asn1_dir.mkdir(parents=True, exist_ok=True)
    header = (
        f"-- ASN.1 extracted from TS {spec_id}, all -- ASN1START / -- ASN1STOP blocks,\n"
        f"-- in document order. Generated by scripts/ensure_specs.py; do not edit.\n\n"
    )
    # Pandoc escapes some punctuation inside code spans; undo the harmless ones.
    def clean(block: str) -> str:
        # Pandoc turns every ASN.1 line into its own paragraph, so the extracted
        # grammar comes out double-spaced. Drop the blank lines inside a block;
        # ASN.1 carries no meaning in them.
        body = [line.rstrip() for line in block.splitlines()]
        return "\n".join(line for line in body if line.strip())

    text = "\n\n".join(clean(b) for b in blocks)
    for escaped, plain in (("\\_", "_"), ("\\-", "-"), ("\\[", "["), ("\\]", "]"),
                           ("\\<", "<"), ("\\>", ">"), ("\\*", "*"), ("\\|", "|")):
        text = text.replace(escaped, plain)
    (asn1_dir / f"{spec_id}.asn").write_text(header + text + "\n")
    return len(blocks)


def write_index() -> int:
    entries = []
    for meta_path in sorted(SPECS.glob("*/*/meta.yaml")):
        try:
            meta = yaml.safe_load(meta_path.read_text()) or {}
        except yaml.YAMLError:
            continue
        entries.append((
            meta.get("id", meta_path.parent.parent.name),
            meta.get("version", meta_path.parent.name),
            meta.get("official_title") or meta.get("title", ""),
            meta.get("converted", ""),
            (meta_path.parent / "asn1").is_dir(),
            meta_path.parent.relative_to(SPECS).as_posix(),
        ))
    lines = [
        "# Converted 3GPP specifications",
        "",
        "Generated by `scripts/ensure_specs.py` — do not edit by hand.",
        "Search with `scripts/spec_lookup.py`; cite as `TS <id> V<version> clause <n>`.",
        "",
        "| TS | Version | Title | ASN.1 | Converted | Contents |",
        "|---|---|---|---|---|---|",
    ]
    for spec_id, version, title, converted, has_asn1, rel in entries:
        lines.append(
            f"| {spec_id} | V{version} | {title} | {'yes' if has_asn1 else '—'} | "
            f"{converted} | [toc]({rel}/toc.md) |"
        )
    if not entries:
        lines.append("| — | — | _nothing converted yet_ | — | — | — |")
    (SPECS / "INDEX.md").write_text("\n".join(lines) + "\n")
    return len(entries)


# ------------------------------------------------------------------- build --

def convert(entry: dict, version: str, zip_name: str) -> str:
    spec_id = entry["id"]
    out = SPECS / spec_id / version
    raw = out / "raw"
    raw.mkdir(parents=True, exist_ok=True)
    url = ARCHIVE.format(series=spec_id.split(".")[0], spec=spec_id) + zip_name
    zip_path = raw / zip_name

    if not zip_path.exists():
        zip_path.write_bytes(fetch(url, binary=True))
    if not zipfile.is_zipfile(zip_path):
        zip_path.unlink(missing_ok=True)
        raise RuntimeError(f"{zip_name} is not a valid zip archive (download corrupted or blocked)")
    sha256 = hashlib.sha256(zip_path.read_bytes()).hexdigest()

    # LibreOffice under snap confinement cannot see /tmp; keep scratch inside the kit.
    scratch = ROOT / "build-tmp"
    scratch.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(dir=scratch) as tmp:
        work = Path(tmp)
        with zipfile.ZipFile(zip_path) as archive:
            for member in archive.namelist():
                if not (work / member).resolve().is_relative_to(work.resolve()):
                    raise RuntimeError(f"unsafe path in {zip_name}: {member}")
            archive.extractall(work)
        for inner in list(work.rglob("*.zip")):          # some specs ship annexes separately
            try:
                with zipfile.ZipFile(inner) as nested:
                    nested.extractall(inner.with_suffix(""))
            except zipfile.BadZipFile:
                continue
        docs = sorted(
            p for p in work.rglob("*")
            if p.suffix.lower() in {".docx", ".doc"} and not p.name.startswith("~")
        )
        if not docs:
            raise RuntimeError(f"no Word document inside {zip_name}")
        markdown = to_markdown(docs, work)

    lines = markdown.splitlines()
    roots, front_end = build_tree(lines)
    if not roots:
        raise RuntimeError("no clause headings recognised — pandoc output looks unexpected")
    rows = write_clauses(lines, roots, front_end, out)
    write_toc(spec_id, version, entry.get("title", ""), rows, out)
    n_asn1 = write_asn1(spec_id, markdown, out) if entry.get("asn1") else 0

    title_3gpp = official_title(lines, spec_id)
    label = entry.get("title", "")
    if title_3gpp and label:
        # Manifest titles are short working labels; warn only when the label shares
        # no significant word with the real title (i.e. it probably names another spec).
        words = {w.lower() for w in re.findall(r"[A-Za-z]{3,}", label)}
        real = {w.lower() for w in re.findall(r"[A-Za-z]{3,}", title_3gpp)}
        if words and not (words & real):
            log(f"    [warn] manifest label {label!r} shares no word with the document "
                f"title {title_3gpp!r} — check the manifest entry for {spec_id}")

    meta = {
        "id": spec_id,
        "title": label,
        "official_title": title_3gpp,
        "version": version,
        "release": int(version.split(".")[0]),
        "source": url,
        "archive": zip_name,
        "sha256": sha256,
        "converted": datetime.now(timezone.utc).date().isoformat(),
        "documents": len(docs),
        "clause_files": len(list((out / "clauses").glob("*.md"))),
        "asn1_blocks": n_asn1,
    }
    (out / "meta.yaml").write_text(yaml.safe_dump(meta, sort_keys=False))

    extra = f", {n_asn1} ASN.1 blocks" if n_asn1 else ""
    return f"{meta['clause_files']} clause files from {len(docs)} document(s){extra}"


def select(manifest: dict, args) -> list[dict]:
    specs = manifest.get("specs") or []
    if args.all:
        return list(specs)
    wanted_tags = {t.strip() for arg in (args.tags or []) for t in arg.split(",") if t.strip()}
    wanted_ids = set(args.spec or [])
    chosen, seen = [], set()
    for entry in specs:
        if entry["id"] in seen:
            continue
        if entry["id"] in wanted_ids or (wanted_tags & set(entry.get("tags") or [])):
            chosen.append(entry)
            seen.add(entry["id"])
    # Ids asked for that the manifest does not know about.
    for spec_id in sorted(wanted_ids - seen):
        chosen.append({"id": spec_id, "title": "(not in manifest)", "tags": [], "_unlisted": True})
    return chosen


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--tags", action="append", metavar="a,b",
                        help="select manifest entries carrying any of these tags (repeatable)")
    parser.add_argument("--spec", action="append", metavar="38.331",
                        help="select this spec id (repeatable)")
    parser.add_argument("--all", action="store_true", help="select every entry in the manifest")
    parser.add_argument("--release", type=int, help="override the manifest's default release")
    parser.add_argument("--dry-run", action="store_true",
                        help="resolve versions and report, download nothing")
    parser.add_argument("--force", action="store_true",
                        help="re-convert even if the version is already present "
                             "(reuses the cached archive)")
    args = parser.parse_args()

    if not (args.tags or args.spec or args.all):
        parser.error("nothing selected: pass --tags, --spec or --all")

    manifest_path = SPECS / "manifest.yaml"
    if not manifest_path.exists():
        sys.exit(f"ensure_specs.py: {manifest_path} is missing")
    manifest = yaml.safe_load(manifest_path.read_text()) or {}
    default_release = args.release or (manifest.get("defaults") or {}).get("release", 18)

    entries = select(manifest, args)
    if not entries:
        log("nothing matched the selection")
        return 0

    if not args.dry_run and not shutil.which("pandoc"):
        sys.exit("ensure_specs.py: pandoc is required to convert specs (apt install pandoc)")

    results: list[tuple[str, str, str, str]] = []   # id, version, status, note
    failed = 0

    for entry in entries:
        spec_id = entry["id"]
        release = entry.get("release", default_release)
        pinned = entry.get("version")
        label = f"{spec_id} (Rel-{release}{', pinned ' + pinned if pinned else ''})"
        log(f"==> {label}")
        try:
            version, zip_name = resolve_version(spec_id, release, pinned)
        except Unreachable as exc:
            results.append((spec_id, "?", "failed", str(exc).split(". ")[0]))
            log(f"    unreachable: {exc}")
            failed += 1
            continue
        except RuntimeError as exc:
            results.append((spec_id, "?", "failed", str(exc)))
            log(f"    {exc}")
            failed += 1
            continue

        out = SPECS / spec_id / version
        if (out / "meta.yaml").exists() and not args.force:
            results.append((spec_id, version, "present", f"specs/{spec_id}/{version}/"))
            log(f"    present: V{version}")
            continue

        if args.dry_run:
            results.append((spec_id, version, "would add", zip_name))
            log(f"    would download {zip_name} -> V{version}")
            continue

        try:
            note = convert(entry, version, zip_name)
            results.append((spec_id, version, "added", note))
            log(f"    added V{version}: {note}")
        except Exception as exc:  # noqa: BLE001 — one bad spec must not stop the rest
            results.append((spec_id, version, "failed", f"{type(exc).__name__}: {exc}"))
            log(f"    FAILED: {exc}")
            failed += 1

    if not args.dry_run:
        total = write_index()
        log(f"specs/INDEX.md regenerated ({total} spec version(s))")

    width = max(len(r[0]) for r in results)
    print()
    print(f"{'SPEC'.ljust(width)}  {'VERSION':<9} {'STATUS':<10} NOTE")
    print(f"{'-' * width}  {'-' * 9} {'-' * 10} {'-' * 40}")
    for spec_id, version, status, note in results:
        print(f"{spec_id.ljust(width)}  {version:<9} {status:<10} {note[:90]}")
    print()

    if failed:
        print(f"{failed} spec(s) failed.", file=sys.stderr)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
