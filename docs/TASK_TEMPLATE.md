# Codex Development Task Template

Use this template for substantial tasks; replace placeholders with concrete requirements. Read AGENTS.md, PROJECT.md and [AGENT_WORKFLOW.md](AGENT_WORKFLOW.md). Keep this task format in the repo; the personal skill refers to it without keeping a duplicate.

## Objective

Implement [one bounded learning activity or repository change] for children roughly aged 3–8, with independently selectable difficulty levels.

## Confirmed inputs

- Existing files and entry points: [paths].
- Learning objective and content language: [specific objective and language].
- Activity length and stopping point: [manual same-level continuation and natural pauses, or a specifically bounded diagnostic/sample].
- Device details: [known model/firmware, or explicitly unknown].
- Existing decisions to retain: [links to relevant documentation].

## Deliverables

- Affected authoring sources and generated outputs: [paths].
- Behavior to implement: [task entry, answers, feedback, navigation and completion].
- Relevant automated and rendered checks: [commands and interactions].
- Durable product/evidence updates: [existing documents, if needed].
- Reusable workflow/skill updates: [only when a lasting procedure changed].

Follow AGENT_WORKFLOW.md for implementation, instruction upkeep and delivery rather than copying its procedure into each task.

## Acceptance criteria

Replace each bracketed value before assigning the task.

- [Entry path] opens and presents the specified activity.
- Text and controls are large and legible in black and white; specify [sizes/layout] as implementation targets pending Kindle validation.
- A tap produces [explicit expected feedback], and repeated taps do not incorrectly duplicate score or advance questions.
- Scoring follows [explicit rule] and navigation follows [explicit rule].
- Each task completes after [defined stopping condition] with a clear pause. Math may continue at the same level manually without a fixed cap.
- There is no continuous animation, autoplay, speed-based pressure, or automatic endless advancement.
- The activity requires no dedicated backend or large framework.
- After initial content/assets have loaded, temporarily disabling the network still allows [specified session actions] to work.
- Missing optional browser features do not prevent the core activity from working, or their limitations are explicitly documented.
- Required learning content does not depend on unverified fonts, glyphs, or rendering features without a fallback.
- The implementation works under the GitHub Pages repository path, if deployment is part of the task.
- Results distinguish completed browser checks from pending Kindle testing.

## Verification evidence

Record useful results in the existing relevant feature/status document. This table is an optional planning aid, not a required separate report.

| Check | Environment | Result | Evidence or limitation |
| --- | --- | --- | --- |
| Initial load and layout | [browser/device] | [pass/fail/pending] | [details] |
| Answer/feedback/score/navigation | [browser/device] | [pass/fail/pending] | [details] |
| Session completion | [browser/device] | [pass/fail/pending] | [details] |
| Brief disconnection after loading | [browser/device] | [pass/fail/pending] | [details] |
| Kindle input, rendering, and refresh | [exact model/firmware or unknown] | [pass/fail/pending] | [details] |

Offline reload/reopening and persistent progress are separate capabilities. Only include them as requirements when explicitly scoped, and verify them independently.

