#!/usr/bin/env python3
"""Validate Mandla Brain's internal design knowledge links, skill metadata and memory JSONL.

Usage: python3 scripts/validate_design_knowledge.py
Standard library only. Never executes downloaded skills or visits external URLs.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIB = ROOT / "design-knowledge"
MAIN = LIB / "README.md"
SKILL_PATHS = [
    ROOT / "skills/design-director/SKILL.md",
    ROOT / ".agents/skills/design-director/SKILL.md",
    ROOT / ".claude/skills/design-director/SKILL.md",
]
REQUIRED_ROOT = ["AGENTS.md", "CLAUDE.md", "AI_INSTRUCTIONS.md", "START_HERE.md"]
LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
FRONTMATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)

errors: list[str] = []
warnings: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


def warn(message: str) -> None:
    warnings.append(message)


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        fail(f"Cannot read {path.relative_to(ROOT)}: {exc}")
        return ""


def check_links(file: Path, content: str) -> int:
    """Resolve local Markdown links; remote links are intentional references."""
    checked = 0
    for match in LINK.finditer(content):
        dest = match.group(1).strip().split(" ", 1)[0].strip("<>")
        if not dest or dest.startswith(("http:", "https:", "mailto:", "tel:", "data:", "#")):
            continue
        # Ignore URL-encoded fragments, query strings and anchors for path validity.
        p = dest.split("#", 1)[0].split("?", 1)[0]
        if not p or p.startswith(("javascript:", "plugin:", "sandbox:")):
            continue
        target = (file.parent / p).resolve()
        checked += 1
        if not target.is_relative_to(ROOT.resolve()):
            fail(f"{file.relative_to(ROOT)}: local link escapes repository: {dest}")
            continue
        if not target.exists():
            fail(f"{file.relative_to(ROOT)}: missing linked file {dest}")
    return checked


def check_skill(path: Path) -> None:
    if not path.is_file():
        fail(f"Missing skill: {path.relative_to(ROOT)}")
        return
    raw = read(path)
    found = FRONTMATTER.match(raw)
    if not found:
        fail(f"Missing YAML frontmatter: {path.relative_to(ROOT)}")
        return
    # No YAML dependency: our declared skill metadata uses simple scalars.
    lines = found.group(1).splitlines()
    fields = {}
    for line in lines:
        match = re.match(r"^([a-z][a-z0-9-]*):\s*(.+)$", line)
        if match:
            fields[match.group(1)] = match.group(2).strip().strip("'\"")
    name = fields.get("name", "")
    description = fields.get("description", "")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name or "INVALID"):
        fail(f"Invalid skill name: {path.relative_to(ROOT)}")
    if name != path.parent.name:
        fail(f"Skill name doesn't match directory: {path.relative_to(ROOT)}")
    if not description or len(description) > 1024:
        fail(f"Skill description missing or too long: {path.relative_to(ROOT)}")
    if len(raw) < 200:
        warn(f"Very short skill: {path.relative_to(ROOT)}")


def check_jsonl(path: Path) -> tuple[int, set[str]]:
    content = read(path)
    ids: set[str] = set()
    count = 0
    for n, line in enumerate(content.splitlines(), 1):
        if not line.strip():
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError as exc:
            fail(f"{path.relative_to(ROOT)}:{n}: {exc}")
            continue
        if not isinstance(obj, dict):
            fail(f"{path.relative_to(ROOT)}:{n}: expected JSON object")
            continue
        count += 1
        record_id = obj.get("id")
        if not isinstance(record_id, str) or not record_id:
            fail(f"{path.relative_to(ROOT)}:{n}: missing stable ID")
            continue
        if record_id in ids:
            fail(f"{path.relative_to(ROOT)}:{n}: duplicate ID {record_id}")
        ids.add(record_id)
    return count, ids


def main() -> int:
    for name in REQUIRED_ROOT:
        if not (ROOT / name).is_file():
            fail(f"Missing mandatory root document: {name}")
    chapters = sorted(LIB.glob("[0-9][0-9]_*.md"))
    if len(chapters) < 31:
        fail(f"Expected chapters 00–30, found {len(chapters)}")
    for number in range(31):
        matches = [x for x in chapters if x.name.startswith(f"{number:02d}_")]
        if len(matches) != 1:
            fail(f"Expected exactly one chapter {number:02d}, found {len(matches)}")
    indexed = read(MAIN)
    for file in chapters:
        if f"({file.name})" not in indexed:
            fail(f"Chapter omitted from index: {file.name}")
        if len(read(file)) < 900:
            warn(f"Suspiciously short chapter: {file.name}")

    md_files = [*LIB.glob("*.md"), *SKILL_PATHS, ROOT / "AGENTS.md", ROOT / "CLAUDE.md",
                ROOT / "AI_INSTRUCTIONS.md", ROOT / "START_HERE.md"]
    checked = 0
    for file in md_files:
        if file.is_file():
            checked += check_links(file, read(file))

    for path in SKILL_PATHS:
        check_skill(path)
    prefs_count, prefs_ids = check_jsonl(ROOT / "memory/preferences.jsonl")
    timeline_count, timeline_ids = check_jsonl(ROOT / "memory/timelines.jsonl")
    if "mandla-design-director-guideline-mandatory" not in prefs_ids:
        fail("Standing design rule missing from memory/preferences.jsonl")
    if "mandla-design-knowledge-base-inaugurated-2026-11-07" not in timeline_ids:
        fail("Design library timeline record missing")
    if not (ROOT / "AI_INSTRUCTIONS.md").read_text(encoding="utf-8").count("Mandatory design-director protocol"):
        fail("AI_INSTRUCTIONS.md has no mandatory design-director section")

    print(f"Checked {len(chapters)} chapter files, {checked} internal links, "
          f"{len(SKILL_PATHS)} skill manifests, {prefs_count} preferences, "
          f"{timeline_count} timeline records")
    for msg in warnings:
        print(f"WARN: {msg}", file=sys.stderr)
    for msg in errors:
        print(f"ERROR: {msg}", file=sys.stderr)
    if errors:
        print(f"VALIDATION FAILED: {len(errors)} errors")
        return 1
    print("PASS: Mandla Brain design knowledge structure and memory records")
    print("Note: no live URLs, design quality, or executable app behavior was tested.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
