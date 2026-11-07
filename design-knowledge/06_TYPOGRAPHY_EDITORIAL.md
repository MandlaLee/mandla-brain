# 06 — Typography and Editorial Design

## Type is architecture
Typography is not a font picker. It determines hierarchy, pacing, reading efficiency, personality, information density and product identity. The quality of an interface can be transformed without changing its colours simply by improving weight, proportion, line length, numbers, alignment and content rhythm.

## Typeface selection criteria
Evaluate each family for:
- readable letterforms at actual size and screen resolution;
- distinguishable I/l/1 and 0/O and numbers critical to the product;
- cap proportions, x-height, counters, terminals, word shapes and character spacing;
- supported scripts, accents, Xitsonga and multilingual copy needs;
- weights and variable font availability;
- licensing for web embedding, app distribution, print, logo modification;
- rendering across browser engines and native OS releases;
- consistent character across display, body and technical data;
- available italic and bold styles, not synthetic rendering if avoidable;
- brand differentiation from category norms.

System fonts are often excellent in native apps. A bespoke display font can still create identity in headings while leaving dense data and labels on a reliable system face. Avoid importing three unrelated families merely to mimic a gallery image.

## Type roles
Define role tokens rather than individual ad hoc values:
- Display: rare expressive headlines in campaigns or editorial.
- H1/H2/H3: structural hierarchy based on content, not only visual size.
- Body large/body: reading and explanation.
- Label: controls, forms, captions and status.
- Metadata: secondary timing, authorship, data source and annotations.
- Numeric: prices, statistics, times and table values—tabular where aligned.
- Code/technical: monospaced content when alignment and scanning require it.

Assign a family, size, line-height, weight, letter-spacing and case rule per role. Capitalisation is a semantic choice: all-caps is often useful for brief controls but can impair rapid reading in paragraphs.

## Practical scale system
Do not apply a preset modular scale blindly. Start from actual content and screen:
- Compact desktop label: often around 11–13 CSS px equivalent depending on environment; ensure readability on target display.
- Comfortable body: often 15–18 px on web with sufficient line height; adjust for font metrics and reading distance.
- Subheads: distinct enough to show hierarchy without becoming a forest of oversized titles.
- Display: based on physical space and meaningful emphasis, not chosen solely to look dramatic.

These ranges are **starting hypotheses**, not universal laws. Native SwiftUI text sizes, printer points and browser CSS pixels have different rendering contexts. Test on the real device and scale settings.

## Line length and measure
Avoid both too-wide editorial columns and cramped multi-line metadata. Consider roughly 45–75 characters per line as an initial reading-text benchmark, then validate font, language and viewport. Dense tables and short labels follow different rules. Use maximum content width for paragraphs; don't centre long blocks of text just because the hero is centred.

A good line-height supports scan and reading: too tight creates visual clutter; too loose fragments sentences. Compare actual letterforms rather than relying on a universal numeric ratio. Ensure zoom/reflow does not clip content.

## Whitespace and hierarchy
Whitespace is an active structural element. More whitespace is not always more elegant: a trading terminal needs information density, while an artist biography benefits from rhythmic breathing room. Establish relationships using vertical spacing: spacing within a group should be smaller than spacing between independent groups. Repeated baselines and alignment matter more than arbitrary round corners.

## Optical alignment
Geometric equality is not visual equality. A triangle, circle and square may need different padding to feel centered. A logo lockup may need visual adjustment despite matching grid coordinates. All-caps micro-labels often need tracking; headings typically need less. Compressed buttons and small icons can require per-asset optical correction, but record exceptions to prevent random inconsistency.

## Numerical typography
For trading, financial, inventory, timers and dashboards:
- use tabular figures for vertically aligned values;
- state the unit consistently (ZAR, USD, %, pips, R-multiple);
- distinguish positive/negative with signs and placement, not colour alone;
- align decimal points when comparison matters;
- show precision appropriate to instrument, not fabricated extra decimals;
- group thousands according to locale;
- reserve monospaced type for data requiring alignment, not every brand headline.
A small typographic error in an SL value can become a product safety issue.

## Editorial hierarchy for websites
Lead with what the visitor is trying to decide. Use an expressive title only when its content is meaningful; follow with a brief credible explanation and proof. Structure headings according to document semantics and reading order. Avoid alternating random fonts and sizes between page sections. Product cards do not need to duplicate an entire heading system if their function is scanning.

## Typography for logos
Assess wordmark as letter shapes and whole-word silhouette. Letterspacing should be optical; custom forms must preserve readability. If a wordmark depends on a proprietary font, record license and construct final vector outlines where appropriate. Preserve a correct textual brand name separate from outlined logo assets for accessibility and search.

## Multi-language typography
Check glyph coverage and fallback for Xitsonga and English (and any other intended language). A font with impressive Latin headlines may render accented or unusual characters poorly. Test translated strings for expansion. Avoid faux-African decorative fonts as shorthand for culture. Language can contribute authentic identity through content and voice rather than stereotypes.

## Contrast, density and conditions
Light grey tiny text on dark blue looks “premium” on a designer's screen but can fail under glare or older hardware. Use text colours as semantic tokens and measure contrast. Test 200% zoom, bold text, low resolution, colour inversion and printed proofs where relevant. Spacing hierarchy should remain intact when type scales up.

## Type QA checklist
- Is the reading order obvious without colour?
- Are key values readable and distinguishable?
- Are all heading levels meaningful?
- Are numeric columns and units aligned?
- Does a longer name or translated sentence fit?
- Do letters render at intended operating system and zoom?
- Are branded and functional typography roles separate?
- Are font licences documented?
- Are title and caption line lengths controlled?
- Is an emphasis level being overused?
- Are there orphaned words, awkward breaks or clipped labels?
- Does the final screen remain recognisable when its colour is removed?

## Sources
[Primer typography foundations](https://primer.style/product/getting-started/foundations/), [IBM Carbon type](https://www.carbondesignsystem.com/), [NASA brand typography](https://www.nasa.gov/nasa-brand-center/brand-guidelines/), [Nielsen Norman Group visual hierarchy](https://www.nngroup.com/articles/visual-design-in-ux-study-guide/), [WCAG text resize and spacing](https://www.w3.org/TR/WCAG22/).