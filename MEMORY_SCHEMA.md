# Mandla Brain Memory Schema

Mandla Brain stores durable structured records as JSON Lines (`.jsonl`). Each line must be one complete valid JSON object. Do not wrap the file in an array and do not split one object across multiple lines.

## Canonical record

```json
{"id":"project-topic-specific-id","type":"decision","subject":"Subject name","project":"Project name or null","key":"stable_machine_key","value":"The actual information or a structured object","status":"active","confidence":"explicit","source":{"type":"chat","conversation_topic":"What was being discussed","conversation_date":"2026-07-16"},"tags":["project-tag","topic-tag"],"created_at":"2026-07-16","updated_at":"2026-07-16"}
```

## Required fields

### `id`

A globally understandable stable identifier.

Rules:

- lowercase;
- words separated by hyphens;
- descriptive enough to distinguish the record;
- do not reuse an ID for an unrelated meaning.

Example:

```text
student-accommodation-campuskey-private-study-mirror
```

### `type`

Describes what kind of memory the record contains.

Recommended values:

- `identity`
- `fact`
- `preference`
- `decision`
- `rule`
- `workflow`
- `goal`
- `status`
- `timeline`
- `repository`
- `unresolved_task`
- `completed_task`
- `rejected_option`
- `technical_environment`
- `branding`
- `constraint`
- `lesson`

Use the most precise type. Do not call everything a fact.

Use `repository` when the record’s main purpose is to identify a repository’s role, source-of-truth status, lineage or editing instruction.

### `subject`

The entity the record is about, such as:

- `Mandla Lee Ndlovu`
- `Kingship Christian Centre`
- `Student Accommodation Successor`
- `Soil & Spear trading`
- `MandlaLee/thethrivegeneration`

### `project`

The broader project name, or `null` for a cross-project personal record.

Use project names consistently. Preferred current names include:

- `Kingship Christian Centre`
- `Student Accommodation Successor`
- `Uni Residentia`
- `Soil & Spear`
- `ML Network`
- `KOTA`
- `Township Shop Tycoon`
- `Born In Mzansi`
- `Cohortly`
- `FYER Ecosystem`
- `Jasper Samuel`
- `Client and Collaborative Sites`
- `Music`
- `Website Samples`
- `Other Projects`
- `Personal Development`
- `Mandla Brain`

Do not use an obsolete project name as the current project value merely because it appeared historically.

When the current project has no final public name, use a transparent temporary descriptor such as `Student Accommodation Successor` rather than inventing a brand.

### `key`

A concise machine-readable description of the specific property.

Examples:

- `deployment_workflow`
- `visual_direction`
- `application_backend`
- `engine_change`
- `assistant_working_style`
- `repository_role`
- `canonical_distinction`

### `value`

The actual memory. It may be:

- a string;
- a number;
- a boolean;
- an array;
- a structured object.

Prefer structured objects when several related details belong together.

For repository records, useful fields may include:

```json
{"role":"production","visibility":"public","current":true,"live_domain":"example.co.za","instruction":"Protect production and test risky changes in staging."}
```

Do not place secret values in this field.

### `status`

Recommended values:

- `active` — currently applicable
- `in_progress` — started but unfinished
- `planned` — intended but not implemented
- `unresolved` — blocked, missing, broken or unverified
- `completed` — verified finished
- `historical` — kept to explain evolution
- `superseded` — replaced by a newer decision
- `rejected` — explicitly not wanted or abandoned

Status describes applicability or progress, not emotional importance.

A repository may be `historical` while still containing useful reusable code. A `rejected` repository must not be revived as the current implementation without a new explicit decision from Mandla.

### `confidence`

Recommended values:

- `explicit` — Mandla directly stated it
- `confirmed` — supported repeatedly or by an artifact
- `inferred` — a reasonable interpretation that still needs care

An inferred record must never silently override an explicit or canonical one.

### `source`

A structured description of where the memory came from.

Typical chat source:

```json
{"type":"chat","conversation_topic":"CampusKey website study workflow","conversation_date":"2026-07-16"}
```

Possible source types include:

- `chat`
- `document`
- `repository`
- `repository_audit`
- `chat_and_repository_audit`
- `website`
- `artifact`
- `user_confirmation`

Do not claim a source that was not actually inspected.

### `tags`

A short array used for retrieval and grouping.

Use stable, lowercase tags such as:

```json
["student-accommodation","website","seo","unresolved"]
```

Avoid dozens of redundant tags.

### `created_at`

The date the underlying information first became known, where available.

Format:

```text
YYYY-MM-DD
```

### `updated_at`

The date the record was last meaningfully changed or reconfirmed.

Do not update this date merely because the file was reformatted.

## Canonical-memory handling

Read `CANONICAL_MEMORY.md`.

A fact can be canonical to Mandla even if another AI considers it small, unusual or not industry-standard.

When a record captures canon:

- use `type: "rule"` or `type: "decision"`;
- use `confidence: "explicit"` when Mandla stated it directly;
- add a `canonical` tag where useful;
- preserve exact names, capitalisation and distinctions;
- do not merge it with a similar project or concept;
- change it only after Mandla explicitly changes it.

Examples include:

- product-name capitalisation;
- project distinctions such as KOTA versus Township Shop Tycoon;
- source-of-truth repository roles;
- a character’s role in a game;
- relationships and business context that affect future decisions.

## File placement

### `memory/identity.jsonl`

Personal identity, professional role, devices and durable environment facts.

### `memory/preferences.jsonl`

Working style, design preferences, assistant behaviour and durable recommendation preferences.

### `memory/timelines.jsonl`

Renames, migrations, major milestones, repository transitions, roadmap corrections and other dated evolution.

### `memory/unresolved.jsonl`

Tasks that are blocked, missing, unfinished or awaiting verification.

### `memory/repositories.jsonl`

Repository roles, visibility, source-of-truth state, predecessor/successor relationships and editing instructions.

### `projects/<project>.jsonl`

Facts, systems, branding, goals and decisions unique to a project.

### Root Markdown briefs

Use a root Markdown brief when a relationship spans several projects or repositories and needs a clear human-readable explanation, such as:

- `REPOSITORY_INDEX.md`
- `STUDENT_ACCOMMODATION_SUCCESSOR.md`
- `GAME_PROJECT_RELATIONSHIPS.md`
- `CLIENT_AND_COLLABORATIVE_SITES.md`

A record may appear in a project file and be referenced from unresolved or timeline files, but avoid exact duplicate records.

## Repository-role records

A repository record should answer, where known:

1. What project does this repository belong to?
2. Is it production, staging, active, prototype, historical, abandoned or empty?
3. Is it the current source of truth?
4. Does it have a predecessor or successor?
5. Is there a live deployment or custom domain?
6. What must an AI do or avoid before editing it?
7. When was the role last verified?

When source-of-truth status changes, update `memory/repositories.jsonl`, `REPOSITORY_INDEX.md`, `PROJECT_INDEX.md` and add a timeline record.

## Updating an existing fact

When the same durable fact changes:

1. Find the existing record.
2. Decide whether the old value must remain as history.
3. If history matters, mark the old record `historical` or `superseded` and add a timeline entry.
4. Add or update the current active record.
5. Set an accurate `updated_at` date.

Example: a project rename should retain the old name in `memory/timelines.jsonl`, while current project records use the new name.

## Resolving an unfinished task

When an unresolved task is genuinely completed:

1. Verify the artifact, deployment, commit or test result.
2. Change or replace the unresolved record only after verification.
3. Add a `completed_task` or timeline record describing the result and location.
4. Preserve useful history about the former blocker.

A verbal claim from an AI without a saved result is not verification.

## Duplicate handling

Delete a record only when it is an accidental duplicate with no unique historical value.

Do not delete an older conflicting decision merely to make the file look clean. Preserve it as historical or superseded when it explains how the project evolved.

Meaningful abandoned ideas, client history and failed approaches may remain valuable if they explain current decisions.

## Sensitive-data rules

This repository is public. Do not store authentication secrets, access tokens, private keys, private webhook URLs, raw database credentials, identity numbers, banking credentials or confidential applicant and customer records.

Store a safe description of the system, relationship or event instead. Another AI needs to know that a credential or private record exists and where it belongs, not receive the secret itself.

## Validation checklist

Before committing a JSONL change:

- every line parses as JSON;
- every record has a unique ID;
- dates use `YYYY-MM-DD`;
- the current project name is used;
- status and type are accurate;
- repository roles agree with `REPOSITORY_INDEX.md`;
- canonical distinctions are preserved;
- no secrets are present;
- unfinished work is not labelled complete;
- historical context has not been accidentally erased.