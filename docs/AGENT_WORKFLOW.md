# Agent workflow and instruction maintenance

This is the repository's maintained reference for development procedure and instruction upkeep. The personal `maintain-kindle-learning-lab` skill carries a concise execution guide and reads this document; agents without that skill follow this document directly. Product requirements and current evidence remain in their existing project documents.

## Begin a task

- Inspect fresh remote `main`, local changes and applicable `AGENTS.md`; preserve unrelated work and use an isolated worktree when needed.
- Read PROJECT.md, SESSION_HANDOFF.md and STATUS.md, then relevant feature documents. Do not ask again about settled goals or decisions. Distinguish confirmed requirements, proposals and assumptions; explain substantial scope or teaching-direction changes before proceeding.
- Converse with the owner in Chinese when appropriate. Write repository code and documentation in English.
- For a substantial task, use TASK_TEMPLATE.md to define concrete affected files, behaviors and acceptance criteria. Do not require a separate task report for a small change.

## Implement and verify

- Edit authoring sources and commit generated pages with them. Consult LEARNING_MODULES.md and MATH_SIX_LEVELS.md for current source/build contracts rather than treating a skill's paths as permanently correct.
- Select checks appropriate to the changed behavior. The skill's `scripts/verify_project.py` lists/runs focused math, learning, UI and documentation checks; inspect current tests when that mapping becomes stale. Without the helper, use the relevant feature document and `tests/` directly.
- Use independent arithmetic, geometry and content predicates. Clicking an authored answer alone does not establish correctness. Check intermediate representations, alternate legal answers, repeated taps, wrong retries, Undo, current phase cues, passive completion, same-level Next, Back and storage failure as applicable.
- Inspect artwork at its actual monochrome display size, including small composite inserts. Confirm distinguishable silhouettes and that every pictured clue refers to a visible feature. Loaded images or different image bytes do not establish recognizable objects. Keep source, license and public attribution synchronized.
- Open the rendered application for changed interactions and relevant layout/assets. Missing browser executables or blocked downloads are blockers, not passing tests. For documentation-only changes, check links, consistency and diffs; do not rerun all activity suites or claim new interaction evidence.
- Keep software checks, desktop browser evidence, owner device reports and observed child comprehension separate. Loaded-page disconnection does not establish offline reload; played marks do not establish mastery. Record concrete limitations.

## Maintain documentation and the skill during each iteration

Before delivery, review whether the task produced a lasting requirement, reusable procedure, failure lesson or new evidence. This is part of the task, not a scheduled background updater. If nothing durable changed, no documentation or skill edit is required.

| Information | Maintained home |
| --- | --- |
| Product goals, device constraints and child experience | PROJECT.md |
| Curriculum, interaction contracts, source/build details and feature tests | Relevant feature document |
| Confirmed owner decisions and reusable project lessons | SESSION_HANDOFF.md |
| Current delivery state, evidence and unresolved checks | STATUS.md |
| Agent execution, instruction upkeep and delivery procedure | This document |
| Concrete task inputs and acceptance format | TASK_TEMPLATE.md |
| Concise invocation/execution guidance and reusable helper resources | Installed personal skill |

1. Update the appropriate existing document in place. Replace obsolete rules, consolidate duplicates and preserve useful rationale/evidence. Avoid per-change reports, mandatory dated entries and chronological logs; Git preserves history.
2. Compare any changed reusable procedure with the installed skill and its helper resources. Update the skill only when the change applies to future tasks: corrected source/build guidance, verification methods, delivery behavior or confirmed workflow preferences. Do not copy changing seed counts, curriculum tables, deployment hashes or test results into it.
3. Use the skill-creator guidance when editing the skill. Keep its automatic trigger narrowly scoped to this repo and retain implicit invocation. Preserve icons and metadata; check that its description, body, references and helpers agree. Follow user instructions over stale workflow text; replace the stale text rather than silently keeping conflicting rules.
4. Validate the skill and actually run changed helpers on an appropriate checkout. Use focused scenario checks when useful; avoid costly screenshot-to-agent review or broad parallel agent runs unless the owner requests them. Inspect repository Markdown links and the exact diff.
5. Save skill edits through its own persistent skill workspace: stage only that skill, commit and push the workspace's current branch. Commit project documentation through this repo's normal delivery path. They are separate repositories; do not claim both are saved if either push fails. Complete the available work and report the exact unsaved part.
6. Keep AGENTS.md as a short entry point with essential project constraints and a minimal fallback delivery rule. Keep detailed procedural instructions here and the skill concise; link to current source documents instead of duplicating them.

The owner authorizes this routine upkeep as part of project work. It does not authorize changing unrelated skills, expanding app permissions or changing product direction without an instruction. If the personal skill is unavailable, maintain repository documentation and report that the installed skill could not be synchronized.

## Deliver directly to main

The owner authorizes routine reading, implementation, verification, direct commits to `main` and publication without a PR or another manual review request. Create a PR only when explicitly requested.

- Finish relevant checks and documentation; inspect fresh remote main and the exact diff.
- Use authenticated git and a guarded fast-forward. If git lacks credentials and the GitHub connector works, create the tested tree/commit and update main with its expected head SHA and `force=false`. Compare the remote tree to the tested local tree before moving the ref. Reconcile a changed head; never force-push over other work.
- Inspect GitHub Pages deployment and verify affected live behavior. For documentation-only changes, verify the published documentation and deployment state without claiming new app or device tests. Report a concrete deployment/browser blocker when applicable.
- Report changes, relevant verification, the live link when applicable and remaining device limits concisely. The owner provides further device feedback.

Task authorization does not override platform approvals, authentication, branch protection or administrator policy. Do not change permission settings or retry a rejected action indirectly to keep delivery moving. Explain concrete remaining blockers accurately.
