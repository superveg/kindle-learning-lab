# Agent Instructions — Kindle Learning Lab

- Scope: `superveg/kindle-learning-lab`, a static learning app for children roughly aged 3–8 using Kindle E Ink browsers.
- Use `maintain-kindle-learning-lab` automatically when available. Read [agent workflow](docs/AGENT_WORKFLOW.md), [product requirements](docs/PROJECT.md), [durable decisions](docs/SESSION_HANDOFF.md) and [current status](docs/STATUS.md) before implementation. Follow the workflow directly when the personal skill is unavailable.
- Preserve static HTML/CSS/Vanilla JavaScript, monochrome contrast, large touch targets, visible task information, picture-led controls and manual continuation without speed pressure. Feature documents define the current curriculum and behavior.
- Write code and documentation in English; owner conversation may be Chinese. Preserve confirmed decisions and distinguish software/browser evidence from actual Kindle or child evidence.
- Routine changes are authorized for testing and direct publication to `main` without a PR or another manual review. Inspect fresh remote main, preserve unrelated work, use guarded fast-forward updates, and verify relevant published results. Create a PR only when explicitly requested; never force-push over another change.
- Before delivery, maintain lasting project knowledge and review whether the personal skill needs a reusable update, following docs/AGENT_WORKFLOW.md. Keep changing facts in repository documents and avoid duplicate logs. Skill installation does not override platform permissions.
