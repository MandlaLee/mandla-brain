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
6. MEMORY_SCHEMA.md
7. memory/identity.jsonl
8. memory/preferences.jsonl
9. The JSONL file for the project I ask about
10. Relevant entries in memory/timelines.jsonl and memory/unresolved.jsonl

After reading, do not give me a generic introduction. Briefly confirm:
- which project I mean;
- what it is trying to achieve;
- which decisions are already settled;
- what remains unfinished;
- which actual repository, ZIP, Drive file or artifact you must inspect before changing anything;
- the smallest practical next step.

Then proceed with the requested work.

Important rules:
- Lead with practical execution, not unnecessary bureaucracy.
- Do not make me repeat settled information.
- Do not treat a planned feature as already implemented.
- Do not claim completion unless the result exists and is saved, committed, deployed or linked.
- Preserve generated artifacts early so they are not lost at the end of the session.
- Use staging before changing live production systems.
- Study public front-end patterns only from what is openly delivered, then create original improved implementations with my own branding, code and content.
- Never store passwords, tokens, banking details, identity numbers or confidential user data in mandla-brain because the repository is public.
- Prioritize deployable, client-ready and income-producing outcomes when that aligns with my request.

When the work changes a durable decision, project state, timeline or unresolved task, update MandlaLee/mandla-brain using the schema in MEMORY_SCHEMA.md.
```

## Short onboarding prompt

```text
Read MandlaLee/mandla-brain starting with START_HERE.md. Load the relevant project file, timelines and unresolved tasks, inspect the actual working artifact, then continue from the latest active decision. Do not revive superseded plans or claim completion without a preserved result.
```

## Prompt for continuing one project

Replace `[PROJECT]` and `[TASK]`.

```text
Use MandlaLee/mandla-brain to take over [PROJECT]. Follow START_HERE.md and AI_INSTRUCTIONS.md, then read the project’s JSONL records, relevant timelines and unresolved tasks. Inspect the real source repository or artifact before editing it.

My task is: [TASK]

First give me a compact handover check containing:
1. current confirmed state;
2. settled decisions you will preserve;
3. current blocker or next action;
4. files or repositories you inspected.

Then perform the work and preserve the result.
```

## Prompt for auditing continuity

```text
Audit MandlaLee/mandla-brain for AI handover quality. Check whether current projects have a clear purpose, current state, settled decisions, related repositories, unresolved work and next actions. Identify contradictions, duplicates, stale records, missing artifact locations and sensitive information that should not be public. Do not rewrite confirmed decisions without evidence.
```

## When the AI has no GitHub connector

Clone or download the repository, then upload the repository or the relevant files to the AI. Begin with:

- `README.md`
- `START_HERE.md`
- `AI_INSTRUCTIONS.md`
- `CURRENT_HANDOVER.md`
- `PROJECT_INDEX.md`
- the relevant project JSONL file
- `memory/preferences.jsonl`
- relevant lines from `memory/timelines.jsonl` and `memory/unresolved.jsonl`

Do not paste passwords, credentials or private client information into the conversation.