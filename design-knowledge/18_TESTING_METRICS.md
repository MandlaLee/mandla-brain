# 18 — Design Research Tests, Metrics and Evidence

## Good design must survive falsifiable tasks
A designer's confidence is not enough. A working testing program distinguishes visual preference from user understanding, ability to complete the task, brand recognition, trust accuracy and production fidelity. Keep tests proportional to stakes. A poster design requires real size/legibility checks; a financial tool requires precise data states, safety and session testing.

## Evidence tiers
**Normative pass/fail:** WCAG contrast, supported device, required output format, exact print constraints.
**Functional:** click through real user task, verify form submission, offline recovery, keyboard actions.
**Qualitative:** participant comments and observed difficulty, contextual interviews.
**Quantitative:** task success rate, errors, time, attribution, retention or conversion where sample permits.
**Creative critique:** designer/brand-owner judgement of distinctiveness and emotional fit.
Don't claim a normative pass from subjective beauty, and don't assert a population-level effect from three personal opinions.

## Usability plan
Define participants, scenario, tasks, success criteria, test order, consent and metrics before seeing the outcome. Use realistic data and ask neutral prompts. Avoid teaching users a pattern immediately before judging whether it is discoverable. Log the sequence, wrong turns, misclicks, clarification requests, recovery and completion. Conduct a post-task interview to understand mental models without overriding behavioural evidence.

### Example task — trading assistant
Show the chart with a current feed, a deliberately stale feed, a cached historical signal, and a WAIT status:
- Which market and timeframe is being viewed?
- Which timeframe generated the signal?
- Is the latest quote live, delayed or simulated?
- Where was the original signal candle and when was trade entry first possible?
- What is reference entry, stop, TP1 and risk/reward?
- Can a previous trade be found and then return to latest?
- Can the inspector collapse and re-open without losing context?
A result showing confusion between historical and executable trade is a serious defect.

### Example task — small business website
Ask visitors to identify the business offer, geographic coverage, proof and total expected cost; contact the business; correct invalid form data; and identify what happens after submission. Test on desktop and an ordinary mobile connection. Don't count clicking submit as success unless submission actually reaches the intended system.

### Example task — logo
Test the mark in category with competitor distractors. Ask for name reading, spontaneous association, category fit and source attribution after controlled exposure. Compare small size, grayscale and crowded poster applications. A novice's forced preference among options is not a reliable brand-asset strength score.

## Visual QA matrix
Test at actual intended screen resolutions and zoom; include:
- most common full-window size;
- minimum supported width/height;
- both side panels expanded/minimized and mixed modes;
- long labels and extreme data;
- empty/loading/error/cached/delayed/success states;
- dark/light and high contrast if supported;
- button hover/focus/disabled;
- actual logo, imagery and legal footer;
- translated/local text;
- reduced motion.
Save screenshots with file names encoding device, state, date and version. Compare against approved baseline and document differences.

## Sample-size humility
Small moderated usability tests can discover important issues; they don't precisely estimate the error rate for all users. Five positive interviews cannot justify “95% trust.” A/B tests need adequate traffic and correct statistical design; changing multiple variables simultaneously makes causality unclear. Distinguish correlation from conversion impact and report uncertainty.

## Brand metrics
Measure separately: brand recognition, attribution, distinctiveness, consideration, trust perception, clarity of category, campaign engagement and real purchase/booking outcomes. A poster may be liked yet fail to communicate event date. A repeated colour may feel unusual but not be associated with the intended brand. Track performance across touchpoints and over time instead of making changes after one arbitrary opinion.

## Product metrics
For complex products, use task time, error counts, support tickets, onboarding drop-off, keyboard navigation efficiency, meaningful feature use, repeated task speed, perceived workload and satisfaction. Define baseline and evaluate after release. Avoid optimizing solely for raw clicks or session time; quick task completion may be better than prolonged engagement.

## Accessibility validation
Automated contrast checkers and audits can catch some faults. Manual keyboard testing, screen-reader walkthroughs, zoom/reflow, reduced motion and real assistive technology trials remain necessary. Do not label a product “fully WCAG compliant” simply because no automated issues appeared. List which criteria and methods were checked.

## Reliability and technical QA
Track app start success, crashes, memory use, invalid data, network failures, state restoration, request races and reproducible exceptions. For image workflows, test transparent backgrounds, file integrity and export format. For web forms, verify real server response and data storage. For visual charts, include timestamp alignment and no look-ahead bias.

## Test report template
- Version and environment.
- Artifact/URL/path tested.
- Task/scenario and test data.
- Expected behaviour.
- Observed behaviour.
- Severity (blocker, major, minor, cosmetic).
- Reproduction steps and screenshots.
- Likely root cause if known.
- Fix and regression check.
- Remaining limitation.
- Reviewer and date.

## Quality targets should reflect stakes
A typo in marketing copy and a wrong financial stop-loss line are different risk categories. Set stricter gates around important data, transaction correctness and privacy. Protect production with staging and rollback where needed. Present known limitations prominently rather than burying them beneath praise for visual polish.

## Metric misuse
- Counting a visually attractive screenshot as “user tested.”
- Calling a study with 3 people statistically representative.
- Reporting artificial backtest gains as achievable trading returns.
- Inventing perceived trust because a palette is blue.
- Assuming conversion lift from button colour without controlled experiment.
- Ignoring regression tests when changing UI layout.
- Claiming a site deployed when a file was merely created.

## Sources
[Nielsen Norman Group usability testing](https://www.nngroup.com/articles/usability-testing-101/), [NN/g aesthetic-usability effect](https://www.nngroup.com/articles/aesthetic-usability-effect/), [W3C evaluation resources](https://www.w3.org/WAI/test-evaluate/), [Google web performance](https://web.dev/articles/vitals), [GOV.UK design system](https://design-system.service.gov.uk/), [GitHub Primer](https://primer.style/product/).