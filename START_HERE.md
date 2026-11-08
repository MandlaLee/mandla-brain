# Start Here · Fast AI handover (v2)

**Canonical AI entry point:** [brain/BOOT.md](brain/BOOT.md). Load it first. The repository is a context and handover system—not the source code for all Mandla projects.

## Retrieve only what the task needs

1. Read [brain/BOOT.md](brain/BOOT.md) (critical rules, precedence, privacy and verification).
2. Resolve the task using [brain/ROUTES.json](brain/ROUTES.json), or [brain/generated/catalog.json](brain/generated/catalog.json). For exact facts use [brain/generated/record-index.json](brain/generated/record-index.json).
3. Read the matching [project card](brain/generated/cards/) and the **original linked JSONL records** needed. The cards are compact generated previews.
4. For code, read [REPOSITORY_INDEX.md](REPOSITORY_INDEX.md) and inspect the **actual target repository**. For design, use [brain/DESIGN_ROUTES.md](brain/DESIGN_ROUTES.md) and the full required design chapters.
5. Validate, preserve and report concrete results, not claims of completion.

**Always respect:** latest user instruction > canonical decision > verified current evidence > older memory or reconstructed handover. Keep historical/rejected decisions as history. No secrets or private records in this public repository.

**Freshness:** the older [CURRENT_HANDOVER.md](CURRENT_HANDOVER.md), [PROJECT_INDEX.md](PROJECT_INDEX.md) and repository role index mainly reflect **16 July 2026**. The [8 November archive](archive/2026-11-08/00-INDEX.md) is newer but partially reconstructed, not an exhaustive audit. [Freshness and proof guide](brain/STATUS.md).

**Full legacy reading protocol:** [preserved here](archive/2026-11-08/pre-ai-v2/START_HERE.md). The [full operating instructions](AI_INSTRUCTIONS.md), [canonical-memory charter](CANONICAL_MEMORY.md), [memory schema](MEMORY_SCHEMA.md), and [capability discovery standard](AI_CAPABILITY_DISCOVERY.md) remain available for focused retrieval. Do not needlessly preload all of them.

**On updates:** original structured JSONL is authoritative. Run `python3 scripts/build_ai_index.py` and `python3 scripts/validate_ai_brain.py` after memory edits; never manually revise derived cards or indexes.
