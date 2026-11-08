# Query and maintenance · AI Brain v2

## Read workflow (no runtime needed)
1. Open [BOOT.md](BOOT.md) (short operating rules).
2. Look up your topic in [ROUTES.json](ROUTES.json). If the task names a canonical project, use [generated/catalog.json](generated/catalog.json) to locate its card.
3. Open the card and only the relevant original JSONL records, not every root handover document.
4. Check [STATUS.md](STATUS.md) when current project state matters, and inspect real work files before acting.

## If a local Python runtime is available
The CLI only reads this repository; it requires Python 3.9+ and no dependencies.

```bash
python3 scripts/query_brain.py --pretty "Kingship worship auditions"
python3 scripts/query_brain.py --pretty "FaceWeave original Deep-Live-Cam"
python3 scripts/query_brain.py --pretty "Phala Digital website redesign"
python3 scripts/query_brain.py --pretty "KHOMELELA"
```

It prints task-specific sources, project cards and exact record pointers; it never claims that an integration is connected.

## After any canonical memory change
```bash
python3 scripts/build_ai_index.py
python3 scripts/build_ai_index.py --check
python3 scripts/validate_ai_brain.py
python3 scripts/validate_design_knowledge.py
```

The deterministic generator recalculates [record-index.json](generated/record-index.json), [catalog.json](generated/catalog.json), [source-checksums.json](generated/source-checksums.json), and the [project cards](generated/cards/).

Do not hand-edit generated views. The structured original records remain authoritative; never write an update to a generated card instead of its source. Never commit secrets or raw private data. The GitHub Actions integrity job runs these checks on matching changes.
