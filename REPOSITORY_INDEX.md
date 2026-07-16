# Repository Index

**Audit date:** 16 July 2026

This file maps Mandla Lee Ndlovu’s GitHub repositories to the projects they belong to. Repository names alone are not reliable indicators of current direction. Read the role and source-of-truth status before editing anything.

## Interpretation rules

- **Production** means the live source that must not be changed casually.
- **Staging** means the controlled testing area for work intended for production.
- **Active** means the repository still represents a current product or useful foundation.
- **Historical** means it is retained to explain evolution or preserve reusable work, but it is not the current implementation.
- **Abandoned** means it must not be revived as the current direction unless Mandla explicitly changes that decision.
- **Concept** means the brand or project remains valid but the repository is not yet a satisfactory implementation.
- **Source of truth pending** means Mandla has confirmed the direction but the replacement repository has not yet been created or uploaded.

## Current source-of-truth repositories

| Project | Repository | Role | Notes |
|---|---|---|---|
| Mandla Brain | `MandlaLee/mandla-brain` | Active source of truth | Cross-model memory, decisions, project continuity and repository map. |
| Kingship Christian Centre | `MandlaLee/thethrivegeneration` | **Production** | Live at `kingshipcentre.co.za`. This is the boss/current website repository. |
| Kingship Christian Centre | `MandlaLee/test` | **Staging** | Test new Kingship features here before production. Sync carefully because production may contain newer fixes. |
| Kingship follow page | `MandlaLee/Kingship-Links` | Selected future foundation | Intended eventually for a follow/link page such as `follow.kingshipcentre.co.za`. It began as a Cohortly test using Kingship as the subject. |
| Mandla portfolio | `MandlaLee/MandlaLee` | Current portfolio | Official current portfolio repository, but the presentation is considered mediocre and should be upgraded after stronger products are polished. |
| WebPfyer | `MandlaLee/WebPfyer` | Active working foundation | The only FYER repository currently considered a working version. It must expand from WebP optimisation into a universal converter. |
| Jasper Samuel | `MandlaLee/JasperSamuel` | Official personal website | Official site; missing a custom domain and a working store backend or Amazon-linked sales flow. |
| 123Kasi | `MandlaLee/123Kasi` | Active MVP | Folder-based media feed with generated `data/feed.json` and GitHub Actions automation. |

## Source of truth not yet on GitHub

| Project | Intended repository | State |
|---|---|---|
| Soil & Spear | `MandlaLee/Soil` | The current Godot 4 project is being developed through Claude. Mandla will upload the latest build and announce when this repository exists. |
| New student-accommodation platform | Name and repository pending | It will replace all SamLee website repositories under a new brand while preserving the strong multi-page SEO architecture. |

## Kingship repository family

| Repository | Classification | Instruction |
|---|---|---|
| `MandlaLee/thethrivegeneration` | Production | Protect it. Inspect before editing. Use staging for risky changes. |
| `MandlaLee/test` | Staging | Current testing repository. Never assume it is ahead of production without comparing commits. |
| `MandlaLee/Kingship-Links` | Future active concept | Preserve for the future Kingship follow subdomain. |
| `MandlaLee/kingship` | Historical | Early church website. Do not treat as current. |
| `MandlaLee/Kingship_Official` | Historical | Older full static website generation. Do not revive as production. |
| `MandlaLee/testthrive` | Historical | Earlier staging/bundle copy. |
| `MandlaLee/v0-hello` | Abandoned experiment | Kingship link-page/v0 experiment; `Kingship-Links` is the selected future follow-page foundation. |
| `MandlaLee/AuditionsKCC` | Abandoned historical prototype | Record for history only. Do not continue or deploy. Official auditions remain inside the main Kingship website. |
| `MandlaLee/Auditions` | Abandoned empty repository | Do not use. |
| `MandlaLee/Kingship-CC-Website` | Abandoned empty repository | Do not use. |

### Kingship auditions canonical direction

- The audition form remains inside the official website in `thethrivegeneration`.
- Reduce page distraction and scrolling rather than moving the system into a separate auditions product.
- Accept both direct video upload and a video link.
- Store application records in Google Sheets and uploaded files in Google Drive.
- The exact current requirements on the official live website are canonical. Future assistants must inspect the live production form before changing durations, file sizes, accepted formats or link rules.

## Student accommodation repository family

| Repository | Classification | Instruction |
|---|---|---|
| `MandlaLee/SamLee` | Historical predecessor | Preserve its broad multi-page SEO approach and useful content architecture. |
| `MandlaLee/samlee-estates-1.2` | Historical repaired predecessor | Preserve accessibility, SEO fixes, application scripts and repaired structure as reference. |
| `MandlaLee/samlee2` | Historical combined predecessor | Preserve its stronger conversion pages and broader SEO structure as reference. |
| `MandlaLee/Uni-Residentia` | Dormant real company/site concept | Uni Residentia was registered with CIPC in 2025 but never operated. Access credentials were lost and its current legal status is unknown. It is not the SamLee successor unless Mandla later decides so. |

The new accommodation platform has no name yet. Do not invent one. Its canonical product principle is to retain the many useful, genuinely differentiated pages that strengthen SEO while rebuilding the brand and implementation from scratch.

## Game repository family

| Repository | Classification | Instruction |
|---|---|---|
| `MandlaLee/ML-NETWORK` | Active studio concept / historical game site | ML Network is Mandla’s intended game studio, but it currently has zero released games. The existing repository mainly reflects the old Shaka’s Adventure era. |
| `MandlaLee/SHAKA-WEBSITE` | Historical | Old promotional site from before Soil & Spear. |
| `MandlaLee/shakasadventures` | Historical browser prototype | Old JavaScript/canvas game prototype. Soil & Spear is now a Godot 4 project. Preserve useful ideas but do not treat this as the current game. |
| `MandlaLee/Township-Shop-Tycoon` | Separate active game concept/prototype | Not KOTA. It is a movement-based pixel RPG/shop simulation where the player moves around the shop and village, drives home or to a factory, restocks and places products on shelves. |

### Soil & Spear canonical direction

- Soil & Spear is the current name.
- Shaka is a character in the world, not the protagonist.
- The current game is under active Godot 4 development through Claude.
- The future GitHub repository is `MandlaLee/Soil`.

### KOTA versus Township Shop Tycoon

- **KOTA:** behind-the-counter service game with no character movement; the player makes kotas, unlocks customers and ingredients, and decorates a shop from shack to restaurant.
- **Township Shop Tycoon:** free movement in a pixel RPG-style shop and village; travel, restocking, shelf placement and wider business simulation.

They may share South African retail themes, but they are separate games and must not be merged casually.

## Cohortly repository family

| Repository | Classification | Instruction |
|---|---|---|
| `MandlaLee/cohortly` | Stagnant unsatisfactory product attempt | The product vision remains valid, but this implementation does not satisfy Mandla. |
| `MandlaLee/Cohortly-Deepseek` | Historical static prototype | Preserve only as a prototype/reference. |

Cohortly’s canonical vision is a music smart-link and fan-intelligence platform combining the strengths of Linkfire and Songwhip. The project is stagnant, not abandoned. A fresh architecture may replace both repositories.

## FYER ecosystem

| Repository | Classification | Instruction |
|---|---|---|
| `MandlaLee/WebPfyer` | Working active foundation | Expand into the universal converter. |
| `MandlaLee/BgFyer` | Incomplete prototype | Background removal product; not yet accepted as a working version. |
| `MandlaLee/BGREMOVER-` | Historical predecessor | Earlier background-removal experiment. |

Canonical product names and capitalisation:

- **BgFyer** — background removal
- **WebPfyer** — universal converter for images, PDFs, documents and web assets
- **BrandFyer** — brand discovery, retrieval and brand-asset workflows
- **DocuFyer** — document creation and office-suite replacement
- **Fyer** — the main Canva-style creative environment and umbrella workspace

The long-term goal is a connected creative ecosystem that reduces Mandla’s dependency on Canva, Microsoft Office, iLovePDF-style services and separate brand-asset tools.

## Portfolio, client and publishing repositories

| Repository | Classification | Context |
|---|---|---|
| `MandlaLee/MandlaLee` | Current portfolio | Upgrade after the products and strongest case studies are polished. |
| `MandlaLee/LeratoKaMihla-Maintainance-Services` | Unpublished friend project | A friend asked Mandla to create a business through CIPC. Mandla also built the website for free. The CIPC process stalled after creating the customer profile, the friend did not return, and the website was never published. |
| `MandlaLee/Ntiyiso` | Stagnant publishing partnership | Ntiyiso is Mandla’s former partner and has a Facebook audience of roughly 38,000. She agreed to front a book-selling project using Amazon, but Mandla has not yet written the books. |
| `MandlaLee/JasperSamuel` | Official personal website | Separate official site closely connected to Kingship; needs domain and commerce/store integration. |
| `MandlaLee/slider` | Discarded | Do not preserve as an active project. Delete or archive later when convenient. |

## Other active or useful repositories

| Repository | Classification | Notes |
|---|---|---|
| `MandlaLee/123Kasi` | Active MVP | Automated folder-to-album media site. |

## Repository editing authority

Mandla permits connected AI assistants to inspect and cross-edit all accessible repositories with broad creative freedom, including reusing strong code and patterns across his own projects. This permission does not remove the duty to:

1. identify production versus staging;
2. inspect the current files before rewriting;
3. preserve working behaviour;
4. avoid exposing secrets or private user records;
5. test before claiming completion;
6. record major cross-repository migrations in Mandla Brain.

## Canonical-memory warning

Some facts may appear minor, unconventional or non-canonical to an AI but are canonical to Mandla. Explicitly marked names, symbols, relationships, philosophies, distinctions and settled meanings must be preserved unless Mandla personally changes them. Do not silently “normalise” his world into what seems more standard.