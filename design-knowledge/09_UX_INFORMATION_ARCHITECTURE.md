# 09 — UX, Information Architecture and Interaction Patterns

## Organise tasks, not widgets
Information architecture answers where people go, what they expect, how they find content and what happens when they act. Before making screens, build a task map: entry context → goal → required information → decision → action → confirmation/recovery. A product with perfect visual polish but broken flow is not successful.

## Navigation design
For a small site, simple descriptive primary navigation can outperform complex mega menus. For a multi-tool app, a persistent tool hierarchy can support context; use collapsible rails to protect workspace space. Design labels in the user's vocabulary, not abstract internal departments. Show current location, make Back/Cancel predictable and keep frequently used functions reachable.

## Mental models
A user expects a clickable item to behave according to common conventions; if it opens a different workflow, explain why. Platform-consistent patterns are especially important for native applications and assistive technology. Innovation belongs where it solves a meaningful problem, not where it adds surprise to basic navigation.

## State inventory
Every important view should have:
- initial, loading, partial loading and slow-server states;
- successful data, no data and empty-but-ready states;
- validation errors and permission errors;
- offline, cached, delayed and stale states;
- empty results after filtering/search;
- submit processing, success and failure recovery;
- disabled components with a reason;
- destructive action confirmation and undo where feasible.
Use state content with genuine next actions. “Something went wrong” without explanation or recovery is incomplete.

## Forms
Labels must remain discoverable. Specify whether a field is required before the user submits. Show format constraints before entry. Provide examples where helpful without using placeholder text as the only label. Validate close to the relevant field, but avoid interrupting typing prematurely. Preserve already entered data after a server failure. Group fields into meaningful steps, not arbitrary screens, and explain why sensitive data is required.

## Content design
Write plain-language actionable messages. A system warning should state what happened, why it matters if known and the immediate remedy. For a trading source, use “5-minute reference feed unavailable; historical markers only” rather than a vague red WAIT badge. Never show an API technical error code as the only user-facing explanation.

## Accessibility semantics
Prefer native HTML controls and OS components where they meet product needs. If implementing custom widgets, follow WAI-ARIA Authoring Practices for role, state, focus order and keyboard behaviour. A component that looks like a button but does not activate via keyboard is broken. Focus must be visible, moved predictably on dialog open/close and never trapped accidentally.
Sources: [W3C APG](https://www.w3.org/WAI/ARIA/apg/), [keyboard interface guidance](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/).

## Error prevention versus error correction
Avoid impossible choices, wrong units, ambiguous selection and silent failures before adding friendly error copy. High-stakes decisions need explicit units, confirmations where appropriate and clear status. Where Undo can safely reverse a change, offer it instead of unnecessary confirmation dialogs. In irreversible workflows, use clearer consequences.

## Search, filters and sorting
Use descriptive controls. Show active filters, result count and empty-results explanation. Preserve query state when navigating to detail and back. Avoid default sorting that appears arbitrary. A search field must have a meaningful label, clear state and keyboard behaviour; do not hide it solely behind a decorative icon on a small screen.

## Progressive disclosure
Progressive disclosure is not hiding every advanced feature. High-frequency tools should remain visible, rare settings can live in menus, and critical status must not be concealed behind a collapsed rail. Test how long experienced users take to reach common actions and how easily newcomers discover hidden controls. Tooltips and accessible names matter for icon-only modes.

## Tables and data
Use sortable headers, aligned numeric fields, clear units, stable row selection and overflow behaviour. Maintain a meaningful empty state. Don't colour an entire row red without explaining risk. For financial data, use tabular numerals and a consistent sign/precision policy. For job data, keep application state and due date separate from decorative rankings.

## Modal discipline
Dialogs interrupt workflows. Prefer inline sections for frequent changes and reserve modal dialogs for focused choices, crucial confirmations or settings where complete context is required. Provide Cancel/Close, keyboard Escape where appropriate and clear apply/save semantics. A preference window must not persist changes before explicit Apply if its UI promises cancelable draft editing.

## Evaluation and metrics
Test important workflows: completion rate, error type, wrong selection, recovery, time to first success and discoverability. For a market app ask participants to identify source timeframe, chart timeframe and staleness. For a website ask them to find real service coverage and submit an enquiry. For a game ask whether interface feedback accurately represents state. Subjective beauty ratings are supplementary.

## Ten-heuristic audit
Use Nielsen's classic heuristics as a heuristic review: status visibility; real-world match; user control; consistency; prevention; recognition; expert efficiency; minimalism; clear error recovery; help. Do not treat checking these boxes as replacing observed usability tests.

## Source links
[NN/g usability heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/), [GOV.UK patterns](https://design-system.service.gov.uk/), [W3C APG](https://www.w3.org/WAI/ARIA/apg/), [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/), [GitHub Primer content and accessibility](https://primer.style/product/getting-started/foundations/).