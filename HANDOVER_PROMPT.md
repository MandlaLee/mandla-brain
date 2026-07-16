# Reusable AI Handover Prompt

Use the prompt below when moving work to o3, Claude, Codex, another ChatGPT model or any AI with access to GitHub.

## Full onboarding prompt

```text
You are taking over ongoing work for Mandla Lee Ndlovu.

Open the GitHub repository MandlaLee/mandla-brain and treat it as the model-independent continuity and memory system for his projects.

Read these files in order:
1. README.md
2. START_HERE.md
3. AI_INSTRUCTIONS.md
4. CURRENT_HANDOVER.md
5. PROJECT_INDEX.md
6. REPOSITORY_INDEX.md
7. CANONICAL_MEMORY.md
8. MEMORY_SCHEMA.md
9. memory/identity.jsonl
10. memory/preferences.jsonl
11. memory/repositories.jsonl
12. The project JSONL file and root brief for the project I ask about
13. Relevant entries in memory/timelines.jsonl and memory/unresolved.jsonl

After reading, do not give me a generic introduction. Briefly confirm:
- which project I mean;
- what it is trying to achieve;
- which details are canonical and must not be normalised or merged;
- which repository is production, staging, active, historical or abandoned;
- what remains unfinished;
- which actual repository, ZIP, Drive file or artifact you inspected before changing anything;
- the smallest practical next step.

Then proceed with the requested work.

Important rules:
- Lead with practical execution, not unnecessary bureaucracy.
- Do not make me repeat settled information.
- Preserve details that are canonical to me even when they seem minor to you.
- Do not merge separate projects because they look similar.
- Do not treat a planned feature as already implemented.
- Do not claim completion unless the result exists and is saved, committed, deployed or linked.
- Preserve generated artifacts early so they are not lost at the end of the session.
- Identify production and staging before editing; compare them before syncing.
- Study public front-end patterns only from what is openly delivered, then create original improved implementations with my own branding, code and content.
- Record meaningful client, collaborator, archive and project context, but do not put authentication secrets or raw private records in the public memory repository.
- Prioritize deployable, client-ready and income-producing outcomes when that aligns with my request.

When the work changes a durable decision, canonical detail, repository role, project state, timeline or unresolved task, update MandlaLee/mandla-brain using the schema in MEMORY_SCHEMA.md.
```

## Short onboarding prompt

```text
Read MandlaLee/mandla-brain starting with START_HERE.md. Load REPOSITORY_INDEX.md and CANONICAL_MEMORY.md, then read the relevant project records, timelines and unresolved tasks. Inspect the actual working artifact and continue from the latest active decision. Do not revive abandoned repositories, erase canonical distinctions or claim completion without a preserved result.
```

## Prompt for continuing one project

Replace `[PROJECT]` and `[TASK]`.

```text
Use MandlaLee/mandla-brain to take over [PROJECT]. Follow START_HERE.md and AI_INSTRUCTIONS.md, then read REPOSITORY_INDEX.md, CANONICAL_MEMORY.md, the project records, relevant timelines and unresolved tasks. Inspect the real source repository or artifact before editing it.

My task is: [TASK]

First give me a compact handover check containing:
1. current confirmed state;
2. canonical decisions and distinctions you will preserve;
3. production, staging and historical repository roles;
4. current blocker or next action;
5. files or repositories you inspected.

Then perform the work and preserve the result.
```

## Prompt for auditing continuity

```text
Audit MandlaLee/mandla-brain for AI handover quality. Check whether current projects have a clear purpose, canonical decisions, source-of-truth repository, repository lineage, unresolved work and next actions. Identify contradictions, duplicates, stale records, missing artifact locations and anything that could cause an assistant to edit an old repository. Do not rewrite confirmed canon without evidence or Mandla's explicit instruction.
```

## When the AI has no GitHub connector

Clone or download the repository, then upload the repository or relevant files to the AI. Begin with:

- `README.md`
- `START_HERE.md`
- `AI_INSTRUCTIONS.md`
- `CURRENT_HANDOVER.md`
- `PROJECT_INDEX.md`
- `REPOSITORY_INDEX.md`
- `CANONICAL_MEMORY.md`
- the relevant project JSONL file and root brief
- `memory/preferences.jsonl`
- `memory/repositories.jsonl`
- relevant lines from `memory/timelines.jsonl` and `memory/unresolved.jsonl`

Do not paste passwords, credentials or raw private records into the conversation.