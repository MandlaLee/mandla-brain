# 27 — Rendered UI Testing, Browser Automation and Visual Regression

## The most consequential missing habit
AI can write syntactically valid code and report success while the actual page contains overlapping cards, a missing font, off-screen controls or dead forms. **Compilation is not visual review**. The reliable loop is implement → run → capture → inspect → interact → fix → recapture → regression-check.

## Separate tests into three layers
**Static analysis:** typecheck, lint, token references, semantic structure and security checks.  
**Rendered inspection:** browser/native screenshots, actual typography, visible state, content clipping and alignments.  
**Interaction:** realistic user workflows, keyboard focus, form submission, content edits, error recovery and persistence.

Passing one layer does not imply passing the others. A screenshot does not establish API success; Playwright accessibility assertions do not prove the product is visually distinctive; a build alone proves neither.

## Browser harness
For a web project:
1. Confirm what technology and launch command the real repository uses; don't assume Next.js.
2. Start a disposable local server; record port, log location and cleanup process.
3. Use an isolated browser profile without real customer credentials.
4. Wait for a **relevant readiness condition** (root landmark, critical chart loaded, expected count). For constantly polling apps, never require global `networkidle` forever.
5. Capture default screen, full-page where useful and screenshots of key interactive states.
6. Discover selectors from actual DOM and accessibility tree. Prefer `getByRole` and `getByLabel` rather than brittle generated classes.
7. Execute target tasks and assert meaningful outcomes. Gather browser console/page exceptions and failed requests.
8. Exercise narrow/mobile viewports, keyboard, reduced motion, zoom and large content.
9. Compare with baseline and classify differences as intended change or regression.
10. Shut down server and browser unless requested otherwise. Protect private fixtures and screenshot content.

### Example Playwright test (adapt to current project)
```ts
import { test, expect } from '@playwright/test';

test('service enquiry is discoverable', async ({ page }) => {
  await page.goto('/');
  await expect(page.getByRole('main')).toBeVisible();
  const enquire = page.getByRole('link', { name: /request.*quote|enquir/i });
  await expect(enquire).toBeVisible();
  await enquire.click();
  await expect(page).toHaveURL(/contact|quote|enquiry/);
  await expect(page.getByRole('textbox', { name: /name/i })).toBeVisible();
});

test('keyboard users can see focused CTA', async ({ page }) => {
  await page.goto('/');
  await page.keyboard.press('Tab');
  const active = page.locator(':focus');
  await expect(active).toBeVisible();
  // Add project-specific assertion for visible focus styling/outline.
});
```
This is illustrative: adjust labels, routes, fixtures and behavior to the real product. URL change alone does **not** prove an enquiry was delivered.

## Screenshot matrix
Capture combinations targeted to risk:
- Desktop 1440px, mid 1024px, tablet 768px, small phone 390px and 320px when web; actual supported dimensions take priority.
- Dark/light if available, default and compact density.
- Primary screens and expanded/collapsed panels.
- Empty, one-item, many-item, loading, offline, error and success.
- Long localized text, price/currency extremes and 200% zoom.
- Hover/keyboard focus/selected/disabled.
- High contrast and reduced motion when supported.

Choose a small stable baseline set for CI, then add critical states when a bug occurred. Too many fragile pixel snapshots can become noise; choose deterministic fonts, data, date, animation states and viewport dimensions. A pixel diff signals *change*, not necessarily a defect—review legitimate changes.

## Baseline design loop
```text
working commit (A) → baseline screenshots → approved change → candidate build (B)
                    → matched viewport + state → compare diffs
                    → categorize as intended/bug → fix → capture again
                    → approve snapshot + tests → commit (B)
```

Name screenshots so their origin and state are identifiable:
`2026-11-07-aurum-macos12-1120x763-both-collapsed-live.png`
`2026-11-07-phaladigital-chromium-390-contact-error.png`

Never check a private person's portrait, address, trading account number, actual API key or application record into a public GitHub screenshot fixture. Use safe synthetic data and obtain permission for reference assets.

## Visual diff tools
Chromium/Playwright screenshot assertions, browser screenshot capture, native screenshot utilities, image diff utilities and visual regression services may help. Exact tools depend on stack. Store canonical screenshots with environment and intended visual design contract. Avoid depending on a third-party SaaS without reviewing privacy and pricing.

Vercel's [web-design-guidelines](https://github.com/vercel-labs/agent-skills/blob/main/skills/web-design-guidelines/SKILL.md) is an audit-style skill; it does not itself prove the rendered app is perfect. Anthropic's [webapp-testing](https://github.com/anthropics/skills/blob/main/skills/webapp-testing/SKILL.md) gives a browser interaction process. Combine both concepts with Mandla's independent creative review.

## Aesthetic critique vs functional critique
**Aesthetic:** identity, composition, hierarchy, typography, originality, density, authenticity, photo direction.  
**Functional:** navigation, keyboard, contrast, overflow, responsive behavior, loading/error state, performance, cross-browser and data correctness.  
Use two passes so one does not silently replace the other. Where possible, have an independent human or separate reviewer inspect a screenshot without seeing the creator's rationale. An AI scoring its own design is a heuristic, not an objective quality measurement.

## Visual states are data fixtures
Use fixtures for:
- Success with realistic varied content;
- Empty list and zero-state;
- Slow API and timeout;
- Error 400/401/403/404/429/500;
- Very long names and descriptions;
- Offline/cached/historical modes;
- Conflicting user settings and interrupted transitions;
- Screen-reader and keyboard-only paths;
- Multi-language expansion and number formats.
Fixtures should be named and checked into the working project when safe; no real user secrets.

## True browser reliability
- A design can pass in Chrome and fail in Safari due to font metrics, input controls or CSS differences.
- A screenshot in an emulated mobile viewport does not prove touch gestures work on a real phone.
- Browser zoom and OS font scaling may expose clipping that viewport-only tests miss.
- WebGL/animation can fail on older hardware.
- Form submission may appear successful on the client while the server rejects it.
- Lighthouse/aXe automation finds only some issues.
Record exact tested environments and outstanding limits.

## Native macOS review
A real SwiftUI app requires native window captures and real window/keyboard interactions; don't treat a web browser as a universal simulator. Test installed `.app` or `.pkg` launch, app icon, toolbar, menus, title, collapsible panels, resizing, keyboard focus, menu commands, notifications, offline behaviour, persistence and CPU/RAM. When changing chart UI, confirm no trading math, time alignment or provider labels have regressed. Test the original supported OS and architecture.

### Mac test matrix
- Installed app launches from Dock/Desktop shortcut.
- Default/min/max window and both side panels expanded/minimized.
- Preferences Save/Cancel semantics and restoration after relaunch.
- Long symbol/timeframe names, numeric precision and currency units.
- Background refresh, network outage and delayed quote.
- Historical marker selection and return-to-live.
- Data source/staleness/WAIT state visibly correct.
- Context controls remain reachable with keyboard or VoiceOver where possible.
- Charts, axes, zones, TP/SL markers don't overlap critical labels.

## Review issue format
Report one issue per line with `[severity] file:line or component — state and viewport — observed — expected — reproduction — screenshot`. Example: `P1 TradeInspectorPanel: compact@1120 — current BUY shown although latest provider candle is stale — show DELAYED and suppress live watch — fixture stale-30min.png`.

## Practical pass/fail gates
Block release for wrong data, misleading trading states, inaccessible critical actions, dead forms, broken navigation, severe overflow, missing source files or privacy leaks. Less serious aesthetics may remain as documented issues with owner sign-off, but repeated generic-template styling conflicts with the creative goal and merits rework rather than a cosmetic badge.

## Source links
[Anthropic webapp testing skill](https://github.com/anthropics/skills/blob/main/skills/webapp-testing/SKILL.md) · [Anthropic Claude Code iteration guidance](https://www.anthropic.com/engineering/claude-code-best-practices) · [Vercel Web Interface Guidelines](https://vercel.com/design/guidelines) · [Playwright docs](https://playwright.dev/docs/intro) · [W3C accessibility evaluation](https://www.w3.org/WAI/test-evaluate/) · [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/).