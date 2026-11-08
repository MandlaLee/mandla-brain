# AI Capability Discovery & Execution Standard
Updated: 2026-11-08 · Cross-project operating rule

## Why this exists
Mandla explicitly challenged assistants for failing to disclose useful capabilities and alternatives when asked how to improve their effectiveness. The assistant acknowledged that it should have proactively explained specialised assistants/Plugins, connected apps, Projects, Work/computer use, automations, reusable skills, Codex, and model thinking settings. This is a durable **recommendation and execution quality requirement**, not a claim that any particular feature is available on every plan or platform.

## Mandatory capability preflight
For a substantial request or when Mandla asks how to make an AI more capable:
1. Identify the real goal, deliverable, success criteria, available budget, deadline, hardware, and source of truth. Reuse existing context; ask only for genuinely missing essentials.
2. **Discover, do not assume**: inspect available tools, connected apps, skills, plugins, repository assets, official product capabilities, and existing open-source solutions relevant to the task. Consider native tools, ChatGPT Projects, Work/computer use, Codex, automation, connectors, reusable agent skills, specialised plugins, and appropriate thinking effort. These are possibilities, not promised entitlements.
3. Offer the **best 1–3 viable paths**, including reuse of existing software versus custom development, with costs, permissions, data/privacy implications, compatibility, performance, maintainability, and expected quality. Avoid a long irrelevant feature catalogue.
4. State which options are **available now**, **require connection/installation/approval**, **need verification**, or **are unavailable**. Never imply that naming an integration in instructions grants access.
5. Recommend the fastest **reliable** route to the intended quality, not the route requiring the most bespoke work. If the user's request is clear, proceed rather than stalling with unnecessary permission questions.
6. Re-evaluate when evidence changes: disclose better approaches or discovered capabilities without waiting to be asked.
7. For long work, preserve milestones and handoffs. Distinguish designed, configured, installed, connected, tested, deployed, and operational. Never claim autonomous inter-agent coordination, live sync, or working integrations without verification.

## Build-versus-reuse gate
Before writing a custom implementation, search for and evaluate the **original software, official SDK, supported integration, maintained open-source project, or existing project code**. Run the smallest representative benchmark on the actual target hardware. Compare function, performance, setup cost, quality, licensing, privacy, and maintenance. Custom-build only where justified; do not force custom code as a default.

### FaceWeave lesson (2026-11-08)
A custom Swift face-swapping/tracking engine was extensively built and optimised before the original Deep-Live-Cam software and model pipeline had been fully tested. Mandla then explicitly paused the custom path and requested Plan B: original models with original software. The lesson is to test the original implementation early and benchmark on his 4 GB Intel Mac before substantial custom optimisation. The Plan B installation/test status must be verified from real artifacts; this note does not assert its final success.

## Agent architecture: SenAI and Phala Digital Developer
Two **private, skills-based plugins** were created on 2026-11-08:
- **SenAI** — project coordination, continuity, research, troubleshooting and cross-project handoffs. Private plugin ID `plugins_6af0c2b51b4481918d689b10b1d9600c`.
- **Phala Digital Developer** — websites, branding, UI/UX, engineering and deployments. Private plugin ID `plugins_6af0c2ca09d88191881fce6479ee73b4`.

They share a **documented reference strategy**: use Mandla Brain and project records. This is **not** evidence of automatic GitHub/Notion connections, autonomous conversations between plugins, or bidirectional sync. Enable authorised connections, inspect actual permissions, and verify real access before claiming it. Plugin creation was confirmed and the uploaded package's skill file listings were checked. Their runtime invocation and integrations have not yet been end-to-end tested.

## Capability matrix (evaluate when relevant)
| Capability | Practical use | Verification required |
|---|---|---|
| Specialised plugins and skills | Repeatable, domain-specific agent behaviour | Created/installed status, actual skill loading, tool permissions |
| GitHub/Notion/Drive connectors | Read/write source-of-truth files and project context | Account connection, scopes, exact repository or file access |
| ChatGPT Projects / persistent workspaces | Group long-running work and files | Current product availability and data scope |
| Work/computer use/remote desktop | Multi-step browser, application and local computer workflows | Supported mode, active connection, permitted actions |
| Codex and engineering skills | Repo-aware code changes, tests and reviews | Repo access, build/runtime checks, actual test results |
| Automations | Scheduled syncs, follow-ups, conditional monitoring | Created schedule, enabled status, last-run evidence |
| Model reasoning settings | Allocate stronger reasoning to complex problems | Actual user plan/menu availability |
| Original software / SDKs | Avoid reinventing a working implementation | Compatibility, licensing, sample benchmark |
| Local/offline AI | Protect privacy and reduce API spending | Hardware, model memory, CPU/GPU, performance |
| Cloud/API approaches | Handle workloads local hardware cannot support | Cost, privacy, permission, availability |

## Evidence and reporting
- **Proposed** ≠ **implemented** ≠ **compiled** ≠ **tested** ≠ **running** ≠ **deployed**.
- Benchmark the actual workload and disclose whether a result is simulated or real-camera/production performance.
- Identify what was changed, where, and how it was verified; preserve rollback paths.
- Don't conceal material limitations, better tools, costs, or likely failure modes.
- Keep private credentials and sensitive records out of this public repository.
- Use the Design Director charter for visual work, and all established source-of-truth and staging rules.

## Accountability
Mandla expects assistants to surface useful capabilities proactively and help him get maximum practical value from available tools, not wait for him to discover features. A missed recommendation should be documented as a process improvement, not excused as deliberate secrecy or hidden knowledge. Future assistants must apply this preflight proportionately and avoid overwhelming simple tasks.
