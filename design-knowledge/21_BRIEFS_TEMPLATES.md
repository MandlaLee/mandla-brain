# 21 — Production-Ready Design Briefs, Research Templates and Review Checklists

These templates are meant to be **filled with verified content**, not pasted into finished brand presentations with invented answers. The templates help a solo designer, client collaborator, Claude, ChatGPT or Codex continue a project consistently. They scale: an app redesign might need all sections; a poster correction may need only brief, production and QA fields.

## Template A — Master creative brief

```text
PROJECT:
OFFICIAL BRAND/PRODUCT NAME (exact spelling):
LEGAL ENTITY, if relevant:
PROJECT OWNER / APPROVER:
DATE / VERSION:
WORKING REPO / SOURCE-OF-TRUTH:
TARGET USERS:
USER JOB TO BE DONE:
DESIRED OUTCOME:
CONTEXT (device, time, environment, language):
CURRENT PAIN / REASON TO DESIGN:
PROJECT CANON TO PRESERVE:
EXISTING BRAND ASSETS AND OWNERS:
ASSET RIGHTS / LICENCES:
CONSTRAINTS (OS, budget, print, bandwidth, font, delivery):
KNOWN COMPETITORS:
REAL REFERENCES WITH URL + DATE:
FORBIDDEN VISUAL CONCEPTS:
CONTENT INVENTORY AND MISSING CONTENT:
FIRST USER ACTION:
SUCCESS CRITERIA:
SAFETY / PRIVACY / ACCESSIBILITY:
REVIEWER / SIGNOFF:
UNKNOWN OR ASSUMED DETAILS (explicitly label):
```

Do not silently choose new official brand names. Do not reinterpret user-approved cultural details. Distinguish current product from historical repositories in Mandla Brain.

## Template B — Brand strategy brief

| Field | Required analysis |
|---|---|
| Audience context | Who is deciding and why now? |
| Category | What would the customer think this product is? |
| Alternative | What do they use if the brand does not exist? |
| Positioning | Benefit, category, proof and meaningful difference |
| Brand promise | Something operationally achievable |
| Distinctive assets | Mark, voice, typography, recurring shape, sound, photo grammar |
| Personality | Three concrete behavioural rules |
| Architecture | Parent/product/creator/co-brand hierarchy |
| Naming | Exact current name; legal/search/cultural concerns |
| Touchpoints | Web, app, social, print, video, signage, packaging |
| Recognition strategy | Which cues repeat across which contexts? |
| Constraints | Existing recognition, licence, vendor, budget |
| Rebrand risk | What equity could be lost? |
| Test | Comprehension, attribution, legibility and category fit |

## Template C — Reference product audit

```text
REFERENCE PRODUCT / REPOSITORY:
SOURCE LINK:
DATE REVIEWED:
PRIMARY USER TASK:
WHAT IT DOES WELL:
HOW THE INFORMATION IS ORGANIZED:
WHAT ITS VISUAL IDENTITY CONSISTS OF:
KEYBOARD, FOCUS, MOBILE, ACCESSIBILITY:
STATE COVERAGE:
REAL INTERACTION OBSERVED / CODE READ:
LIMITATIONS:
COPYRIGHT / TRADEMARK LIMITS:
PRINCIPLE TO ADAPT:
WHAT NOT TO COPY:
ORIGINAL IMPLEMENTATION IDEA:
TEST THAT WOULD REJECT OUR IDEA:
```

For repo research also record licence, maintained/archived, release status, token/component package locations, tested use and target framework.

## Template D — Distinctive direction comparison

Produce three substantial directions before approval when the identity is not already decided:
| Criterion | Direction A | Direction B | Direction C |
|---|---|---|---|
| Design thesis | | | |
| User/task hierarchy | | | |
| Logo/mark approach | | | |
| Typography role | | | |
| Colour ratio/meaning | | | |
| Spatial grammar | | | |
| Imagery/illustration | | | |
| Motion/voice | | | |
| Accessibility trade-off | | | |
| Production feasibility | | | |
| Competitive confusion risk | | | |
| Evidence vs hypothesis | | | |
| Project canon preserved? | | | |
| Test scenario | | | |

Avoid three versions of the same rounded-card arrangement. Visual routes should be structurally distinct.

## Template E — Complete visual identity handoff

Include final approved:
1. Brand positioning, audience and evidence.
2. Official names and naming/voice policy.
3. Primary and secondary logo lockups; icon-only where appropriate.
4. One-colour, reverse, small and print variants.
5. Clear space and minimum sizes *measured*.
6. Colour palette with HEX/sRGB and print equivalents when applicable.
7. Typography roles with font names, weight, size, leading and licence.
8. Layout grid, spacing rhythm, safe zones and alignment.
9. Icon/illustration style and file sources.
10. Photography direction with consent and crop rules.
11. Motion, lower thirds, captions or sound if relevant.
12. Brand voice with examples for marketing, error and help.
13. Website/app/social/print/merchandise examples.
14. Co-branding rules and legal mark usage.
15. Forbidden uses with specific examples.
16. Component tokens (if a digital product).
17. Accessibility guidance and approved contrast pairs.
18. Editable master assets and exports.
19. Governance: owner, version, exceptions and archive.
20. Tests: scale, audience, production and rights.

## Template F — Screen-by-screen UX specification

```text
SCREEN / ROUTE:
USER TASK:
ARRIVAL STATE:
PRIMARY VISUAL OBJECT:
NAVIGATION CONTEXT:
AVAILABLE ACTIONS:
HIGH FREQUENCY ACTIONS:
SECONDARY ACTIONS:
DATA SOURCES:
AUTHORITY / TIMESTAMP:
COMPONENTS:
TYPE AND COLOR ROLES:
KEYBOARD AND FOCUS BEHAVIOUR:
EMPTY / LOADING / ERROR / OFFLINE / STALE:
MINIMUM WINDOW / PHONE SIZE:
LONG CONTENT / TRANSLATION:
RISKS AND FALSE CONFIDENCE:
ACCESSIBILITY TESTS:
VISUAL QA SCREENSHOTS:
FUNCTIONAL ACCEPTANCE TEST:
OWNERSHIP / VERSION:
```

## Template G — Logo acceptance checklist

```text
[ ] Exact official name correct
[ ] Distinctive against category competitors
[ ] Readable and recognizable at smallest needed size
[ ] Black/white and grayscale versions tested
[ ] Reverse/light/dark verified
[ ] No confusing resemblance to existing protected marks
[ ] Correct symbol/wordmark proportions
[ ] Clear-space and minimum-size specifications measured
[ ] Print/embroidery limitations tested
[ ] Cultural/linguistic meanings reviewed
[ ] Vector master preserved
[ ] Transparent raster masters exported correctly
[ ] Font and asset rights verified
[ ] Co-branding and app/social variants prepared
[ ] Source and revision documented
[ ] Client/user signoff or unresolved status explicit
```

## Template H — UI review scorecard

Evaluate against [Chapter 19](19_CRITIQUE_QA.md). Assign 0–4 with written evidence for task clarity, brand specificity, typography, hierarchy, accessibility, state truth, responsive layout, production integrity, functional reliability and handoff. Critical safety failures fail irrespective of visual average. Record screenshots, failed scenarios, fixes and retests.

## Template I — Visual bug ticket

```text
ID:
SEVERITY: blocker / major / minor / cosmetic
AFFECTED COMPONENT:
CURRENT BUILD / OS / DEVICE:
REPRO STEPS:
EXPECTED:
ACTUAL:
SCREENSHOT / VIDEO / LOG:
CAUSE (confirmed / suspected):
ROOT RULE VIOLATED:
FIX:
REGRESSION TEST:
STATE: new / investigating / fixed / verified / deferred
VERIFIED COMMIT:
```

## Template J — Trading signal UI acceptance

```text
[ ] Market/symbol, quote unit and source displayed
[ ] Chart timeframe and signal timeframe distinct
[ ] Candle-open vs candle-confirmed timestamps clear
[ ] Signal marker projected to correct execution timestamp
[ ] BUY/SELL reference entry not mistaken for broker fill
[ ] Stop direction is valid for signal
[ ] Target direction and R:R calculation valid
[ ] Data freshness, offline/demo/historical labeled
[ ] No fresh alert from stale candles
[ ] No repeated duplicate notifications
[ ] Historical signals computed without looking ahead
[ ] Unsupported interval/provider errors recoverable
[ ] Panel minimized/expanded at target width
[ ] Backtest assumes spread, fees and OHLC limitations
[ ] No automatic execution without explicit feature authorization
```

## Template K — Print/vendor specification

Project, substrate, dimensions, bleed/safe area, colour process/spot limit, profile, artwork vector/raster types, minimum stroke, fonts/outline, quantity, packaging die, physical sample, vendor approval, approved proof reference, legal labels, costs and production version. Keep supplier assumptions separate from confirmed specifications.

## Template L — Design decision record

```markdown
# DDR-0001 — Short decision name
Date:
Status: proposed / accepted / superseded
Related project and source repo:
Problem and user task:
Existing canonical identity:
References and evidence level:
Options:
Decision and rationale:
Rejected alternatives and why:
Design tokens/components affected:
Accessibility/production concerns:
Validation tasks and results:
Rollback or future revision plan:
Owner and files:
```

## Template M — Final delivery verification

Before declaring a design task complete:
- Did we inspect the real target artifact?
- Are the official brand spelling and approved direction preserved?
- Did the design differ from interchangeable templates?
- Are high-impact tasks and states tested?
- Was the actual code/build/export rendered and inspected?
- Are required variants/exports present?
- Are claims and data truthful?
- Is the repository/version/path recorded?
- Are licence/cultural concerns addressed?
- Is the user able to open/download the final artifact?
- Are unresolved defects and caveats stated?

## Automated-agent handover
When one model continues another's work, read the source-of-truth repo, latest Design Decision Record, current artifact location, screenshots and unresolved issues. Don't treat a prior assistant's success claim as verification. The Design Director Charter and chapter index should be loaded in every substantial visual workflow.

## Sources
[NN/g usability heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/), [W3C WCAG](https://www.w3.org/TR/WCAG22/), [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/), [GitHub Primer](https://primer.style/product/).