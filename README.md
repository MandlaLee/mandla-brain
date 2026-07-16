# Mandla Brain

Mandla Brain is the model-independent source of truth for Mandla Lee Ndlovu’s ongoing work, decisions, preferences, project history and unfinished tasks.

It exists so that work begun with one AI model or service can continue with another—ChatGPT, o3, Claude, Codex or any future assistant—without forcing Mandla to explain his entire world again.

This is not primarily a source-code repository. It is a structured continuity and handover system. Actual application and website code may live in separate repositories referenced by the records here.

## Start here

A new AI assistant must read these files in this order:

1. [`START_HERE.md`](START_HERE.md)
2. [`AI_INSTRUCTIONS.md`](AI_INSTRUCTIONS.md)
3. [`CURRENT_HANDOVER.md`](CURRENT_HANDOVER.md)
4. [`PROJECT_INDEX.md`](PROJECT_INDEX.md)
5. [`MEMORY_SCHEMA.md`](MEMORY_SCHEMA.md)
6. The relevant files in `memory/` and `projects/`

A ready-to-copy onboarding prompt is available in [`HANDOVER_PROMPT.md`](HANDOVER_PROMPT.md).

## Why this repository exists

Mandla works across web development, design, music, ministry systems, property, games, writing and digital products. Long conversations with AI assistants have produced important decisions and detailed project systems. Those decisions must not disappear when:

- a conversation reaches its limit;
- an AI subscription or model changes;
- a ZIP or generated artifact is lost;
- another assistant takes over;
- a project pauses and resumes later;
- an older decision is accidentally treated as current.

The repository preserves durable context while separating current decisions, history and unresolved work.

## Repository structure

- `memory/identity.jsonl` — Mandla’s identity and technical environment.
- `memory/preferences.jsonl` — durable working, design and recommendation preferences.
- `memory/timelines.jsonl` — important changes, milestones and project evolution.
- `memory/unresolved.jsonl` — unfinished, blocked or unverified work.
- `projects/*.jsonl` — project-specific facts, systems, decisions, branding and goals.
- Root Markdown files — human- and AI-readable navigation, rules and current handover context.

Each `.jsonl` file contains one complete JSON object per line. See [`MEMORY_SCHEMA.md`](MEMORY_SCHEMA.md).

## Core principles

1. **Continuity over model loyalty.** No project should depend on one AI model remembering a private conversation.
2. **Practical work first.** Help Mandla ship, deploy, preserve and earn—not merely discuss possibilities.
3. **Current decisions outrank old ideas.** Historical records explain evolution but must not silently override active decisions.
4. **Never invent completion.** A build is complete only when the file, commit, deployment or verified result exists.
5. **Preserve artifacts immediately.** Generated projects should be saved, committed or delivered before session limits are reached.
6. **Inspect before changing.** Read the relevant memory and actual code repository before making structural changes.
7. **Original improvement, not lazy imitation.** Public products may be studied for patterns, then rebuilt with Mandla’s own code, branding and content.
8. **No secrets.** This repository is public. Never store passwords, API keys, access tokens, private credentials, passport numbers, banking details, confidential counselling records or other sensitive personal information.

## Primary project areas

- Kingship Christian Centre and its ministries, website and administration systems
- SamLee Estates student accommodation and SEO platform
- Soil & Spear
- KOTA
- Born In Mzansi
- YK Nazarene and Kingship music projects
- 123Kasi
- WEBPFYER, Formfyer and ML CODE
- Children’s books and other creative projects
- Mandla’s web-development portfolio, tools and commercial growth

## For human collaborators

Treat the repository as a briefing room. Begin with `START_HERE.md`, identify the project being discussed, read its JSONL file and unresolved records, then inspect the actual working repository or files before claiming what exists.

## Last onboarding overhaul

16 July 2026 — the repository was upgraded from a collection of structured memories into an explicit cross-model AI handover system.