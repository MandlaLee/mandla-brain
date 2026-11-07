# 08 — Layout, Composition and Visual Hierarchy

## Composition is how information becomes understandable
Good layouts prioritize action, reveal relationships and give each element sufficient space relative to importance. A twelve-column grid is a tool, not a guarantee of quality. Start by understanding the structure of content: a chart needs different geometry from a promotional essay, a maintenance-service list and a social interview poster.

## Information hierarchy
For each screen or page, write an ordered list of what a first-time user must understand in five seconds, what matters during active use and what can be hidden until requested. Allocate visual emphasis accordingly. A giant title above a tiny trading chart is wrong if chart analysis is the core task. A wall of equally weighted cards makes priority unclear.

## Grid strategy
Establish a modular spacing scale, a baseline rhythm and deliberate columns. The IBM Carbon 2x Grid offers a useful example: an 8-pixel mini-unit, responsive scaffolds, controlled gutter patterns and several layout models suited to editorial versus high-density product work. It is not a command to force 16 columns into every application; adapt to real needs.
Source: [Carbon 2x Grid overview](https://www.carbondesignsystem.com/building-blocks/foundations/2x-grid/overview).

## Content-first layout models
- **Editorial model:** text, image and narrative flow; controlled measure and pacing.
- **Product/content model:** navigation, reading area, contextual tools and clear task hierarchy.
- **High-density model:** full-width workspace, data tables, charts and direct interaction.
- **Campaign model:** one strong moment, distinct typography, memorable imagery and a simple next step.
- **Transactional model:** focused step-by-step progression with visible errors and confidence.
- **Service directory model:** search/filter results with meaningful scanning and accessible structure.

A brand can support more than one model across touchpoints while using a consistent identity grammar.

## Proportion and alignment
Align real content, not just component edges. Common optical defects include text baselines falling out of rhythm, icon bounding boxes miscentered, inconsistent edge padding, nested cards with unaligned gutters, random heading offsets and uneven whitespace. Create major anchors for header, primary content, secondary rail and footer. Inspect at full-size screenshot and zoom in to catch irregular spacing.

## Density as a task requirement
Information density is not an enemy. Compare number of meaningful actions and facts visible without scrolling, their accuracy and readability. Desktop power tools often benefit from compact controls and persistent data context; users may want to collapse panels to enlarge the primary canvas. Marketing pages may benefit from wider editorial rhythm. Too much emptiness can be as harmful as overcrowding.

## Card discipline
Cards are appropriate when elements represent discrete comparable objects, summaries or actions. They are not appropriate as a default wrapper around every paragraph, stat, button and label. Ask whether a border provides meaningful grouping. If removing the card makes the page clearer, remove it. Use one primary content surface rather than a stack of nested rounded rectangles for a chart-centric tool.

## Responsive adaptation
A layout cannot simply shrink uniformly. At narrow widths, change the hierarchy: dock or collapse rails, prioritize one primary task, move secondary data behind accessible controls and keep key actions visible. Validate content reflow with text zoom and long labels. At large widths, do not stretch reading paragraphs across the entire screen; use sensible measure and purposeful margins.

## Balance and negative space
Symmetry can signal stability; asymmetry can create interest, but neither is inherently more professional. Use deliberate weight: a dense photograph might need an open typographic area. An asymmetrical poster must still show event date/location clearly. Negative space separates concepts, not just makes screenshots minimalist.

## Visual rhythm system
Set repeated:
- edge margins and gutter ratios;
- type-baseline relationships;
- space within versus between groups;
- image aspect ratios and crop rules;
- border and separator conventions;
- radius families only where they serve affordance;
- icon optical sizes;
- numerical alignment;
- responsive collapse behaviour.

## Layout testing checklist
At the intended minimum window:
1. Can users see the primary task without scrolling?
2. Are tools discoverable in compact mode?
3. Do loading and error messages fit in the same structure?
4. Do text enlargements or translated strings overflow?
5. Do column widths change proportionally without losing important information?
6. Do empty states leave an understandable purpose?
7. Are fixed and sticky elements preventing access to content?
8. Are touch/pointer/keyboard targets reasonable for the input modality?
9. Are alignment relationships consistent across screens?
10. Does the design remain recognisable when names/logos are hidden?

## Example—Aurum layout lesson
A trading app on a 1366×768 physical display may have a 1120-pixel working window. Fixed wide side panels can turn the price graph into a narrow decorative element. Use user-resizable or collapsible navigation and an inspector, with the chart the visual anchor. Ensure controls still have discoverable labels/tooltips/keyboard access. Reserve colour for trading direction, warnings and selections, not arbitrary decoration.

## Example—creator media
An interview series poster often depends on human faces, venue/date and host identity. A rigid template of “hero photo, three feature cards, testimonials” is absurd. Compose around subject, thumbnail crop, typographic signature, high-contrast location/time and repeatable episode numbering.

## Sources
[Carbon 2x Grid guidelines](https://www.carbondesignsystem.com/building-blocks/foundations/2x-grid/guidelines), [Primer layout](https://primer.style/product/getting-started/foundations/), [Apple Designing for macOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-macos), [Atlassian spacing guidelines](https://atlassian.design/foundations/spacing), [Nielsen Norman Group visual design](https://www.nngroup.com/articles/visual-design-in-ux-study-guide/).