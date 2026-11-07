# 19 — Design Critique, Red-Team Review and Final Quality Gate

## Critical principle
The user saying “looks like AI” is feedback on specificity, craft and coherence; it cannot be resolved reliably by adding visual effects. Conduct a structured audit of the actual screen, not a speculative restyle. Critique must be concrete and actionable.

## Ten categories of visual and product defects
1. **Identity sameness:** could an unrelated business replace the wordmark and own this screen?
2. **Weak hierarchy:** everything competes; crucial information lacks prominence.
3. **Overcomponentization:** cards within cards, rounded corners everywhere, no unifying space rhythm.
4. **Typography failure:** unreadable small labels, inconsistent weights, poor number alignment, random headline sizes.
5. **Colour failure:** insufficient contrast, arbitrary accents, semantic contradiction, red/green-only meaning.
6. **Composition failure:** awkward empty areas, repeated grid monotony, broken baseline, crowded controls.
7. **Content failure:** placeholders, fake testimonials, vague copy, incorrect names or data.
8. **Interaction failure:** non-working buttons, hidden focus, confusing navigation, inaccessible compact icons.
9. **State failure:** delayed prices labelled live, wrong progress, “success” without server confirmation, stale caches.
10. **Production failure:** wrong export size, illegible logo, unlicensed assets, app only compiles but isn't installed.

A product can be technically bug-free yet fail identity. Conversely, a beautiful brand board may fail real manufacturing.

## The cold-read assessment
Give a screenshot to someone unfamiliar with the product and ask:
- What is this?
- Who is it for?
- What can you do on this screen?
- Which information is most important?
- Is the system live, waiting, complete or unavailable?
- Where would you click next?
Don't explain first. Record misinterpretations. This tests communication, not general aesthetic preference.

## The no-logo identity test
Mask logo, product name and famous photography. Are the typography, composition, shape, motion, voice, recurring layout, category-specific structures and details distinct enough? This is a creative diagnostic, **not** scientific proof of brand recall. If all cues are generic, revise the identity rather than enlarging the logo.

## Density audit
Compute roughly how much of the primary viewport is used for the core task versus chrome or decoration; compare with task demands. A chart user needs a large graph; a photographer needs image/canvas area; an applicant needs forms and application progress. Remove redundant summary boxes that repeat status already shown. Secondary panels should be collapsible if they reduce the main work unnecessarily.

## Visual-polish inspection
At 100% real screen size inspect:
- outer and inner margins;
- alignment along baselines and common edges;
- text clipping and wrap;
- icon optical centering;
- line-height, tracking and data precision;
- floating tool overlap;
- chart axes, dates and indicator collision;
- inconsistent radius and border weight;
- shadows and elevated surface boundaries;
- button states;
- empty/loading/historical vs live appearance;
- multi-language labels and longest words;
- image crop, facial accuracy and skin-tone lighting;
- mobile menus and bottom bars;
- print margins and thin strokes.

A one-pixel error is not equally serious everywhere; prioritize high-frequency/central elements, safety and visible inconsistencies.

## Rubric with actionable scoring
Rate 0–4 per criterion, recording evidence rather than aesthetic preference:
| Criterion | 0 | 2 | 4 |
|---|---|---|---|
| Task clarity | Core task unclear | Task possible but visually buried | Primary action instantly evident |
| Brand specificity | Interchangeable template | Some signature cues | Cohesive and distinctive identity |
| Typography | Illegible/inconsistent | Functional with defects | Strong hierarchy and precise typesetting |
| Information architecture | Lost/navigation broken | Understandable with friction | Predictable, efficient, accessible |
| Accessibility | Blocking issues | Partial checks / some deficiencies | Verified against target criteria |
| State truth | Misleading status | Some ambiguity | States and provenance explicit |
| Responsive/workspace | Broken at common size | Acceptable with cramped areas | Adaptive and efficient |
| Production quality | Unusable output | Usable with avoidable defects | Editable, reproducible, fit for medium |
| Functional reliability | Major defects | Minor reproducible defects | Targeted regression passes |
| Handoff | Unverifiable | Files exist with gaps | Source, rights, tests and version preserved |

This is a *team review heuristic*, not a validated universal quality score. For high-stakes interfaces, certain criteria (state truth, functional correctness, accessibility) are pass/fail gates regardless of total score.

## Screenshot red-team procedure
1. Capture current real artifact (not assistant reconstruction).
2. Strip away emotional attachment; annotate concrete issues.
3. Compare at least three relevant real references.
4. Identify which failures are structural versus cosmetic.
5. Draft changed information architecture/visual thesis.
6. Fix highest-impact structural issues first.
7. Implement with tokens and component consistency.
8. Capture fresh screenshot and compare against previous.
9. Test compact and expanded layouts and alternate states.
10. Record remaining issues and reason.

## User experience red team
- Start in a no-data state.
- Disable network.
- Switch modes/timeframes rapidly.
- Enter invalid data.
- Resize the window below usual width.
- Use keyboard and screen-reader navigation.
- Increase text size or zoom.
- Attempt to recover from a failed submit.
- Interact while loading.
- Navigate backward and return; check preserved state.
- Close and reopen; check settings and source status.
- Use a feature with a very long label or unusual locale.

## Branding red team
- Show logo at 16px.
- Convert to mono/greyscale.
- Print on rough stock.
- Add alongside 5 partner marks.
- Compare blind among competitors.
- Remove name from icon and observe attribution.
- Test pronunciation and cultural implications.
- Ensure no protected imagery is reused.
- Verify export transparent alpha and vector masters.
- Test on actual phone cover/profile/photo thumbnail, not just a hero mockup.

## Definition of completion
A project is not complete when:
- the design is only described;
- mockup looks polished but code unchanged;
- images are generated but not integrated;
- code builds but app never launches;
- source files exist but aren't committed/preserved;
- user cannot access/download files;
- only default state was tested;
- source data is outdated/misleading;
- logos have no original editable master;
- known critical issues are dismissed as “fine.”
Completion requires an inspectable saved artifact, clear tested scope and honest limitations.

## Source library
[NN/g usability heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/), [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [W3C accessibility evaluation](https://www.w3.org/WAI/test-evaluate/), [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/), [Primer accessibility](https://primer.style/product/), [Carbon](https://carbondesignsystem.com/).

## Final question
If Mandla sees the result at actual size, will it feel like a purposeful, finished, authentic product built for his world—or a familiar AI template wearing a new colour? If the honest answer is the latter, revise before calling it final.