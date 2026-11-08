#!/usr/bin/env python3
"""Rebuild deterministic AI retrieval indexes from canonical Mandla Brain JSONL."""
import argparse
import collections
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "brain" / "generated"
SCHEMA = "mandla-brain.ai-retrieval.v2"
FIELDS = ["file", "line", "id", "project", "key", "type", "status", "updated_at"]
ORDER = {"active": 0, "in_progress": 1, "implemented": 2, "planned": 3,
         "unresolved": 4, "completed": 5, "historical": 6, "superseded": 7, "rejected": 8}
REQUIRED = {"id", "type", "subject", "project", "key", "value", "status", "confidence",
            "source", "tags", "created_at", "updated_at"}

def dump(obj):
    return json.dumps(obj, ensure_ascii=False, indent=2, sort_keys=True) + "\n"

def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")

def preview(value, limit=145):
    raw = value if isinstance(value, str) else json.dumps(value, ensure_ascii=False, separators=(",", ":"))
    raw = " ".join(raw.replace("|", "/").split())
    return raw if len(raw) <= limit else raw[:limit-1].rstrip() + "…"

def collect():
    records, hashes, errors, seen = [], {}, [], set()
    files = sorted((ROOT/"memory").glob("*.jsonl")) + sorted((ROOT/"projects").glob("*.jsonl"))
    for file in files:
        rel = file.relative_to(ROOT).as_posix()
        raw = file.read_bytes()
        hashes[rel] = hashlib.sha256(raw).hexdigest()
        for line_num, line in enumerate(raw.decode("utf-8").splitlines(), start=1):
            if not line.strip():
                continue
            try:
                rec = json.loads(line)
            except Exception as exc:
                errors.append(f"{rel}:{line_num} invalid JSON: {exc}")
                continue
            missing = REQUIRED - rec.keys()
            if missing:
                errors.append(f"{rel}:{line_num} missing: {sorted(missing)}")
            ident = rec.get("id")
            if not isinstance(ident, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", ident):
                errors.append(f"{rel}:{line_num} invalid id: {ident}")
            if ident in seen:
                errors.append(f"{rel}:{line_num} duplicate id: {ident}")
            seen.add(ident)
            for field in ("created_at", "updated_at"):
                if not isinstance(rec.get(field), str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", rec[field]):
                    errors.append(f"{rel}:{line_num} invalid {field}")
            if not isinstance(rec.get("tags"), list):
                errors.append(f"{rel}:{line_num} tags not array")
            rec["_path"], rec["_line"] = rel, line_num
            records.append(rec)
    return records, hashes, errors

def card(project, records):
    ordered = sorted(records, key=lambda x: (ORDER.get(x.get("status"), 10), x["_path"], x["_line"]))
    dates = [x.get("updated_at", "") for x in ordered]
    counts = collections.Counter(x.get("status", "?") for x in ordered)
    lines = [f"# {project}", "",
        "> Auto-generated QUICKLOOK, not authoritative. The linked JSONL values and current user instructions outrank these abbreviated previews.",
        "> Project and repository status may have changed since the structured record dates. Check actual live artifacts.",
        "",
        f"Records: {len(ordered)} · Latest structured update: {max(dates) if dates else 'unknown'}",
        "Source statuses: " + ", ".join(f"{s}={n}" for s,n in sorted(counts.items())), ""]
    last = None
    for rec in ordered:
        status = rec.get("status", "?")
        section = "Active / pending" if ORDER.get(status, 10) <= 4 else "Completed / historical"
        if section != last:
            lines += ["## " + section, ""]
            last = section
        path, line = rec["_path"], rec["_line"]
        key = str(rec.get("key","?")).replace(chr(96), "'")
        value = "(preview omitted; open source)" if project=="Personal Development" else preview(rec.get("value"))
        lines.append(f"- **{key}** [{status}; {rec.get('updated_at')}] {value} · [{rec.get('id')}](../../../{path}#L{line})")
    lines += ["", "Read original record for full value, provenance and confidence. A plan, compile or conversational report is not a live-system test.", ""]
    return "\n".join(lines)

def build():
    records, hashes, errors = collect()
    if errors:
        return {}, errors
    files = sorted(hashes)
    file_number = {file:i for i,file in enumerate(files)}
    rows = [[file_number[r["_path"]],r["_line"],r.get("id"),r.get("project"),
             r.get("key"),r.get("type"),r.get("status"),r.get("updated_at")] for r in records]
    by_project = collections.defaultdict(list)
    extras = {"memory/unresolved.jsonl","memory/repositories.jsonl",
              "memory/timelines.jsonl","memory/preferences.jsonl"}
    for rec in records:
        name = rec.get("project")
        if isinstance(name,str) and name and (rec["_path"].startswith("projects/") or rec["_path"] in extras):
            by_project[name].append(rec)
    files_out, projects, slugs = {}, [], set()
    for name in sorted(by_project,key=str.casefold):
        ident = slug(name)
        if not ident or ident in slugs:
            errors.append("duplicate project slug: "+name)
            continue
        slugs.add(ident)
        group = by_project[name]
        path = f"brain/generated/cards/{ident}.md"
        subcards=[]
        if len(group) > 35:
            by_file=collections.defaultdict(list)
            for r in group:
                by_file[r["_path"]].append(r)
            summary=[f"# {name} · compact routing card", "",
              "> Generated index only. Open ONE subcard for the relevant subtopic, then the linked original records. Not evidence of current runtime state.", ""]
            for source,subset in sorted(by_file.items()):
                part=slug(source.replace(".jsonl","").replace("/","-"))
                subpath=f"brain/generated/cards/{ident}--{part}.md"
                files_out[subpath]=card(name+" / "+source,subset)
                subcards.append(subpath)
                keywords=", ".join(sorted({str(r.get("key","?")) for r in subset})[:8])
                summary.append(f"- [{source}]({Path(subpath).name}): {len(subset)} records. Keys: {keywords}.")
            summary += ["", "Use original records to verify full values, provenance, and confidence. July memory is not November production evidence.", ""]
            files_out[path]="\n".join(summary)
        else:
            files_out[path]=card(name,group)
        projects.append({"name":name,"slug":ident,"card":path,
          "subcards":subcards,
          "record_count":len(group),"source_files":sorted({r["_path"] for r in group}),
          "newest_record_date":max(r.get("updated_at","") for r in group),
          "statuses":dict(sorted(collections.Counter(r.get("status","?") for r in group).items()))})
    files_out["brain/generated/record-index.json"] = json.dumps({
        "schema":SCHEMA,"fields":FIELDS,"files":files,"records":rows,
        "note":"Metadata pointer index. Original JSONL source contains full value and provenance."},ensure_ascii=False,separators=(",",":")) + "\n"
    files_out["brain/generated/catalog.json"] = dump({
        "schema":SCHEMA,"source_total":len(hashes),"record_total":len(records),
        "project_total":len(projects),"projects":projects,
        "entry":"brain/BOOT.md","routes":"brain/ROUTES.json","records":"brain/generated/record-index.json",
        "note":"Project cards are noncanonical previews, not live status."})
    files_out["brain/generated/source-checksums.json"] = dump({
        "schema":SCHEMA,"algorithm":"sha256","sources":hashes,
        "note":"Canonical JSONL hashes for deterministic drift detection."})
    return files_out, errors

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check",action="store_true")
    args = parser.parse_args()
    content, errors = build()
    for e in errors:
        print("ERROR",e,file=sys.stderr)
    if errors: return 1
    existing = {p.relative_to(ROOT).as_posix() for p in OUT.rglob("*") if p.is_file()} if OUT.exists() else set()
    stale = sorted(existing-set(content))
    changed = []
    for path,text in content.items():
        file=ROOT/path
        if not file.is_file() or file.read_text(encoding="utf-8")!=text:
            changed.append(path)
            if not args.check:
                file.parent.mkdir(parents=True,exist_ok=True)
                file.write_text(text,encoding="utf-8")
    if args.check and (changed or stale):
        print("INDEX DRIFT",*(changed+stale),sep="\n- ")
        return 1
    if not args.check:
        for path in stale:
            (ROOT/path).unlink()
    print(f"OK: {len(content)} generated files; {len(content)-3} cards; {len(changed)} changed; {len(stale)} stale")
    return 0
if __name__=="__main__":
    sys.exit(main())
