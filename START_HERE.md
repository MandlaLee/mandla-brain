# Start Here — AI Handover Protocol

This file is the mandatory entry point for any AI assistant helping Mandla Lee Ndlovu.

Do not begin by guessing from repository names, scanning random files or repeating generic advice. Load the relevant context first, identify the actual source of truth, then act.

## Required reading order

### 1. Understand the system

Read:

1. `README.md`
2. `AI_INSTRUCTIONS.md`
3. `CURRENT_HANDOVER.md`
4. `PROJECT_INDEX.md`
5. `REPOSITORY_INDEX.md`
6. `CANONICAL_MEMORY.md`
7. `MEMORY_SCHEMA.md`

### 2. Understand Mandla

Read:

- `memory/identity.jsonl`
- `memory/preferences.jsonl`

Use these records to understand Mandla’s devices, skills, design preferences, working style and constraints. Preferences often determine whether a result is useful.

### 3. Identify the correct repository role

Read:

- `REPOSITORY_INDEX.md`
- `memory/repositories.jsonl`

Before editing code, determine whether a repository is:

- production;
- staging;
- active foundation;
- prototype;
- historical predecessor;
- abandoned;
- empty;
- or a future repository not yet created.

Never assume the newest-looking repository name is current. Never push an older staging copy over newer production work.

### 4. Load the relevant project context

Identify the project from `PROJECT_INDEX.md`, then read its project file and any root brief.

Common files include:

- `projects/kingship-christian-centre-ministry.jsonl`
- `projects/samlee-estates.jsonl`
- `projects/student-accommodation-successor.jsonl` when present
- `STUDENT_ACCOMMODATION_SUCCESSOR.md`
- `projects/soil-and-spear.jsonl`
- `GAME_PROJECT_RELATIONSHIPS.md`
- `projects/kota.jsonl`
- `projects/born-in-mzansi.jsonl`
- `projects/cohortly.jsonl`
- `projects/fyer-ecosystem.jsonl`
- `projects/music.jsonl`
- `projects/websites.jsonl`
- `projects/other-projects.jsonl`
- `CLIENT_AND_COLLABORATIVE_SITES.md`

### 5. Check canon, history and unfinished work

Read:

- `CANONICAL_MEMORY.md` for details Mandla considers settled and authoritative;
- `memory/timelines.jsonl` for renames, migrations, milestones and corrected roadmaps;
- `memory/unresolved.jsonl` for unfinished work, missing artifacts, bugs and pending decisions.

Filter by project and tags. Do not treat every unresolved item as part of the current request.

### 6. Inspect the real working files

Mandla Brain describes projects but is not usually the source-code repository.

Before editing or claiming the current state of a website, app, game or document:

1. Find the repository, Drive file, ZIP or uploaded artifact.
2. Inspect its actual contents.
3. Compare the artifact with Mandla Brain’s intended state.
4. Report any mismatch clearly.
5. Verify whether production is ahead of staging.

For Kingship Christian Centre:

- Production: `MandlaLee/thethrivegeneration`
- Staging: `MandlaLee/test`
- Live domain: `kingshipcentre.co.za`

Do not change production merely because a planned feature appears in Mandla Brain.

For Soil & Spear:

- Current Godot work is being developed through Claude.
- Intended repository: `MandlaLee/Soil`.
- Until Mandla uploads it, old Shaka repositories are historical references only.

For the new student-accommodation platform:

- The final name and repository do not yet exist.
- The SamLee repositories are historical references whose strong SEO architecture should be preserved.

## Canonical distinctions

Do not merge similar-looking projects or ideas when Mandla has explicitly distinguished them.

Examples:

- KOTA is not Township Shop Tycoon.
- Soil & Spear is not the old Shaka’s Adventure implementation.
- `thethrivegeneration` is production; the other full Kingship sites are historical.
- WebPfyer, BgFyer, BrandFyer, DocuFyer and Fyer have different roles.
- Uni Residentia is not automatically the new accommodation brand.

When unsure whether a detail is canonical, ask the smallest necessary question before changing it.

## Before taking action

Give Mandla a compact internal-state summary only when useful. It should identify:

- the project you believe he means;
- the active source repository or artifact;
- the current confirmed decision;
- the unfinished task or requested outcome;
- any assumption that could change the result.

Then proceed. Avoid unnecessary permission loops when the request is clear.

## Decision precedence

When records conflict, use this order:

1. A newer explicit instruction from Mandla in the current conversation
2. An explicitly marked canonical rule
3. An active explicit decision in the repository
4. A newer confirmed active record
5. A current `in_progress` or `planned` record
6. Historical context
7. Superseded or rejected options

Never revive an older name, design direction, repository or roadmap merely because it appears earlier in history.

## Completion standard

Do not say a task is finished unless the result can be demonstrated through at least one of these:

- a committed file;
- a working deployment;
- a downloadable artifact;
- a saved document or design;
- a verified database or integration;
- a reproducible test result.

If an AI says it generated a ZIP but the ZIP cannot be found, the task remains unresolved.

## Working style Mandla expects

- Lead with the practical solution.
- Build and preserve real deliverables.
- Keep caveats proportional to the actual risk.
- Do not confuse public front-end study with unauthorized backend access.
- Study useful patterns deeply, then rebuild original and improved systems.
- Avoid generic AI templates and interchangeable design decisions.
- Protect working production systems through staging and comparison.
- Think ahead about scalability, maintenance, automation and income.
- Preserve Mandla’s canon even when it seems minor to the assistant.

## End-of-session responsibility

Before a substantial session ends:

1. Preserve all generated artifacts.
2. Commit or save completed work.
3. Record important new decisions and canonical clarifications.
4. Update unresolved tasks honestly.
5. Add timeline entries for major changes.
6. Update repository roles when a source of truth changes.
7. Keep secrets and raw private records out of the public repository.

## First response after loading this repository

A capable assistant should be able to say, in its own words:

> I understand who Mandla is, which project is active, which repository is the source of truth, what is canonical, what remains unfinished and which real files I must inspect before continuing.

If the assistant cannot say that accurately, it has not loaded enough context yet.