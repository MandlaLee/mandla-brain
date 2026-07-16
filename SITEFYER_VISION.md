# SiteFyer Vision

**Status:** Confirmed product direction; V1 planned

**Canonical name:** SiteFyer

SiteFyer is the FYER ecosystem product for downloading, mirroring, inspecting and eventually comparing publicly delivered websites. It is intended to replace Mandla's dependency on SiteSucker while becoming more useful for website study, preservation, rebuilding and ongoing monitoring.

## Product identity

SiteFyer is not merely a one-page downloader. Its long-term identity is a website-mirroring and website-intelligence workspace that can preserve publicly delivered site files, make them usable offline, organise the result and later explain how the website is structured.

It belongs to the FYER ecosystem alongside BgFyer, WebPfyer, BrandFyer, DocuFyer and Fyer.

## Current implementation priority: V1 Mirror Mode only

Do not begin with Study Mode, Compare Mode, cloud collaboration or a heavy browser-rendering system. The first release must focus on creating a reliable local mirror from a public website.

### V1 content scope

Mirror Mode must download:

- HTML pages
- CSS files
- JavaScript files
- images
- SVG files
- fonts
- favicons
- web manifests
- PDFs
- other publicly linked documents
- video files directly hosted by the website
- assets referenced inside CSS
- assets referenced through `srcset`
- assets referenced through `<picture>` elements
- assets referenced through inline styles

### Minimum mirror behaviour

The downloaded result should preserve enough structure for practical offline use:

- crawl internal public pages within the selected scope;
- preserve or recreate a sensible directory structure;
- avoid downloading the same resource repeatedly;
- rewrite internal page and asset references to local paths where possible;
- record failures instead of silently omitting them;
- produce a crawl manifest showing what was requested, downloaded, skipped or failed;
- allow the user to choose a destination and preserve the completed mirror as a normal folder, with ZIP export considered part of the practical delivery workflow.

These behaviours support Mirror Mode; they must not expand V1 into analysis or comparison features.

## V1 architecture direction

A completely browser-only GitHub Pages application cannot reliably fetch arbitrary public websites because browsers enforce cross-origin restrictions. SiteFyer V1 should therefore be a lightweight local application:

1. A browser-based interface opened on the user's computer.
2. A small local server that performs crawling, downloading and file writing.
3. A local output folder containing the mirrored site and crawl manifest.

The implementation should favour lightweight HTTP downloading and HTML/CSS parsing before introducing full browser automation. It must remain practical on Mandla's Early-2015 Intel MacBook Air with 4 GB RAM and macOS Monterey.

## Explicit V1 exclusions

The first release does not need:

- Study Mode reports
- Compare Mode or change monitoring
- accounts or cloud synchronisation
- team collaboration
- login automation
- private dashboard capture
- paywall or access-control bypassing
- backend, database or private API reconstruction
- streaming-platform video extraction
- perfect mirroring of every complex JavaScript application
- a heavy browser engine for every page

SiteFyer works with files and pages publicly delivered by websites. It does not imply access to private server systems.

## Future mode: Study Mode

After Mirror Mode is stable, SiteFyer may analyse the captured website and generate:

- page inventory
- sitemap-style hierarchy
- navigation structure
- headings and metadata
- internal and external link reports
- image, font, CSS and JavaScript inventories
- repeated component observations
- form and public endpoint observations
- SEO structure
- accessibility observations
- screenshots
- content clusters
- broken-link and missing-asset reports
- structured teardown files suitable for learning and original rebuilding

Study Mode should support Mandla's clean-room workflow: inspect what a public website openly delivers, learn from its information architecture and user experience, then create an original implementation with Mandla's own code, branding, content and improvements.

## Future mode: Compare Mode

A later version may revisit a previously mirrored website and identify:

- new or removed pages
- changed text
- changed images and assets
- navigation changes
- metadata changes
- new CSS or JavaScript files
- file-size changes
- other meaningful public-front-end differences

## Future technical expansion

After the lightweight crawler is reliable, SiteFyer may add:

- optional JavaScript-rendered crawling for sites that require browser execution;
- a remote rendered-site worker when Mandla's local hardware is insufficient;
- desktop packaging for macOS, Windows and Linux;
- pause and resume across long jobs;
- saved crawl profiles and recurring comparison jobs;
- deeper reporting and screenshot automation.

These are later phases and must not delay the first usable mirror release.

## FYER ecosystem integration

Future connections may include:

- sending downloaded images and web assets to WebPfyer for conversion and optimisation;
- sending discovered logos, colours and brand assets to BrandFyer;
- generating website-study reports through DocuFyer;
- managing SiteFyer projects inside the main Fyer workspace.

## Canonical boundary

The confirmed current direction is:

> Build SiteFyer V1 as a lightweight local Mirror Mode product that downloads the complete publicly delivered file set listed above. Preserve the larger Study and Compare vision in memory, but do not build those modes until Mirror Mode is reliable and preserved.
