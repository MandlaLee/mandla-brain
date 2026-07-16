# Mandla Brain

Mandla Brain is the model-independent source of truth for Mandla Lee Ndlovu’s ongoing work, decisions, preferences, project history, repository roles and unfinished tasks.

It exists so that work begun with one AI model or service can continue with another—ChatGPT, o3, Claude, Codex or any future assistant—without forcing Mandla to explain his entire world again.

This is not primarily a source-code repository. It is a structured continuity and handover system. Actual application and website code lives in separate repositories mapped in `REPOSITORY_INDEX.md`.

## Start here

A new AI assistant must read these files in this order:

1. [`START_HERE.md`](START_HERE.md)
2. [`AI_INSTRUCTIONS.md`](AI_INSTRUCTIONS.md)
3. [`CURRENT_HANDOVER.md`](CURRENT_HANDOVER.md)
4. [`PROJECT_INDEX.md`](PROJECT_INDEX.md)
5. [`REPOSITORY_INDEX.md`](REPOSITORY_INDEX.md)
6. [`CANONICAL_MEMORY.md`](CANONICAL_MEMORY.md)
7. [`MEMORY_SCHEMA.md`](MEMORY_SCHEMA.md)
8. The relevant files in `memory/`, `projects/` and the root project briefs

A ready-to-copy onboarding prompt is available in [`HANDOVER_PROMPT.md`](HANDOVER_PROMPT.md).

## Why this repository exists

Mandla works across web development, design, music, ministry systems, property, games, writing and digital products. Long conversations with AI assistants have produced important decisions and detailed project systems. Those decisions must not disappear when:

- a conversation reaches its limit;
- an AI subscription or model changes;
- a ZIP or generated artifact is lost;
- another assistant takes over;
- a project pauses and resumes later;
- an older decision is accidentally treated as current;
- a historical repository is mistaken for production;
- an AI decides that a small but canonical detail is unimportant.

The repository preserves durable context while separating current canon, history, rejected directions and unresolved work.

## Repository structure

- `memory/identity.jsonl` — Mandla’s identity and technical environment.
- `memory/preferences.jsonl` — durable working, design and recommendation preferences.
- `memory/timelines.jsonl` — important changes, milestones and project evolution.
- `memory/unresolved.jsonl` — unfinished, blocked or unverified work.
- `memory/repositories.jsonl` — structured repository roles and source-of-truth status.
- `projects/*.jsonl` — project-specific facts, systems, decisions, branding and goals.
- `REPOSITORY_INDEX.md` — human-readable map of production, staging, active, historical and abandoned repositories.
- `CANONICAL_MEMORY.md` — rules for preserving details that are canonical to Mandla.
- Root project briefs — cross-project relationships and current clarifications.

Each `.jsonl` file contains one complete JSON object per line. See [`MEMORY_SCHEMA.md`](MEMORY_SCHEMA.md).

## Current root project briefs

- [`STUDENT_ACCOMMODATION_SUCCESSOR.md`](STUDENT_ACCOMMODATION_SUCCESSOR.md)
- [`GAME_PROJECT_RELATIONSHIPS.md`](GAME_PROJECT_RELATIONSHIPS.md)
- [`CLIENT_AND_COLLABORATIVE_SITES.md`](CLIENT_AND_COLLABORATIVE_SITES.md)

## Core principles

1. **Continuity over model loyalty.** No project should depend on one AI model remembering a private conversation.
2. **Practical work first.** Help Mandla ship, deploy, preserve and earn—not merely discuss possibilities.
3. **Current decisions outrank old ideas.** Historical records explain evolution but must not silently override active decisions.
4. **Mandla’s canon is authoritative.** Do not normalise away distinctions or details he has explicitly settled.
5. **Repositories have roles.** Identify production, staging, prototypes, historical copies and abandoned experiments before editing.
6. **Never invent completion.** A build is complete only when the file, commit, deployment or verified result exists.
7. **Preserve artifacts immediately.** Generated projects should be saved, committed or delivered before session limits are reached.
8. **Inspect before changing.** Read the relevant memory and actual code repository before making structural changes.
9. **Original improvement, not lazy imitation.** Public products may be studied for patterns, then rebuilt with Mandla’s own code, branding and content.
10. **Keep secrets out of this public repository.** Record the system and context without storing authentication secrets or raw private records.

## Primary project areas

- Kingship Christian Centre and its ministries, website and administration systems
- The unnamed student-accommodation successor and historical SamLee work
- Soil & Spear and ML Network
- KOTA and Township Shop Tycoon
- Born In Mzansi
- Cohortly
- The FYER ecosystem: BgFyer, WebPfyer, BrandFyer, DocuFyer and Fyer
- YK Nazarene and Kingship music projects
- 123Kasi
- Jasper Samuel, Ntiyiso and other client or collaborative sites
- Mandla’s portfolio, tools and commercial growth
- Children’s books and other creative projects

## For human collaborators

Treat the repository as a briefing room. Begin with `START_HERE.md`, identify the project being discussed, read its project and repository records, then inspect the actual working repository or files before claiming what exists.

## Last major audit

16 July 2026 — all accessible MandlaLee repositories were audited, contradictions were clarified with Mandla, repository roles were mapped, stale unresolved records were corrected and new project-family briefs were added.