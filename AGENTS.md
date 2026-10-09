# Agent Instructions — Kindle Learning Lab

## Scope and communication

- Keep repository changes focused on the Kindle children's interactive learning system.
- Use English for project communication, code, and documentation.
- Read docs/PROJECT.md before implementation and preserve existing project decisions.
- Do not repeatedly ask about the product purpose or target age.
- Explain the reason before proposing a change to project scope or technical direction.
- Distinguish confirmed requirements, proposals, and unverified assumptions.

## Product and child experience

- Target children aged 3–4 using an Amazon Kindle E Ink reader's built-in browser.
- Support early math, literacy, shape recognition, branching stories, and simple games.
- Use simple interactions that aim to be usable with minimal adult help.
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

- The Kindle model, firmware, browser capabilities, and deployment status are currently unknown or unverified.
- Record important technical decisions in reusable repository documentation, with rationale and validation status.
- Use docs/TASK_TEMPLATE.md when preparing Codex development tasks; include concrete implementation steps and acceptance criteria.
- Report what was changed, how it was verified, and what still requires actual Kindle testing.
- Desktop or iPhone browser checks do not establish Kindle compatibility.
