# Kindle Learning Lab — Project Instructions

These requirements guide the project's design and development.

For current evidence and durable session decisions, read [STATUS.md](STATUS.md) and [SESSION_HANDOFF.md](SESSION_HANDOFF.md).

## Project goal

Build interactive learning content for children roughly aged 3–8 using Kindle E Ink readers, including early math, literacy, shape recognition, branching stories, and simple games.

## Devices and environment

- Primary development and discussion workflow: iPhone + ChatGPT.
- Target device: Amazon Kindle E Ink reader; the exact model is still to be supplied.
- Deployment: GitHub repository + GitHub Pages.
- Access: web pages opened in Kindle's built-in browser.
- No dedicated backend server.

## Technical requirements

- Prefer HTML, CSS, and Vanilla JavaScript.
- Avoid large frameworks and complex dependencies where possible.
- Prioritize compatibility with Kindle's limited browser and processing power.
- Use black-and-white high contrast, large text, and large buttons.
- Avoid continuous animation, frequent refreshes, complex graphics, and autoplay.
- Support selectable answers, immediate feedback, score tracking, and question navigation.
- Where feasible, allow interaction to continue during a brief disconnection after the page has initially loaded.
- Do not assume support for all modern Web APIs. Clearly label unverified functionality as pending testing.

## Child experience

- Math reference ages: roughly 3–8 years, with six independently selectable task levels.
- Keep operation simple and minimize the need for adult assistance.
- Early-level children may not yet be reading; later-level instructions still need concise visual support. Use pictograms for activity selection, navigation, feedback, and story choices; minimize visible text while retaining numerals and letters as learning content.
- Design activities for suggested 10–15 minute sessions.
- Math practice may continue for as many questions as the child chooses, per the owner's 2026-10-09 direction. Use manual next-question navigation and an always-available Back action; do not impose a three-question cap or use automatic advancement, clicking incentives, or complex reward systems.
- Emphasize learning, exploration, and understanding rather than answering speed.
- Show the task and necessary information at entry. Do not hide numerical answers behind unexplained taps on models; demonstrations are optional explicit tools. Reference pictures are passive.

## Planned subject expansion

The owner approved a detailed planning phase for Logic, Chinese, English, Everyday Science and Stories/Social Situations, in that order. Each subject uses six freely selectable capability levels, broadly aimed at ages 3–8/9; age is a reference, not a lock or developmental norm. The immediate learner is three. Preserve picture-led entry and honestly labeled adult narration for nonreaders. See [LEARNING_EXPANSION_PLAN.md](LEARNING_EXPANSION_PLAN.md) for proposed content, interaction contracts and staged acceptance. New modules are not yet implemented; complete planning before later implementation work.

## Working practices

- Use English for project communication, code, and documentation.
- Continue existing project decisions and technical conventions.
- Implement, check, push, and merge routine project changes autonomously; the owner does not need to review or merge PRs. A branch and PR may still be used for history, then merged by the agent.
- Check the resulting GitHub Pages deployment and provide the page link. The owner accepts changes by trying the deployed interface on their device.
- Do not repeatedly ask about Kindle's intended use or the product's goals.
- Record important technical decisions in reusable documentation.
- After each change, automatically review and maintain durable project knowledge in the existing relevant documents. Record lasting requirements, rationale, reusable lessons and decision-relevant evidence; replace superseded content and remove duplication. Keep current state concise. Do not keep a chronological change log or require documentation for temporary implementation details; Git preserves history.
- Provide actionable instructions and acceptance criteria for Codex development tasks.
- Explain the reason before proposing changes to project scope or technical direction.
- Do not present unconfirmed information as established fact.

## Repository scope

Keep repository changes focused on the Kindle children's interactive learning system and its development.

## Pending confirmation and testing

- Exact Kindle model and firmware version.
- Browser support for the selected HTML, CSS, and JavaScript features.
- On-device text and button sizes, tap response, and E Ink refresh behavior.
- Continued interaction after initial loading during a disconnection; offline reopening or reloading requires separate validation.
- GitHub Pages deployment has succeeded. The owner reported that v0.1 worked well on their Kindle; the v0.2 pictogram interface needs a device recheck. See [pictogram decisions and test status](PICTOGRAMS.md).

