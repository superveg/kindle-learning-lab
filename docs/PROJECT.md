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

- The owner requests a simpler picture-led interface and levels 7–12 beyond the original six. Reduce menu and operation prose while keeping essential learning content and conditions visible. Use composed, inverse and multi-condition reasoning; avoid increasing every child’s arithmetic range just because another strand is easy.


- Math reference ages: roughly 3–8 years, with twelve independently selectable task levels.
- Keep operation simple and minimize the need for adult assistance.
- Early-level children may not yet be reading; later-level instructions still need concise visual support. Use pictograms for activity selection, navigation, feedback, and story choices; minimize visible text while retaining numerals and letters as learning content.
- Design activities for suggested 10–15 minute sessions.
- Math practice may continue for as many questions as the child chooses, per the owner's 2026-10-09 direction. Use manual next-question navigation and an always-available Back action; do not impose a three-question cap or use automatic advancement, clicking incentives, or complex reward systems.
- Emphasize learning, exploration, and understanding rather than answering speed.
- Show the task and necessary information at entry. Do not hide numerical answers behind unexplained taps on models; demonstrations are optional explicit tools. Reference pictures are passive.

## Planned subject expansion

The owner approved a detailed planning phase for Logic, Chinese, English, Everyday Science and Stories/Social Situations, in that order. Each subject uses twelve freely selectable capability levels, broadly aimed at ages 3–8/9; age is a reference, not a lock or developmental norm. The immediate learner is three. Preserve picture-led entry and honestly labeled adult narration for nonreaders. See [LEARNING_EXPANSION_PLAN.md](LEARNING_EXPANSION_PLAN.md) for curriculum direction. All five modules now contain twelve levels and three families per level; see [LEARNING_MODULES.md](LEARNING_MODULES.md) for delivered content, contracts and verification limits.

## Development instructions

Use [AGENT_WORKFLOW.md](AGENT_WORKFLOW.md) for execution, verification, direct-main delivery and ongoing documentation/skill maintenance. Use the personal `maintain-kindle-learning-lab` skill when available; agents without it follow the repository workflow directly. This document remains the source of product requirements.

## Repository scope

Keep repository changes focused on the Kindle children's interactive learning system and its development.

## Pending confirmation and testing

- Exact Kindle model and firmware version.
- Browser support for the selected HTML, CSS, and JavaScript features.
- On-device text and button sizes, tap response, and E Ink refresh behavior.
- Continued interaction after initial loading during a disconnection; offline reopening or reloading requires separate validation.
- GitHub Pages deployment has succeeded. The owner reported that v0.1 worked well on their Kindle; the v0.2 pictogram interface needs a device recheck. See [pictogram decisions and test status](PICTOGRAMS.md).

