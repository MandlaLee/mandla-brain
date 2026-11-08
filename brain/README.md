# Brain v2: retrieval layer
This directory is a **fast access layer**, not a replacement for Mandla's canonical information. Read [BOOT.md](BOOT.md) first.

- [ROUTES.json](ROUTES.json): curated intent/alias routing.
- [RULES.md](RULES.md): concise cross-model rules; source of truth remains root instructions and current user direction.
- [STATUS.md](STATUS.md): date and verification caveats.
- [DESIGN_ROUTES.md](DESIGN_ROUTES.md): minimum relevant design chapters.
- [generated/catalog.json](generated/catalog.json): machine-generated topic, project and source lookup.
- [generated/record-index.json](generated/record-index.json): pointer index for all JSONL records.
- [generated/cards/](generated/cards/): preview cards, generated from structured records; not canonical.
- [../scripts/build_ai_index.py](../scripts/build_ai_index.py): reproducible index builder and check mode.
- [../scripts/validate_ai_brain.py](../scripts/validate_ai_brain.py): integrity and compatibility validation.

**Rule:** No generated preview may silently supersede the original memory JSONL, current user instructions or the real working repository. Do not manually edit generated files. Rebuild them after changing structured memory.
