# 23 — Research Sources, Primary References, GitHub Repositories and Evidence Registry

**Research version:** 7 November 2026. This catalog includes official standards and original organization docs, public GitHub implementations, practitioner analyses and published research. Links serve as provenance and starting points; product documentation can evolve. A listed source is not a universal recommendation or an authorization to reuse its artwork. See [Chapter 20](20_GITHUB_REPO_STUDY.md) for original practical comparisons.

## How to use this catalogue

**Normative / standards**: rules to check against intended conformance. **Official platform documentation**: correct platform interaction conventions, sometimes advisory. **Official open-source implementation**: actual code and documented project patterns. **Peer-reviewed research**: general findings with limits, not proof of commercial causality. **Practitioner critique/guide**: useful tested experience and opinion, often subjective. **Visual inspiration**: examples and galleries, not proof of functionality or audience outcomes.

Read the original source relevant to the current task and record access date, relevant section and version. If a reference is missing or unavailable, state that rather than invent its content. Check licenses/trademarks before copying code, fonts, logos or assets.

## A — Human-computer interaction and accessibility: primary standards

| Source | URL | Type | What to examine |
|---|---|---|---|
| W3C WCAG 2.2 | https://www.w3.org/TR/WCAG22/ | Normative | Text contrast, use of colour, resize, reflow, focus, motion, target size and semantics |
| W3C contrast minimum | https://www.w3.org/TR/WCAG22/#contrast-minimum | Normative | Normal text 4.5:1, large text 3:1; understand exceptions |
| W3C use of colour | https://www.w3.org/TR/WCAG22/#use-of-color | Normative | Non-colour signals for meaning |
| W3C target size minimum | https://www.w3.org/TR/WCAG22/#target-size-minimum | Normative | Pointer target minimum and exceptions |
| W3C WAI-ARIA APG | https://www.w3.org/WAI/ARIA/apg/ | Normative/example guidance | Dialog, menu, listbox, accordion and keyboard patterns |
| W3C keyboard interface | https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/ | Guidance | Focus order and interaction |
| W3C evaluation toolkit | https://www.w3.org/WAI/test-evaluate/ | Official guidance | Accessibility testing beyond automated scans |
| W3C image tutorial | https://www.w3.org/WAI/tutorials/images/ | Official guidance | Image alternatives and meaningful descriptions |
| W3C SVG2 | https://www.w3.org/TR/SVG2/ | Standard | Vector image definitions and capabilities |

## B — Native platform guidance

| Source | URL | Type | What to examine |
|---|---|---|---|
| Apple Human Interface Guidelines | https://developer.apple.com/design/human-interface-guidelines/ | Official platform | Native component, layout and app behaviours |
| Designing for macOS | https://developer.apple.com/design/human-interface-guidelines/designing-for-macos | Official platform | Desktop menus, panels, multitasking and window interaction |
| Apple Sidebars | https://developer.apple.com/design/human-interface-guidelines/sidebars | Official platform | Sidebar behaviour and hierarchy |
| Apple Toolbars | https://developer.apple.com/design/human-interface-guidelines/toolbars | Official platform | Tool placement and customization |
| Apple App Icons | https://developer.apple.com/design/human-interface-guidelines/app-icons/ | Official platform | Platform icon fidelity and export |
| Apple SF Symbols | https://developer.apple.com/sf-symbols/ | Official platform | Symbols, rendering, licensing and weight alignment |
| Apple SwiftUI navigation | https://developer.apple.com/documentation/swiftui/navigation | Official platform | Native navigation architecture |
| Material Design 3 | https://m3.material.io/ | Official platform system | Mobile guidance and motion principles |
| Material Motion | https://m3.material.io/styles/motion/overview | Official platform guidance | Motion as a way to support continuity |

## C — Open-source GitHub design systems: actual source

| Project | GitHub | Observed role / caveat |
|---|---|---|
| GitHub Primer React | https://github.com/primer/react | React implementation of a large product design system |
| GitHub Primer Primitives | https://github.com/primer/primitives | Core design token/assets patterns |
| IBM Carbon | https://github.com/carbon-design-system/carbon | Multi-package components, icons, type, grid, tokens and motion |
| Microsoft Fluent UI | https://github.com/microsoft/fluentui | React components and version migration across an ecosystem |
| Radix UI | https://github.com/radix-ui/primitives | Accessibility-oriented low-level primitives |
| shadcn/ui | https://github.com/shadcn-ui/ui | Code-owned components; risk of default AI-template aesthetic |
| Ant Design | https://github.com/ant-design/ant-design | Enterprise React patterns and dense forms/tables |
| HashiCorp Helios | https://github.com/hashicorp/design-system | Tokens, Flight icons, documentation and components |
| Porsche Design System | https://github.com/porsche-design-system/porsche-design-system | Brand-inflected components and visual-regression process |
| Equinor Design System | https://github.com/equinor/design-system | Figma, tokens, docs, components, icons |
| Tailwind Headless UI | https://github.com/tailwindlabs/headlessui | Unstyled accessible interaction patterns |
| Chakra UI | https://github.com/chakra-ui/chakra-ui | Theming and accessible components |
| Shopify Polaris | https://github.com/Shopify/polaris | Commerce-specific patterns; verify current package/archive states |
| Adobe Spectrum Web Components | https://github.com/adobe/spectrum-web-components | Current successor family for many Spectrum web components |
| Adobe Spectrum CSS | https://github.com/adobe/spectrum-css | README identifies this legacy repository as archived |
| Meta Astryx | https://github.com/facebook/astryx | Public beta; claims substantial internal use, independently unverified; verify release/status before relying on it |
| Trendyol Komposto | https://github.com/Trendyol/komposto | Android Compose system with screenshot testing and tokens |

**Research quality note:** The repos above were identified through official GitHub repo metadata and public README or discovery results. Several key READMEs were directly fetched, including Primer, Carbon, Fluent, Radix, shadcn, Ant, HashiCorp, Headless UI, Adobe Spectrum CSS and others. This is a curated reading and comparison set, **not a formal independent security, code-quality or production audit of every listed repo**.

## D — Official design-system guidelines and documentation

| Organization | URL | Focus |
|---|---|---|
| Primer | https://primer.style/product/ | GitHub design foundations and product patterns |
| Carbon | https://carbondesignsystem.com/ | Tokens, themes, components, grid and motion |
| Carbon 2x Grid | https://www.carbondesignsystem.com/building-blocks/foundations/2x-grid/overview | Spatial system |
| Atlassian | https://atlassian.design/ | Content, foundations, spacing and components |
| Atlassian spacing | https://atlassian.design/foundations/spacing | Spacing foundation |
| GOV.UK | https://design-system.service.gov.uk/ | Tested public-service patterns and components |
| GOV.UK Getting Started | https://design-system.service.gov.uk/get-started/ | Guided use of existing patterns |
| HashiCorp Helios | https://helios.hashicorp.design | Token/icon/component usage |
| Porsche | https://designsystem.porsche.com | Brand-specific component documentation |
| Adobe Spectrum | https://spectrum.adobe.com/ | Adobe design principles and components |
| Radix UI | https://www.radix-ui.com/primitives/docs | Low-level accessibility API |
| shadcn/ui | https://ui.shadcn.com/docs | Source ownership and components |
| Headless UI | https://headlessui.com/ | Unstyled accessible components |
| W3C Design Tokens Community Group | https://www.designtokens.org/ | Working design-token standardization and format |

## E — Branding, logo and identity

| Source | URL | Type and caveat |
|---|---|---|
| NASA Brand Center | https://www.nasa.gov/nasa-brand-center/ | Official standards/rights guidance |
| NASA Brand Guidelines | https://www.nasa.gov/nasa-brand-center/brand-guidelines/ | Master usage, identity policy, distinct NASA legal protection |
| NASA Historical Manual | https://www.nasa.gov/image-article/nasa-graphics-standards-manual/ | Historical identity case study, not a downloadable asset licence |
| UnderConsideration Brand New | https://www.underconsideration.com/brandnew/ | Practitioner critiques and case studies; inherently evaluative |
| Ehrenberg-Bass research | https://assets.marketingscience.info/annual-report-2009.pdf | Branding research and distinctive assets concepts |
| WIPO Traditional Cultural Expressions | https://www.wipo.int/en/web/traditional-knowledge/tce | Cultural expressions and rights |
| GS1 Barcodes | https://www.gs1.org/standards/barcodes | Print/packaging barcode constraints |
| International Color Consortium | https://www.color.org/ | Colour management and ICC references |
| Adobe bleed/marks | https://helpx.adobe.com/indesign/using/marks-bleeds.html | Print production guidance |

## F — Research into psychology, usability and perception

| Publication | URL | Type and important limitation |
|---|---|---|
| Jonauskaitė & Möhr colour-emotion review | https://pubmed.ncbi.nlm.nih.gov/39806242/ | Peer-reviewed review; 132 studies, 42,266 participants, 64 countries; abstract association ≠ guaranteed behavior |
| Aslam cross-cultural colour in marketing | https://www.tandfonline.com/doi/abs/10.1080/13527260500247827 | Academic cross-cultural marketing colour review |
| Nielsen Norman Group 10 heuristics | https://www.nngroup.com/articles/ten-usability-heuristics/ | Widely used UX inspection principles, heuristic not experimental proof for a given design |
| Nielsen Norman Group aesthetic usability | https://www.nngroup.com/articles/aesthetic-usability-effect/ | Beautiful interfaces may mask usability flaws |
| Nielsen Norman Group first impressions | https://www.nngroup.com/articles/first-impressions-human-automaticity/ | Short-exposure research; not task-conversion proof |
| Nielsen Norman Group visual design study guide | https://www.nngroup.com/articles/visual-design-in-ux-study-guide/ | Structured design topics and practitioner guidance |
| NN/g Usability Testing 101 | https://www.nngroup.com/articles/usability-testing-101/ | Practical testing method |
| NN/g recognition vs recall | https://www.nngroup.com/articles/recognition-and-recall/ | Navigation and memory load guidance |

## G — Web product quality, content and performance

| Source | URL | Scope |
|---|---|---|
| Google Search Central SEO starter | https://developers.google.com/search/docs/fundamentals/seo-starter-guide | Search content and site technical fundamentals |
| web.dev Web Vitals | https://web.dev/articles/vitals | Performance metrics, not conversion guarantee |
| web.dev Responsive Design | https://web.dev/learn/design | Responsive web practice |
| W3C image alternative text | https://www.w3.org/WAI/tutorials/images/ | Accessible image handling |
| MDN | https://developer.mozilla.org/ | Browser standards and implementation patterns |

## H — Cultural and geographic context

| Source | URL | Scope and caveat |
|---|---|---|
| South African History Online | https://www.sahistory.org.za/ | South African historical context; verify specific claims |
| South African National Heritage Council | https://www.nhc.org.za/ | Heritage research entry point |
| UNESCO culture | https://www.unesco.org/en/culture | Cultural expression and heritage concepts |
| WIPO Traditional Cultural Expressions | https://www.wipo.int/en/web/traditional-knowledge/tce | Rights and safeguarding |
| Relevant local creators and speakers | Primary interviews or permissioned archives | Necessary to validate real meanings; no fabricated interview results |

## I — Technical limits of source use
1. The existence of a repository and stars do not prove accessibility or engineering quality.
2. A README can be outdated. Verify active release/branch, archived status and actual tested code paths.
3. “Free” and open source do not necessarily mean trademark, font, imagery or brand assets are available for reuse.
4. User-interface screenshots can demonstrate a design pattern but do not independently prove conversion, accessibility or reliability.
5. An empirical colour-emotion association should not be reported as universal causation in buyer behaviour.
6. A case-study agency's reported business lift may be self-attributed or uncontrolled; independent validation required.
7. Normative standards are scoped. WCAG conformance claims need criterion-by-criterion evaluation of a real target.
8. User-specific canon is sourced from the user's decisions, not from general web research.

## J — Source-review log template
For future additions:
```text
DATE ACCESSED:
SOURCE URL / EXACT PAGE:
AUTHOR OR ORGANIZATION:
SOURCE TYPE (normative/peer-reviewed/official docs/repo/practitioner/inspiration):
VERSION / RELEASE / REPO BRANCH:
WHAT WAS ACTUALLY READ OR EXECUTED:
RELEVANT OBSERVATION:
LIMITATIONS / CONFLICTS:
LICENCE / TRADEMARK NOTES:
CONCLUSION THAT CAN BE TRANSFERRED:
PROJECT-SPECIFIC VALIDATION NEEDED:
```

## Research methodology for this library
Research combined official web design/branding guidance, multiple semantic search workstreams across strategic branding, logo systems, psychology, typography and GitHub design systems, plus direct connected GitHub repository metadata and official README fetches. Findings were organized as practical guidance and linked to original sources where relevant. This is a curated handbook, not an independently peer-reviewed original academic study. For new platform versions, date-sensitive standards or future design toolchains, verify against current sources.

## Reference use and ethics
The manual consists of original synthesis and short attributed references; it does not redistribute protected brand manuals in full, copyrighted illustrations or third-party fonts. Do not commit external logo images into this public repo for convenience. The source library is maintained so another assistant can cross-check before designing.