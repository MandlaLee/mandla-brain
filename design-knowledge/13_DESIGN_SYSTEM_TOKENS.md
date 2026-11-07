# 13 — Design Systems, Tokens and Component Engineering

## A design system is governed decisions plus working implementations
A UI kit is a set of components; a design system includes principles, foundations, patterns, token conventions, accessibility contracts, code usage, governance and evidence. Consistency saves time only when the components solve real tasks. Reusing generic components without adapting brand expression can create indistinguishable products.

## Token architecture
Organise tokens by **meaning**, not arbitrary visual values.
- Reference tokens: raw colour ramps, space increments, type metrics, radius sizes, border widths, shadows.
- Semantic tokens: background-canvas, surface-raised, text-primary, text-secondary, brand-primary, focus-ring, state-danger, state-warning, border-subtle, trade-buy, trade-sell.
- Component tokens: button-primary-fill, input-border-focus, chart-grid-stroke, nav-rail-selected, inspector-gutter, toast-alert-spacing.
- State/variant tokens: hover, pressed, selected, disabled, error, dark/light, high-contrast and compact.
- Platform exports: CSS custom properties for web, SwiftUI colour/styles for native Mac, Compose or other native equivalents as required.

A simple semantic token scheme:
```json
{
  "color": {
    "text": {"primary": "{color.neutral.950}", "secondary": "{color.neutral.650}"},
    "surface": {"canvas": "{color.neutral.50}", "raised": "{color.neutral.100}"},
    "state": {"warning": "{color.amber.650}", "danger": "{color.red.700}"}
  },
  "space": {"xs": 4, "sm": 8, "md": 12, "lg": 20, "xl": 32}
}
```
This is a **concept sketch**, not a fully conforming DTCG format; consult the latest specification and toolchain before exporting real machine-readable tokens. Never blindly assign semantic danger or status from brand primary.

## Components
A component specification should include:
1. Purpose and user task.
2. Variants and intended use.
3. Anatomy and content rules.
4. States: default, hover, focus, active, pressed, selected, disabled, loading and error.
5. Keyboard behaviour and accessible name.
6. Screen-reader role/state.
7. Geometry and spacing from tokens.
8. Long-label and localization behaviour.
9. Light/dark/high-contrast versions.
10. Data, API and privacy implications if relevant.
11. Misuse examples and known limitations.
12. Unit, integration and screenshot tests.
If the component relies on a brand-specific shape or icon, document which features are flexible and which identify the brand.

## Studied models
**IBM Carbon** combines colour/spacing/type tokens, React/web components, icons, pictograms, grid and motion packages. Its source shows scale and the importance of semantic foundations. [Official repo](https://github.com/carbon-design-system/carbon).

**GitHub Primer** supplies reusable components and design guidelines for code-heavy products; valuable for focus, accessibility, layout, high-density interfaces. [Primer React](https://github.com/primer/react).

**Fluent UI** offers Microsoft's cross-product component conventions, a lesson in ecosystem consistency and version migration (v8/v9). [Repo](https://github.com/microsoft/fluentui).

**Radix UI** prioritizes accessibility primitives independent of most visible styling. A strong foundation when a brand needs its own art direction. [Repo](https://github.com/radix-ui/primitives).

**shadcn/ui** makes component source available for adaptation: helpful for owning code, but raw default styling frequently produces recognisable template aesthetics. Customise structure and information architecture, not only palette. [Repo](https://github.com/shadcn-ui/ui).

**HashiCorp Helios** provides tokens, components, icons and documented conventions. [Repo](https://github.com/hashicorp/design-system).

**Porsche Design System** demonstrates brand-specific component engineering, visual-regression and quality processes. [Repo](https://github.com/porsche-design-system/porsche-design-system).

Design systems are tools to learn from, not exact visual identities to transfer. Verify licences, versions and target framework before reusing code.

## Accessibility contract
Design tokens alone don't make an interface accessible. Implement correct semantic HTML/native roles, focus order, contrast, disabled information, reduced motion, target sizes, keyboard access, screen-reader labels and appropriate live-region announcements. Component QA should have automated tests plus manual real interaction; automated accessibility scans cannot prove usability.

## Quality and visual regression
Use screenshot test baselines at defined sizes and states. Include production content extremes, color modes, zoom, RTL where relevant and error/empty states. Compare diffs and judge whether they indicate deliberate redesign or regressions. A UI that builds but shifts its central controls offscreen at compact width is defective.

## Versioning and governance
Define who may add/change a token, how it is reviewed, how deprecated values are communicated and how consumers migrate. Track semantic changes and include changelog examples. Avoid allowing every page to invent new button variants. Conversely, don't over-engineer a 3-page prototype into an enterprise-scale library before the core interaction is validated.

## Design-to-code handoff
Provide source design spec, token definitions, component states, typography, responsive rules, icon sources, image assets, motion, accessibility notes, test cases and examples. Compare code result against real mockups at exact resolution. Record exceptions, don't hide them in magic constants.

## Cross-platform principles
Keep meaning shared but allow platform-native behaviour. A semantic “warning” role can remain constant while a macOS SwiftUI control behaves differently from an HTML button. Don't force a desktop app to feel like a web app solely for code reuse.

## CI/CD minimum standards
For large projects:
- token schema validation;
- lint/typecheck;
- unit and interaction tests;
- keyboard and focus coverage;
- screenshot/visual regression;
- accessibility automation;
- bundled size/performance checks;
- manual acceptance of release candidate.
Include repository status and version. Check if a public example is maintained, archived, experimental or historical.

## “Done” standard
A design-system component isn't done because it's in Figma. It must be documented, implemented or intentionally marked design-only, tested and adopted in a real context. Brand identity has to survive the component implementation; avoid making every product feel like the same shadcn preset.

## Sources
[IBM Carbon GitHub](https://github.com/carbon-design-system/carbon), [GitHub Primer React](https://github.com/primer/react), [Microsoft Fluent UI](https://github.com/microsoft/fluentui), [Radix Primitives](https://github.com/radix-ui/primitives), [shadcn/ui](https://github.com/shadcn-ui/ui), [HashiCorp Helios](https://github.com/hashicorp/design-system), [W3C WAI-ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/), [Design Tokens Community Group](https://www.designtokens.org/).