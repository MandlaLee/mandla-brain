# 28 — UI Engineering Cookbook: Real Components, Responsive Layout, Forms and Data States

## Design craft must survive implementation
A skill that makes prettier mockups but doesn't teach reliable code is incomplete. This chapter converts the brand/UX handbook into implementable patterns for HTML/CSS/JS, React, Next.js and native desktop work. The examples are **illustrative patterns**; choose the correct framework and tested APIs of the actual codebase, not whichever sample looks easiest.

## Component boundary principles
A component is a meaningful reusable unit when it owns a coherent interaction or visual responsibility. Avoid building one component per HTML tag and avoid one giant 2,000-line page with tangled state. Prefer composition with explicit responsibilities:
- Page shell: navigation, primary content region, status and overflow behaviour.
- Data view: renders actual input and clearly different loading/error/empty/success states.
- Interaction component: keyboard, focus, controlled state, disabled and recovery.
- Brand component: mark, signature typography, campaign framing, consistent art direction.
- Utility: formatting, safe data conversion and functions not coupled to presentation.

Do not let a shared theme accidentally override a specific client identity. Shared engineering quality can coexist with different brand component styling.

## Semantic HTML first
Actions use buttons; destinations use links; forms use labels; lists use lists and data tables use proper tabular structure. A clickable card may wrap a link if the whole card truly navigates, but avoid nested interactive targets. ARIA should enhance semantic controls, not replace them unnecessarily.

```html
<main id="content">
  <form aria-labelledby="request-heading">
    <h1 id="request-heading">Request a quotation</h1>
    <label for="service">Service</label>
    <select id="service" name="service" required>
      <option value="">Choose a service</option>
      <option value="website">Business website</option>
    </select>
    <button type="submit">Request quotation</button>
    <p id="form-status" role="status" aria-live="polite"></p>
  </form>
</main>
```
The markup is a starting point. Add real validation, backend request, safe response handling and accessible error focus. Don't simulate delivery in the UI if the server never received the request.

## Responsive layout without arbitrary fixed widths
A sidebar and primary canvas should flex, with clear min/max sizes and graceful collapse:
```css
.workspace {
  display: grid;
  grid-template-columns: var(--rail-width, 12rem) minmax(0, 1fr) var(--inspector-width, 18rem);
  min-width: 0;
}
.workspace[data-rail-collapsed="true"] { --rail-width: 3.5rem; }
.workspace[data-inspector-collapsed="true"] { --inspector-width: 3rem; }
.workspace > * { min-width: 0; }
@media (max-width: 800px) {
  .workspace { grid-template-columns: minmax(0, 1fr); }
  .workspace__rail, .workspace__inspector { /* explicit drawer/sheet strategy */ }
}
```
The placeholder comment is intentional: the correct mobile drawer approach must handle focus trapping, dismissal, return focus and screen-reader semantics. Do not paste a CSS declaration without implementing its behaviour. A physical target device is the final authority for the values.

## Token discipline
Avoid one-off repeated hex colours and arbitrary corner radii in hundreds of components. Use reference tokens under semantic roles:
```css
:root {
  --surface: #ffffff;
  --text: #17212a;
  --text-muted: #465664;
  --focus: #0067c8;
  --radius-control: 0.4rem;
  --gap-base: 0.75rem;
}
:where(button, a, input, select, textarea):focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}
@media (prefers-reduced-motion: reduce) {
  .optional-motion { animation: none; transition: none; }
}
```
These colours are neutral **example values**, not Mandla's default brand palette. Every project's current canonical palette and contrast checks override them. Check link/text/button contrast under actual backgrounds and non-text component contrast too.

## Data states as a discriminated union
A component should not be able to report “success” while simultaneously “loading.” Use explicit state models:
```ts
type Resource<T> =
  | { status: 'idle' }
  | { status: 'loading' }
  | { status: 'success'; data: T; receivedAt: number }
  | { status: 'empty'; receivedAt: number }
  | { status: 'error'; message: string; canRetry: boolean }
  | { status: 'stale'; data: T; receivedAt: number };
```
The state machine must be driven by actual provider events. A stale state isn't the same as a failed request. A historical signal is an archived record, not a live trade suggestion.

## Forms and asynchronous operations
- Validate input before network, preserving user-entered values.
- Prevent duplicate submits after a request begins; keep Cancel/Retry meaningful.
- Distinguish client validation success from server acceptance.
- Never expose private API keys in frontend bundles or a public repo.
- Give each field clear label, autocomplete and error message.
- Prevent race conditions when switching forms, filters or timeframe.
- Manage cancellation when routes change.
- Write tests against the actual submit handler and its server result.

## Status precision
A live data widget should show at least provider, data age and failure state when relevant. A successful polling HTTP request is not proof its returned candle is current. Distinguish fetch time and market data time. A claim like “Real time” must be supported by an appropriate contract and timestamps, not an animation.

## Performance prioritization for React/Next
Use [Vercel's React Best Practices](https://github.com/vercel-labs/agent-skills/blob/main/skills/react-best-practices/SKILL.md) as a technical checklist **when this exact stack is used**:
- Eliminate dependent request waterfalls that can run in parallel.
- Avoid unnecessary bundle imports; lazy-load heavy components when appropriate.
- Memoize expensive work only after identifying actual rerender cost.
- Prevent unnecessary repeated layout measurements.
- Give images dimensions and sensible loading priority.
- Use measured web-vitals and profiling rather than cargo-cult optimisation.
- Keep source/data boundaries secure on server environments.

Don't rewrite a working static site into Next.js just to use a fashionable optimization playbook. Framework migration is a separate product decision and risk.

## Native SwiftUI translation
For macOS, use native components and layout patterns where they fit. Keep source/provider models, signal analysis and chart rendering separated. Use app-scoped state carefully, avoid overlapping refresh tasks and persist user preferences without leaking secrets. Validate compile target against macOS/Intel constraints and test the installed app. Browser screenshot tooling alone cannot verify this.

## Accessibility code quality
Keyboard activation; visible focus; accessible icon names; informative statuses; reduced motion; meaningful image alternatives; no colour-only risk; WCAG target/contrast requirements; and no uncontrolled modal focus. Avoid adding ARIA to native semantic elements without purpose. Verify with an actual screen reader or equivalent platform tool where possible.

## “Polish” code review
Look for these defects in actual code:
- random `margin-top: -7px` offsets to hide structural alignment errors;
- deeply nested cards with same radius and shadow;
- thirty unrelated hex colours;
- button labels and handlers that disagree;
- click handlers on non-interactive divs;
- hard-coded desktop widths;
- animations using layout properties in every frame;
- empty states that leave only a spinner;
- icons with no accessible name;
- hidden scrollbars that mask unreachable content;
- overflow ellipsis concealing essential amounts/units;
- inaccurate status when provider request changes;
- user-entered form data discarded on network error;
- imported fonts/icons with no licence or unnecessary network dependency.

## Example implementation-ready acceptance test
```text
Given an empty symbol history,
When a user opens the chart,
Then the screen shows "No saved history" with recovery action;
no previous BUY/SELL marker is displayed; the source is not labelled live.
Given delayed 5-minute reference data,
When live refresh finishes,
Then the title/summary clearly reads "Delayed";
no new live trade alert is issued; historical entries remain identifiable.
```

## Deliverables
Source commit, meaningful component specification, token map, generated/owned artwork list, test cases, real screenshots in target states, performance and accessibility notes, and explicit known limits. Never call a CSS-only change a fully verified product upgrade.

## Sources
[W3C WAI-ARIA APG](https://www.w3.org/WAI/ARIA/apg/) · [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) · [Vercel interface rules](https://github.com/vercel-labs/web-interface-guidelines/blob/main/command.md) · [Vercel React best practices](https://github.com/vercel-labs/agent-skills/blob/main/skills/react-best-practices/SKILL.md) · [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/).