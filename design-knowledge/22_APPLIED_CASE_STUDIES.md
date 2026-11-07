# 22 — Applied Case Studies and Project-Specific Design Directions

**Scope:** This chapter applies the handbook's methods to known categories and illustrative briefs. It records design *criteria and hypotheses*, not approval of a new visual direction, name, palette, marketing claim or technical implementation. For actual work, read the latest current project repository, user brief and canonical memory; those take precedence.

## Case A — Aurum: native macOS trading assistant

### Product premise
Aurum is a native macOS trading analysis assistant with Gold at its core, other experimental market feeds, signal-first operation and historical review. Its defining user job is to interpret market price action, inspect signal conditions, locate reference entry/stop/targets, and distinguish confirmed or historical opportunities from current executable quotes. It runs on an older Intel MacBook with limited RAM. It is not an auto-execution trading bot.

### Design problem
Aurum's earlier interfaces resembled an AI-generated dashboard: oversized metric cards, dark navy background, rounded panels, floating price chart and decorative toolbar elements. The user found the general appearance polished but generic. Later feedback requested smaller, independently minimizable side panels and reliable trade markers that align across chart timeframes. Quality includes solving these interaction problems, not merely inventing new gradients.

### Appropriate research references
- [Apple macOS HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-macos): native menu, sidebar, toolbar, focus/window conventions.
- [GitHub Primer](https://primer.style/product/): dense professional data UI and accessible controls.
- [IBM Carbon](https://www.carbondesignsystem.com/): semantic tokens and consistent data visualization grammar.
- [Porsche Design System](https://designsystem.porsche.com/): precision, restrained identity and visual regression discipline.
- Professional charting apps as observed product references: study information hierarchy and plot interaction, not branding or proprietary indicators.

### Primary visual hierarchy
1. Market / chart timeframe / source / last candle time / data freshness.
2. Dominant price graph with readable axes and restrained overlays.
3. BUY/SELL/WAIT state with honest confirmation and decision limitations.
4. Entry/SL/TP and risk/reward in inspectable but collapsible context.
5. Historical opportunity timeline, filter and navigation.
6. Signal diagnostics, settings, download/cache and backtesting as optional depth.

### Design system thesis
More like a well-calibrated analytical instrument than a default SaaS dashboard. Distinction may emerge through type, precision of lines, tool grammar, consistent spacing and a carefully developed original mark. Avoid commodity neon-purple “fintech” look, arbitrary candles in logo, excessive colour, stacked cards and fake alert urgency.

### Component requirements
Chart, price axis, time axis, position marker, zone band, signal line, price ladder, status chip, provider freshness, market selector, timeframe selector, history strip, collapsed nav rail, inspector, diagnostics and safety note. Each has a loading/error/cached state. The graph should occupy the maximum feasible space at 1120px window width.

### Critical tests
- 1m/5m/15m/1h historical entry projection preserves time and price.
- Live signal only when reference candles are recent and completed.
- SL below BUY and above SELL, TP direction valid.
- No “profit guarantee” or executed-order wording.
- Network loss shows cache clearly; history remains inspectable.
- No repeated expensive scans every quote tick.
- Sidebar/inspector minimized independently; state restored after restart.
- Full-screen screenshot has no line or label collision.
- Memory/CPU stays reasonable on a 4GB Intel Mac.
- Installer, desktop alias and signed bundle launch correctly.

### Possible distinctive creative route (unapproved)
A restrained graphite/ink instrument with one unusual blue geometry and a custom monospace numeric hierarchy, with large dark chart workspace and selective high-contrast decision colours. This is an artistic hypothesis. The current blue mark and established user approval should be respected until a new identity is explicitly accepted.

## Case B — Phala Digital: local web-development service

### Premise and customer job
A locally rooted digital service helps an owner-operated business understand the available web package, see real proof, request a quote and feel confident that publication and support are clear. The work is judged by live websites, actual contact flows and portfolio credibility rather than trends.

### Creative challenge
Avoid two common traps: generic coding-bracket tech logos and cream/black minimalist agency templates with vague “We craft digital excellence” copy. The brand needs a distinctive point of view connected to actual service and market realities.

### Strategic hypotheses
- Clarity and trustworthy examples matter strongly to the target client.
- Local relevance is valuable when documented through real projects, not generic “Africa” patterns.
- The brand could use unusual geometric forms or typographic treatment while maintaining a businesslike tone.
These assumptions need client interviews and a current service brief before public claims.

### Website architecture
Offer and inclusions → selected live client projects → process from brief to launch → scope/pricing if current/approved → FAQs/ongoing support → verified contact and WhatsApp. Distinguish genuine client work from sample concepts. Live URLs and screenshots must be validated; no invented testimonials.

### Brand applications
Logo on site header and invoice, social avatar, proposal template, service pricing card, project case study, WhatsApp introduction and portfolio thumbnails. The identity should remain consistent without relying on one big gradient hero.

### QA
Verify all live client URLs, responsive navigation, form submission, WhatsApp links, copy accuracy, image rights, offer pricing accuracy, site metadata, performance and accessibility. Test on South African mobile connectivity.

## Case C — FENRY: apparel identity under production constraints

### Premise
FENRY is a clothing label; current design decisions must respect approved brand personality and physical printing constraints, including limited colours and avoided gradients/thin lines where specified by the user.

### Design challenge
A digital image generator might create spectacular photographic graphics that cannot be screen printed or reproduced in embroidery. Treat production as a design material.

### Creative process
1. Clarify capsule theme, garment style, audience and actual printer method.
2. Develop a recognisable visual grammar: mark, typography, repeat motifs, placement, print hierarchy.
3. Build one-colour and limited-spot versions first.
4. Test chest pocket, full front, back, care label and hang tag.
5. Obtain supplier tolerances for fine gaps and stitching.
6. Create garments with multiple neutral/fabric colours.
7. Produce a physical sample if possible.
8. Document approved print files, colour separations and asset ownership.

### Anti-patterns
Random aggressive bear/animal motifs with no brand rationale, copied luxury monograms, disposable “streetwear” graphics, gradients that cannot print, unlicensed typography, mockups alone and inconsistent capsule identities.

### QA
Do mono/contrast reductions; confirm print colour count, line thickness and vendor proof; preserve vector master and correct brand spelling. Check that no prohibited violent imagery appears in capsules where excluded.

## Case D — Mandla Lee: artist, interview host, creator identity

### Premise
A creator-led brand must allow music releases, video interviews, event coverage and public persona to coexist. The host's credibility and personality are central assets, while each series needs repeatable packaging.

### Identity architecture questions
Is the interview series “Mandla Lee presents...” or a separately named show endorsed by the host? Does the music artist mark appear directly, or should the video use a separate editorial signature? How do collaborations with local event brands look? These are project decisions to be confirmed, not invented.

### Recognition asset system
- A distinct typographic opening title and on-screen lower third.
- Consistent small face-aware video thumbnail layout, series numbering and event marker.
- A limited recurring colour and motion vocabulary.
- A short audio/visual ident where legally permissible.
- Reusable guest/venue credits without obscuring faces.
- Original portrait photography and real locations.
- Editable thumbnail and lower-third templates for repeated production.

### Design challenge
Do not trap the creator into imported podcast-tech styling. Visual grammar can emerge from actual personality, Xitsonga expression, street interviews, music culture and documentary authenticity. A blurred stock city image or random safari colours would not represent the work.

### QA
Test thumbnails at phone size, title comprehension, audio captions, correct artist/venue credit, face likeness and actual event sponsorship permissions. Preserve a brand system flexible enough for future music/video content.

## Case E — Hodela Restaurant and local food game art

### Premise
A stylised township restaurant service game is judged by the consistency and playability of its environment, sprites, menus and interactions. A beautiful static scene is not a game-ready sprite atlas.

### Visual direction
Study reference mobile restaurant games for clarity, then establish a specific local environment informed by real food spots. A corrugated-sheet “zinc” shack, timber counter and recognisable ingredients can be deliberately stylised while respecting actual context. The design should not arbitrarily introduce brick shopfronts or unrelated props contrary to the user's approved sketch.

### Production requirements
Camera angle, asset scale, sprite bounding boxes, transparent background, separate hit areas, character animation states, layering, inventory of objects, UI contrast and build target. Test each image in the engine at actual size and movement. Maintain distinct detail levels for foreground interactables and background decoration.

### QA
Original art assets generated or commissioned with consistent geometry, transparent sprites with no matte edges, proper animations, playable collision/hit zones, responsive UI, save flow and installed Mac build when a native game is required.

## Case F — Kingship Christian Centre / ministry media

### Premise
The project has an established source-of-truth repository, stage/production distinction and approved theological and visual identity. Any change must read current canon and production before designing.

### Visual concerns
Church visitors may need service times, location, leadership, discipleship streams, event information and appropriate giving/contact. The site should be accessible to newcomers and avoid performative animation. Brand imagery can be contemporary and spiritually grounded without generic stock worship photos as a substitute for real community.

### Governance
Verify current ministry name, approved visual marks, branch architecture, feature requirements and source repository. Preserve production through staging comparison. Avoid creating separate app pages that duplicate agreed official forms. Only use real permissioned imagery and claims.

## Case G — Multi-brand projects and client work

### Problem
A portfolio across construction, property, maintenance, towing, publishing and digital tools cannot become one visual template merely because it shares a developer. Each brand needs distinct industry fit, proof, audience and content. “Template reuse” can mean component and engineering reuse, but should not mean identical visual direction.

### Cross-project portfolio QA
An assistant should compare five project screenshots with logos hidden. If each is the same hero and three cards, redesign the visual languages. Preserve shared engineering quality (accessibility, responsive behaviour, form reliability, maintainable code) while making each brand's structure and imagery distinctive.

## Case-study decision record
For each live project capture: current brief, intended audience, source repo, existing approved design, reference products, visual thesis, alternatives considered, meaningful differences, interactions, actual screenshots/tests, open issues and verified artifact location. Update this chapter only with project-owner approval when a proposed hypothesis becomes canonical.

## Related chapters
[Brand Strategy](02_BRAND_STRATEGY_POSITIONING.md) · [Logo Engineering](04_LOGO_DESIGN_ENGINEERING.md) · [Native Desktop](10_NATIVE_DESKTOP_APPS.md) · [Cultural Context](17_CULTURAL_CONTEXT_SOUTH_AFRICA.md) · [QA](19_CRITIQUE_QA.md).