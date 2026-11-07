# 24 — Design Glossary, Decision Records and Maintenance Rules

## Purpose
Design work often fails when team members use the same word for different concepts. This glossary clarifies technical and strategic terms, distinguishes evidence from taste, and standardizes change records. Definitions are working design language, not substitute for referenced standards.

## Strategic brand terms
- **Brand:** the set of associations and expectations people form through repeated interactions with a business, creator, product or organization.
- **Brand strategy:** decisions about audience, positioning, promise, competitive context, architecture and recognition.
- **Positioning:** the focused reason to choose a brand within a relevant category/context.
- **Differentiation:** a useful perceived reason one offer differs from alternatives.
- **Distinctiveness:** cues that make a brand easy to recognize and correctly identify.
- **Distinctive brand asset:** recurring non-name cue such as color combination, sound, mark, shape or typographic signature linked to the brand.
- **Brand salience:** brand's availability in memory at relevant choice occasions; not simply social visibility.
- **Category entry point:** a situation or need that may prompt someone to think of a product category.
- **Brand architecture:** organization of parent, sub-brand, endorsed or separate product identities.
- **Brand voice:** consistent character expressed through word choice, syntax, rhythm and contextual tone.
- **Art direction:** intentional rules for imagery, illustration, perspective, crop, lighting and visual narrative.
- **Style guide:** rules and examples for consistent expression.
- **Brand manual:** broader documentation of positioning, identity standards, usage, touchpoints and governance.

## Logo and typography terms
- **Logo:** a primary identifying mark, which can be typographic, symbolic or combined.
- **Logotype/wordmark:** brand name represented as stylized lettering.
- **Monogram:** mark built from initials or overlapping letters.
- **Lockup:** defined relationship between mark, wordmark and optional descriptor/endorser.
- **Responsive logo:** a controlled family of variants adapted to scale/context.
- **Clear space / exclusion zone:** minimum area kept free around a logo.
- **Minimum size:** smallest production size preserving intended identification.
- **Master artwork:** authoritative editable source, not a flattened preview.
- **Optical kerning:** manually adjusted letter spacing based on perceived rather than mathematical equality.
- **X-height:** height of lowercase x in a typeface, one factor affecting perceived size.
- **Cap height:** height of typical uppercase letters, often used for alignment or clear-space measures.
- **Leading/line height:** vertical distance between text baselines.
- **Measure:** width or approximate character count of a line of text.
- **Tabular numerals:** numerals with consistent width for aligned numeric columns.
- **Typeface family:** related set of font styles, weights and widths; not a generic appearance label.

## Layout and component terms
- **Grid:** structure controlling columns, margins, gutters and alignment.
- **Baseline rhythm:** repeated vertical alignment system based on text and spacing.
- **Spacing token:** named reusable gap/inset specification.
- **Semantic token:** a design value named by its role, e.g. text-warning or surface-raised.
- **Reference token:** underlying raw colour/size/value, which semantic tokens may reference.
- **Component:** reusable UI element with appearance, state and interaction contract.
- **Design system:** governed rules, foundations, patterns, components and testing practices.
- **Design debt:** inconsistent or unsupported patterns that increase maintenance and user friction.
- **Progressive disclosure:** reveal advanced detail when relevant without hiding critical actions.
- **Information architecture:** organization, labeling and navigation structure.
- **Affordance:** clue about what an element can do.
- **Visual hierarchy:** arrangement that guides attention according to meaning and tasks.
- **Information density:** amount of meaningful usable information within available space.
- **Responsive design:** layout and behaviour adapting to environment, width and input method.
- **Adaptive design:** context-specific presentation/behaviour beyond simple proportional resizing.
- **State:** current condition of a component or system (loading, active, selected, disabled, error, offline).
- **Microcopy:** short functional writing for labels, instructions, errors and feedback.

## Research and testing terms
- **Normative standard:** published formal requirement with defined conformance terms.
- **Heuristic:** practical guideline useful for critique, not a universal law.
- **Hypothesis:** testable design proposition.
- **Qualitative research:** observed behaviour, interviews, context and explanatory themes.
- **Quantitative measure:** counted outcomes, e.g. errors, time, attribution or conversion.
- **Attribution test:** whether users connect an asset with the correct brand.
- **Preference test:** whether people like one alternative; does not prove task efficacy.
- **Usability test:** observation of representative users attempting realistic tasks.
- **Aesthetic-usability effect:** tendency to perceive visually appealing interfaces as easier, potentially hiding actual friction.
- **Visual regression:** comparing rendered output against an approved baseline to find unintended changes.
- **Accessibility audit:** testing relevant requirements, assistive technology and interaction needs.
- **Acceptance criteria:** explicit conditions required before work can be considered finished.
- **Production proof:** print/manufacturing sample used to verify real physical output.
- **Source-of-truth:** authoritative current document, repository, asset or approved decision.

## Digital product terms
- **Chart timeframe:** interval used to display price bars.
- **Signal timeframe:** interval used by a signal engine to make its decision; may differ from chart timeframe.
- **Reference entry:** analysed price level, not guaranteed executable broker fill.
- **Stale data:** last available source state is old relative to the expected update period.
- **Cached data:** previously saved source; may be useful but is not automatically live.
- **Look-ahead bias:** analysis/backtests using future information unavailable at decision time.
- **Risk/reward R:** measured return relative to defined risk, requiring assumptions about fills, stops and fees.
- **Reduced motion:** accessibility setting that requests less animation.
- **Focus order:** sequence of keyboard/assistive navigation through controls.
- **Responsive identity:** brand-system variations for different media while preserving recognition.

## Design Decision Record (DDR)
Every substantial project design choice should be traceable:
```markdown
# DDR-0001: [Decision title]
Date: YYYY-MM-DD
Project and source of truth:
Status: proposed / approved / rejected / superseded
Problem to solve:
Current user requirement and canonical constraints:
Research sources reviewed (links and dates):
Alternatives considered:
Decision:
Why this is appropriate:
Brand distinctiveness:
Accessibility / technical / print implications:
Measured or observed evidence:
Testing conducted:
Known limitations:
Artifact files / commits:
Owner and approval:
```

A new design direction does not become canonical just because an assistant writes it into a speculative case study. A decision becomes active only when approved or explicitly part of the user's current request and properly implemented.

## Change and maintenance procedure
1. Identify the affected chapter and current project.
2. Verify the underlying new evidence, guidance or user feedback.
3. Record which previous rule has changed and why.
4. Add updated references with dates and appropriate licence context.
5. Update associated templates/examples and the chapter index if relevant.
6. Mark older brand decisions historical/superseded rather than silently deleting them.
7. Run any automated link checks and manual review possible.
8. Commit all changes to Mandla Brain with a descriptive message.
9. If another system syncs from this repository, verify that sync separately; a GitHub commit alone does not guarantee remote indexing has already occurred.

## Rule precedence and availability
Current explicit user instruction > applicable safety/accessibility/legal constraints > canonical project brand decisions > verified working artifacts > cross-project handbook > external design systems > current fashion. The handbook's standing requirement to consult relevant chapters is recorded in [AI_INSTRUCTIONS.md](../AI_INSTRUCTIONS.md), [START_HERE.md](../START_HERE.md), and [memory/preferences.jsonl](../memory/preferences.jsonl). It is a **cross-model repository rule** and does not itself claim to alter ChatGPT's account-level Memory settings.

## Library validation checklist
- All listed chapters exist and their links work.
- A source library exists with traceable primary references.
- Every significant claim says whether it is normative, supported, observed or hypothetical.
- No copyrighted third-party design assets or fonts have been copied into the public repository.
- The portable SKILL.md links to the correct full handbook.
- The mandatory reading rule is linked from existing AI handover documents.
- The structured memory JSONL remains valid with unique stable IDs.
- The chapter index distinguishes project-specific approved canon from illustrative hypotheses.
- The library is sufficiently detailed to act as a practical working manual, not just a set of slogans.

## Final instruction to future assistants
Read this library, but don't become trapped in theory. Understand the project, study credible references, produce a distinct solution, build it, inspect it, improve it, preserve it and tell the truth about what was verified. A successful design is not the longest manual; it is the best work informed by the manual.