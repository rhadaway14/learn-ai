# Persona Review — Foundations Reference Lessons

**Scope:** Lessons 1–3 and the optional Foundations workbench  
**Method:** structured heuristic walkthrough using `PERSONA_TESTING.md`, source-independent learner routes, automated contract checks, and API persistence tests  
**Limitation:** no observed external human sessions have been completed yet; this is a pre-pilot review, not empirical usability proof.

## Findings and remediation

| Finding | Persona | Severity | Resolution |
|---|---|---:|---|
| Core and advanced material existed, but the route choice was not visible at lesson entry | N and E | Confusing | Added a two-lane entry panel with time estimate, required/optional language, and direct anchors |
| “Engineer extension” could be mistaken for required work before programming readiness | N | Blocking risk | Activity labels now state that the core is required and the extension is optional; lane copy repeats the no-code boundary |
| Experienced learners had to finish the core path before discovering whether deeper content existed | E | Inefficient | Added an Engineer-path preview link at the top of every reference lesson |
| The workbench stored notes but did not show the selected activity contract | N and E | Confusing | It now loads mission, estimated time, guided/challenge/extension objectives, artifact name, and lesson link from the activity JSON |
| Evidence fields assumed learners knew what to write | N | Confusing | Renamed hypothesis as prediction/hypothesis and added observation and conclusion prompts with examples of acceptable evidence |
| Runtime outage feedback did not clearly preserve a fallback | N | Blocking risk | The guide remains usable without the API and the UI tells learners to copy notes into the worksheet |

## Post-remediation scores

| Dimension | Persona N | Persona E | Evidence |
|---|---:|---:|---|
| Path clarity | 5 | 5 | Two learning lanes appear immediately after navigation |
| Prerequisite safety | 5 | 4 | Core is no-code; advanced prerequisites are explicit; implementation waits for Engineering Lab A |
| Interaction feedback | 5 | 4 | Numeric output, interpretation, failure, and recovery exist; advanced extensions remain specifications before the bridge |
| Activity completion | 5 | 5 | Three levels, artifact, evidence, acceptance criteria, and workbench guide |
| Continuity | 5 | 5 | AI-story plus P1-I01 through P1-I03 downstream links |
| Advanced value | N/A | 5 | Mechanics, scale, production risk, architecture question, and extension |
| Operational ease | 5 | 4 | Static path requires only a browser; Docker runtime is optional and tested structurally, but container startup needs host verification |

## Decision

Lessons 1–3 pass the pre-pilot persona gate. They are approved as the conversion reference for Lessons 4–10, subject to these conditions:

1. Run at least one observed session with a genuinely new-to-AI learner before treating the rubric as empirical evidence.
2. Run the Compose profile on Windows Docker Desktop and one Unix-like host before advertising it as fully host-validated.
3. Preserve the top-of-lesson lane choice, optional-extension wording, activity-driven workbench guide, and fallback behavior in later conversions.
4. Feed human pilot findings back into the contract and retest these reference lessons before bulk conversion.
