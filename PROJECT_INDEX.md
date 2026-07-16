# Project Index

This is the high-level map of Mandla Lee Ndlovu’s active, paused and planned work. It is a navigation document, not a substitute for the project JSONL files or actual source repositories.

Statuses reflect the known state on 16 July 2026 and must be verified against current artifacts when work resumes.

## Priority lens

When Mandla has not specified another priority, use this order:

1. Work that can protect or generate income soon
2. Time-sensitive Kingship Christian Centre launch and compliance work
3. Existing projects that are close to a usable delivery
4. Critical bugs or missing artifacts that block progress
5. Longer-term creative and game development

Do not use this ranking to override a direct current request.

---

## 1. Mandla Brain

**Status:** Active infrastructure  
**Purpose:** Preserve model-independent continuity across ChatGPT, o3, Claude, Codex and future assistants.  
**Source:** Root Markdown files, `memory/*.jsonl`, `projects/*.jsonl`  
**Current direction:** GitHub JSONL is the durable source of truth; Notion may act as a dashboard and Google Drive as a file vault.  
**Immediate responsibility:** Keep the handover documents current, prevent duplicate or contradictory memories and never store secrets.

---

## 2. Kingship Christian Centre

**Status:** Active and time-sensitive  
**Purpose:** Establish and operate a Christian church and connected ministry ecosystem centred on worship, prayer, campus ministry, marriage and relationships, music production and community outreach.  
**Primary people:** Jasper Samuel is the principal leader referenced throughout the project; Mandla supports strategy, systems, design, web development, branding and operations.  
**Target:** Midrand, Gauteng; launch planning is centred on September 2026.  
**Project memory:** `projects/kingship-christian-centre-ministry.jsonl`  
**Related memory:** `projects/music.jsonl`, `projects/websites.jsonl`, `projects/other-projects.jsonl`, `memory/timelines.jsonl`, `memory/unresolved.jsonl`

**Known website repositories:**

- Production: `MandlaLee/thethrivegeneration`
- Staging: `MandlaLee/test`

**Confirmed brand direction:** Intentional minimalism; bold condensed typography; black, gold and white; structured layouts; restrained brush accents; no random icons, symbols or unnecessary text.

**Major systems and ministries:**

- Kingship Worship
- Kingship Music Production
- Thrive In Two
- Campus / UniThrive ministry
- Prayer ministry
- Open Hands outreach and giving
- Events, media, sermons and galleries
- Administration databases and future admin portal

**Current roadmap:**

- Phase 2 administration was completed through Batch 3H.
- Phase 3 is automation and integration.
- Phase 4 is the admin portal.
- Additional databases beyond the agreed roadmap are optional backlog, not mandatory next phases.

**Important current work:**

- Audit production and staging repositories, forms, Apps Script endpoints, spreadsheet tabs and data routes.
- Continue staging cleanup without risking production.
- Connect event data from Google Sheets through Apps Script or JSON.
- Preserve and verify audition, ministry and application workflows.
- NPO registration has been submitted; future assistants should verify the live status before describing it as approved.
- Prepare and maintain post-registration governance, accounting, annual-reporting and compliance templates without storing private identity details in this public repository.

**Do not:** Change production before staging verification; invent a venue; expose applicant, counselling, banking or identity data.

---

## 3. SamLee Estates

**Status:** Active commercial project  
**Purpose:** Build a student-accommodation company and high-performing information platform for Bloemfontein, especially students connected to UFS and CUT.  
**Company structure:** SamLee Holdings is the holding company; SamLee Estates is the operating brand.  
**Project memory:** `projects/samlee-estates.jsonl`  
**Related:** `projects/websites.jsonl`, `memory/unresolved.jsonl`

**Brand direction:** Institutional UFS-inspired navy, red, white and light-grey system; blue S and red L identity; no glassmorphism.

**Website strategy:**

- Accommodation clusters by audience, institution, affordability and location
- UFS and CUT hub pages
- Bloemfontein location content
- NSFAS guides and FAQs
- Student and parent guides
- 50–100 genuinely useful SEO pages
- Approximately 100 FAQs
- Google Business Profile activity and review growth

**Current competitive study:** CampusKey is a reference for information architecture, UX and commercial presentation. Mandla is using SiteSucker to create a private local mirror of the publicly delivered front end for study. The goal is an original, improved SamLee implementation—not a republished clone.

**Immediate work:**

- Inspect the local CampusKey study archive and extract reusable principles.
- Complete the structured application form, Apps Script endpoint and spreadsheet workflow.
- Build and verify the deployable SamLee site.
- Prioritize pages and features that can attract real enquiries and demonstrate Mandla’s commercial web-development ability.

---

## 4. Soil & Spear

**Status:** In progress; technically blocked  
**Purpose:** A 2D isometric role-playing game set in an alternate or stylised 1800s Southern Africa, inspired by the depth and freedom of Hero’s Adventure while maintaining an original world, art direction and systems.  
**Project memory:** `projects/soil-and-spear.jsonl`  
**Related:** `memory/timelines.jsonl`, `memory/unresolved.jsonl`

**Current engine:** Godot 4. Godot 3.5 was abandoned because of scaling blur and development friction.

**Core direction:** Begin as nobody in Nameless Village; choices, reputation, factions, multiple endings, regional trade, training, literacy, healing, farming, hunting, forging and relationship systems.

**Art direction:** Isometric or angled top-down pixel art with chunky readable pixels, dark-brown outlines, warm African earth colours and modular environment assets.

**Immediate blocker:** Resolve global-class parse failures, unresolved `TraitSystem`, type-inference problems and missing method references before promising a Godot-ready build.

**Deliverable goal:** A preserved Godot-ready ZIP and a complete Phase 1 centred on Nameless Village.

---

## 5. KOTA

**Status:** In progress; missing preserved build  
**Purpose:** A South African kota-shop management game inspired by the approachable customer-service loop of Good Pizza, Great Pizza, but rebuilt around South African food, people, humour, regions and culture.  
**Project memory:** `projects/kota.jsonl`  
**Related:** `memory/unresolved.jsonl`

**Core direction:** Customers and ingredients unlock over days; characters from different communities visit the shop; dialogue, reputation, gifts, training, missions and regional culture deepen the simulation.

**Art direction:** Friendly stylised waist-up or waist-high characters on transparent backgrounds, readable silhouettes, authentic variety and no generic stereotypes.

**Known problem:** Claude previously reported completing a build, but the ZIP was not preserved. Treat the build as unresolved unless an actual file is found.

**Immediate work:** Recover or regenerate the build, preserve it early, replace placeholder assets and continue customer chapters in organised batches.

---

## 6. Born In Mzansi

**Status:** Early development / system planning  
**Purpose:** A complete South African life-simulation game with the broad accessibility of BitLife but a distinct interface, identity, systems and local cultural depth.  
**Project memory:** `projects/born-in-mzansi.jsonl`

**Development bundles:** Core engine; navigation; player ageing and history; family; education; careers; money and property; health and death; crime and prison; fame, sports, music and social media; business and politics; South African data.

**Immediate work:** Continue in modular bundles, preserve every generated bundle and avoid attempting the entire codebase as one unverified output.

---

## 7. Music — YK Nazarene and Kingship Music

**Status:** Active creative development  
**Purpose:** Create Gospel-centred songs, memorable hooks, TikTok-ready content, streaming releases and live worship recordings.  
**Project memory:** `projects/music.jsonl`

**Artist identity:** YK Nazarene.  
**Production preference:** Energetic, hype hip-hop or trap with strong bounce and memorable hooks; generation prompts must not rely on naming artists.  
**Constraint:** Suno style prompts must remain within 1000 characters.

**Current ideas:** “I don’t move by fear, I move by faith” and the image of being lost at sea and pulled back to shore by God.

**Immediate work:** Turn ideas into preserved song drafts, release plans and reusable content packages rather than losing work inside generation sessions.

---

## 8. 123Kasi

**Status:** In progress  
**Purpose:** A GitHub Pages media site with folder- or album-based content shown newest to oldest.  
**Project memory:** `projects/other-projects.jsonl`

**Architecture:** Generate `feed.json` automatically with a GitHub Actions `build-feed.yml` workflow and correctly handle deleted content.

**Brand:** Lime-green rounded bold identity with a K favicon inside a lime circle.

**Immediate work:** Complete and verify feed generation and deletion handling in the actual source repository.

---

## 9. WEBPFYER

**Status:** In progress; delivery unresolved  
**Purpose:** A free, private, browser-based image-to-WebP converter.  
**Project memory:** `projects/other-projects.jsonl`, `memory/unresolved.jsonl`

**Immediate work:** Complete, preserve and deliver a downloadable or deployable build. Do not allow another session to end with the project only described but not saved.

---

## 10. Formfyer

**Status:** Selected product direction  
**Purpose:** A form-related product or platform intended to simplify creating and handling web forms.  
**Project memory:** `projects/other-projects.jsonl`

**Immediate work:** Clarify the minimum viable product, business model and relationship to Mandla’s existing Apps Script, spreadsheet and web-form workflows before large-scale implementation.

---

## 11. ML CODE

**Status:** Planned  
**Purpose:** A lightweight browser-based code editor with live preview.  
**Project memory:** `projects/other-projects.jsonl`

**Immediate work:** Define a small, deployable first version instead of overbuilding.

---

## 12. Children’s Books

**Status:** In progress  
**Purpose:** Square illustrated books for Eliora and Elroi, using warm family-friendly storytelling, zoomed-out environments and integrated page text.  
**Project memory:** `projects/other-projects.jsonl`

**Completed milestone:** A 20-page book titled *The Sleepy Dragon* was completed; later work focused on richer vocabulary.

---

## 13. Website Portfolio and Freelance Growth

**Status:** Active commercial foundation  
**Purpose:** Demonstrate Mandla’s range as a South African freelance web developer and convert his skills into paid work.  
**Project memory:** `projects/websites.jsonl`, `memory/preferences.jsonl`

**Core rule:** Every sample must feel like a distinct brand world with its own audience, emotion and customer behaviour. Avoid generic AI templates and repeated site structures.

**Immediate work:** Prioritize polished, deployed, client-relevant examples and a clear sales journey over endlessly expanding the list of hypothetical niches.

---

## Personal and technical continuity

**Primary device:** Early-2015 Intel MacBook Air, 4 GB RAM, macOS Monterey 12.7.6. Heavy local tooling and builds must respect these limits.

**Secondary device:** iMac A1311 awaiting a trusted macOS Sierra recovery path.

**Education:** UFS 2027 BCom Marketing application was pending in the latest recorded state; verify before updating.

See `memory/identity.jsonl`, `memory/preferences.jsonl` and `memory/unresolved.jsonl` for details.