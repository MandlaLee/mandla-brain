# 01 — Design Research, Discovery and Competitive Study

## Why research begins before the mood board
A reference screenshot is not a brief. The research question is not merely “what looks good?” but “what must this specific person accomplish, under which conditions, with which existing expectations and constraints?” Strong teams study task flow, content, failure states, perception, brand associations and technical reality together. For a complex interface, first sketch its information architecture in plain language; styling follows a clear model.

## Research brief — required fields
Document: project and exact approved name; audience and language; primary task; current alternative; why the task matters; real workflows and pain points; expected frequency; time pressure; trust and safety risks; devices and minimum specs; content/data sources; company or creator canon; visual assets and rights; current production/staging files; budgets; accessibility; evidence quality; success metrics; research gaps.

If information is genuinely unavailable, write “working assumption” next to it. A designer who makes plausible guesses without labelling them creates fictional research.

## User interview protocol
Ask about specific recent events, not hypothetical preferences. “Walk me through your last job application” reveals actions; “would you use an attractive job app?” invites agreement. Start with context, ask what happened, investigate points where tools were changed, where information was copied, what caused doubt, and what success actually meant. Avoid steering toward a feature you already want to build. Ask consent before recording; anonymise research notes, particularly in a public repository. Observe task actions when possible because reported preferences may not match actual behaviour.

Interview script:
1. “What were you trying to do?”
2. “What made you start?”
3. “Show me where you went first.”
4. “What did you expect that button/label to do?”
5. “What was difficult or uncertain?”
6. “What did you try when it failed?”
7. “How did you know it was finished?”
8. “What did you trust or distrust?”
9. “Would you do anything differently next time?”
10. “What is important that I have not asked?”

## Competitor and adjacent-product analysis
Study three categories: direct competitors, best-in-class adjacent tools, and a deliberately different visual approach. For each capture the source URL, date, product, target user, primary task, visual hierarchy, information density, navigation, gestures, keyboard behaviours, empty/loading/error states, design tokens if public, typography, icon grammar, copy style, accessibility, strengths, weaknesses and what **should not** transfer.

Create a comparison matrix with columns: Task | Real reference | Observed rule | Context | Transferable principle | Risk | Original design response | Test. Do not write only “inspired by TradingView.” A useful statement is “Trading interfaces keep price action continuously visible while tool panels adapt to workspace width; adopt an independently collapsible inspector, but retain a distinct Aurum identity.”

### Repository source examination
For open-source design systems inspect actual documentation and implementation, not only the README screenshot. Look for:
- theme token definitions, contrast roles and semantic naming;
- component API/state contracts;
- accessible keyboard interactions;
- focus-ring and screen-reader test coverage;
- visual regression tests;
- icon licensing and available sizes;
- responsive behavior and density variants;
- upgrade/deprecation strategy;
- whether the project is actively maintained or archived.

Important: a GitHub repository is evidence that a pattern is implemented by its maintainers, not proof that the pattern is universally optimal.

## Evidence hierarchy
**Normative**: current WCAG, HIG, standards with explicit requirements. **Research-supported**: peer-reviewed studies or documented usability tests; note sample and limitations. **Practitioner observation**: decisions in shipped systems; useful but context-specific. **Critique**: reasoned evaluation of work (not a measurement of universal impact). **Inspiration**: galleries, mockups or style references. Explicitly label untested design hypotheses.

## Content audit
Inventory actual headings, names, services, prices, dates, product attributes, photos, rights, disclaimers, FAQ, support channels and error text. Classify each as verified, drafted, missing, expired or prohibited to publish. An invented testimonial or random phone number is a trust defect, not a placeholder the designer may silently pass off as finished.

For software, include realistic data extremes: empty list; 1, 10, 1000 items; long labels; localized text; unusually large numbers; negative values; missing logos; offline status; permission denied; slow queries. For a chart, include an actual quiet market session, large volatility spike, gaps, missing candles, narrow viewport, history review, rapid timeframe switching and invalid data.

## Synthesis into design hypotheses
Write each conclusion as:
- Observation: what was seen and in which sample;
- Problem: effect on a real user task;
- Hypothesis: which change might improve it;
- Proposed mechanism: why it could work;
- Prototype: specific visual/interaction choice;
- Potential failure: trade-off or excluded user;
- Test: observation/metric that could disprove it;
- Status: untested, supported, rejected or revised.

Example: “On the 1120-pixel MacBook window, expanded navigation and inspector reduce chart width. A collapsible rail may preserve task context without permanent space use. Test whether users can still discover market switching and entry inspection when minimized.”

## Divergent visual directions
For a new project, sketch three incompatible *structural* concepts before producing a polished mockup. One might be a utilitarian instrument, another editorial and character-led, another expressive and modular. Each must include a content hierarchy, brand signals, intended motion and primary-state layout. Three accent colours on the same generic dashboard are not three directions.

Evaluate concepts on appropriateness, differentiation, task completion, accessibility, scalability, hardware fit and production feasibility. Describe trade-offs openly. A beautiful direction may be inappropriate if it requires heavy video background on a 4 GB Mac.

## Research on limited budgets
A small moderated task test can identify serious usability issues. Do not infer precise population-level percentages from five interviews. Use concise, objective tasks and record completion, errors, confusion and time where sensible. Collect impressions only after behavioural observation to reduce the aesthetic-usability bias. Conduct fast first-impression tests separately from realistic task tests.

For a logo: blind category comparison, naming readability, black/white and 24-pixel recognition and false competitor attribution. For packaging: physical sample legibility and shelf-context recognition. For a website: task-based find-contact/understand-offer/submit-enquiry flow, including on low-end mobile. For software: critical states and safe failure recovery.

## Production reality audit
Before designing ask: what is the current OS? browser versions? device resolution? minimum RAM? deployment environment? database and API limits? licensed font availability? print vendor process? maximum ink colours? approved domain? image formats? These constraints often determine whether the work can be delivered. Inspect the actual project before rewriting it. For a native macOS app on Monterey, use compatible APIs and check the full launch, not merely compilation.

## Research deliverables
The final discovery package should include:
- one-page executive brief with links to evidence;
- audience/task and context map;
- current product screenshot/asset audit;
- benchmark matrix with at least three references when appropriate;
- complete authentic content inventory;
- brand canon and excluded directions;
- hypothesis register;
- initial information architecture;
- three candidate creative territories;
- proposed accessibility and UX test cases;
- source registry with dates and licences.

## Avoid
Visual-gallery collecting without synthesis; unsourced psychology claims; interview questions that steer toward the designer's preferred answer; copied UI/brand assets; redesigning existing recognizable brand assets without knowing why; asserting user preferences were validated when they were guessed; shipping on a screenshot with no functional testing.

## Primary sources
[Nielsen Norman Group usability heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/); [first impression testing](https://www.nngroup.com/articles/first-impressions-human-automaticity/); [visual design study guide](https://www.nngroup.com/articles/visual-design-in-ux-study-guide/); [GOV.UK tested patterns](https://design-system.service.gov.uk/get-started/); [GitHub Primer foundations](https://primer.style/product/getting-started/foundations/).