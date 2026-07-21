# Customer Journey Map — composition reference

**Slug:** `journey` · **Tool:** Excalidraw (Mermaid `journey` for a crude version) · **Phase:** 2 · **Source of truth:** personas, JTBD, interviews

## Purpose
Show the path (phases) a customer travels through when interacting with the product/service, and the emotions they feel along the way. Captures actions, touchpoints, thoughts, and a satisfaction curve per phase. Surfaces pain points and improvement opportunities.

## When to use / when NOT
- **Use** to capture the **whole experience over time** (buying, onboarding, support), including where the customer struggles and how they feel.
- **NOT** for detailed in-app steps or logical task flow (→ `flow` / `wireflow`). Journey = experience + emotion; flow = concrete sequential steps.

## Element vocabulary
| Element | Meaning | Rules |
|---|---|---|
| Horizontal band | **Phase / Stage** | High-level step on the timeline (Discover, Buy...). Left-to-right, chronological. |
| Swimlane row | **Customer actions** | What the customer does in each phase. Active voice, short. |
| Swimlane row | **Thoughts** | One representative thought/question per phase. |
| Continuous line | **Emotional curve** | Mood across phases: high = delight, low = frustration. |
| Icon / label | **Touchpoint** | Channel of interaction (web, store, email). Placed at the action. |
| Red marker | **Pain point** | Where the user feels friction. Tied to the causing action. |
| Yellow marker | **Opportunity** | Where the experience could be improved. Tied to an action. |

## Composition rules
- Phases ordered left-to-right as separate columns.
- Below phases, parallel swimlanes: at minimum **Actions** and **Thoughts** (the Actions row is the backbone).
- Draw one **continuous emotional curve** across all phases (peaks = positive, troughs = negative).
- Pain points (red) and opportunities (yellow) attach to specific actions in their phase.
- The map is **linear** — one sequence, no branches/loops (branching → use `flow`; a separate scenario → a separate map).
- No backstage/internal steps (that's a service blueprint, not a journey map).

## Canonical structure
- Top: horizontal phase bands with names.
- Under each phase: swimlane cells for Actions and Thoughts.
- Emotional curve running above/below the phases with peaks and dips.
- Pain/opportunity markers near the relevant actions.
- Left: persona name + scenario; right: end state ("goal achieved" / "escalated to support").

## Anti-patterns
- Overcrowding (tiny text, long sentences).
- Flat hierarchy — nothing stands out; emphasize phase titles and the emotional curve.
- Multiple personas/scenarios in one map (each needs its own).
- Omitting the emotional curve (loses the key context).
- Turning it into an internal-department workflow (that's a blueprint).
- Too many colors (limit ~4-5) or no color coding at all.

## Rendering
- **Mermaid:** no faithful CJM type; the `journey` type gives phases + numeric scores but no true emotional curve or rich swimlanes. Prefer Excalidraw. Mermaid `flowchart` can only list phases as nodes (no emotion).
- **Excalidraw:** horizontal axis = phases; vertical bands = layers (Actions, Thoughts). Phase/blocks as labelled rectangles; emotional curve as a smooth line with emotion icons at key points. Colors by meaning: green = positive moment, red = pain, blue = standard step, yellow/orange = opportunity. Generous spacing; phase titles and the emotion line larger/bolder.

## Required inputs
- Persona name + scenario.
- Ordered phases.
- Per phase: customer actions, touchpoints, main thoughts/motivations.
- Emotion level per phase (e.g. 1-5 scale).
- Identified pain points and opportunities.

## Worked example (structural)
Ordering pizza online (persona: "Peter", evening order):
- **Discover** — action: sees social ad (Facebook); thought: "I'm hungry for pizza"; emotion: mildly positive; opportunity: first-order discount (yellow).
- **Choose** — action: browses restaurant site; thought: "hope it arrives on time"; emotion: neutral; pain: slow menu load (red); opportunity: speed up page (yellow).
- **Pay** — action: enters details, submits; thought: "looking forward to it"; emotion: high on success (green); pain: failed payment (red); opportunity: more payment methods.
- **Delivery** — action: tracks + receives; thought: "when will it come?"; emotion: high satisfaction on arrival.

Emotional curve dips at the pain points and rises sharply after successful delivery.
