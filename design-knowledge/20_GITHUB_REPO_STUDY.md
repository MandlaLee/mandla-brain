# 20 — Open-Source GitHub Design Systems: Comparative Study and Adaptation

**Research pass: 7 November 2026.** The official repositories and accessible README files of the projects below were examined through the connected GitHub source. The comparisons describe documented architecture and useful design practices, not an exhaustive line-by-line audit or an independent usability benchmark. Verify current release, archival state and licence before actual code reuse.

## What to study in code, not only in screenshots
Every useful design-system repo reveals decisions about:
1. **Foundations:** typography, semantic colour, spacing, grid, elevation, icon sizing.
2. **Token architecture:** raw primitives versus semantic aliases and components.
3. **Component contracts:** behaviour, keyboard, accessibility, variants and disabled/error states.
4. **Application patterns:** forms, table pages, navigation, filters, detail views, modals and responsive layouts.
5. **Governance:** docs, release notes, migration guides, contributions, deprecations.
6. **Quality systems:** CI, unit tests, screenshot/visual regression, a11y testing, Storybook or demos.
7. **Brand expression:** how the system carries recognizable identity without forcing the same screen everywhere.
8. **Licensing:** whether source can be reused, under which terms, and whether icons/fonts/assets have separate rights.

The right outcome is a set of **adaptable principles**. Copying the demo site's particular buttons, cards, colours, logo or default dashboard makes Mandla's work look like a relabelled template.

## Comparative matrix

| Repository | Core emphasis observed in official source | Useful transferable lesson | What not to imitate |
|---|---|---|---|
| [GitHub Primer React](https://github.com/primer/react) | GitHub's React implementation of Primer; product foundations and components | High-density product clarity, accessibility and consistent interactive components | GitHub's visual identity, repo-specific navigation without adapting tasks |
| [IBM Carbon](https://github.com/carbon-design-system/carbon) | React/web components, Sass, colour/type/layout/motion tokens, icons, pictograms | End-to-end foundations and token/component alignment at scale | Enterprise ceremony or IBM-branded visual language in small apps |
| [Microsoft Fluent UI](https://github.com/microsoft/fluentui) | Components supporting a large Microsoft web product ecosystem and version migrations | OS ecosystem consistency, detailed states and migration discipline | Microsoft-specific appearance in unrelated creator products |
| [Radix Primitives](https://github.com/radix-ui/primitives) | Low-level accessible and customisable primitives | Separate functional accessibility from visual identity | Mistaking unstyled primitives for complete UX or brand direction |
| [shadcn/ui](https://github.com/shadcn-ui/ui) | Open source code distributed for ownership/adaptation | Own implementation rather than depending on a rigid black box | Shipping recognizable default shadcn styling as the finished brand |
| [Ant Design](https://github.com/ant-design/ant-design) | Enterprise-class React library and design language | Form/table density, predictable complex-app interaction and composition | Overcomplicated enterprise controls for simple products |
| [HashiCorp Helios](https://github.com/hashicorp/design-system) | Components, tokens, Flight icons, documentation, tooling | Versioned shared components and coherent icon/token governance | Copying HashiCorp icon assets or cloud-console patterns indiscriminately |
| [Porsche Design System](https://github.com/porsche-design-system/porsche-design-system) | Branded web components, tokens, quality tooling, visual tests | Strong brand expression coexisting with production engineering | Borrowing Porsche's distinct protected aesthetic/assets |
| [Equinor Design System](https://github.com/equinor/design-system) | Figma tooling, React components, token packages and icons | Design-to-code asset pipelines and multidisciplinary governance | Heavy enterprise tooling when a simple project needs fewer moving parts |
| [Tailwind Headless UI](https://github.com/tailwindlabs/headlessui) | Unstyled accessible interaction components | Build original brand styling around robust behaviour | Treating ready-made behaviour as a complete visual design |
| [Chakra UI](https://github.com/chakra-ui/chakra-ui) | Accessible component primitives and styling foundations | Responsive/state consistency and scalable theming | Default components as substitute for content architecture |
| [Adobe Spectrum Web Components](https://github.com/adobe/spectrum-web-components) | Modern Spectrum component implementation | Cross-product interaction consistency and web component strategy | Adobe brand identity or proprietary imagery |
| [Adobe Spectrum CSS (archived)](https://github.com/adobe/spectrum-css) | Earlier CSS implementation of Spectrum | Learn historical component structure and migration thinking | Treating an archived repo as the primary current stack |
| [Shopify Polaris](https://github.com/Shopify/polaris) | Commerce design patterns and repository lineage | Merchant workflows, practical patterns and clear content guidance | Reusing old archived packages or a merchant-only UI for unrelated apps |

## Primer: product clarity and accessibility
The official Primer React README describes the React implementation of GitHub's Primer Design System and points to its documentation. Its relevance to Mandla is a disciplined way to build consistent interactive tools with accessibility expectations and reusable variants. GitHub products often display complex code, issues and tables; their information density is worth studying for developer tools, dashboards and administrative software.

**Adapt:** semantically named tokens; coherent focus, controls and table patterns; responsive hierarchy; documented icon conventions.  
**Do not copy:** GitHub logo/corporate styling, repository-specific terms, a workbench architecture where an app has a different core task.  
**Study paths:** [README](https://github.com/primer/react/blob/main/README.md), [Primer docs](https://primer.style/react/), [Primer foundations](https://primer.style/product/), [Primer primitives](https://github.com/primer/primitives).  
**Suggested experiment:** build the same settings panel using native controls and a custom component system; compare focus behaviour, label clarity and cramped layout before deciding.

## Carbon: foundations that extend into production
Carbon's official repo explicitly separates packages for design tokens, colour themes, type, layout, motion, grid, icons, pictograms and components. This matters: an identity can be expressed through coordinated roles and consistently deployed, not an assortment of hardcoded style values. For a small native app, Carbon is useful as a *systems thinking reference*, not a dependency that should be copied into SwiftUI.

**Adapt:** layout rhythm, semantic token separation, component state inventory, pictogram-versus-icon distinction and quality automation.  
**Avoid:** enterprise breadth as an excuse to build 500 components before validating the main user task.  
**Study:** [repo](https://github.com/carbon-design-system/carbon), [grid guidelines](https://www.carbondesignsystem.com/building-blocks/foundations/2x-grid/guidelines), [design foundations](https://carbondesignsystem.com/).

## Fluent UI: ecosystem conventions and state coverage
Microsoft Fluent UI supports a broad product ecosystem. Its README discusses multiple React generations, illustrating that migrating design systems is itself an ongoing engineering challenge. For Mandla projects this is a lesson in preserving stable user behaviour when styles, packages and patterns evolve. Do not blindly mix incompatible generations or use web patterns to fake native macOS behaviour.

**Adapt:** component contracts, state handling, consistent affordances, accessible interaction and migration planning.  
**Avoid:** imposing Microsoft corporate branding on cultural or creator identities.  
**Study:** [Fluent UI repo](https://github.com/microsoft/fluentui) and current project docs linked from it.

## Radix and Headless UI: behaviour separate from brand
Accessible unstyled primitives are an antidote to the notion that a component library must determine your entire brand. These repositories emphasize keyboard/focus behaviour and accessibility while leaving styling responsibility with the implementer. This separation is especially useful when original visual language matters.

**Adapt:** interaction contracts, dialog/menu/listbox behaviour, test patterns and predictable accessibility.  
**Avoid:** treating the presence of accessible primitives as proof the final product is accessible. Colour, content, responsive layout and task design still need testing.  
**Study:** [Radix](https://github.com/radix-ui/primitives), [Headless UI](https://github.com/tailwindlabs/headlessui).

## shadcn/ui: code ownership with a visual trap
shadcn/ui's README presents customisable open code that developers can adapt. This is excellent for source ownership and practical extension. But it creates a specific risk: an AI assistant may assemble a dashboard using default cards, round corners and colours and assume the system is finished. The result can be technically good but brand-indistinct.

**Adapt:** learn patterns, understand component source, test states and implement intentional variants.  
**Avoid:** a default component gallery becoming the actual brand concept. Change task hierarchy, spatial model, type, interactions and real-content grammar—not simply the accent colour.  
**Study:** [repo](https://github.com/shadcn-ui/ui), [documentation](https://ui.shadcn.com/docs).

## Ant Design: dense enterprise workflows
Ant Design contains many controls suited to data-heavy enterprise applications. Study forms, tables, filtering, navigation and state completeness. It is strong evidence that a working professional tool needs more than visual minimalism. However an entertainment app, artist site or simple utility rarely benefits from inheriting an entire enterprise information architecture.

**Adapt:** complex-form state handling, table conventions, data presentation and form validation.
**Avoid:** administrative density and corporate hierarchy when the user needs a focused creative experience.
**Study:** [repo](https://github.com/ant-design/ant-design).

## HashiCorp Helios: governance and documented tools
HashiCorp's official repository documents component packages, Flight icons, token packages and an MCP-related design-system interface. It demonstrates design-system governance and ways to make guidance available to developers and automated agents. That is relevant to Mandla Brain's desire for cross-model continuity.

**Adapt:** token/source organization, icon exports, documentation and tool-driven reference.  
**Avoid:** unnecessarily replicating a full enterprise platform.  
**Study:** [repo](https://github.com/hashicorp/design-system), [docs](https://helios.hashicorp.design).

## Porsche Design System: brand expression plus rigor
The Porsche repo is particularly relevant to the question “can a design system be distinct rather than generic?” Its official description frames branded products and quality in one component library, and its documentation refers to visual regression approaches. The lesson is that recognizability and engineering accuracy should reinforce each other.

**Adapt:** brand-specific tokens, consistency of detail, release and visual-test discipline.  
**Avoid:** appropriating a luxury automotive company's marks, colour hierarchy or signature styling.  
**Study:** [repo](https://github.com/porsche-design-system/porsche-design-system), [docs](https://designsystem.porsche.com).

## Equinor: design-to-code coordination
Equinor's repo describes Figma assets, published tokens, React components, icons and docs. Its strength is repeatability across designers and engineers. For a multi-project maker, a scaled-down variant can eliminate the mismatch between Photoshop/Canva references and implemented UI.

**Adapt:** token export pipeline, component demos, versioning and icon governance.  
**Avoid:** unnecessary infrastructure for a 3-page portfolio or small utility.  
**Study:** [repo](https://github.com/equinor/design-system).

## Spectrum: check archived status, not just popularity
The original [Adobe Spectrum CSS](https://github.com/adobe/spectrum-css) README identifies the repository as archived and directs readers to [Spectrum Web Components](https://github.com/adobe/spectrum-web-components). This illustrates why raw GitHub star counts and old tutorials are not enough. Never recommend abandoned or legacy components as current production standards without investigating migration paths.

**Adapt:** component documentation, internationalization/accessibility goals, variant analysis and deprecation practices.  
**Avoid:** defaulting to obsolete code merely because a blog contains a polished screenshot.

## Applying findings to Mandla's work
**Aurum:** study Primer's dense navigation, Carbon's tokens, macOS HIG native interactions, and Porsche's precision and visual regression. Build an original chart-first interface, not a cloned React dashboard. Verify signal time, source freshness and real app launch.

**Phala Digital:** use editorial typography and coherent visual identity rather than a generic startup shadcn card template. Build real service content, authentic client case studies and clear WhatsApp/contact process.

**FENRY:** borrow governance and token consistency, not web UI component styles. Physical reproduction and apparel manufacturing should determine artwork forms.

**Mandla Lee creator brands:** emphasize authentic photos, editorial type, motion/episode grammar and source ownership instead of enterprise design-system layouts.

## A repeatable GitHub repo audit template
- Repository, owner, URL and current branch.
- Readme/docs source inspected and date.
- Licence, maintenance/archival status and significant versions.
- Structure: packages, assets, tokens, icons, docs, tests.
- Components of interest and their states/keyboard behaviours.
- Visual language characteristics and brand ownership.
- Evidence of testing and production readiness.
- Strengths transferable as principles.
- Misfits to this product and caveats.
- A proposed original implementation and a validation experiment.
- Attribution and permissible code/asset use.

## A note on open source
A permissive code licence does not automatically license brand marks, screenshots, trademarks, third-party fonts or bundled photographs. Check specific file licences, attribution requirements and trademark policies. Do not upload vendor assets to Mandla Brain merely to make research easier; link the upstream originals.

## Conclusion
The best lesson from the studied repositories is **separation of concerns and discipline**: strong task architecture, brand expression, accessible behaviour, semantic tokens, real content, versioning and repeatable testing. A software library can give excellent buttons; it cannot decide what makes Aurum unmistakably Aurum or a Phalaborwa artist series authentically local. That is creative direction built on research and deliberate choices.

### Reference collection
[Primer](https://github.com/primer/react) · [Carbon](https://github.com/carbon-design-system/carbon) · [Fluent UI](https://github.com/microsoft/fluentui) · [Radix](https://github.com/radix-ui/primitives) · [shadcn/ui](https://github.com/shadcn-ui/ui) · [Ant Design](https://github.com/ant-design/ant-design) · [HashiCorp Helios](https://github.com/hashicorp/design-system) · [Porsche Design System](https://github.com/porsche-design-system/porsche-design-system) · [Equinor Design System](https://github.com/equinor/design-system) · [Headless UI](https://github.com/tailwindlabs/headlessui) · [Chakra UI](https://github.com/chakra-ui/chakra-ui) · [Adobe Spectrum Web Components](https://github.com/adobe/spectrum-web-components).