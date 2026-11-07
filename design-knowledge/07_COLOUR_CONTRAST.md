# 07 — Colour Systems, Contrast and Perception

## Colour does several different jobs
A brand palette communicates identity; functional colour communicates state; neutral surfaces support hierarchy; illustration and photography have their own art direction. Treat these as related but separate systems. A brand's primary green does not have to be the colour for every “success” state if that creates ambiguity, and red is never the sole way to communicate loss.

## Colour roles instead of random swatches
Define:
1. Brand primary and secondary, with source-approved variants.
2. Neutral foreground/background/surfaces/borders across light/dark modes.
3. Text primary/secondary/disabled/inverse.
4. Information/success/warning/danger/selection/focus roles.
5. Data visualization series with a colour-blind-safe fallback.
6. Icon and illustration use.
7. On-colour foreground combinations with tested contrast.
8. Print equivalents when required (CMYK, Pantone/spot).
9. Colour restrictions (forbidden pairings, inaccessible small-text usage).
10. Token ownership and change procedure.

## Accessibility is concrete
WCAG 2.2 Level AA requires at least **4.5:1 contrast for ordinary text** and **3:1 for qualifying large text**, with exceptions including logotypes. Non-text UI elements and focus-state visibility have additional requirements. These are accessibility criteria, not a suggestion that every design must look greyscale. Check actual foreground/background combinations *after* transparency and overlays. Don't reuse a visually measured screenshot contrast as the canonical token value without verifying the actual pixels or CSS styles.

Source: [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/), specifically [Contrast Minimum](https://www.w3.org/TR/WCAG22/#contrast-minimum) and [Use of Colour](https://www.w3.org/TR/WCAG22/#use-of-color).

## The palette construction procedure
1. Study current brand assets; preserve recognizable identity where approved.
2. Map tasks and semantic states.
3. Choose neutral canvas levels and readable text scale.
4. Choose primary identity hue(s), then create tonal variants.
5. Test every required foreground/background pair, not isolated swatches.
6. Check dark and light surfaces with true text and actual buttons.
7. Evaluate neutral mode, greyscale, common colour-vision differences.
8. Stress-test in busy photographic content, outdoor use and older monitors.
9. Prepare print proofs and vendor colour references.
10. Create a palette usage guide that specifies proportion and role in context.

## Colour psychology—properly qualified
A 2025 systematic review reports consistent patterns in how colours are associated with emotions across studies and countries, but the associations are **many-to-many** and do not imply a given palette will produce a specific consumer action. Context, culture, brightness and saturation matter. Use proposed emotions as hypotheses, not guaranteed outcomes. Source: [systematic review](https://pubmed.ncbi.nlm.nih.gov/39806242/).

## Dark interfaces
Dark backgrounds are appropriate in many low-light technical and entertainment contexts, but careless dark palettes create low contrast, near-black banding and over-emphasised neon accents. Use several disciplined surface elevations, clear separators only where needed, readable text, selected-state differentiation and purposeful accent distribution. Design screenshots should be checked on the actual target panel; dark contrast is not universal.

## Data visualization
Map meaning consistently. For financial trading:
- BUY/SELL, profit/loss, resistance/support must have text, geometry or direct labels in addition to hue.
- Show actual source/candle timestamps and stale-feed state.
- Ensure series distinguishability against grid, zone overlays and annotations.
- Restrict high saturation to essential signals and exceptions.
- Do not over-encode a single bar with six conflicting colours.
For a multi-series product chart, use unique markers, stroke styles and direct labels where colour alone would fail.

## Print versus screen
HEX/sRGB values are not a guarantee of identical CMYK or fabric printing. Provide approved physical samples, proof references, spot ink specifications and acceptable tolerances when print matters. A digital gradient may be fine in a music poster but inappropriate for a limited-colour apparel screen print. Make a vendor-ready 1-colour version even if digital identity uses many colours.

## Branding with restrained colour
When an existing brand has a recognised primary hue, use that asset consistently without making every component the same colour. Strong identities can use one surprising combination, large neutral areas and distinctive composition. Building “distinctiveness” by random high-contrast accents undermines a system.

## State-colour QA
Check all combinations in the actual working states:
- base, hover, pressed, selected, keyboard focus;
- disabled and loading;
- success, warning, danger and information;
- offline, demo, delayed, historical and live;
- inverse content and photographic overlays.
If a text colour fails contrast on a card background, change it or its role; don't rationalise that it “looks sleek.”

## Implementation hints
Use semantic design tokens rather than hardcoding status colours into components. For example, “text-warning” should be the same functional role on website, macOS and mobile while physical colour values can adapt to platform appearance. Define focus ring as a separate token. Beware opacity: lowering an accessible text colour's opacity may reduce contrast below the target. Version all palette changes.

## Common mistakes
Misusing bright colours for all controls, duplicating red for unrelated data states, mixing arbitrary shadow colours, gradienting the logo despite print constraints, using red/green alone, decorating content with colour psychology myths, setting text so pale it cannot be read, confusing brand primary with danger status, and assuming printer output matches the RGB monitor.

## Source references
[WCAG 2.2](https://www.w3.org/TR/WCAG22/), [Colour-emotion systematic review](https://pubmed.ncbi.nlm.nih.gov/39806242/), [Primer colour guidelines](https://primer.style/product/getting-started/foundations/), [Carbon colour and theming](https://github.com/carbon-design-system/carbon), [NASA standards](https://www.nasa.gov/nasa-brand-center/brand-guidelines/).