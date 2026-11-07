# 14 — Interaction, Motion and Microcopy

## Behaviour is part of identity
A brand becomes tangible when a control behaves predictably, a transition has character without delay and an error message is both human and useful. Decorative animation alone is not sophistication. Interaction design communicates cause, state, progress, hierarchy and consequences.

## Principles of feedback
Every meaningful action should have a comprehensible response: pressed state, loading indicator, success confirmation or error with recovery. Match feedback strength to consequences. A routine sidebar expansion doesn't need a full-screen celebration; submitting a job application requires a reliable delivered/failed state that distinguishes local form completion from server confirmation.

## Motion with purpose
Use animation to:
- preserve spatial continuity when a sidebar collapses;
- distinguish entering versus leaving;
- show which object moved and where;
- indicate progress on a meaningful operation;
- draw attention to important state changes;
- reinforce distinctive brand character where it doesn't obstruct tasks.

Motion should not simulate impossible state. A “trade opportunity found” pulse cannot imply a profitable outcome. A progress bar must not pretend data has been fully uploaded when the app only initiated a request.

## Timing and easing
Choose timing relative to interaction and cognitive load. Small toggles and state changes are generally brief; page transitions can be slightly longer when helping maintain context. Excessively slow motion makes repeated work frustrating, especially in power-user tools. Avoid one global animation duration for every interaction. Measure perceived delay and preserve instant access to critical data.

## Reduce motion
Respect platform and browser prefers-reduced-motion/accessibility settings. Provide static alternatives for animated feedback. Never make essential status visible only through motion. Avoid flash and overly intense looping animations. Motion branding is an enhancement, not a gate.

## Microcopy specification
Define vocabulary for:
- primary action (“Save changes,” not vague “Proceed”);
- secondary action (“Review draft,” “Open inspector”);
- warning with consequence;
- error with cause where known and recovery;
- confirmation of what was actually completed;
- empty state explaining why;
- offline/stale/partial information;
- permissions and privacy purpose;
- destructive-action confirmation.
Avoid generic AI prose in applications. Label the actual thing the user controls: timeframe, source, chart, trade history, app state.

## Interaction patterns
**Hover** should not be the only method of discovery. **Focus** should have strong visible treatment and predictable keyboard order. **Pressed** state confirms responsiveness. **Disabled** controls should state a reason, with help text if needed. **Selected** state should remain clear without relying solely on colour. **Loading** should block duplicate submissions while preserving navigation when safe.

## Destructive actions
Deleting projects, revoking access or discarding work needs explicit consequences. Where practical, offer reversible Undo. Confirmation dialogs are appropriate when loss is irreversible or high stakes, but overusing confirmations trains users to click through automatically. Prefer prevention and clear labels.

## Tooltips and icon-only rails
Compact navigation can free valuable screen space but may become cryptic. Provide stable tooltips, accessible names, keyboard shortcuts and a clear expansion affordance. Tooltip text should describe the action, not repeat a vague category (“Inspector” → “Show trade entry, stop and targets”).

## Stale and disconnected states
When connectivity changes, avoid abrupt switching between real and simulated values. Make cached/historical data visually distinct, preserve existing user work safely and present a retry path. When data is delayed, label it; never animate a stale price as if a live tick arrived. The copy must communicate the actual trust boundary.

## Error-message template
“[What happened]. [What remains safe/available]. [How to recover].”
Example: “5-minute signal data is unavailable. Existing saved chart remains visible, but no current trade entries will be issued. Check the connection or switch to saved-history review.” Avoid unsupported claims about what caused the failure.

## Audio and tactile feedback
Sound is optional and may be distracting; give users control. For mobile haptics use native platform conventions and avoid excessive alerts. Do not claim a signal notification was delivered merely because a system request was queued. Consider notifications as part of the brand voice, including clear market, direction, timestamp and action limitations.

## Motion QA
- Does animation help people understand the change?
- Does it interrupt repetitive or high-stakes work?
- Are reduced-motion settings respected?
- Can keyboard and screen-reader users perceive the same state?
- Does state remain correct if animations are interrupted?
- What happens during rapid repeated toggles?
- Are there accidental overlapping elements or disappearing focus?
- Does the transition preserve chart and scroll position?
- Does the process use too much CPU on older devices?

## Content QA
Remove filler: “Your journey begins here,” “Unleash potential,” “Experience innovation.” Write concrete outcomes and truthful states. Test different lengths, tone for negative events, translation and capitalization. Allow editorial personality in marketing, but keep control labels direct. In financial/product operations, prioritize precision over excitement.

## Sources
[Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/), [W3C WCAG 2.2 motion and focus](https://www.w3.org/TR/WCAG22/), [Material Design motion](https://m3.material.io/styles/motion/overview), [WAI-ARIA APG](https://www.w3.org/WAI/ARIA/apg/), [NN/g feedback and usability heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/).