# Software, AI, desktop utilities and games

## FaceWeave / FaceWeave Live — ACTIVE, top priority
**Goal:** True AI face swapping using uploaded source face on still images and live webcam, on older Intel Mac; local/offline and native macOS app.
- Original app: `~/Desktop/FaceWeave.app`; original Swift sources in `~/Desktop/FaceWeave/Source/`.
- Live app: `~/Desktop/FaceWeave Live.app`; SwiftUI/AVFoundation/Vision/CPU mesh renderer sources in `~/Desktop/FaceWeave/Live Source/`; tests in `Live Tests/`.
- Current live renderer uses Vision landmarks and triangle-based warping, **not** true identity replacement. User video test showed weak swap and intermittent black preview.
- Research checkout: `~/Desktop/FaceWeave/Research/Deep-Live-Cam`; repo `hacksider/Deep-Live-Cam`; Python 3.11.9 from Python.org; venv in checkout.
- Installed compatible versions: NumPy 1.26.4, OpenCV 4.10.0.84, ONNX Runtime 1.19.2. Current repo requirements newer and incompatible with this Mac; avoid source builds.
- Models: `models/inswapper_128_fp16.onnx` (~265 MiB), `models/gfpgan-1024.onnx` (~349 MiB). License/commercial usage unresolved.
- **Verified 2026-11-08:** InSwapper loaded via CPUExecutionProvider, inputs `target [1,3,128,128]` and `source [1,512]`, output `[1,3,128,128]`. Synthetic inference produced finite tensor. Load ~1.95 sec; first inference ~9.85 sec. This **does not prove** successful swap or viable frame rate.
- Missing: compatible identity embedding model (typically recognition/ArcFace family), correct 5-point alignment, image color conversion, inference on actual source/target, compositing, webcam integration, optimization/benchmark.
- Plan A: lean native FaceWeave AI engine, SwiftUI UI retained, CPU or CoreML when proven. Plan B: get original Deep-Live-Cam working using compatible dependencies. Preserve both existing apps. Test 256p/360p; profile RAM and latency.
- **Next:** locate/install licensed compatible face embedding model, verify real still-image swap, integrate camera, benchmark repeated frames and optimize. No claim of completion yet.

## SenAI — existing utility and future deferred expansion
- Historical name: user's previous assistant “SenAI,” described by user as funny, diligent, remembered jokes/failures and maintained a list of postponed ideas. Current ChatGPT assistant accepted same name **without claiming to be the original**. See `senai/handoff-letter-2026-11-08.md`.
- Existing local `~/Desktop/SenAI.app`; sources `~/Downloads/SenAI_Project/`; zip `~/Downloads/SenAI.zip`. Python 3.9 stdlib Tkinter GUI/CLI. Commands: doctor, download, setup venv, build, test, debug, repo clone, models scan, assets, verify, backup, JSON pipeline.
- CLI doctor reportedly worked; GUI launch not verified; Gatekeeper warning appeared. Not a general autonomous coding LLM.
- Deferred: safe unattended local development assistant with allowlisted builds/tests/backups/logs, resource limits and approval boundaries. Revisit after FaceWeave works.

## Aurum — macOS trading signals
- Native macOS app, Xcode/Swift; initially XAUUSD, later NAS100 and US30. Signal-only, no automatic trade execution.
- Features requested: live chart, 1m–1y timeframes, S/R and role switches, supply/demand, BOS/CHoCH, 8am high/low and 9am 1H FVG context, entries, $ markers, TP/SL, historical opportunities, notifications, offline fallback, zoom/pan, diagnostics, backtesting BUY then SELL.
- Providers: Twelve Data; Yahoo Finance trial for US30/NAS100 when free feed questioned. **Live data accuracy remains to be verified.**
- Problems: missed BUY, WAIT logic, entries misaligned across timeframes. Requested 100 historical tests, final bugfix, professional brand and collapsible side panels.
- Desktop shortcut: preserve older version renamed “Aurum old”; new shortcut to updated build. Backup requested `Aurum backup` on Desktop. **Actual present state requires inspection.**

## TIRHANI (formerly JOBBOT AI) — local job assistant
- Intel 4GB, strictly local AI, no paid APIs. Continuous job matching/application assistance; voice push-to-talk and local Mac commands.
- Visual: subtle Tsonga culture, floating movable true sphere, no border/background, Siri-like waves.
- Movement bug reported twice and later reported fixed. Asked for all phases and very large text-pattern library (“billions”); this is a request, **not evidence it was implemented**.
- Job application actions need user review and safe boundaries.

## IDGEN 2.0 — synthetic SA ID test utility
- macOS native utility for synthetic South African ID test data; date/year/month/gender, valid checksum, random/sequential, manual count, CSV export as text (no scientific notation), optional TEST label, no separators in raw digits.
- Custom “Bovoza mode” sequence 080–089 incrementing; earlier request to remove “TEST” then acceptance to retain it.
- Compiled .pkg, installation into Applications fixed after initial failure, branded box-like package icon and UI overhaul requested/reported. Desktop code folder and shortcut. **Use only in controlled synthetic testing; do not target real identities or government systems.**
- Earlier spreadsheet outputs called “spotify 100” and folder “spotify 03NOV” requested.

## DOLBOT — synthetic mock CFONLINE test bot
- User's mock website `https://mandlalee.github.io/CFONLINE/`. Reads DOB/gender/name parameters; generates synthetic test IDs, uses John/Doe defaults, submits to mock endpoint, records outcomes (ID found, first name invalid, surname invalid, ID not found) in `~/Desktop/DOL.txt` with timestamp.
- GUI: WhatsApp-like, green-circle logo with flipped DB face, start inputs, Get Individuals button, animated slime circle, results table.
- Mac app `DOLBOT Dev.app` and launch shortcut requested/created in past sessions; launch/debug work and final review requested. Reported waiting for mock database connection; **do not assume connected**. No real government data probing.

## Hodela Restaurant — local Mac cooking game
- Separate from Township Tycoon (leave Township Tycoon unchanged).
- Inspired by order-preparation games, but distinctly kasi: kotas, fatcakes, chips, russians, shack made from corrugated/zinc sheets, wooden counter, customer sprites, ingredients, dialogue UI.
- User provided sketch and references, requested scene image then transparent individual sprites, added character and further polish. Supporting asset sheet/concept art exists in user files.
- Native playable desktop icon requested, **not a web game**. No verified finished playable build.

## Other software / product ideas
- **Cohortly:** link-in-bio analytics (clicks, device, location, referrer, cancellation, streaming site), liquid-glass Next.js/React UI. Status unknown.
- **FOTOFYER:** on-device photo→PDF, JPG→PDF, compressor, background remover, document scanner. Status unknown.
- **AppFYER:** ZIP-to-app converter. Status unknown.
- **Township Tycoon:** separate game; do not replace with Hodela Restaurant.
- **Face swapping companion research:** user explored Deep-Live-Cam, live overlay, helper bot downloading dependencies and combination of bots into SenAI.
- **SC19 automation:** `automation.py` and `sc19-auto.py` on Desktop, user requested launching/testing. Current code/status unknown; inspect rather than assume working.
