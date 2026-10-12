#!/usr/bin/env python3
"""gfs -- reference implementation of the Git for Strategy pipeline contract.

SPEC.md at the repository root is the source of truth; this file implements it.
Standard library only, Python 3.9+, no network, no telemetry.

    gfs.py init [--root DIR] [--name NAME]
    gfs.py new TYPE TITLE [--root DIR] [--date YYYY-MM-DD]
    gfs.py validate [--root DIR] [--strict] [--json]
    gfs.py status [--root DIR] [--brief] [--json] [--today YYYY-MM-DD]
    gfs.py gate SPEC_FILE [--root DIR] [--today YYYY-MM-DD]
    gfs.py seeds suggest TEXT | seeds index [--write] | seeds check
    gfs.py selfcheck

Exit codes: 0 clean, 1 findings (or a failed gate), 2 usage error or no workspace.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
import tempfile
import urllib.parse
from pathlib import Path

SPEC_VERSION = "1.0"
PLUGIN_ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = PLUGIN_ROOT / "templates"
PLUGIN_SEEDS = PLUGIN_ROOT / "seeds"

FRESH_DAYS = 7
OVERDUE_DAYS = 14

# name -> folder, naming rule, required sections, status values (None = no Status field)
TYPES = {
    "scout": ("scouts", "dated",
              ["Tension", "Routes", "Open questions", "Verification"],
              ["Open", "Decided", "Parked"]),
    "decision": ("decisions", "numbered",
                 ["Context", "Decision", "Consequences"],
                 ["Proposed", "Accepted", "Superseded", "Rejected"]),
    "spec": ("specs", "living",
             ["Problem", "Current state", "Scope", "Success criteria", "Non-goals", "Risks"],
             ["Draft", "Ready", "In build", "Shipped", "Retired"]),
    "contract": ("contracts", "living",
                 ["Provider", "Consumer", "Integration points", "Open questions"],
                 ["Draft", "Agreed", "Retired"]),
    "commission": ("commissions", "dated",
                   ["Pre-flight", "Context", "Requirements", "Success criteria",
                    "Constraints and non-goals", "Done when"],
                   ["Draft", "Ready", "Out", "Done"]),
    "research": ("research", "dated", ["Question", "Claims", "Gaps"], ["Open", "Closed"]),
    "runbook": ("runbooks", "living", ["TL;DR", "Steps", "Verify", "Known debt"],
                ["Current", "Retired"]),
    "audit": ("audits", "dated", ["Scope", "Findings", "Fixes"], ["Open", "Closed"]),
    "draft": ("drafts", "living", ["Copy", "Fact-check log"],
              ["Draft", "Checked", "Published", "Withdrawn"]),
    "retro": ("retros", "dated",
              ["What went well", "What was hard", "What we would change", "Seeds", "Actions"],
              ["Draft", "Closed"]),
    "session": ("sessions", "dated",
                ["Decided", "Evidence", "Open questions", "Next move"], None),
    "seed": ("seeds", "living",
             ["What it is", "Why it matters", "The pattern", "Revisit when",
              "What it refuses", "Grew from"], None),
}
DECISION_EXPECTED = ["Options considered", "Ruling", "Revisit when", "Verification"]
FIXED = {
    "status": ("STATUS.md", ["Where we are", "Decision notes", "Next"]),
    "nexus": ("STRATEGY.md", ["Orientation", "Hot facts", "Router", "Rules that bite here", "Bookend"]),
}
PHASES = [("Explore", "scout"), ("Decide", "decision"), ("Specify", "spec"),
          ("Commission", "commission"), ("Learn", "retro")]
CORE_DIRS = ["scouts", "decisions", "specs", "commissions", "retros"]

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
SLUG = r"[a-z0-9]+(?:-[a-z0-9]+)*"
NAME_RES = {
    "dated": re.compile(rf"^(\d{{4}}-\d{{2}}-\d{{2}})_{SLUG}\.md$"),
    "living": re.compile(rf"^{SLUG}\.md$"),
    "numbered": re.compile(rf"^(\d{{3}})-{SLUG}\.md$"),
}
FIELD_RE = re.compile(r"^\*\*([A-Za-z][A-Za-z ]*):\*\*\s*(.*?)\s*$")
HEADING_RE = re.compile(r"^##\s+(.+?)\s*#*\s*$")
NUMBER_PREFIX_RE = re.compile(r"^\d+(?:\.\d+)*\.?\s+")
LINK_RE = re.compile(r"\[[^\]]*\]\((<[^>]+>|[^)\s]+)(?:\s+\"[^\"]*\")?\)")
INLINE_CODE_RE = re.compile(r"`[^`]*`")
CHECKBOX_RE = re.compile(r"^\s*[-*]\s+\[[ xX]\]\s+\S")
OPEN_CHECKBOX_RE = re.compile(r"^\s*[-*]\s+\[ \]\s+\S")
SCHEME_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")


# ---------------------------------------------------------------- parsing

class Doc:
    """One markdown artifact, parsed just enough to check it against the contract.

    Fenced code and HTML comments are skipped: links and checkboxes inside them do not count.
    """

    def __init__(self, path: Path):
        self.path = path
        self.error = ""
        try:
            self.text = path.read_bytes().decode("utf-8-sig")
        except UnicodeDecodeError:
            self.error = "not valid UTF-8"
            self.text = ""
        self.lines = self.text.splitlines()
        self.front: dict = {}
        self.title = ""
        self.fields: dict = {}
        self.sections: list = []
        self.section_body: dict = {}
        self.links: list = []
        self._parse()

    def _parse(self):
        lines = self.lines
        start = 0
        if lines and lines[0].strip() == "---":
            for i in range(1, len(lines)):
                if lines[i].strip() == "---":
                    self.front = parse_front_matter(lines[1:i])
                    start = i + 1
                    break
        in_fence = False
        in_comment = False
        in_header = True
        current = None
        for raw in lines[start:]:
            line, in_comment = strip_comments(raw, in_comment)
            stripped = line.strip()
            if stripped.startswith("```") or stripped.startswith("~~~"):
                in_fence = not in_fence
                continue
            if in_fence or not stripped and raw.strip():
                continue
            if not self.title and line.startswith("# "):
                self.title = line[2:].strip()
                continue
            heading = HEADING_RE.match(line)
            if heading:
                in_header = False
                name = NUMBER_PREFIX_RE.sub("", heading.group(1)).strip()
                current = name
                self.sections.append(name)
                self.section_body.setdefault(name, [])
                continue
            if in_header:
                field = FIELD_RE.match(stripped)
                if field:
                    self.fields[field.group(1).strip().lower()] = field.group(2)
            if current is not None:
                self.section_body[current].append(line)
            for target in LINK_RE.findall(INLINE_CODE_RE.sub("", line)):
                self.links.append(target)

    def has_section(self, name: str) -> bool:
        return self.find_section(name) is not None

    def find_section(self, name: str):
        want = name.lower()
        for section in self.sections:
            if section.lower().startswith(want):
                return section
        return None

    def field(self, name: str) -> str:
        return self.fields.get(name.lower(), "").strip()

    def section_text(self, name: str) -> str:
        section = self.find_section(name)
        return "\n".join(self.section_body.get(section, [])) if section else ""

    def resolve(self, target: str):
        """Resolve a relative link target to a Path, or None for URLs, anchors, and root-relative links."""
        if target.startswith("<") and target.endswith(">"):
            target = target[1:-1]
        if SCHEME_RE.match(target) or target.startswith(("#", "/")):
            return None
        clean = urllib.parse.unquote(target.split("#", 1)[0].split("?", 1)[0])
        if not clean:
            return None
        return (self.path.parent / clean).resolve()

    def local_links(self):
        """Yield (raw target, resolved Path) for every relative link."""
        for target in self.links:
            resolved = self.resolve(target)
            if resolved is not None:
                yield target, resolved

    def related_links(self):
        out = []
        for target in LINK_RE.findall(self.fields.get("related", "")):
            resolved = self.resolve(target)
            if resolved is not None:
                out.append(resolved)
        return out


def strip_comments(line: str, in_comment: bool):
    """Remove HTML comment text from one line; return (line, still inside a comment)."""
    out = ""
    rest = line
    while rest:
        if in_comment:
            end = rest.find("-->")
            if end < 0:
                return out, True
            rest = rest[end + 3:]
            in_comment = False
        else:
            begin = rest.find("<!--")
            if begin < 0:
                return out + rest, False
            out += rest[:begin]
            rest = rest[begin + 4:]
            in_comment = True
    return out, in_comment


def parse_front_matter(lines):
    """Parse the small YAML subset seeds use: `key: value`, and lists as `- item` or `[a, b]`."""
    data: dict = {}
    key = None
    for raw in lines:
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        item = re.match(r"^\s*-\s+(.*)$", raw)
        if item and key is not None:
            if not isinstance(data.get(key), list):
                data[key] = []
            data[key].append(unquote(item.group(1)))
            continue
        pair = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$", raw)
        if pair:
            key = pair.group(1)
            value = pair.group(2).strip()
            if value.startswith("[") and value.endswith("]"):
                data[key] = [unquote(v) for v in value[1:-1].split(",") if v.strip()]
            elif value:
                data[key] = unquote(value)
            else:
                data[key] = []
    return data


def unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def parse_date(value: str):
    value = value.strip()
    if not DATE_RE.match(value):
        return None
    try:
        return dt.date.fromisoformat(value)
    except ValueError:
        return None


def slugify(title: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    slug = slug[:60].rstrip("-")
    return slug or "untitled"


def status_value(doc: Doc, kind: str) -> str:
    value = doc.field("status")
    if not value and kind == "decision":
        return "Proposed"
    return value


def status_matches(value: str, allowed) -> str | None:
    """Exact match, except that `Superseded` may be followed by what superseded it."""
    low = value.strip().lower()
    for option in allowed:
        if low == option.lower():
            return option
        if option == "Superseded" and re.match(r"^superseded\b", low):
            return option
    return None


def has_ruling(doc: Doc) -> bool:
    """A ruled decision names its decider and records the ruling itself."""
    return bool(doc.field("decider")) and bool(doc.section_text("Ruling").strip())


def open_items(doc: Doc, section: str) -> list:
    return [l.strip() for l in doc.section_text(section).splitlines() if OPEN_CHECKBOX_RE.match(l)]


def doc_dates(doc: Doc, kind: str):
    """Return (date, updated) for a doc; dated file names stand in for a missing Date in decisions."""
    date = parse_date(doc.field("date")) if doc.field("date") else None
    if date is None and kind == "decision":
        named = NAME_RES["dated"].match(doc.path.name)
        if named:
            date = parse_date(named.group(1))
    updated = parse_date(doc.field("updated")) if doc.field("updated") else None
    return date, updated


def newest_date(doc: Doc, kind: str):
    date, updated = doc_dates(doc, kind)
    candidates = [d for d in (date, updated) if d]
    return max(candidates) if candidates else None


# ---------------------------------------------------------------- workspace

def find_root(start: Path, walk_up: bool = True):
    """The workspace holding `start`: ./STRATEGY.md or ./strategy/STRATEGY.md, here or in a parent."""
    start = start.resolve()
    for folder in [start, *start.parents] if walk_up else [start]:
        if (folder / "STRATEGY.md").is_file():
            return folder
        if (folder / "strategy" / "STRATEGY.md").is_file():
            return folder / "strategy"
    return None


def resolve_root(arg):
    if arg:
        root = Path(arg).resolve()
        if not (root / "STRATEGY.md").is_file():
            found = find_root(root, walk_up=False)
            if found is None:
                fail(f"no STRATEGY.md in {root} or {root / 'strategy'} -- run `gfs.py init` first")
            return found
        return root
    root = find_root(Path.cwd())
    if root is None:
        fail("no workspace here: expected ./STRATEGY.md or ./strategy/STRATEGY.md (run `gfs.py init`)")
    return root


def fail(message: str, code: int = 2):
    print(f"gfs: {message}", file=sys.stderr)
    sys.exit(code)


def artifact_files(root: Path, kind: str):
    folder = root / TYPES[kind][0]
    if not folder.is_dir():
        return []
    return sorted(p for p in folder.glob("*.md")
                  if p.name.lower() != "readme.md" and not p.name.startswith(("_", ".")))


def load_all(root: Path):
    docs = {}
    for kind in TYPES:
        docs[kind] = [Doc(p) for p in artifact_files(root, kind)]
    return docs


def render_template(kind: str, title: str, date: str, number: str = "", name: str = "") -> str:
    path = TEMPLATES / f"{kind}.md"
    if not path.is_file():
        fail(f"missing template {path}")
    text = path.read_text(encoding="utf-8")
    for key, value in (("title", title), ("date", date), ("number", number),
                       ("name", name), ("slug", slugify(title)), ("spec", SPEC_VERSION)):
        text = text.replace("{{" + key + "}}", value)
    return text


# ---------------------------------------------------------------- commands

def cmd_init(args) -> int:
    root = Path(args.root or ".").resolve()
    root.mkdir(parents=True, exist_ok=True)
    today = dt.date.today().isoformat()
    name = args.name or root.name
    created, kept = [], []
    for fixed, kind in (("STRATEGY.md", "nexus"), ("STATUS.md", "status")):
        target = root / fixed
        if target.exists():
            kept.append(fixed)
            continue
        target.write_text(render_template(kind, name, today, name=name), encoding="utf-8")
        created.append(fixed)
    for folder in CORE_DIRS:
        path = root / folder
        if not path.exists():
            path.mkdir()
            (path / ".gitkeep").write_text("", encoding="utf-8")
            created.append(folder + "/")
    print(f"Workspace: {root}")
    for item in created:
        print(f"  created  {item}")
    for item in kept:
        print(f"  kept     {item} (already there)")
    print()
    print("Next:")
    print("  Claude Code   add the line `@STRATEGY.md` to your CLAUDE.md so every session reads the nexus")
    print("  Other agents  point AGENTS.md (or your tool's rules file) at STRATEGY.md")
    print("  Dojo MCP      set DOJO_ADR_PATH to this workspace's decisions/ folder")
    print("  Then          /scout, or: gfs.py new scout \"<the tension>\"")
    return 0


def cmd_new(args) -> int:
    kind = args.type
    if kind not in TYPES:
        fail(f"unknown type {kind!r}; one of: {', '.join(TYPES)}")
    root = resolve_root(args.root)
    date = args.date or dt.date.today().isoformat()
    if not DATE_RE.match(date) or parse_date(date) is None:
        fail(f"bad date {date!r}; use YYYY-MM-DD")
    folder, naming, _, _ = TYPES[kind]
    slug = slugify(args.title)
    number = ""
    if naming == "dated":
        filename = f"{date}_{slug}.md"
    elif naming == "numbered":
        existing = [int(m.group(1)) for p in artifact_files(root, kind)
                    for m in [NAME_RES["numbered"].match(p.name)] if m]
        number = f"{(max(existing) + 1) if existing else 1:03d}"
        filename = f"{number}-{slug}.md"
    else:
        filename = f"{slug}.md"
    target = root / folder / filename
    if target.exists():
        fail(f"{target} already exists", 1)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(render_template(kind, args.title, date, number=number), encoding="utf-8")
    print(target)
    return 0


def validate_doc(doc: Doc, kind: str, root: Path):
    errors, warnings = [], []
    if doc.error:
        return [doc.error], []
    folder, naming, required, statuses = TYPES[kind]
    name_match = NAME_RES[naming].match(doc.path.name)
    if kind == "decision" and not name_match:
        name_match = NAME_RES["dated"].match(doc.path.name)
    if not name_match:
        hint = {"dated": "YYYY-MM-DD_slug.md", "living": "slug.md", "numbered": "NNN-slug.md"}[naming]
        errors.append(f"file name should look like {hint}")

    if kind == "seed":
        for key in ("name", "tagline", "triggers"):
            if not doc.front.get(key):
                errors.append(f"seed front matter needs `{key}`")
        if doc.front.get("name") and doc.front["name"] != doc.path.stem:
            errors.append(f"seed name `{doc.front['name']}` should match file name `{doc.path.stem}`")
        if doc.front.get("triggers") and not isinstance(doc.front["triggers"], list):
            errors.append("seed `triggers` should be a list")
    else:
        if not doc.title:
            errors.append("missing H1 title")
        date, updated = doc_dates(doc, kind)
        raw_date = doc.field("date")
        if raw_date and parse_date(raw_date) is None:
            errors.append(f"Date `{raw_date}` is not YYYY-MM-DD")
        elif date is None:
            errors.append("missing **Date:** header field")
        if doc.field("updated") and updated is None:
            errors.append(f"Updated `{doc.field('updated')}` is not YYYY-MM-DD")
        if naming == "dated" and name_match and date and name_match.group(1) != date.isoformat():
            warnings.append(f"file name date {name_match.group(1)} differs from Date {date.isoformat()}")
        if statuses is not None:
            value = doc.field("status")
            if not value:
                if kind == "decision":
                    warnings.append("no **Status:** field; read as Proposed")
                else:
                    errors.append("missing **Status:** header field")
            elif status_matches(value, statuses) is None:
                errors.append(f"Status `{value}` is not one of: {', '.join(statuses)}")

    for section in required:
        if not doc.has_section(section):
            errors.append(f"missing required section `## {section}`")
    if kind == "decision":
        for section in DECISION_EXPECTED:
            if not doc.has_section(section):
                warnings.append(f"missing expected section `## {section}`")
        ruled = status_matches(status_value(doc, kind), ["Accepted", "Rejected"])
        if ruled and not doc.field("decider"):
            errors.append(f"{ruled} decision needs a **Decider:** — the person who ruled")
        if ruled and not doc.section_text("Ruling").strip():
            errors.append(f"{ruled} decision needs the ruling, in the decider's words, under `## Ruling`")
    if kind == "commission":
        if not any(target.parent.name == "specs" for _, target in doc.local_links()):
            warnings.append("links no spec — a commission should link the spec it implements")

    for target, resolved in doc.local_links():
        if not resolved.exists():
            errors.append(f"broken link: {target}")
    return errors, warnings


def validate_workspace(root: Path):
    findings = []  # (level, path, message)
    docs = load_all(root)
    for kind, items in docs.items():
        for doc in items:
            errors, warnings = validate_doc(doc, kind, root)
            findings += [("error", doc.path, m) for m in errors]
            findings += [("warning", doc.path, m) for m in warnings]
    numbers: dict = {}
    for doc in docs["decision"]:
        m = NAME_RES["numbered"].match(doc.path.name)
        if m:
            numbers.setdefault(int(m.group(1)), []).append(doc.path.name)
    for number, names in sorted(numbers.items()):
        if len(names) > 1:
            findings.append(("error", root / "decisions",
                             f"decision number {number:03d} used twice: {', '.join(names)}"))
    for kind, (filename, sections) in FIXED.items():
        path = root / filename
        if not path.is_file():
            if kind == "nexus":
                findings.append(("error", path, "missing STRATEGY.md"))
            continue
        doc = Doc(path)
        if doc.error:
            findings.append(("error", path, doc.error))
            continue
        if not doc.title:
            findings.append(("error", path, "missing H1 title"))
        if parse_date(doc.field("date")) is None:
            findings.append(("error", path, "missing or malformed **Date:** header field"))
        for section in sections:
            if not doc.has_section(section):
                findings.append(("error", path, f"missing required section `## {section}`"))
        for target, resolved in doc.local_links():
            if not resolved.exists():
                findings.append(("error", path, f"broken link: {target}"))
    count = sum(len(v) for v in docs.values())
    return findings, count


def cmd_validate(args) -> int:
    root = resolve_root(args.root)
    findings, count = validate_workspace(root)
    errors = [f for f in findings if f[0] == "error"]
    warnings = [f for f in findings if f[0] == "warning"]
    if args.json:
        print(json.dumps({
            "root": str(root), "artifacts": count,
            "errors": [{"path": rel(p, root), "message": m} for _, p, m in errors],
            "warnings": [{"path": rel(p, root), "message": m} for _, p, m in warnings],
        }, indent=2))
    else:
        for level, path, message in findings:
            print(f"{level.upper():7} {rel(path, root)}: {message}")
        print(f"{count} artifacts checked: {len(errors)} errors, {len(warnings)} warnings")
    if errors or (args.strict and warnings):
        return 1
    return 0


def rel(path: Path, root: Path) -> str:
    try:
        return str(path.resolve().relative_to(root.resolve()))
    except ValueError:
        return str(path)


def freshness(age):
    if age is None:
        return "undated"
    if age <= FRESH_DAYS:
        return "active"
    if age <= OVERDUE_DAYS:
        return "quiet"
    return "dormant"


def pipeline_report(root: Path, today: dt.date):
    docs = load_all(root)
    inbound: dict = {}
    for kind, items in docs.items():
        for doc in items:
            for _, target in doc.local_links():
                inbound.setdefault(target, set()).add((kind, doc.path.resolve()))
    for filename in ("STATUS.md", "STRATEGY.md"):
        path = root / filename
        if path.is_file():
            for _, target in Doc(path).local_links():
                inbound.setdefault(target, set()).add(("fixed", path.resolve()))

    def linked_from(doc: Doc, kinds=None):
        sources = inbound.get(doc.path.resolve(), set())
        return [s for s in sources if s[1] != doc.path.resolve() and (kinds is None or s[0] in kinds)]

    phases = []
    for label, kind in PHASES:
        items = docs[kind]
        dates = [d for d in (newest_date(doc, kind) for doc in items) if d]
        newest = max(dates) if dates else None
        age = (today - newest).days if newest else None
        phases.append({"phase": label, "type": kind, "count": len(items),
                       "newest": newest.isoformat() if newest else None,
                       "age_days": age, "state": freshness(age) if items else "empty"})
    others = {kind: len(items) for kind, items in docs.items()
              if kind not in dict((k, 1) for _, k in PHASES) and items}

    attention = []
    for doc in docs["scout"]:
        date = newest_date(doc, "scout")
        if status_matches(doc.field("status"), ["Open"]) and date and (today - date).days > OVERDUE_DAYS:
            attention.append(f"scout still Open after {(today - date).days} days: {rel(doc.path, root)}")
    for doc in docs["spec"]:
        date = newest_date(doc, "spec")
        if (status_matches(doc.field("status"), ["Ready"]) and date
                and (today - date).days > OVERDUE_DAYS and not linked_from(doc, {"commission"})):
            attention.append(f"Ready spec with no commission after {(today - date).days} days: "
                             f"{rel(doc.path, root)}")
    for doc in docs["commission"]:
        if status_matches(doc.field("status"), ["Done"]) and not linked_from(doc, {"retro"}):
            attention.append(f"Done commission with no retro yet: {rel(doc.path, root)}")
    for doc in docs["decision"]:
        if status_matches(status_value(doc, "decision"), ["Accepted"]):
            pending = open_items(doc, "Consequences")
            if pending:
                attention.append(f"Accepted decision with {len(pending)} propagation item"
                                 f"{'s' if len(pending) != 1 else ''} still open: {rel(doc.path, root)}")
    return {"root": str(root), "today": today.isoformat(), "phases": phases,
            "other": others, "attention": attention}


def cmd_status(args) -> int:
    root = resolve_root(args.root)
    today = parse_date(args.today) if args.today else dt.date.today()
    if today is None:
        fail(f"bad --today {args.today!r}")
    report = pipeline_report(root, today)
    if args.json:
        print(json.dumps(report, indent=2))
        return 0
    if args.brief:
        parts = []
        for p in report["phases"]:
            parts.append(f"{p['phase']} {p['state']}" + (f" ({p['count']})" if p["count"] else ""))
        print(f"Strategy workspace {rel(root, Path.cwd()) or '.'}: " + " · ".join(parts) + ".")
        if report["attention"]:
            print("Needs attention: " + "; ".join(report["attention"][:3])
                  + (f"; and {len(report['attention']) - 3} more" if len(report["attention"]) > 3 else "")
                  + ".")
        return 0
    print(f"Pipeline health — {root} — {report['today']}")
    print()
    print(f"  {'Phase':<11} {'Files':>5}  {'Newest':<10}  State")
    for p in report["phases"]:
        newest = p["newest"] or "—"
        print(f"  {p['phase']:<11} {p['count']:>5}  {newest:<10}  {p['state']}")
    if report["other"]:
        print()
        print("  Also: " + ", ".join(f"{k} {v}" for k, v in sorted(report["other"].items())))
    print()
    if report["attention"]:
        print("Needs attention:")
        for item in report["attention"]:
            print(f"  - {item}")
    else:
        print("Nothing needs attention.")
    print()
    print(f"Phase states: active = newest artifact {FRESH_DAYS} days old or less; quiet = older; "
          f"dormant = older than {OVERDUE_DAYS} days. Ages come from header dates.")
    return 0


def cmd_gate(args) -> int:
    root = resolve_root(args.root)
    today = parse_date(args.today) if args.today else dt.date.today()
    if today is None:
        fail(f"bad --today {args.today!r}; use YYYY-MM-DD")
    path = Path(args.spec)
    if not path.is_absolute():
        candidate = (Path.cwd() / path)
        path = candidate if candidate.exists() else root / path
    if not path.is_file():
        fail(f"no such spec: {args.spec}")
    doc = Doc(path)
    checks = []
    status = doc.field("status")
    checks.append(("marked Ready", status_matches(status, ["Ready"]) is not None,
                   f"Status is `{status or 'missing'}`"))
    missing = [s for s in TYPES["spec"][2] if not doc.has_section(s)]
    checks.append(("has every required section", not missing,
                   "missing: " + ", ".join(missing) if missing else ""))
    criteria = doc.find_section("Success criteria")
    boxes = [l for l in doc.section_body.get(criteria, [])] if criteria else []
    checks.append(("states a success criterion as a checkbox",
                   any(CHECKBOX_RE.match(l) for l in boxes), "no `- [ ]` item under Success criteria"))
    accepted = []
    for target in doc.related_links():
        if target.parent.name == "decisions" and target.is_file():
            decision = Doc(target)
            if status_matches(status_value(decision, "decision"), ["Accepted"]) and has_ruling(decision):
                accepted.append(target)
    checks.append(("links an Accepted decision, with its ruling, under Related", bool(accepted),
                   "no Accepted decision with a Decider and a Ruling linked in **Related:**"))
    ok = all(passed for _, passed, _ in checks)
    print(f"Pre-commission gate — {rel(path, root)}")
    for label, passed, detail in checks:
        print(f"  {'PASS' if passed else 'FAIL'}  {label}" + ("" if passed or not detail else f" — {detail}"))
    newest = newest_date(doc, "spec")
    if newest and (today - newest).days > OVERDUE_DAYS:
        print(f"  WARN  spec is {(today - newest).days} days old — re-check the current state before commissioning")
    print("Gate: " + ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


# ---------------------------------------------------------------- seeds

def seed_dirs(root_arg):
    dirs = []
    root = None
    if root_arg:
        root = resolve_root(root_arg)
    else:
        root = find_root(Path.cwd())
    if root and (root / "seeds").is_dir():
        dirs.append(root / "seeds")
    if PLUGIN_SEEDS.is_dir() and PLUGIN_SEEDS.resolve() not in [d.resolve() for d in dirs]:
        dirs.append(PLUGIN_SEEDS)
    return dirs


def load_seeds(directory: Path):
    out = []
    for path in sorted(directory.glob("*.md")):
        if path.name.lower() == "readme.md" or path.name.startswith(("_", ".")):
            continue
        out.append(Doc(path))
    return out


STOPWORDS = set("""about also been being could does doing from have here into just keep like make
more need only should some than that their them then there they this want were what when where
which will with would your""".split())


def score_seed(doc: Doc, text: str) -> int:
    """Three points for a whole trigger phrase found in the text, one for each meaningful word."""
    low = " " + re.sub(r"[^a-z0-9]+", " ", text.lower()) + " "
    score = 0
    for trigger in doc.front.get("triggers") or []:
        phrase = " " + re.sub(r"[^a-z0-9]+", " ", trigger.lower()).strip() + " "
        if phrase.strip() and phrase in low:
            score += 3
        else:
            score += sum(1 for w in phrase.split()
                         if len(w) > 3 and w not in STOPWORDS and f" {w} " in low)
    return score


def cmd_seeds(args) -> int:
    if args.action == "suggest":
        text = " ".join(args.text or [])
        if not text.strip():
            fail("seeds suggest needs a description of what you are working on")
        ranked = []
        for directory in seed_dirs(args.root):
            for doc in load_seeds(directory):
                score = score_seed(doc, text)
                if score:
                    ranked.append((score, doc))
        ranked.sort(key=lambda pair: (-pair[0], pair[1].path.stem))
        if not ranked:
            print("No seed matched. Browse seeds/README.md, or describe the situation in other words.")
            return 0
        for score, doc in ranked[:3]:
            print(f"{doc.front.get('name')}: {doc.front.get('tagline')}")
            print(f"  {doc.path}")
        return 0

    if args.plugin:
        directory = PLUGIN_SEEDS
    elif args.root:
        directory = resolve_root(args.root) / "seeds"
        if not directory.is_dir():
            fail(f"no seeds/ folder in {directory.parent}", 1)
    else:
        root = find_root(Path.cwd())
        directory = root / "seeds" if root and (root / "seeds").is_dir() else PLUGIN_SEEDS
    index_path = directory / "README.md"
    generated = seed_index(directory)
    if args.action == "index":
        if args.write:
            if not write_index(index_path, generated):
                print(f"{index_path}: no index markers (<!-- seeds:start --> ... <!-- seeds:end -->); nothing written")
                return 1
            print(f"wrote {index_path}")
        else:
            print(generated)
        return 0
    if args.action == "check":
        current = read_index(index_path)
        if current is None:
            print(f"{index_path}: no index markers (<!-- seeds:start --> ... <!-- seeds:end -->)")
            return 1
        if current.strip() != generated.strip():
            print(f"{index_path}: index is out of date — run `gfs.py seeds index --write`")
            return 1
        print(f"{index_path}: index matches {len(load_seeds(directory))} seeds on disk")
        return 0
    fail("seeds needs one of: suggest, index, check")
    return 2


GROUP_ORDER = ["foundations", "structure", "grounding", "deciding", "honesty", "execution"]


def seed_index(directory: Path) -> str:
    groups: dict = {}
    for doc in load_seeds(directory):
        group = (doc.front.get("group") or "other").strip().lower()
        groups.setdefault(group, []).append(doc)
    order = [g for g in GROUP_ORDER if g in groups] + sorted(g for g in groups if g not in GROUP_ORDER)
    out = []
    for group in order:
        out.append(f"### {group.capitalize()}")
        out.append("")
        out.append("| Seed | Tagline |")
        out.append("|---|---|")
        for doc in sorted(groups[group], key=lambda d: d.path.stem):
            title = doc.title or doc.path.stem
            out.append(f"| [{title}]({doc.path.name}) | {doc.front.get('tagline', '')} |")
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def read_index(path: Path):
    if not path.is_file():
        return None
    text = path.read_text(encoding="utf-8")
    m = re.search(r"<!-- seeds:start -->\n(.*?)<!-- seeds:end -->", text, re.S)
    return m.group(1) if m else None


def write_index(path: Path, generated: str) -> bool:
    """Rewrite the generated block of a seeds README; create the README if there is none."""
    text = path.read_text(encoding="utf-8") if path.is_file() else "# Seeds\n\n<!-- seeds:start -->\n<!-- seeds:end -->\n"
    if not re.search(r"<!-- seeds:start -->\n.*?<!-- seeds:end -->", text, re.S):
        return False
    new = re.sub(r"<!-- seeds:start -->\n.*?<!-- seeds:end -->",
                 lambda _: "<!-- seeds:start -->\n" + generated + "<!-- seeds:end -->", text, flags=re.S)
    path.write_text(new, encoding="utf-8")
    return True


# ---------------------------------------------------------------- selfcheck

def cmd_selfcheck(args) -> int:
    problems = []
    for kind in list(TYPES) + list(FIXED):
        if not (TEMPLATES / f"{kind}.md").is_file():
            problems.append(f"templates/{kind}.md is missing")
    with tempfile.TemporaryDirectory() as tmp:
        ws = Path(tmp) / "ws"
        quiet(lambda: cmd_init(argparse.Namespace(root=str(ws), name="selfcheck")))
        for kind in TYPES:
            if (TEMPLATES / f"{kind}.md").is_file():
                quiet(lambda k=kind: cmd_new(argparse.Namespace(type=k, title=f"Selfcheck {k}",
                                                                root=str(ws), date="2026-01-02")))
        findings, _ = validate_workspace(ws)
        for level, path, message in findings:
            if level == "error":
                problems.append(f"template output fails validation: {rel(path, ws)}: {message}")
    for doc in load_seeds(PLUGIN_SEEDS):
        errors, _ = validate_doc(doc, "seed", PLUGIN_ROOT)
        problems += [f"seeds/{doc.path.name}: {e}" for e in errors]
    current = read_index(PLUGIN_SEEDS / "README.md")
    if current is None or current.strip() != seed_index(PLUGIN_SEEDS).strip():
        problems.append("seeds/README.md index is out of date — run `gfs.py seeds index --write`")
    for command in sorted((PLUGIN_ROOT / "commands").glob("*.md")):
        doc = Doc(command)
        if not doc.front.get("description"):
            problems.append(f"commands/{command.name}: front matter needs `description`")
        for ref in re.findall(r"\$\{CLAUDE_PLUGIN_ROOT\}/([^\"'`\s)]+)", doc.text):
            if not (PLUGIN_ROOT / ref).exists():
                problems.append(f"commands/{command.name}: references missing {ref}")
    manifest = PLUGIN_ROOT / ".claude-plugin" / "plugin.json"
    try:
        version = json.loads(manifest.read_text(encoding="utf-8"))["version"]
        changelog = (PLUGIN_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
        top = re.search(r"^## \[([^\]]+)\]", changelog, re.M)
        if not top or top.group(1) != version:
            problems.append(f"plugin.json version {version} does not match the newest CHANGELOG entry")
    except (OSError, KeyError, ValueError) as exc:
        problems.append(f"cannot read plugin.json or CHANGELOG.md: {exc}")
    problems += check_rule_counts()
    problems += check_spec_table()
    examples = PLUGIN_ROOT / "examples"
    if examples.is_dir():
        for nexus in sorted(examples.glob("*/STRATEGY.md")):
            findings, _ = validate_workspace(nexus.parent)
            for level, path, message in findings:
                problems.append(f"examples/{rel(path, examples)}: {level}: {message}")
    for problem in problems:
        print(f"FAIL  {problem}")
    print("selfcheck: " + ("clean" if not problems else f"{len(problems)} problems"))
    return 0 if not problems else 1


NUMBER_WORDS = {w: i for i, w in enumerate(
    "zero one two three four five six seven eight nine ten eleven twelve".split())}


def numbered_items(text: str, heading: str) -> int:
    """Count `1.`-style items directly under a `## heading`, up to the next `## `."""
    m = re.search(rf"^## {re.escape(heading)}\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
    return len(re.findall(r"^\d+\.\s", m.group(1), re.M)) if m else 0


def check_rule_counts():
    """The docs say how many invariants there are; re-derive the number from SPEC.md."""
    problems = []
    spec_text = (PLUGIN_ROOT / "SPEC.md").read_text(encoding="utf-8")
    count = numbered_items(spec_text, "Invariants")
    readme = PLUGIN_ROOT / "README.md"
    if readme.is_file():
        listed = numbered_items(readme.read_text(encoding="utf-8"), "The rules")
        if listed != count:
            problems.append(f"README.md lists {listed} rules; SPEC.md has {count} invariants")
    docs = [PLUGIN_ROOT / "README.md", PLUGIN_ROOT / "SPEC.md", PLUGIN_ROOT / "llms.txt"]
    docs += sorted((PLUGIN_ROOT / "docs").glob("*.md"))
    for path in docs:
        if not path.is_file():
            continue
        for word in re.findall(r"\b(\w+) (?:rules|invariants)\b", path.read_text(encoding="utf-8"), re.I):
            n = NUMBER_WORDS.get(word.lower())
            if n is not None and n != count:
                problems.append(f"{path.name} says '{word} rules/invariants'; SPEC.md has {count}")
    return problems


def check_spec_table():
    """SPEC.md is the source of truth: its types table must match what this script enforces."""
    problems = []
    text = (PLUGIN_ROOT / "SPEC.md").read_text(encoding="utf-8")
    m = re.search(r"^### Types\s*$(.*?)(?=^##)", text, re.M | re.S)
    if not m:
        return ["SPEC.md has no `### Types` table"]
    rows = {}
    for line in m.group(1).splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 5 and cells[0] and cells[0] not in ("Type",) and not set(cells[0]) <= set("-"):
            rows[cells[0]] = cells
    for kind, (folder, naming, sections, statuses) in TYPES.items():
        row = rows.pop(kind, None)
        if row is None:
            problems.append(f"SPEC.md types table has no row for `{kind}`")
            continue
        spec_sections = [x.strip() for x in row[3].split("·")]
        spec_statuses = None if row[4] in ("—", "-") else [x.strip() for x in row[4].split(",")]
        if row[1].strip("`").rstrip("/") != folder or row[2] != naming:
            problems.append(f"SPEC.md `{kind}`: folder/name `{row[1]}`/{row[2]} vs gfs.py {folder}/{naming}")
        if spec_sections != sections:
            problems.append(f"SPEC.md `{kind}`: sections differ from gfs.py")
        if spec_statuses != statuses:
            problems.append(f"SPEC.md `{kind}`: status values differ from gfs.py")
    for kind, (filename, sections) in FIXED.items():
        row = rows.pop(kind, None)
        if row is None:
            problems.append(f"SPEC.md types table has no row for `{kind}`")
        elif row[1].strip("`") != filename or [x.strip() for x in row[3].split("·")] != sections:
            problems.append(f"SPEC.md `{kind}`: file or sections differ from gfs.py")
    for extra in rows:
        problems.append(f"SPEC.md types table has `{extra}`, which gfs.py does not know")
    return problems


def quiet(fn):
    import contextlib
    import io
    with contextlib.redirect_stdout(io.StringIO()):
        return fn()


# ---------------------------------------------------------------- main

def build_parser():
    parser = argparse.ArgumentParser(prog="gfs.py", description="Git for Strategy pipeline contract tools.")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("init", help="create a workspace (STRATEGY.md, STATUS.md, core folders)")
    p.add_argument("--root", help="workspace directory (default: current directory)")
    p.add_argument("--name", help="workspace name (default: directory name)")
    p.set_defaults(func=cmd_init)

    p = sub.add_parser("new", help="create an artifact from its template; prints the new path")
    p.add_argument("type", help="one of: " + ", ".join(TYPES))
    p.add_argument("title")
    p.add_argument("--root")
    p.add_argument("--date", help="YYYY-MM-DD (default: today)")
    p.set_defaults(func=cmd_new)

    p = sub.add_parser("validate", help="check artifacts against the contract")
    p.add_argument("--root")
    p.add_argument("--strict", action="store_true", help="treat warnings as failures")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_validate)

    p = sub.add_parser("status", help="pipeline health")
    p.add_argument("--root")
    p.add_argument("--brief", action="store_true", help="two lines, for session start")
    p.add_argument("--json", action="store_true")
    p.add_argument("--today", help="YYYY-MM-DD (default: today)")
    p.set_defaults(func=cmd_status)

    p = sub.add_parser("gate", help="pre-commission gate for one spec")
    p.add_argument("spec")
    p.add_argument("--root")
    p.add_argument("--today", help="YYYY-MM-DD (default: today)")
    p.set_defaults(func=cmd_gate)

    p = sub.add_parser("seeds", help="suggest seeds, or keep the seed index honest")
    p.add_argument("action", choices=["suggest", "index", "check"])
    p.add_argument("text", nargs="*")
    p.add_argument("--root")
    p.add_argument("--write", action="store_true", help="with `index`: rewrite seeds/README.md")
    p.add_argument("--plugin", action="store_true",
                   help="with `index` or `check`: use the seeds that ship with this plugin")
    p.set_defaults(func=cmd_seeds)

    p = sub.add_parser("selfcheck", help="check this repository: templates, seeds, commands, version")
    p.set_defaults(func=cmd_selfcheck)
    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
