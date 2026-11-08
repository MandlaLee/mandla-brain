# AI Brain structure revisions

## v2 · 2026-11-08
- Audited 86 pre-migration files and 310 canonical structured records across 24 JSONL files.
- Established the fast [BOOT.md](BOOT.md) path, compact policy and task router, freshness/provenance model, and design chapter selector.
- Converted root START_HERE and HANDOVER_PROMPT into concise compatibility entrypoints; preserved the original texts under the dated archive.
- Retained existing canonical JSONL files and design knowledge intact.
- Added deterministic record and project indexes, split large project cards into small subtopic cards, and built an offline topic query CLI.
- Added integrity validation and a targeted GitHub Actions workflow to catch stale generated data or broken links.
- Updated README, AGENTS, CLAUDE and relevant handover headers to prefer context-on-demand while preserving full policies.
- FaceWeave/Deep-Live-Cam Plan B and private plugin status are treated as provenance-sensitive: not a confirmed live deployment or automatic inter-agent sync.

**Success criterion:** a new assistant can start with a small boot document, route a task, open only relevant source facts, and verify actual completion without treating stale snapshots as truth.
