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
samlee-campuskey-private-study-mirror
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
- `unresolved_task`
- `completed_task`
- `rejected_option`
- `technical_environment`
- `branding`
- `constraint`
- `lesson`

Use the most precise type. Do not call everything a fact.

### `subject`

The entity the record is about, such as:

- `Mandla Lee Ndlovu`
- `Kingship Christian Centre`
- `SamLee Estates website`
- `Soil & Spear trading`

### `project`

The broader project name, or `null` for a cross-project personal record.

Use project names consistently. Preferred current names include:

- `Kingship Christian Centre`
- `SamLee Estates`
- `Soil & Spear`
- `KOTA`
- `Born In Mzansi`
- `Music`
- `Website Samples`
- `Other Projects`
- `Personal Development`
- `Mandla Brain`

Do not use an obsolete project name as the current project value merely because it appeared historically.

### `key`

A concise machine-readable description of the specific property.

Examples:

- `deployment_workflow`
- `visual_direction`
- `application_backend`
- `engine_change`
- `assistant_working_style`

### `value`

The actual memory. It may be:

- a string;
- a number;
- a boolean;
- an array;
- a structured object.

Prefer structured objects when several related details belong together.

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
- `rejected` — explicitly not wanted

Status describes applicability or progress, not emotional importance.

### `confidence`

Recommended values:

- `explicit` — Mandla directly stated it
- `confirmed` — supported repeatedly or by an artifact
- `inferred` — a reasonable interpretation that still needs care

An inferred record must never silently override an explicit one.

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
- `website`
- `artifact`
- `user_confirmation`

Do not claim a source that was not actually inspected.

### `tags`

A short array used for retrieval and grouping.

Use stable, lowercase tags such as:

```json
["samlee","website","seo","unresolved"]
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

## File placement

### `memory/identity.jsonl`

Personal identity, professional role, devices and durable environment facts.

### `memory/preferences.jsonl`

Working style, design preferences, assistant behaviour and durable recommendation preferences.

### `memory/timelines.jsonl`

Renames, migrations, major milestones, roadmap corrections and other dated evolution.

### `memory/unresolved.jsonl`

Tasks that are blocked, missing, unfinished or awaiting verification.

### `projects/<project>.jsonl`

Facts, systems, branding, goals and decisions unique to a project.

A record may appear in a project file and be referenced from unresolved or timeline files, but avoid exact duplicate records.

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

## Security rules

This repository is public. Never store:

- passwords;
- access tokens;
- API keys;
- private webhook URLs;
- database passwords or connection strings;
- banking details;
- passport, national ID or tax numbers;
- private home addresses;
- confidential counselling, member, applicant or donor records.

Safe replacement example:

```json
{"key":"database_credentials","value":"Credentials are stored in the secure deployment environment and are not committed to Mandla Brain."}
```

## Validation checklist

Before committing a JSONL change:

- every line parses as JSON;
- every record has a unique ID;
- dates use `YYYY-MM-DD`;
- the current project name is used;
- status and type are accurate;
- no secrets are present;
- unfinished work is not labelled complete;
- historical context has not been accidentally erased.