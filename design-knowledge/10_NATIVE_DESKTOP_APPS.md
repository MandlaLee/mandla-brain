# 10 — Native Desktop Applications and Professional Workspaces

## Desktop software is not a webpage in a window
A professional desktop app must understand keyboard and pointer interaction, resizable windows, persistent workspaces, menus, OS conventions, system permissions, resource limits, native typography, drag and drop, accessibility and multi-window workflow. Decorative dashboard cards are secondary to the work. A trading assistant needs a large graph and an intelligible signal inspector; a photo converter needs clear file drop/queue; a voice-controlled agent needs understandable listening/permission state.

## Begin with the task surface
Define the screen's dominant object: chart, video timeline, file list, document, canvas, database table or conversation. Give it the most usable area. Organise secondary functions as rails, toolbars, inspectors, popovers and contextual menus. A primary canvas that occupies only 40% of the desktop window because of oversized cards and ornamental sections is a failure.

### Workspace architecture
A flexible macOS layout may use:
- **Global navigation rail** (projects/markets/tools): always visible in compact form, independently collapsible.
- **Primary canvas** (chart/document): resizable, zoomable, scrollable, stateful.
- **Inspector** (properties, trade plan, metadata): context-aware, independently collapsible.
- **Toolbar**: only high-frequency commands, primary status and selection context.
- **Status bar**: accurate source/connection, progress, error and safety information.
- **Quick actions**: menu, keyboard command, command palette where justified.
- **Settings**: system-level behaviour and preferences, not essential context permanently occupying the chart.

Not every app needs all parts. A utility may require only one focused panel with a queue. Judge complexity by the user task, not by the desire to imitate a professional terminal.

## Native conventions
Study the target platform's current Human Interface Guidelines. On macOS, respect menu bar semantics, key commands (Command-R refresh when appropriate, Command-comma preferences, Escape for dismissal), focus, standard scrolling, document/file patterns, accessibility and predictable window movement. Tooltips supplement icon-only tools but do not substitute for accessible names. The placement of navigation and inspectors should be stable through resizing.

### Panel collapse specification
For each side panel document expanded/minimized width, minimum content size, which controls survive in icon-only mode, expansion affordance, keyboard access, persistence across restarts and state transitions. Collapsing a panel must reclaim space rather than leave a vacant margin. A closed inspector should not hide critical warnings or ongoing destructive actions.

### Window-size matrices
Test at:
- user's actual default window dimensions;
- minimum supported width/height;
- maximized and near-fullscreen;
- with each panel open, each closed, and both closed;
- with display scaling and increased text size where supported;
- on small external monitor if applicable.
Inspect actual screenshots, not just a compile. Watch for clipped toolbars, duplicated scrollbars, dialog stacking and overlapped titles.

## Data-dense interfaces
Use hierarchy based on decision:
- What is the user looking at?
- How recent and authoritative is the information?
- What can they do next?
- What context must remain visible while doing it?
- How do they recover from failure?
A trading instrument should align prices with tabular numerals; show units, timestamp and reference interval; separate entry price from order execution; and preserve price scale while switching views. A status badge must describe actual feed state, not serve as branding.

## Chart design
Charts are instruments. Define data source, instrument, currency/unit, timeframe, zone methods, data resolution, session time zone, axis precision, candles completed versus live, gaps, zoom/pan semantics, markers and overlay collision policy. Don't assume that all drawing layers can be shown at once. Use toggles for secondary annotations with clear defaults.

### Historical signal alignment
Assign immutable source signal time (when conditions were confirmed) and actionable time (next available candle). Project onto each chart's actual time coordinate and prices; do not regenerate independent historical entry markers on every displayed timeframe unless the user changes signal basis. Explicitly label differences between signal timeframe and viewing timeframe.

### Financial safety UI
A BUY/SELL marker is not proof of profitability. Show:
- signal rule outcome and rejected conditions;
- source provider, timestamp and stale/offline/demo/historical states;
- reference entry, SL, TP levels and RR;
- current market quote versus last confirmed candle;
- no auto-execution unless separately enabled with explicit authorization;
- known fill/slippage and spread limitations;
- duplicate alert prevention and signal expiry;
- backtesting assumptions and limits.
A visual redesign that alters indicator logic, risk math or data freshness labels without tests can cause financial harm.

## Performance and memory
Design for the actual hardware. On older Intel macOS devices with 4 GB RAM, avoid huge embedded browser processes, repeated full-history recomputation on each tick, excessive blur/filters and hundreds of simultaneously materialized views. Cache validated historical signals keyed by source data, cancel obsolete asynchronous requests, virtualize large tables and measure CPU/memory after a full session. Don't optimize only startup screenshot quality.

### Refresh concurrency
There must be a clear policy when live refreshes overlap:
- one active request per source/key;
- cancel or discard superseded work;
- avoid incorrectly pairing chart data and signal reference data from different generations;
- indicate progress without blocking the user;
- ensure an unavailable reference feed cannot leave an outdated BUY/SELL watch as if current;
- never silently switch to simulated data and label it live.
Test manual refresh while automatic refresh, interval switch and symbol switch occur.

## Error and loading states
A blank chart can mean connecting, no candles, API quota error, unsupported timeframe, weekend market closure or offline cache. Display precise status and next action. Show a clear distinction between “no signal found” and “unable to evaluate signal” and between “last update” and “last candle time.” Critical finance UI must remain accurate under network failure.

## Native branding
A Dock icon, toolbar glyph, app name, title bar, window controls, selected states, custom typography and characteristic motion should work as one identity. Do not use the logo as the sole source of distinction. Avoid over-branding the price chart with decorative shapes that compromise readability. Validate icon at actual small sizes; create proper 1x/2x raster assets from a preserved original vector.

## Testing protocol
1. Verify app builds for minimum macOS version and CPU architecture.
2. Launch from installed bundle and existing desktop shortcut, not only from source executable.
3. Open/close settings; make changes, cancel, reopen and verify unchanged settings.
4. Confirm Apply commits settings once and updates feed appropriately.
5. Toggle every panel and window size; verify state persists across restart.
6. Test keyboard shortcuts and VoiceOver or accessibility names where feasible.
7. Switch charts, signals, markets and feed modes rapidly; confirm latest request wins.
8. Test offline mode, no cached data, stale cache, delayed provider, missing API key, quota and unsupported intervals.
9. Check controls with long text, localized number formatting and zoom.
10. Capture full-window screenshots and fix actual overlap/spacing defects.
11. Check CPU, RSS, memory pressure and crash reports over a meaningful session.
12. Save a backup, release notes and reproducible regression suite before installation.

## macOS architecture decisions
Use view models or unidirectional data flow; keep trading calculations and data fetching outside rendering code. Use semantic colours and symbols, not state-dependent magic strings in arbitrary view components. Keep chart time projection as a testable pure function. Make unit/currency formatters explicit. Keep user settings persisted but avoid exposing credentials in logs, public repos or screenshots.

## Recognising fake desktop design
Signs: giant card grid above the working surface, no menu/keyboard support, web-only components floating inside a native window, hard-coded widths that make resizing unusable, decorative icon strings without labels, fake connection statuses, lack of file integration, or dark-mode effects that degrade information hierarchy. Fix these structural problems before polishing shadows.

## Sources and examples
[Apple designing for macOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-macos), [Apple sidebars](https://developer.apple.com/design/human-interface-guidelines/sidebars), [Apple toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars), [SwiftUI navigation](https://developer.apple.com/documentation/swiftui/navigation), [NN/g recognition vs recall](https://www.nngroup.com/articles/recognition-and-recall/), [W3C WCAG](https://www.w3.org/TR/WCAG22/).

## Acceptance criteria
Primary task dominates visual hierarchy; panels reclaim space when collapsed; statuses are truthful; keyboard and window workflows work; data alignment and precision are correct; app launches on intended hardware; testing uses actual artifacts; no regressions to critical calculations; relevant brand personality is visible without obstructing the work.