# Change and verification log

Use this file for every delivered project change. Keep entries concise: date, concrete change, reason, checks and unresolved limits. Update STATUS.md and relevant feature/decision documents in the same delivery. Distinguish a test command that passed from a planned check. Do not store credentials, unrelated personal information or a full chat transcript here.

## 2026-10-10 — runtime question quality and documentation workflow

- Added an eight-task page-memory history per topic/level and up to twelve candidate generations for the selected variant. Cosmetic art, dot positions and answer order do not count as a new arithmetic task. Preserve three-variant balance, manual uncapped practice, stable retries and existing storage keys.
- Reason: random generation alone can repeat a recent task; balanced variants alone do not ensure varied quantities. Small banks retain a bounded repeat fallback instead of hanging.
- Reviewed structural level progression; retained the existing curriculum boundaries rather than treating larger numbers as a new level. Added QUESTION_QUALITY.md and checks for task constraints, recent variety, menu continuity and constant-random fallback.
- Recorded the owner's requirement to document every delivered ChatGPT Work change in AGENTS.md, PROJECT.md and SESSION_HANDOFF.md; linked this log in README and refreshed the task template's outdated age/session defaults.
- Verification: passed 1,296 legacy and 891 higher-level solved questions, direct-answer checks, ES5 parsing and 1,080 quality samples across all sixty combinations. Deployment/live-browser evidence will be recorded after publication. Actual Kindle performance and child comprehension remain unverified.

## 2026-10-10 — remove discovery taps and preserve handoff

- Bridge, bundle and regroup questions expose answers immediately; picture transformations are optional explicit controls. Numeric models start visible; hints use one explicit action. Added entry cues.
- Added SESSION_HANDOFF.md and STATUS.md, reviewed existing repository documents, and required future developers to read the durable project state.
- Passed 1,296 legacy plus 891 higher-level generated-question checks and direct-answer checks. Pages deployed implementation `1268f4ec04cfa5734687c620757adf3ed3b888a3`. Live Chrome confirmed direct level-5 subtraction, optional regrouping with stable choices and same-level continuation; evidence was recorded in `b00ebbab9d4454057b68f6fb40e652d56377bdb7`.
- The owner's confusing-question examples were unspecified; identified patterns were fixed, while other tasks remain an audit priority. Browser checks do not establish actual Kindle or child comprehension.

Earlier implementation history remains in feature documents and Git commits; this log does not retroactively claim a complete per-change record.
