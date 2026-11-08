#!/usr/bin/env python3
"""Low-cost Mandla Brain topic and record finder. Runs offline, no API keys."""
import argparse
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
def tokens(s):
    return {t for t in re.findall(r"[a-z0-9]+",s.lower()) if len(t)>2}
def norm(s):
    return " ".join(re.findall(r"[a-z0-9]+",s.lower()))
def score_alias(query,alias):
    a,q=norm(alias),norm(query)
    if not a:return 0
    if q==a:return 100+len(a)
    if re.search(r"(?<!\w)"+re.escape(a)+r"(?!\w)",q):return 40+len(a)
    common=len(tokens(a)&tokens(q))
    return common*3 if common and common==len(tokens(a)) else 0
def search(query,limit=6):
    routes=json.loads((ROOT/"brain/ROUTES.json").read_text())
    index=json.loads((ROOT/"brain/generated/record-index.json").read_text())
    catalog=json.loads((ROOT/"brain/generated/catalog.json").read_text())
    topics=[]
    for topic in routes["topics"]:
        score=max((score_alias(query,a) for a in topic["aliases"]),default=0)
        if score:topics.append((score,topic))
    topics.sort(key=lambda x:(-x[0],x[1]["id"]))
    selected=[t for _,t in topics[:3]]
    projects=[]
    aliases=routes.get("alias_to_project",{})
    hits=[(score_alias(query,a),n) for a,n in aliases.items() if score_alias(query,a)]
    hits.sort(reverse=True)
    for _,name in hits:
        if name not in projects:projects.append(name)
    for topic in selected:
        for name in routes.get("topic_to_project",{}).get(topic["id"],[]):
            if name not in projects:projects.append(name)
    matched_records=[]
    for row in index["records"]:
        f,n,ident,project,key,kind,status,date=row
        fields=[ident or "",project or "",key or ""]
        sc=max(score_alias(query,v) for v in fields)
        # Loose shared words (such as "original" or "digital") are too noisy.
        # Only return exact phrase/alias matches in metadata.
        if sc >= 40:
            matched_records.append((sc,row))
    matched_records.sort(key=lambda x:(-x[0],x[1][0],x[1][1]))
    records=[{
        "id":row[2],"project":row[3],"key":row[4],"status":row[6],
        "source":index["files"][row[0]],"line":row[1]
    } for _,row in matched_records[:limit]]
    selected_projects=[]
    for name in projects:
        entry=next((p for p in catalog["projects"] if p["name"]==name),None)
        if entry:selected_projects.append({"name":name,"card":entry["card"]})
    source_paths=[entry["card"] for entry in selected_projects]
    for entry in selected:
        for source in entry["sources"]:
            if source not in source_paths:source_paths.append(source)
    return {
      "query":query,"boot":"brain/BOOT.md",
      "topics":[t["id"] for t in selected],
      "project_cards":selected_projects,
      "read_next":source_paths[:12],
      "record_hits":records,
      "note":"Source paths are retrieval suggestions, not verified runtime facts. Read full canonical records and current artifact before acting."
    }
if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("query",nargs="+",help="task description or project name")
    parser.add_argument("--limit",type=int,default=6)
    parser.add_argument("--pretty",action="store_true")
    args=parser.parse_args()
    obj=search(" ".join(args.query),limit=max(1,min(args.limit,20)))
    print(json.dumps(obj,ensure_ascii=False,indent=2 if args.pretty else None))
