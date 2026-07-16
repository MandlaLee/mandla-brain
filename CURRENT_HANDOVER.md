# Current Handover Brief

**Snapshot date:** 16 July 2026  
**Purpose:** Give a new AI enough current context to continue Mandla’s work without depending on earlier private conversations.

This document is a snapshot. The structured records and actual project repositories remain the source of truth.

Read these additional files before touching code:

- `REPOSITORY_INDEX.md`
- `CANONICAL_MEMORY.md`
- `STUDENT_ACCOMMODATION_SUCCESSOR.md`
- `GAME_PROJECT_RELATIONSHIPS.md`
- `CLIENT_AND_COLLABORATIVE_SITES.md`

## Who Mandla is

Mandla Lee Ndlovu is a South African freelance web developer, graphic designer, musician, author and game creator. His core web skills are HTML, CSS, JavaScript and MySQL. He frequently uses GitHub Pages and custom domains.

His primary machine is an Early-2015 Intel MacBook Air with 4 GB RAM running macOS Monterey 12.7.6. Solutions must not casually assume Apple Silicon, large memory, modern macOS-only software or heavy local infrastructure.

Mandla uses AI as an engineering, creative and strategy partner. He expects practical action, preservation of real deliverables and continuity across models.

## Canonical-memory principle

Some details may appear small or unusual to another AI but are canonical to Mandla. Explicit distinctions, names, symbols, relationships, product meanings and project rules must be preserved exactly unless Mandla changes them.

Do not collapse similar-looking projects into one merely because an AI finds the distinction inconvenient. Examples include:

- KOTA versus Township Shop Tycoon
- Kingship production versus historical Kingship repositories
- Soil & Spear versus old Shaka’s Adventure repositories
- the different roles inside the FYER ecosystem

## Repository editing authority

Mandla permits connected AI assistants to inspect and cross-edit his accessible repositories and reuse strong work across his own projects. This permission comes with responsibility:

- identify production, staging, prototypes and historical copies;
- inspect actual files before rewriting;
- preserve working behaviour;
- test before claiming completion;
- do not overwrite live production from an older repository;
- record major migrations and source-of-truth changes here.

## Immediate project state

### Kingship Christian Centre

Kingship is live and time-sensitive.

- Live domain: `kingshipcentre.co.za`
- Production: `MandlaLee/thethrivegeneration`
- Staging: `MandlaLee/test`
- Production is the boss/current website.
- `kingship`, `Kingship_Official` and `testthrive` are historical.
- `AuditionsKCC`, `Auditions` and `Kingship-CC-Website` are abandoned.
- `Kingship-Links` is retained for a future link/follow subdomain.

Current roadmap:

- Phase 2 administration completed through Batch 3H
- Phase 3 automation and integration
- Phase 4 admin portal

Auditions remain inside the official website. The page should be simplified so visitors reach the form quickly without unnecessary scrolling or distraction. The system accepts both direct video upload and video links. Application records go to Google Sheets and uploaded files go to Google Drive.

The exact audition requirements on the live official site are canonical. Inspect production before changing duration, file-size, format or link rules.

Production already received the major image, logo, favicon, WhatsApp, leadership, ministry, worship, media and gallery replacements. Five sermon thumbnails remain from the latest audit:

1. Built for Purpose
2. A Culture of Prayer
3. Identity in Christ
4. Building Healthy Relationships
5. Leadership as Service

“Faith That Moves” is already installed.

Important next actions:

1. Compare production and staging before more staging work.
2. Inventory every form, Apps Script endpoint, spreadsheet tab and data route.
3. Verify the auditions-to-Sheets-and-Drive flow end to end.
4. Build the integration map.
5. Confirm NPO approval before treating post-registration obligations as active.

### New student-accommodation platform

The future replacement has no name yet. Do not invent one.

The three existing SamLee repositories are historical predecessors:

- `MandlaLee/SamLee`
- `MandlaLee/samlee-estates-1.2`
- `MandlaLee/samlee2`

The new platform should preserve the strongest SamLee concept: many genuinely useful SEO pages organised around UFS, CUT, Bloemfontein locations, NSFAS, room types, affordability, applications, parent concerns and student guides.

CampusKey is being studied using SiteSucker. The goal is to understand its publicly delivered information architecture and customer journey, then build an original improved system.

Important next actions:

1. Finish the CampusKey teardown.
2. Choose the new brand name.
3. Create the replacement repository.
4. reuse the strongest SEO, accessibility, application and conversion patterns from the old builds.
5. Verify the real application workflow.

### Uni Residentia

Uni Residentia was registered through CIPC in 2025 but never operated. The original account access details were lost and its present status is unknown.

Do not assume Uni Residentia is active or use it as the new accommodation brand without verification.

### Soil & Spear

Soil & Spear is being built in Godot 4 through Claude.

- Current title: Soil & Spear
- Shaka is a character, not the main character.
- Intended repository: `MandlaLee/Soil`
- Latest project has not yet been uploaded to GitHub.

Historical predecessors:

- `MandlaLee/ML-NETWORK`
- `MandlaLee/SHAKA-WEBSITE`
- `MandlaLee/shakasadventures`

Do not use the old Shaka repositories as the current source code.

The next reliable technical audit should happen after Mandla uploads the latest Godot project to `MandlaLee/Soil`.

### ML Network

ML Network is Mandla’s intended game-studio identity. It remains a concept with zero released games. Its existing repository mainly reflects the old Shaka’s Adventure period.

### KOTA

KOTA is a stationary behind-the-counter kota-shop game. The player prepares food, serves customers, unlocks ingredients and characters, and upgrades the shop from a shack into a restaurant.

A previously claimed Claude build was not preserved. Recover or regenerate it in smaller saved bundles.

### Township Shop Tycoon

`MandlaLee/Township-Shop-Tycoon` is a separate movement-based pixel RPG/shop simulation. It includes village movement, truck travel, factory restocking, shelf placement and broader shop management.

Do not merge it with KOTA. Shared technology can be considered later, but the games have different player experiences.

### Cohortly

Cohortly should work like Linkfire meets Songwhip: universal music links, attractive public release pages, attribution, campaign tracking and fan intelligence.

The project is stagnant, not abandoned. Neither existing repository satisfies Mandla:

- `MandlaLee/cohortly`
- `MandlaLee/Cohortly-Deepseek`

A fresh architecture can replace both after reusable parts are inspected.

### FYER ecosystem

Canonical names:

- BgFyer
- WebPfyer
- BrandFyer
- DocuFyer
- Fyer

Purpose:

- BgFyer removes backgrounds.
- WebPfyer becomes the universal converter for images, PDFs, documents and web assets.
- BrandFyer handles brand discovery and assets.
- DocuFyer becomes the office/document environment.
- Fyer becomes the main Canva-style creative workspace.

Repository state:

- `MandlaLee/WebPfyer` is the only working FYER version.
- `MandlaLee/BgFyer` is an incomplete prototype.
- `MandlaLee/BGREMOVER-` is historical.

The long-term goal is to reduce dependency on Canva, Microsoft Office, iLovePDF-style tools and separate brand-asset services.

### 123Kasi

The static owner-uploaded MVP is more advanced than earlier memories suggested. The folder-to-album feed, generated `data/feed.json` and GitHub Actions feed updates are implemented.

Public user uploads would be a later backend product stage requiring storage, authentication and moderation.

### Jasper Samuel official website

`MandlaLee/JasperSamuel` is Jasper Samuel’s official personal website, separate from but closely connected to Kingship.

It needs:

- a custom domain;
- a real store backend or an Amazon-linked catalogue.

### Ntiyiso publishing project

Ntiyiso is Mandla’s former partner and has a Facebook audience of approximately 38,000. She agreed to be the public-facing partner for selling books through Amazon.

The project is stalled because Mandla has not yet written the books. The website repository is not proof of an existing catalogue.

### Lerato Ka Mihla Maintenance Services

A friend asked Mandla to help create a business through CIPC. Mandla also built a website for free. The process stalled after the CIPC customer profile was created, the friend did not return, and the website was never published.

It may later become a polished portfolio case study after content and technical verification.

### Mandla portfolio

`MandlaLee/MandlaLee` is the current portfolio repository. Mandla considers it mediocre.

Do not merely redesign it with more placeholders. First polish the strongest real products and case studies, then rebuild the portfolio around proof of work and a clear route to paid enquiries.

### Discarded repository

`MandlaLee/slider` is discarded and must not be treated as active.

## Commercial priority

Mandla needs existing work converted into visible, deployable and sellable proof. Prefer:

- finishing WebPfyer and the FYER foundation;
- rebuilding the student-accommodation platform under a strong new brand;
- turning Kingship and Jasper Samuel into strong case studies;
- reviving Cohortly as a real product;
- polishing the portfolio around working products and real client work.

Do not automatically add more concepts when existing work can be finished and sold.

## Known risks

- An older repository may be mistaken for production.
- Staging may be behind production.
- A planned feature may be mistaken for implemented code.
- An AI may erase a canonical distinction because it seems minor.
- Builds may be described as complete without being preserved.
- The user’s 4 GB Intel Mac may be ignored.
- Projects may remain impressive ideas instead of becoming income-producing products.

## Required behaviour before ending substantial work

1. Save or commit the deliverable.
2. Verify it exists.
3. State exactly what was completed.
4. Record the location.
5. Update the relevant memory and unresolved work.
6. Leave a clear next action.

## Best first action for a new AI

Ask Mandla which project he wants to continue. Then read the relevant project records, `REPOSITORY_INDEX.md`, unresolved tasks and the actual working repository. Do not ask him to repeat settled information.