# Pictogram Interface — v0.2

## Confirmed requirements and device feedback

On 2026-10-09, the owner reported that the previous Hub worked well on their Kindle and that the buttons worked correctly. The model and firmware were not supplied. This is an overall owner report, not evidence that every item in the formal device checklist was tested.

The child is not yet reading. Use pictures as the primary way to choose activities, navigate, understand feedback, and make story choices. Minimize visible child-facing text. Keep numerals and letters where they are the learning content, and retain English adult instructions and accessible labels.

## Implementation decisions

- Use simple, black-and-white PNG pictograms for blocks, shapes, a letter, a rabbit, a house, an arrow, a check mark, a retry arrow, a carrot garden, and a duck pond.
- Embed every PNG as a data URL in the HTML file so no image requests are needed during interaction. PNG/data-URL rendering must be verified on the actual Kindle; the earlier test did not cover this new representation.
- Choose raster pictograms instead of emoji or icon fonts to avoid font-dependent appearance. No SVG, canvas, framework, or animation is introduced.
- Keep the existing button elements, click handlers, minimum 68px control height, ES5 script syntax, and manual navigation. Icon-based tiles may be taller than the original text tiles.
- Use a house for Home, an arrow for Next, a check mark for success/completion, and a circular arrow for another attempt. These meanings may need a brief adult demonstration.
- Keep the target circle and selectable shapes drawn with the previously used CSS borders. Shape matching now has a visible target rather than a written prompt.
- Use progress dots in counting; move score details and instruction sentences into visually hidden accessible text.
- Show story choices as scenes. The rabbit and selected carrot/duck scene remain visible at completion. Adults may narrate the full ending using the accessible text.
- Use a double border on a chosen option, keeping its white image background consistent with the button.

`tools/create_icons.py` creates the exact PNG data URLs using Pillow as an optional development dependency. The shipped page has no build or runtime dependency on Python or Pillow.

## Verification

- Passed: ES5 parsing and jsdom interaction checks, including embedded PNG URLs, retries, visual-feedback visibility, repeated taps, scoring, finite completion, reset, navigation, both story choices, and adult controls.
- Inspected the generated pictograms visually as a contact sheet.
- Pending: full browser layout checks and actual Kindle rendering of v0.2, including PNG data URLs, icon-button layout, selected borders, and the child's understanding of each icon.
- Offline reload, persistent progress, and the formal disconnection checklist remain unverified.
