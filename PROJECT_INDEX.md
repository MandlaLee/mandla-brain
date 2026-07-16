# Project Index

This is the high-level map of Mandla Lee Ndlovu’s active, paused, historical and planned work. It is a navigation document, not a substitute for the project records or actual source repositories.

**Snapshot date:** 16 July 2026

Read [`REPOSITORY_INDEX.md`](REPOSITORY_INDEX.md) before editing code. Repository names alone do not identify the current source of truth.

## Priority lens

When Mandla has not specified another priority, use this order:

1. Work that can protect or generate income soon
2. Time-sensitive Kingship Christian Centre launch, compliance and operations
3. Existing products that are close to a usable delivery
4. Critical bugs, missing artifacts and source-of-truth problems
5. Longer-term creative and game development

Do not use this ranking to override a direct current request.

## Canonical-memory rule

Some facts may look minor or unconventional to another AI but are canonical to Mandla. Read [`CANONICAL_MEMORY.md`](CANONICAL_MEMORY.md). Do not silently merge, normalise or discard explicitly settled distinctions.

---

## 1. Mandla Brain

**Status:** Active infrastructure  
**Repository:** `MandlaLee/mandla-brain`  
**Purpose:** Preserve model-independent continuity across ChatGPT, o3, Claude, Codex and future assistants.

**Core files:**

- `START_HERE.md`
- `AI_INSTRUCTIONS.md`
- `CURRENT_HANDOVER.md`
- `PROJECT_INDEX.md`
- `REPOSITORY_INDEX.md`
- `CANONICAL_MEMORY.md`
- `memory/*.jsonl`
- `projects/*.jsonl`

**Immediate responsibility:** Keep repository roles, active canon, history and unresolved work accurate. Preserve meaningful client, collaborator, idea and project context without confusing old records with current direction.

---

## 2. Kingship Christian Centre

**Status:** Active, live and time-sensitive  
**Live domain:** `kingshipcentre.co.za`  
**Production repository:** `MandlaLee/thethrivegeneration`  
**Staging repository:** `MandlaLee/test`  
**Project memory:** `projects/kingship-christian-centre-ministry.jsonl`

Kingship is the most operationally complex project. It includes worship, music production, prayer, campus ministry, marriage and relationships, outreach, events, administration systems and future automation.

**Current roadmap:**

- Phase 2 administration completed through Batch 3H
- Phase 3: automation and integration
- Phase 4: admin portal
- Additional databases beyond the agreed roadmap are optional backlog

**Website repository rules:**

- `thethrivegeneration` is the boss/current live website.
- `test` is the only current staging repository.
- `kingship`, `Kingship_Official` and `testthrive` are historical.
- `AuditionsKCC`, `Auditions` and `Kingship-CC-Website` are abandoned.
- `Kingship-Links` is retained for a future follow page such as `follow.kingshipcentre.co.za`.
- `v0-hello` is an abandoned experiment.

**Auditions canonical direction:**

- Auditions remain inside the official main website.
- Reduce distraction and scrolling instead of moving auditions into a separate product.
- Accept both direct video upload and a video link.
- Store application records in Google Sheets and uploaded files in Google Drive.
- The exact requirements currently shown on the official live site are canonical. Inspect production before changing them.

**Current website state:**

Production received the major logo, favicon, WhatsApp, leadership, ministry, worship, media and gallery placeholder replacements. The remaining visual gap from the latest audit is five sermon thumbnails:

1. Built for Purpose
2. A Culture of Prayer
3. Identity in Christ
4. Building Healthy Relationships
5. Leadership as Service

The “Faith That Moves” thumbnail is already installed.

**Important next actions:**

- Compare production and staging before further staging work.
- Inventory forms, Apps Script endpoints, spreadsheet tabs and data routes.
- Produce a trusted integration map.
- Verify the live auditions-to-Sheets-and-Drive workflow.
- Prepare post-registration governance and reporting templates after NPO approval is confirmed.

---

## 3. New Student Accommodation Platform — Name Pending

**Status:** Planned rebuild and active research  
**Final name:** Not chosen  
**Repository:** Not created  
**Brief:** `STUDENT_ACCOMMODATION_SUCCESSOR.md`

This new platform will replace all current SamLee website generations under a new name.

**Canonical strength to preserve:**

The SamLee project’s many-page SEO architecture is deliberate and valuable. Preserve useful pages grouped by institution, location, student type, affordability, NSFAS questions, applications, parent concerns and practical university guidance.

**Historical reference repositories:**

- `MandlaLee/SamLee`
- `MandlaLee/samlee-estates-1.2`
- `MandlaLee/samlee2`

Use them as references and sources of strong code or content, not as the final current website.

**Competitive research:**

CampusKey is being studied using a private SiteSucker mirror of its publicly delivered website. Extract principles, identify weaknesses and create an original improved implementation.

**Immediate next actions:**

- Complete the CampusKey teardown.
- Choose the new company and platform name.
- Define the new repository.
- Reuse the best SEO, accessibility, application and conversion patterns from the SamLee predecessors.
- Build and test the real application workflow.

---

## 4. Uni Residentia

**Status:** Dormant historical company; current legal status unknown  
**Repository:** `MandlaLee/Uni-Residentia`

Uni Residentia was registered through CIPC in 2025 but was never used operationally. Mandla no longer has the original account access details.

**Do not:** Assume Uni Residentia is the new accommodation brand or that the company is currently active.

**Next action:** Verify its CIPC status and determine whether access can be recovered.

---

## 5. Soil & Spear

**Status:** Active development in Godot 4  
**Future repository:** `MandlaLee/Soil`  
**Current project location:** Being developed through Claude; latest build not yet uploaded to GitHub  
**Project memory:** `projects/soil-and-spear.jsonl`  
**Relationship brief:** `GAME_PROJECT_RELATIONSHIPS.md`

**Canonical direction:**

- Soil & Spear is the current title.
- Shaka is a character in the world, not the main character.
- The player begins as nobody in Nameless Village.
- The current engine is Godot 4.

**Historical repositories:**

- `MandlaLee/ML-NETWORK`
- `MandlaLee/SHAKA-WEBSITE`
- `MandlaLee/shakasadventures`

These preserve the older Shaka’s Adventure era and may contain reusable ideas, but none is the current source code.

**Current work:** Continue building in Godot, then upload the latest project to `MandlaLee/Soil` and audit the actual state before updating technical blockers.

---

## 6. ML Network

**Status:** Game-studio concept  
**Repository:** `MandlaLee/ML-NETWORK`

ML Network is Mandla’s intended game studio or publisher identity. It currently has zero released games. The existing repository mainly reflects older Shaka’s Adventure promotion.

**Next action:** Reposition the studio around the actual game catalogue once Soil & Spear or another game reaches a demonstrable state.

---

## 7. KOTA

**Status:** In progress; preserved build still unresolved  
**Project memory:** `projects/kota.jsonl`

KOTA is a behind-the-counter South African kota-shop service game. The player does not walk around. The core experience is preparing food, serving distinct customers, unlocking ingredients and characters, and decorating the shop from a shack into a restaurant.

**Do not merge with Township Shop Tycoon.**

**Immediate work:** Recover or regenerate the build in saved bundles and continue the customer, ingredient and shop-progression systems.

---

## 8. Township Shop Tycoon

**Status:** Separate game prototype  
**Repository:** `MandlaLee/Township-Shop-Tycoon`  
**Relationship brief:** `GAME_PROJECT_RELATIONSHIPS.md`

Township Shop Tycoon is a movement-based pixel RPG/shop simulation. The player can move around the shop and village, drive a truck home or to a factory, restock goods, place items on shelves and manage a broader retail business.

It shares a South African township retail setting with KOTA, but the gameplay model is fundamentally different.

---

## 9. Born In Mzansi

**Status:** Early development and system planning  
**Project memory:** `projects/born-in-mzansi.jsonl`

A South African life simulation with modular systems covering ageing, family, education, work, money, health, crime, fame, business, politics and South African cultural data.

**Immediate work:** Continue one verified bundle at a time and preserve each artifact.

---

## 10. Cohortly

**Status:** Stagnant but not abandoned  
**Project memory:** `projects/cohortly.jsonl`

Cohortly should function like Linkfire meets Songwhip: universal music links, attractive public release pages, attribution, campaign tracking and fan intelligence.

Neither current repository satisfies Mandla:

- `MandlaLee/cohortly` — unsatisfactory private product attempt
- `MandlaLee/Cohortly-Deepseek` — historical static prototype

`Kingship-Links` began as a Cohortly test but now belongs to Kingship’s future follow-page plan.

**Next action:** Design a fresh architecture that can become a real deployable and monetisable product.

---

## 11. FYER Ecosystem

**Status:** One working foundation plus planned ecosystem  
**Project memory:** `projects/fyer-ecosystem.jsonl`

Canonical product names:

- **BgFyer** — background removal
- **WebPfyer** — universal converter
- **BrandFyer** — brand discovery and asset workflows
- **DocuFyer** — document creation and office replacement
- **Fyer** — main Canva-style creative environment and umbrella workspace

**Repository state:**

- `MandlaLee/WebPfyer` — the only FYER implementation currently considered working
- `MandlaLee/BgFyer` — incomplete prototype
- `MandlaLee/BGREMOVER-` — historical predecessor

**WebPfyer direction:** Expand the current WebP/web-image optimiser into a universal converter for images, PDFs, documents and web assets.

**Ecosystem goal:** Reduce dependency on Canva, Microsoft Office, iLovePDF-style services and separate brand-asset tools.

---

## 12. 123Kasi

**Status:** Active MVP  
**Repository:** `MandlaLee/123Kasi`

The folder-to-album feed and GitHub Actions generation workflow are implemented. The site generates `data/feed.json` and can update the feed after content changes.

**Future stage:** Public uploads would require backend storage, authentication, moderation and reporting. That is a later product expansion, not part of the current static owner-uploaded MVP.

---

## 13. Jasper Samuel Official Website

**Status:** Official site; commerce and domain incomplete  
**Repository:** `MandlaLee/JasperSamuel`  
**Context:** `CLIENT_AND_COLLABORATIVE_SITES.md`

This is Jasper Samuel’s official personal website, separate from but closely connected to Kingship.

**Missing:**

- Custom domain
- Store backend, Amazon-linked catalogue or another suitable sales flow

---

## 14. Ntiyiso Publishing Project

**Status:** Stagnant collaboration  
**Repository:** `MandlaLee/Ntiyiso`  
**Context:** `CLIENT_AND_COLLABORATIVE_SITES.md`

Ntiyiso has an existing Facebook audience of approximately 38,000 and agreed to be the public-facing partner for selling books through Amazon.

**Blocker:** The books have not yet been written.

---

## 15. Lerato Ka Mihla Maintenance Services

**Status:** Unpublished, stalled friend project  
**Repository:** `MandlaLee/LeratoKaMihla-Maintainance-Services`  
**Context:** `CLIENT_AND_COLLABORATIVE_SITES.md`

The CIPC setup stalled after the customer profile was created, and the friend did not return. Mandla built the website for free, but it was never published.

It may later serve as a polished portfolio case study after technical and content verification.

---

## 16. Website Portfolio and Freelance Growth

**Status:** Active commercial foundation  
**Repository:** `MandlaLee/MandlaLee`

This is Mandla’s current portfolio, but Mandla considers it mediocre. Upgrade it after the strongest products and projects are polished so the portfolio can present real proof rather than weak placeholders.

**Priority case studies:**

- Kingship Christian Centre
- Jasper Samuel
- WebPfyer
- BgFyer when working
- New student-accommodation platform
- Lerato Ka Mihla if completed as a case study
- Cohortly when rebuilt

**Core design rule:** Every project should have a distinct brand world and customer journey. Avoid generic AI templates.

---

## 17. Music — YK Nazarene and Kingship Music

**Status:** Active creative development  
**Project memory:** `projects/music.jsonl`

Create Gospel-centred songs, memorable hooks, TikTok-ready content, streaming releases and worship recordings. Preserve song drafts and release assets rather than leaving them inside temporary generation sessions.

---

## 18. Formfyer

**Status:** Selected but underdefined direction  
**Project memory:** `projects/other-projects.jsonl`

Clarify whether Formfyer remains a standalone product inside or alongside the FYER ecosystem, then define a small deployable first version.

---

## 19. ML CODE

**Status:** Planned  
**Project memory:** `projects/other-projects.jsonl`

A lightweight browser-based code editor with live preview. Keep the first version small and demonstrable.

---

## 20. Children’s Books

**Status:** In progress  
**Project memory:** `projects/other-projects.jsonl`

Includes illustrated books for Eliora and Elroi. A 20-page book titled *The Sleepy Dragon* was completed.

---

## Discarded repository

`MandlaLee/slider` is discarded and must not be treated as an active project.

---

## Personal and technical continuity

**Primary device:** Early-2015 Intel MacBook Air, 4 GB RAM, macOS Monterey 12.7.6.  
**Secondary device:** iMac A1311 awaiting a trusted macOS Sierra recovery path.  
**Education:** UFS 2027 BCom Marketing application was pending in the latest recorded state; verify before updating.

See `memory/identity.jsonl`, `memory/preferences.jsonl`, `memory/timelines.jsonl`, `memory/repositories.jsonl` and `memory/unresolved.jsonl` for structured details.