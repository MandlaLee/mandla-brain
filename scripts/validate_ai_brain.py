#!/usr/bin/env python3
"""Verify portable AI retrieval layer, internal links and canonical source integrity."""
from __future__ import annotations
import importlib.util
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
ERRORS=[]
def expect(ok,message):
    if not ok: ERRORS.append(message)

def load(path):
    return json.loads((ROOT/path).read_text(encoding="utf-8"))

def check_refs():
    routes=load("brain/ROUTES.json")
    expect(routes.get("version")==2,"router version not 2")
    aliases=set()
    for t in routes["topics"]:
        expect(t.get("id") and t.get("sources") and t.get("aliases"),
               "route incomplete: "+str(t.get("id")))
        for a in t.get("aliases",[]):
            expect(isinstance(a,str) and a.strip(),"blank alias")
        for path in t.get("sources",[]):
            expect((ROOT/path).is_file(),"route source missing: "+path)
        expect(t.get("id") not in aliases,"duplicate route id: "+str(t.get("id")))
        aliases.add(t.get("id"))
    for name in routes.get("topic_to_project",{}):
        expect(name in aliases,"topic_to_project references unknown topic: "+name)
    manifest=load("brain/generated/catalog.json")
    expect(manifest.get("schema")=="mandla-brain.ai-retrieval.v2","catalog schema mismatch")
    names={p["name"] for p in manifest["projects"]}
    for group in routes.get("topic_to_project",{}).values():
        for name in group:
            expect(name in names,"missing catalog project: "+name)
    for name in routes.get("alias_to_project",{}).values():
        expect(name in names,"unknown project alias: "+name)
    index=load("brain/generated/record-index.json")
    expect(len(index["fields"])==8,"index schema width")
    expect(len(index["records"])==manifest["record_total"],"index and catalog record counts differ")
    expect(len(index["files"])==manifest["source_total"],"source count differs")
    ids=set()
    for row in index["records"]:
        expect(len(row)==8,"invalid row width")
        f,line,ident,project,key,kind,status,date=row
        expect(isinstance(f,int) and 0<=f<len(index["files"]),"invalid file ID")
        expect(isinstance(line,int) and line>0,"invalid source line")
        expect(ident not in ids,"duplicate record ID in index")
        ids.add(ident)
        file=ROOT/index["files"][f]
        if file.is_file() and 0<line<=len(file.read_text().splitlines()):
            original=json.loads(file.read_text().splitlines()[line-1])
            expect(original.get("id")==ident, "wrong pointer: "+str(ident))
        else:expect(False,"missing/out-of-range source line: "+str(ident))
    for item in manifest["projects"]:
        expect((ROOT/item["card"]).is_file(),"project card missing: "+item["card"])
        for sub in item.get("subcards",[]):
            expect((ROOT/sub).is_file(),"subcard missing: "+sub)
    for path in ("brain/BOOT.md","brain/RULES.md","brain/STATUS.md","brain/ROUTES.json",
                 "brain/DESIGN_ROUTES.md","START_HERE.md","HANDOVER_PROMPT.md",
                 "scripts/build_ai_index.py","scripts/query_brain.py"):
        expect((ROOT/path).is_file(),"required entry missing: "+path)
    for path,maximum in {"brain/BOOT.md":4300,"brain/RULES.md":4800,
                         "START_HERE.md":3000,"HANDOVER_PROMPT.md":2800}.items():
        expect((ROOT/path).stat().st_size<=maximum,path+" exceeds fast-start budget")
    return manifest

def exact_case(path):
    # macOS HFS/APFS may be case-insensitive; GitHub Actions Linux is not.
    # Test lexical components, not realpath(), to catch wrong-case links locally.
    try:
        rel=Path(os.path.normpath(str(path))).relative_to(ROOT)
        current=ROOT
        for part in rel.parts:
            if part not in {p.name for p in current.iterdir()}:
                return False
            current=current/part
        return True
    except (ValueError, FileNotFoundError, NotADirectoryError):
        return False

def check_markdown_links():
    files=[ROOT/"README.md",ROOT/"START_HERE.md",ROOT/"HANDOVER_PROMPT.md",
           ROOT/"AGENTS.md",ROOT/"CLAUDE.md",ROOT/"AI_INSTRUCTIONS.md",
           *list((ROOT/"brain").rglob("*.md"))]
    link_re=re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
    for file in files:
        if not file.is_file():continue
        for match in link_re.finditer(file.read_text(encoding="utf-8")):
            target=match.group(1).split("#",1)[0].strip()
            if not target or target.startswith(("https://","http://","mailto:","#")):
                continue
            if target.startswith("<") and target.endswith(">"):target=target[1:-1]
            if " " in target:continue
            path=Path(os.path.normpath(str(file.parent/target)))
            expect(path.is_relative_to(ROOT.resolve()),f"link escapes repo: {file}: {target}")
            if path.is_relative_to(ROOT.resolve()):
                expect(path.exists() and exact_case(path),
                       f"broken/wrong-case link: {file.relative_to(ROOT)} -> {target}")

def check_queries():
    sys.path.insert(0,str(ROOT/"scripts"))
    import query_brain
    cases=[
      ("Deep-Live-Cam faceweave original models","faceweave"),
      ("KHOMELELA Mandla Lee music","music-media"),
      ("Hodela Restaurant game","games"),
      ("Kingship worship auditions","kingship"),
      ("Phala Digital website redesign","phala-digital"),
      ("How can GPTs plugins make my AI more efficient","ai-capabilities"),
      ("Notion sync Mandla Brain","brain-maintenance"),
      ("NFP XAUUSD unemployment report","trading"),
      ("TIRHANI macOS app","mac-apps"),
    ]
    for q,topic in cases:
        r=query_brain.search(q)
        expect(topic in r["topics"],"incorrect route: "+q+" => "+str(r["topics"]))
        expect(len(r["record_hits"])<=6,"result limit exceeded: "+q)
        for path in r["read_next"]:
            expect((ROOT/path).is_file(),"query route missing file: "+path)
    k=query_brain.search("Kingship worship auditions")
    expect(any(x["name"]=="Kingship Christian Centre" for x in k["project_cards"]),
           "Kingship route not selecting project")
    p=query_brain.search("Phala Digital website redesign")
    expect("design" in p["topics"],"redesign not triggering design charter")

def main():
    check_refs()
    check_markdown_links()
    check_queries()
    script=[sys.executable,str(ROOT/"scripts"/"build_ai_index.py"),"--check"]
    done=subprocess.run(script,cwd=ROOT,capture_output=True,text=True)
    expect(done.returncode==0,"generated indexes stale: "+(done.stdout+done.stderr)[-700:])
    if ERRORS:
        print("FAILED:",len(ERRORS),"issues")
        for err in ERRORS:print(" -",err)
        return 1
    print("PASS: AI routing, JSONL pointers, generated data, source links and 9 real-world task routes")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
