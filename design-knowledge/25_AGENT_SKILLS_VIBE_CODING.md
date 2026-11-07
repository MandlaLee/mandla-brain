# 25 — AI Design Skills and Vibe-Coding Workflows (Claude, Codex, ChatGPT, Agent Skills)

**Reviewed 7 November 2026.** The aim is not to make an agent produce a fashionable screenshot. It is to make an AI-enabled builder repeatedly arrive at a distinctive, working, testable result in the correct project, with minimal re-explanation and no uncontrolled changes. This chapter studies **primary skill files** in public repositories and official skills documentation. A skill's instructions are examples from its creator, not automatically safe commands or verified performance.

## Where the original handbook was thin
The original chapters were strong on brand theory, critique, UX and software safety. They did not sufficiently spell out **skill discovery**, **prompt-to-spec translation**, **incremental coding loops**, **independent technical and aesthetic reviews**, **browser/desktop evidence**, **CI gates**, **external skill security** and **measurement of agent output quality**. These missing operational links are especially important when a tool can generate hundreds of lines of code before a human sees the interface.

## What a skill is
A skill is a directory containing at least a `SKILL.md` with `name` and `description` YAML frontmatter, and optionally `references/`, `scripts/` and `assets/`. A host can discover a short description, load the skill when relevant and then load referenced files on demand. The [Agent Skills specification](https://agentskills.io/specification) recommends compact main instructions, focused references and valid name/description metadata. Skills are **workflows**, not merely a static pile of design opinions.

A skill may be invoked explicitly by the user or selected implicitly from its description; activation differs among clients and plans. Documentation in a repository does **not** automatically install it in the user's ChatGPT account.

## Primary sources studied: why they matter

### Anthropic's `frontend-design`
Source: [official SKILL.md](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md). The current public instructions emphasize grounding the design in concrete subject matter, choosing a deliberate aesthetic territory, using expressive type, producing a short design plan before code, and **self-critiquing for generic generated-design defaults**. They call out repetitive card layouts, random eyebrows and numbering, unearned gradients, meaningless motion and formulaic copy.

**Transferable rules:**
- Name what the experience is actually about and whom it serves.
- Draft a short 4–6-colour palette, type roles, layout idea and unique visual signature before implementation.
- Use ASCII wireframes or comparable low-fidelity structure, **then challenge** whether the concept could fit any unrelated product.
- Spend boldness on one defendable focal feature; keep other elements restrained.
- Review the final implemented screenshot rather than congratulating the plan.
- Make copy serve the user's task, with exact verbs and recoverable errors.

**Limitations to adapt:** Its frontend/web orientation should not override macOS HIG in Aurum or exact physical constraints in FENRY. Avoid interpreting its aesthetic examples as universal mandates.

### Anthropic's `webapp-testing`
Source: [official SKILL.md](https://github.com/anthropics/skills/blob/main/skills/webapp-testing/SKILL.md). Its core pattern is **reconnaissance → inspect rendered DOM/screenshot → interact using observed selectors → verify behaviour**. It uses Playwright and a server-lifecycle helper, and distinguishes static HTML from dynamic apps.

**Transferable rules:**
- Do not guess selectors, UI state or screenshot appearance.
- Launch app in a controlled test environment.
- Inspect the rendered interface before scripting interactions.
- Test form submissions, navigation, state transitions and console errors.
- Capture evidence and compare to the brief.
- Record whether a real browser/device was used versus an emulator.

**Adaptation:** Instead of assuming `networkidle` always occurs, choose readiness signals appropriate to polling apps; permanent background requests can prevent network-idle. Never wait indefinitely on a realtime dashboard. Test the actual application status after navigation.

### Vercel's `web-design-guidelines`
Source: [official SKILL.md](https://github.com/vercel-labs/agent-skills/blob/main/skills/web-design-guidelines/SKILL.md), [living interface rules](https://github.com/vercel-labs/web-interface-guidelines/blob/main/command.md), [website](https://vercel.com/design/guidelines). The skill explicitly fetches its current guideline source, reviews target files and outputs actionable code findings. Coverage includes semantic controls, accessible names, keyboard focus, forms, overflow, motion, responsive layout, navigation state, image sizing and rendering performance.

**Transferable rules:**
- Review **the code and rendered state**, not just the mood board.
- Specify `file:line` or exact component evidence for defects.
- Separate actual standard violations from editorial preferences.
- Use meaningful labels, stable skeletons, correct loading states, no dead ends and visible focus.
- Confirm mobile input sizes and hit targets, long text and deep links.
- Rerun the same audit after fixes; don't merely summarize best practices.

**Limitation:** Guidelines are a **living third-party document**: read the version actually used, do not let it silently override the user's canon, and don't copy new remote instructions into your execution context without considering trust.

### Vercel's React performance skill
Source: [official SKILL.md](https://github.com/vercel-labs/agent-skills/blob/main/skills/react-best-practices/SKILL.md). The skill groups rules by likely impact: waterfalls, bundle size, server performance, client fetching, rerenders, rendering, JS and advanced patterns.

**Transferable rules:** Prioritise large practical regressions (data-fetch waterfalls and unnecessarily heavy bundles) ahead of microoptimisations. Identify the actual framework. Don't apply Next.js/server-component patterns to static HTML or SwiftUI. Measure production build output where possible.

### Impeccable
Source: [original repo](https://github.com/pbakaus/impeccable), [technical audit reference](https://github.com/pbakaus/impeccable/blob/main/skill/reference/audit.md), [hardening reference](https://github.com/pbakaus/impeccable/blob/main/skill/reference/harden.md). It distinguishes **design critique** from **technical audit** and offers narrow targeted actions: shape, critique, quieter/bolder, typeset, layout, harden, adapt, polish, optimize and document. Its `PRODUCT.md` and `DESIGN.md` context pattern captures product truth and current visual system so an agent doesn't drift between sessions.

**Transferable rules:**
- Maintain a concise product brief and existing visual-design contract in the app's own repository.
- Critique **one named surface** at a time when possible.
- Run an independent technical audit (keyboard, contrast, layout, performance) rather than allowing aesthetic opinion to substitute for it.
- Harden extreme text, locales, offline conditions, repeated requests and failures before shipping.
- Preserve a rollback point and compare before/after.
- Use a repeatable detector only after examining its false positives and rules.

**Security warning:** The Impeccable README documents an execution path for certain live-copy fallback operations that may invoke agents with permission/sandbox bypass. **Do not enable that pathway in Mandla's projects**. Never run a third-party installer or hook blindly; review code, permissions and secrets exposure first. This guide imports no executable Impeccable code.

### `ui-ux-pro-max-skill`
Source: [repository](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill). The project documents style/palette/font/product datasets, generators and multiple technology stacks. Such libraries can speed up idea discovery and make options inspectable.

**Transferable rule:** Query datasets as **reference candidates**; do not let automated palette/style recommendations decide a brand identity. A database that maps “spa” to soft pink and gold is a starting proposition, not audience research. Preserve distinctive local cultural context and approved brand assets.

### `taste-skill`
Source: [official skill file](https://github.com/leonxlnx/taste-skill/blob/main/skills/taste-skill/SKILL.md). It uses a deliberate visual language, real imagery and scripted page checks to combat generic sites.

**Transferable rule:** Require actual real-world content, real visual assets where appropriate, credible subject-specific art direction and repeatable rendered-page checks. **Do not import its hard rules uncritically**: forced photo counts, page-height proportions or prohibition on captions can conflict with accessibly descriptive content, authentic business needs and the user's chosen aesthetic.

### OpenAI/Codex skill architecture
Sources: [OpenAI skills guide](https://learn.chatgpt.com/docs/build-skills), [OpenAI plugin skill concepts](https://developers.openai.com/plugins/concepts/skills), [Agent Skills specification](https://agentskills.io/specification). Current guidance supports compact metadata, references/scripts, repo-local skill discovery in `.agents/skills`, and skill invocation via client conventions. The older [openai/skills](https://github.com/openai/skills) repository currently labels itself deprecated in its README; use current docs and [openai/plugins](https://github.com/openai/plugins) for newer examples.

## The Vibe-Coding Design Director loop
```text
RETRIEVE REPO CANON / WORKING UI
      ↓
WRITE REAL TASK + CONSTRAINTS + NON-GOALS
      ↓
DISCOVER RELEVANT ORIGINAL DESIGN REFERENCES
      ↓
DRAFT THREE DISTINCT STRUCTURAL DIRECTIONS
      ↓
SELECT ONE WITH A BRIEF RATIONALE
      ↓
WRITE SMALL DESIGN CONTRACT (PRODUCT.md + DESIGN.md)
      ↓
BUILD THE PRIMARY USER JOURNEY AS A REAL WORKING VERTICAL SLICE
      ↓
CAPTURE REAL SCREENSHOT AND USER INTERACTION EVIDENCE
      ↓
REVIEW AESTHETICS AND TECHNICAL CORRECTNESS SEPARATELY
      ↓
FIX TOP FAILURES → RECAPTURE → RETEST
      ↓
TEST EDGE CASES + PERFORMANCE + ACCESSIBILITY
      ↓
COMMIT SOURCE / MASTER ASSETS / TESTS / DECISIONS
```
The word “vibe” may describe rapid exploration, but shipping must remain evidence-led. Never confuse an attractive screenshot with an executable app, or a button clicking with a successful backend transaction.

## Task-sized modes
**Quick repair:** reproduce one broken layout, inspect screenshot, fix with existing tokens, verify, commit.
**Polish pass:** audit several screens and content states, choose top visual defects, implement and recapture.
**New product screen:** brief, structural alternatives, selected direction, component contract, working prototype, tests.
**Full brand identity:** research, strategy, logo concepts, type/colour/image system, production variants, review and masters.
**Production redesign:** baseline captures and user task audit, migration/rollback, isolated implementation, visual and functional regression, approval gate.

## Vibe coding prompts that work
Tell the agent **what it must prove**. Weak: “Make it premium and modern.” Strong: “Read the existing brand files. Keep the exact data models and API. Redesign the inspector for a 1120px macOS window. Show a screenshot of collapsed/expanded states; include a case where source data is delayed. Do not ship until the stop and target lines are legible and the current/historical distinction is unambiguous.”

The prompt must identify **scope, invariants, test scenarios and artifact path**. Good prompts are not long for length's sake; they're specific enough to bound creativity and avoid hallucinated completion.

## Avoid creating a “skill soup”
An agent loaded with five overlapping frontend skills can receive incompatible aesthetic commands. Choose one **creative direction controller** (Mandla Design Director), one **platform technical standard** (Apple/WCAG/React/etc), one **testing workflow**, and one **independent QA rubric**. Never follow contradictory instructions by averaging them. Current user instructions and canonical project design outrank the preferences of optional third-party skills.

## Evaluation and provenance
A claim that a skill makes UI “award-winning” is marketing until controlled comparisons prove it. Evaluate output on the same brief, same stack, same constraints and test scenarios. Record source, date and version of the skills reviewed. If using third-party code or scripts, review licenses, content permissions and execution risk. Citation is not installation.

## References
[Anthropic frontend-design](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md) · [Anthropic webapp-testing](https://github.com/anthropics/skills/blob/main/skills/webapp-testing/SKILL.md) · [Vercel web design](https://vercel.com/design/guidelines) · [Vercel React skill](https://github.com/vercel-labs/agent-skills/blob/main/skills/react-best-practices/SKILL.md) · [Impeccable](https://github.com/pbakaus/impeccable) · [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) · [Agent Skills](https://agentskills.io/specification).