# Agent Instructions — Kindle Learning Lab

## Scope and communication

- Keep repository changes focused on the Kindle children's interactive learning system.
- Use English for project communication, code, and documentation.
- Read docs/PROJECT.md before implementation and preserve existing project decisions.
- Do not repeatedly ask about the product purpose or target age.
- Explain the reason before proposing a change to project scope or technical direction.
- Distinguish confirmed requirements, proposals, and unverified assumptions.

## Product and child experience

- Target children aged 3–5 using an Amazon Kindle E Ink reader's built-in browser.
- Support early math, literacy, shape recognition, branching stories, and simple games.
- Use simple interactions that aim to be usable with minimal adult help.
- The child is not yet reading. Prefer pictograms for navigation, choices, and feedback; keep numerals and letters when they are the learning content. See docs/PICTOGRAMS.md.
- Design natural stopping points for suggested 10–15 minute sessions, without speed pressure, endless questions, or reward mechanics that encourage repeated clicking.
- Activities may use selectable answers, immediate feedback, scores, and question navigation.

## Implementation constraints

- Prefer static HTML, CSS, and Vanilla JavaScript, hosted on GitHub Pages with no dedicated backend.
- Avoid large frameworks and complex dependencies.
- Use black-and-white high contrast, large text, and large touch targets.
- Avoid continuous animation, frequent refreshes, complex graphics, and autoplay.
- Favor conservative browser features and low processing cost; the exact JavaScript/CSS baseline remains to be verified on the device.
- Where feasible, load the data and assets needed for the active session up front so interaction can continue during a brief disconnection.
- Do not treat continued interaction in an already loaded page as proof that offline reload or reopening works.
- Do not require or claim support for modern APIs (including service workers or persistent storage) without device testing or a working fallback.

## Evidence, documentation, and tasks

- The exact Kindle model and firmware remain unknown. GitHub Pages has deployed successfully. On 2026-10-09 the owner reported that the localStorage marker test and all four v0.4 capability checks passed on their Kindle: counting restoration, nine-cell selection, manual local updates, and the tested simple SVG/PNG comparison. See docs/CAPABILITY_TESTS.md. Treat this as evidence for those tested behaviors on that device; offline behavior, other SVG features, and other Kindle models remain unverified.
- Record important technical decisions in reusable repository documentation, with rationale and validation status.
- Use docs/TASK_TEMPLATE.md when preparing Codex development tasks; include concrete implementation steps and acceptance criteria.
- Report what was changed, how it was verified, and what still requires actual Kindle testing.
- Desktop or iPhone browser checks do not establish Kindle compatibility.

## Delivery workflow

- The owner has authorized routine project changes to be implemented, checked, pushed, and merged without a manual PR review or another confirmation request.
- Use a feature branch and PR when useful for change history, then merge it autonomously after appropriate checks. A PR is not a handoff requiring the owner to act.
- Let the existing GitHub Pages deployment run after merging; inspect deployment status and report the live page link.
- The owner validates the result by opening the deployed page on their device and providing feedback.
- Report development checks and device-testing limitations accurately. Continue to explain changes to project scope or technical direction before implementing them.

