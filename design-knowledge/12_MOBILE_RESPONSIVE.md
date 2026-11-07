# 12 — Mobile, Responsive and Adaptive Design

## Responsive isn't simply shrinking
An interface must adapt its information architecture, priorities, navigation and interaction to the user's viewport and input device. A 1920px desktop design reduced to 375px can become a cramped, unreadable stack. Responsive design prioritises the same essential user task with appropriately different spatial patterns.

## Start with conditions
Research actual devices, connection quality, browser/OS availability, physical viewing conditions and local data affordability. A mobile viewer in sunlight with intermittent signal has different needs from a desktop editing session. Use content and workflow to choose breakpoints; never choose a breakpoint solely because a popular CSS framework does.

## Information priority
Identify what must be visible on a small screen: primary action, critical state, identity and recovery path. Move secondary controls into discoverable drawers or tabs. When a task requires a wide chart or table, offer deliberate horizontal exploration/zoom rather than collapsing important data into meaningless tiny labels.

## Touch and pointer
Interactive targets must meet relevant accessibility requirements; WCAG 2.2 introduces a minimum target-size success criterion with exceptions. Comfortable touch sizes depend on platform and context; platform HIG guidance may recommend larger practical targets. Ensure adjacent actions are not easily confused. Custom drag gestures must not make scrolling or zoom unavailable. For desktop mode, retain pointer hover tooltips, focus and keyboard shortcuts.

## Responsive type
Reading size should remain comfortable. Check line length, character expansion, text zoom, long names, number formats and localized languages. Headlines must not dominate the whole first viewport. A phone screen with all-caps micro-labels and 9px text is not sophisticated; it is inaccessible.

## Image design
Use deliberate crops at multiple ratios. Hero images should retain faces and important details when narrowed; do not simply use CSS cover with unpredictable crop. Store crop anchors or alternate exports. Make foreground text readable over imagery and provide alt text for meaning, not decorative objects. Avoid downloading full-resolution images when a smaller responsive source would suffice.

## Navigational adaptation
A header may become a clear menu or bottom navigation depending on number of high-frequency destinations. Hiding the entire site behind a hamburger can be harmful if contact and main actions are urgent. Show current location and accessible close behaviour. Persistent bars must not obscure content or interfere with the OS safe area.

## Forms and keyboard types
Use appropriate input types (email, number, telephone), validation and labels. Do not force desktop date pickers or tiny select fields on phone. Check visible viewport when keyboard opens; ensure the submit button and error text remain reachable. Avoid multi-step forms that forget progress after network failure. For South African services, phone and WhatsApp contact actions should be real and consent-aware.

## Device and network states
Test typical and very narrow devices, tablet/split view, orientation change, slow 3G-like network emulation, offline, reduced data mode and low memory. Cache appropriately without showing stale information as live. Don't assume all users have unlimited mobile data, high-resolution OLED displays or modern phones.

## Content adaptation
Prioritize information and change its presentation without silently hiding legal caveats, pricing conditions, risks or accessibility explanations. For a trading app, a phone may show a compact chart plus entry summary with an explicit “open inspector” action; stop/target levels must remain accessible. For a concert poster, primary face, event name, date, location and ticket details should survive thumbnail cropping.

## Progressive enhancement
Provide meaningful content before heavy JavaScript completes where possible. Use semantic HTML and browser-native controls. Ensure interactions remain recoverable if images or fonts fail. A minimal fallback view can be more useful than a fully animated loading screen.

## Breakpoint audit
Test at minimum:
- 320/360/375/390/430 CSS px widths where applicable;
- mid-size tablets;
- 768 and 1024 px layouts;
- a standard desktop width;
- browser zoom 200% and narrower resizable windows.
These are test samples, not mandatory CSS breakpoint values. The layout should adapt when content no longer fits; actual design dictates breakpoints.

## Typical mobile failures
Tiny icons, accidental horizontal overflow, modals taller than screen, fixed CTA covering content, hidden validation errors, unreadable chart labels, image subject cropped out, non-working WhatsApp links, full-screen animation blocking the task, overcomplicated hamburger structures and excessive performance cost.

## QA checklist
Can all primary tasks be completed with one hand? Are focus and active states visible? Are text and controls readable outdoors? Do forms use correct keyboards? Does data-heavy content support accessible exploration? Are all routes and menu actions reachable in landscape and portrait? Does screen-reader order match reading order? Are saved preferences and draft forms retained safely?

## Sources
[WCAG 2.2 target size](https://www.w3.org/TR/WCAG22/#target-size-minimum), [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/), [Material Design foundations](https://m3.material.io/), [web.dev responsive design](https://web.dev/learn/design), [GOV.UK Design System](https://design-system.service.gov.uk/).