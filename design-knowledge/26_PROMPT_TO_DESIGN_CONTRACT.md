# 26 — From Plain-English Vibe Prompt to Precise Design Contract

## The missing bridge
A vibe-coding agent is excellent at filling blanks, but those blanks can be dangerous: inventing the brand, improvising an architecture, changing application business rules or hallucinating test success. The job of the Design Director is to **make important blanks explicit while leaving purposeful creative freedom**.

## Context files in the working project
A substantial app or website should use two concise local documents, inspired by [Impeccable's PRODUCT.md and DESIGN.md approach](https://github.com/pbakaus/impeccable):
- `PRODUCT.md`: what the app genuinely is, audience, core tasks, data/logic invariants, supported hardware, non-goals, state inventory, key user vocabulary.
- `DESIGN.md`: current approved visual identity, typography, semantic colour, grid, component rules, image direction, responsive layout, examples, prohibited motifs, screenshot baselines and design decision history.

They belong in the **working product repo**, not automatically in the cross-project Mandla Brain repository. Avoid overwriting similarly named existing project files without inspecting them. The design contract makes the current creative direction inspectable, not immutable.

### Minimal `PRODUCT.md` example
```markdown
# Product — example only
App: Aurum, native macOS trading assistant
Core job: inspect price action and reference BUY/SELL/WAIT signals
Not a broker: no automatic order execution
Audience: discretionary trader using MacBook at ~1120px window width
Reality constraints: Intel, 4GB RAM, older macOS; feed freshness matters
Invariants: trading strategy calculations, signal timestamps, risk math,
source/provider distinction and original project canon may not drift
Primary scenarios: live chart, historical review, delayed feed, offline cache,
rapid timeframe switching, minimized inspector
Success: clear signal reasoning and accurate entry/SL/TP position
```

### Minimal `DESIGN.md` example
```markdown
# Design — example hypothesis, not approved redesign
Identity canon: inspect approved Aurum assets before changing marks
Thesis: calibrated instrument, chart-first, low visual noise
Hierarchy: source/time → chart → signal/diagnostics → contextual history
Type: system UI for labels; tabular numbers for price/stop/targets
Panels: independently collapsible and persist state
Warnings: not colour alone; show timestamp and recoverable status
Forbidden: giant summary cards crowding chart, fake live badges,
unrelated glow or gradients, generic candle clipart
Visual proofs: screenshots at min/default/max width and each panel state
```

## A five-part design prompt
Use this structure in Claude/Codex/ChatGPT when requesting a real implementation:
1. **Context:** official repo/app, canonical decisions and screenshots. “Read AI_INSTRUCTIONS.md and design-knowledge relevant chapters.”
2. **Goal:** one primary user outcome stated in human terms.
3. **Constraints/invariants:** data model, endpoints, permission, device, accessibility, brand canon and what **must not change**.
4. **Creative freedom:** which visual dimensions may change, references and expected distinctiveness.
5. **Proof/delivery:** screenshots, tests, source commit, production rollback and what must be demonstrated.

An agent should produce a *short plan* before writing hundreds of lines: key screens, data/interaction states, tokens, spatial thesis and two or three known risks. The plan itself should be reviewed against generic-template failure patterns and approved brand constraints.

## The “one risky change at a time” rule
Separate changes into:
- **Content/copy** (labels, descriptions, verified business details).
- **Presentation** (tokens, spacing, typography, images).
- **Interaction** (navigation, panels, keyboard, focus).
- **Business logic** (trading rules, checkout, permissions).
A visual change should ideally avoid rewriting business logic. If a cross-layer change is necessary, explicitly scope and test it. Never combine a total redesign, a data-source migration and a new signal algorithm in one unreviewed commit.

## Vertical slices
Before implementing an entire site, build one complete flow with real data and states: e.g. homepage → service detail → enquiry → confirmation, or chart → select history marker → inspect trade → return to live. A slice must include backend integration where necessary, not only visuals. Test it before multiplying pages. Source: [Anthropic coding iteration guidance](https://www.anthropic.com/engineering/claude-code-best-practices).

## Component acceptance contract
For each important component record:
```text
NAME:
WHY IT EXISTS:
INPUTS AND TYPES:
VISIBLE CONTENT:
ACTION / EXPECTED RESULT:
DEFAULT / HOVER / FOCUS / DISABLED / LOADING / ERROR:
RESPONSIVE AND OVERFLOW:
KEYBOARD / SCREEN READER:
REALISTIC DATA FIXTURES:
PERFORMANCE BUDGET:
SPECIFIC TEST:
APPROVED BRAND TOKENS:
```

Example: A “Trade inspector” receives a selected signal and data freshness, displays entry/stop/targets, differentiates confirmed history from current watch, can collapse without losing selected signal, and must not display a live-trading CTA when feed is stale.

## Intentional design direction
Complete before coding:
- **Visual thesis:** one sentence describing why the interface belongs to the brand.
- **Two contrasting references:** one for interaction, one for brand expressiveness; state which details **not** to copy.
- **Anti-reference:** a template aesthetic to avoid and why.
- **Signature element:** one recognisable but task-compatible visual feature.
- **Tokens:** named typography, surfaces, accents, spacing and radius principles.
- **Layout model:** low-fidelity ASCII of main components at exact target width.
- **Proof:** a screenshot, user task or test that could show the concept failed.

## Prompt packs
### A — Start a new branded frontend
```text
Read Mandla Brain's design-director charter and task chapters, then inspect
this repo, assets, current brand canon, and content.
Build an original visual identity and working frontend for [product].
Audience: [actual job]. Primary action: [specific task].
Keep [unchangeable architecture/flows]. Do not invent testimonials or contacts.
Propose three structurally distinct directions; choose one with a rationale.
Write PRODUCT.md and DESIGN.md (do not overwrite existing files).
Implement one complete vertical slice with semantic components and tokens.
Show real desktop+mobile screenshots, error/empty states, accessible focus,
click-through results, and list exactly which tests ran.
Commit only the files required; preserve a rollback point.
```

### B — Redesign existing UI that “looks AI”
```text
Inspect the running application and capture a baseline at actual device size.
Do not change business logic, APIs, strategy calculations or existing brand name.
Audit repeated cards, hierarchy, type scale, density, empty states and brand cues.
Document three top root causes and one coherent design thesis.
Redesign the primary task surface first; reuse current product components where
safe. Capture before/after screenshots at default and minimum size.
Test keyboard, data freshness, navigation and long content.
Give exact changed files and functional regression results.
```

### C — Polish a single component
```text
Only edit [component + related tokens/tests]. Keep existing API and behaviour.
Reproduce a specific visual defect. Inspect current screenshot/DOM.
Fix hierarchy, spacing, optical alignment, focus and overflow.
Show evidence from one screenshot and an interaction test.
Do not restyle unrelated screens or add new dependencies without justification.
```

### D — Design a logo from a brand brief
```text
Read approved brand strategy/canon and logo engineering chapter.
Study competitors, avoid protected similarity and use exact approved name.
Create three fundamentally different concept constructions.
Test black/white, reverse, 16px, one-colour, mobile avatar, print and sign.
Provide source/editable vector and transparent exports, clear-space and use guide.
Don't claim legal trademark clearance from a visual similarity search.
```

### E — Web audit and hardening
```text
Use an isolated dev server and current browser renderer.
Capture baseline screenshots at [defined viewports] and log console errors.
Test forms, CTA routes, empty/slow/failed network, 200% zoom,
keyboard focus, color contrast and reduced motion.
Return file:line defects with severity and concrete reproduction evidence.
Fix blockers first, rerun, and attach before/after screenshots.
Do not report untested flows as passing.
```

## AI-specific failure modes
- **Confident invention:** agent says “all fixed” without opening the app.
- **Stale context:** agent applies an outdated project name or UI screenshot.
- **Library style leakage:** agent copies an example component as if it defines brand character.
- **Aesthetic homogenization:** three alternatives vary only palette.
- **Overwriting:** agent replaces entire codebase while solving one layout issue.
- **False task completion:** link/button visually works but destination/action fails.
- **Unbounded polishing:** repeated visual tweaks introduce regressions.
- **Hidden dependencies:** adding large animation/browser runtimes to low-RAM apps.
- **Permission overreach:** running commands not required for design, editing unrelated files or accessing secrets.

## Human approval without needless friction
Proceed autonomously on reversible, in-scope design implementation using existing user instructions and backups. Ask for a decision when it materially changes brand canon, pricing/claims, legal usage, production deployment or destructive actions. Show the concrete trade-off rather than long generic questionnaires.

## Design decision record
A one-paragraph summary after each iteration: what changed, problem it solved, reference/evidence, screenshot/test result, risk, next targeted revision and saved commit. Future assistants must be able to identify the current accepted design without guessing from old images.

## Sources
[Anthropic frontend skill](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md) · [Impeccable](https://github.com/pbakaus/impeccable) · [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/) · [Mandla Brain QA](19_CRITIQUE_QA.md).