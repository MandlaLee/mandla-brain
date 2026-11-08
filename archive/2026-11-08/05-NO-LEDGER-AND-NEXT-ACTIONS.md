# NO Ledger and milestone-driven next actions

A NO is **not a rejection**. It is an explicit pause with a reason and a trigger for reconsideration. Do not silently resurrect postponed work, and do not discard it.

| Idea | Status | Reason | Revisit trigger |
|---|---|---|---|
| Full autonomous local SenAI coding agent | **Deferred by agreement, 2026-11-08** | FaceWeave's actual swap is unfinished; 4GB RAM and safety limits | FaceWeave demonstrates real swap with measured performance |
| New unrelated Mac apps during FaceWeave work | **Focus policy, not a blanket refusal** | User wants better completion discipline | FaceWeave milestone or user explicitly reprioritizes |
| Original Deep-Live-Cam full stack | **Plan B fallback** | Latest dependencies incompatible with Intel Monterey; heavy RAM | Plan A stalls or fails benchmark |
| Core ML conversion/quantization for FaceWeave | **Optimization candidate** | Must first establish baseline correctness | Real swap works but performance insufficient |

## FaceWeave next actions (ordered)
1. Verify existing model and file inventory; avoid overwriting FaceWeave/FaceWeave Live.
2. Obtain a compatible, appropriately licensed face-recognition embedding model and five-point alignment path.
3. Produce **real still-image swap** using supplied test images; verify result visually.
4. Benchmark repeat inference latency, CPU, RAM and stability; synthetic first inference ~9.85 sec is insufficient for live.
5. Integrate pipeline with camera capture, proper compositing and robust error handling.
6. Test with user, handle black preview, optimize for Intel 4GB.
7. Package/brand, test app launch, record known limitations, then mark milestone complete.

## Completion definition
A build is not finished merely because dependencies install or a process exits zero. Require demonstrable feature behavior, relevant tests, user-visible usability, and accurate release notes.

## Review cadence
Review NO Ledger after a meaningful completion milestone, not every time a new idea appears. Preserve original rationale and append updates with dates.
