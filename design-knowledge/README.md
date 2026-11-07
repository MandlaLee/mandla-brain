# Mandla Brain — Design & Brand Knowledge Base
**Version 1.1 · 2026-11-07 · Cross-project · Living reference**

This is the model-independent foundation for visual identity, logo design, branding psychology, desktop apps, websites, mobile UX, games, typography, posters, art direction, packaging, merchandising and quality assurance. It is intentionally a multi-chapter manual, not a one-page inspiration checklist. It describes practical procedures, evidence levels, rejection criteria, source links and production handoffs.

## Non-negotiable reading order
1. Read [00 — Design Director Charter](00_DESIGN_DIRECTOR_CHARTER.md).
2. Examine the actual project and canonical identity in Mandla Brain. Current user instructions and active brand canon outrank generic references.
3. Read [01 — Research](01_RESEARCH_DISCOVERY.md), followed by the chapters relevant to the task.
4. For logos and branding, read 02–07, 15–19 and 26, 29. For native apps, read 08–10, 13–14, 18–22 and 25–30. For websites, read 08–09, 11–14, 18–21 and 25–30. For games, read 08–10, 12–15, 17–19 and 25–27. For AI-led visual implementation **always** read 25–30, especially the safety and rendered-test chapters.
5. Study real references, build original alternatives, implement, inspect at actual size, fix issues and preserve verified files.
6. When revising a design, use the same rules instead of silently choosing a new style.

## The complete library
| Chapter | Subject | Purpose |
|---|---|---|
| [00](00_DESIGN_DIRECTOR_CHARTER.md) | Design director charter | Standing instruction, quality gates, hierarchy |
| [01](01_RESEARCH_DISCOVERY.md) | Research and discovery | Audience, benchmarks, design hypotheses |
| [02](02_BRAND_STRATEGY_POSITIONING.md) | Brand strategy | Positioning, audiences, architecture, messaging |
| [03](03_BRAND_PSYCHOLOGY_EVIDENCE.md) | Brand psychology | Mental availability, perception, evidence and myths |
| [04](04_LOGO_DESIGN_ENGINEERING.md) | Logo engineering | Concepts, geometry, variants and testing |
| [05](05_BRAND_IDENTITY_SYSTEMS.md) | Brand identity systems | Voice, visuals, recognition assets, co-branding |
| [06](06_TYPOGRAPHY_EDITORIAL.md) | Typography | Font choice, hierarchy, metrics, readable systems |
| [07](07_COLOUR_CONTRAST.md) | Colour and perception | Accessibility, semantics, colour systems |
| [08](08_LAYOUT_COMPOSITION.md) | Layout and composition | Grids, balance, alignment, density |
| [09](09_UX_INFORMATION_ARCHITECTURE.md) | UX and information architecture | Navigation, task flows, forms, errors |
| [10](10_NATIVE_DESKTOP_APPS.md) | Native desktop apps | macOS, keyboard interaction, trading workspace |
| [11](11_WEB_EDITORIAL_CONVERSION.md) | Websites | Content, credibility, SEO, conversion |
| [12](12_MOBILE_RESPONSIVE.md) | Mobile and responsive | Smaller screens, touch, network realities |
| [13](13_DESIGN_SYSTEM_TOKENS.md) | Design systems | Token architecture, components, governance |
| [14](14_INTERACTION_MOTION_MICROCOPY.md) | Interaction and motion | Transitions, feedback, wording, states |
| [15](15_IMAGERY_ILLUSTRATION_ICONS.md) | Art direction | Photography, illustration, symbols, asset rights |
| [16](16_PRINT_MERCH_PACKAGING.md) | Production | Print, apparel, packaging, vendor proofs |
| [17](17_CULTURAL_CONTEXT_SOUTH_AFRICA.md) | Cultural context | Xitsonga, Limpopo, township context, ethical representation |
| [18](18_TESTING_METRICS.md) | Research testing | Task success, attribution, validation |
| [19](19_CRITIQUE_QA.md) | Critique and QA | Visual defect taxonomy and acceptance gates |
| [20](20_GITHUB_REPO_STUDY.md) | GitHub studies | Original analysis of authoritative repos |
| [21](21_BRIEFS_TEMPLATES.md) | Working templates | Ready-to-fill briefs, audits, decisions |
| [22](22_APPLIED_CASE_STUDIES.md) | Applied cases | Aurum, Phala Digital, FENRY and other contexts |
| [23](23_SOURCE_LIBRARY.md) | Sources | Links, attribution, confidence, licensing |
| [24](24_GLOSSARY_DECISIONS.md) | Glossary | Meaningful shared design terminology |
| [25](25_AGENT_SKILLS_VIBE_CODING.md) | Claude, Codex and ChatGPT design skills | Primary-source comparison and vibe-coding workflow |
| [26](26_PROMPT_TO_DESIGN_CONTRACT.md) | Prompt-to-design contract | Useful design prompts, real constraints, clear working files |
| [27](27_RENDERED_BROWSER_DESKTOP_REVIEW.md) | Browser and desktop visual testing | Screenshot, interaction and regression methodology |
| [28](28_UI_ENGINEERING_IMPLEMENTATION.md) | Implementation cookbook | Semantic code, tokens, state models and performance |
| [29](29_AGENT_SKILL_INSTALL_SECURITY.md) | Skill discovery and safety | Agent paths, safe installation and third-party script risks |
| [30](30_DESIGN_AGENT_EVALUATIONS.md) | Design agent evaluations | Comparison fixtures, rubric, scorecard and failure tests |

**Skill entry:** [skills/design-director/SKILL.md](../skills/design-director/SKILL.md). This lightweight SKILL.md directs compatible assistants to this full library, rather than duplicating it.

## AI-assisted design: the release workflow

For a vibe-coded frontend, do **not** stop at code generation. Follow [skill research (25)](25_AGENT_SKILLS_VIBE_CODING.md) → [prompt contract (26)](26_PROMPT_TO_DESIGN_CONTRACT.md) → [implementation (28)](28_UI_ENGINEERING_IMPLEMENTATION.md) → [rendered UI test (27)](27_RENDERED_BROWSER_DESKTOP_REVIEW.md) → [quality audit (19)](19_CRITIQUE_QA.md) → [agent evaluations (30)](30_DESIGN_AGENT_EVALUATIONS.md). Check [skill security (29)](29_AGENT_SKILL_INSTALL_SECURITY.md) before installing anything external. Record screenshots and verified outcomes.

**Discovered skill entrypoints:** [canonical SKILL.md](../skills/design-director/SKILL.md), [Claude Code wrapper](../.claude/skills/design-director/SKILL.md), [Codex wrapper](../.agents/skills/design-director/SKILL.md). The wrappers do not install the skill in the user's account or in unrelated repositories; they make the instruction discoverable **when the agent is running inside Mandla Brain**. An independent working project should deliberately link or install the canonical skill.

**Validation:** `python3 scripts/validate_design_knowledge.py` from repository root checks local chapter references, skill metadata and structured memory JSONL. It does not audit remote link availability or the visual quality of actual projects.

## What makes a reference credible?
A normative platform/standard (W3C, Apple) has different authority from a GitHub implementation (observed engineering choices), a peer-reviewed review (research), a trained practitioner's guide (heuristic) and a screenshot gallery (inspiration only). The evidence classification appears in the charter. Link every factual claim to a credible source; distinguish opinion and artistic judgement.

## Design is not one visual template
A financial trading app should prioritize accurate data states, task focus and fast comparison. An artist visual identity should build a memorable creative language and recognizability. A church website may need warmth, inclusive navigation and truthful content. A small construction company site needs actual service details and trustworthy contact paths. A clothing label requires industrial print constraints. Applying the same dashboard cards and gradient everywhere violates the purpose of this library.

## Copyright and brand rights
Study public examples for patterns and principles, not by copying protected marks, photos, proprietary icon libraries or marketing text. Check code licenses and font rights. Cite contributors where ideas are used. No third-party font files should be committed here.

## Maintenance
Update sources when design systems change, clearly date decisions, retain rationale and mark obsolete guidance. A guide is useful only if future assistants can navigate it, reproduce its processes and verify real output. This repository is public; do not commit credentials or confidential client material.

*Research foundation: [Apple macOS HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-macos), [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [Nielsen Norman Group](https://www.nngroup.com/articles/ten-usability-heuristics/), [Primer](https://primer.style/product/), [Carbon](https://carbondesignsystem.com/), [NASA Brand Center](https://www.nasa.gov/nasa-brand-center/brand-guidelines/).*