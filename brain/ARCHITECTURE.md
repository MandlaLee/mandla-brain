# Mandla Brain v2: retrieval architecture

## Goal
Reduce an AI's initial read from seven large root documents to one compact [BOOT.md](BOOT.md) and an on-demand topic lookup while preserving Mandla's entire existing knowledge and canon.

## Layers

1. **Control plane:** [BOOT.md](BOOT.md), [RULES.md](RULES.md), [STATUS.md](STATUS.md), [DESIGN_ROUTES.md](DESIGN_ROUTES.md). Tiny, high-value operating context.
2. **Router:** [ROUTES.json](ROUTES.json), curated aliases and source selection (human-/AI-maintained). No model-specific tool dependency.
3. **Retrieval index:** [generated/catalog.json](generated/catalog.json), [generated/record-index.json](generated/record-index.json), generated project cards. Rebuilt deterministically from JSONL; **not another source of truth**.
4. **Canonical knowledge:** unchanged root `memory/*.jsonl`, `projects/*.jsonl`, design chapters, and repository role mapping.
5. **Chronological evidence:** historical root documents and November archive with explicit freshness labels.
6. **Compatibility:** original root filenames and design skill paths remain available for Claude, Codex, existing automations, pinned links, Notion workflows and other assistants.

## Decisions
- **Markdown + JSON, not opaque proprietary encoding.** Markdown is robust for agent instructions; JSONL stores canonical records and provenance; compact JSON provides deterministic discovery. Minimal Python is optional for local search and validation.
- **No destructive moves of structured JSONL and design chapters.** Moving them would invalidate external citations, skills and syncs. The legacy long START_HERE and HANDOVER_PROMPT texts are preserved under `archive/2026-11-08/pre-ai-v2/`, and root entrypoints now route quickly.
- **Generated previews may omit information.** Source records and their confidence/updated_at always outrank previews; production must be verified independently.
- **Task-specific reading over bulk preloading.** A request about Aurum should not force a full read of the Kingship ministry, SEO history, design textbook or other unrelated projects.
- **Reproducibility over manual duplication.** When a canonical record changes, rebuild indexes with the included script and rely on CI to catch stale outputs.
- **Freshness is part of retrieval.** July snapshots and reconstructed November archives have distinct evidence levels.
- **No actual agent autonomy is created by a plugin pointer.** Plugin connections and runtime capabilities require independent verification.

## Safe migration and rollback
- The initial branch baseline was Git commit `0ebc554520e356c203d15b83b46dfa2122c33dea` (8 November 2026).
- Source records in `memory/` and `projects/`, 31 design chapters and skill files were intentionally not rewritten.
- A backup branch or the known baseline commit restores the prior state. The archived original entrypoints are available even if only one root document needs to be restored.
- An agent should update its prompts to read `brain/BOOT.md`, but legacy clients still reading `START_HERE.md` will be redirected.
