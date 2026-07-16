# Start Here — AI Handover Protocol

This file is the mandatory entry point for any AI assistant helping Mandla Lee Ndlovu.

Do not begin by guessing from repository names, scanning random files or repeating generic advice. Load the relevant context first, then act.

## Required reading order

### 1. Understand the system

Read:

1. `README.md`
2. `AI_INSTRUCTIONS.md`
3. `CURRENT_HANDOVER.md`
4. `PROJECT_INDEX.md`
5. `MEMORY_SCHEMA.md`

### 2. Understand Mandla

Read:

- `memory/identity.jsonl`
- `memory/preferences.jsonl`

Use these records to understand Mandla’s devices, skills, design preferences, working style and constraints. Do not treat preferences as decorative trivia; they often determine whether a result is useful.

### 3. Load only the relevant project context

Identify the project from `PROJECT_INDEX.md`, then read its project file. Common files include:

- `projects/kingship-christian-centre-ministry.jsonl`
- `projects/samlee-estates.jsonl`
- `projects/soil-and-spear.jsonl`
- `projects/kota.jsonl`
- `projects/born-in-mzansi.jsonl`
- `projects/music.jsonl`
- `projects/websites.jsonl`
- `projects/other-projects.jsonl`

### 4. Check history and unfinished work

Read:

- `memory/timelines.jsonl` for renames, migrations, milestones and corrected roadmaps.
- `memory/unresolved.jsonl` for unfinished work, missing artifacts, bugs and pending decisions.

Filter by the project name and tags instead of treating every unresolved item as part of the current request.

### 5. Inspect the real working files

Mandla Brain describes projects but is not always the project’s source-code repository.

Before editing or claiming the current state of a website, app, game or document:

1. Find the referenced repository, Drive file, ZIP or uploaded artifact.
2. Inspect its actual contents.
3. Compare the artifact with Mandla Brain’s intended state.
4. Report any mismatch clearly.

For Kingship Christian Centre, the known website repositories are:

- Production: `MandlaLee/thethrivegeneration`
- Staging: `MandlaLee/test`

Do not change production merely because a planned feature appears in Mandla Brain.

## Before taking action

Give Mandla a compact internal-state summary only when it is useful. It should identify:

- the project you believe he means;
- the current confirmed decision;
- the unfinished task or requested outcome;
- any assumption that could change the result.

Then proceed. Avoid unnecessary permission loops when the request is already clear.

## Decision precedence

When records conflict, use this order:

1. A newer explicit instruction from Mandla in the current conversation
2. An active explicit decision in the repository
3. A newer confirmed active record
4. A current `in_progress` or `planned` record
5. Historical context
6. Superseded or rejected options

Never revive an older name, design direction, repository or roadmap merely because it appears earlier in the history.

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
- Keep legal, policy and technical caveats proportional to the actual risk.
- Do not confuse public front-end study with unauthorized backend access.
- Study useful patterns deeply, then rebuild original and improved systems.
- Avoid generic AI templates and interchangeable design decisions.
- Protect working production systems with staging and verification.
- Think ahead about scalability, maintenance, automation and income.

## End-of-session responsibility

Before a substantial session ends:

1. Preserve all generated artifacts.
2. Commit or save completed work.
3. Record important new decisions.
4. Update unresolved tasks honestly.
5. Add timeline entries for major changes.
6. Never store credentials or sensitive personal data in this public repository.

## First response after loading this repository

A capable assistant should be able to say, in its own words:

> I understand who Mandla is, which project is active, what decisions are already settled, what remains unfinished, and which actual files I must inspect before continuing.

If the assistant cannot say that accurately, it has not loaded enough context yet.