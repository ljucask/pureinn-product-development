# User Story Map — composition reference

**Slug:** `storymap` · **Tool:** Excalidraw (no native Mermaid type) · **Phase:** 5 · **Source of truth:** `/features/feature_list.md`, MVP scope · **Standard:** Jeff Patton's User Story Mapping

## Purpose
Visualize the backlog in **user-journey order**. Horizontal axis = the backbone of user activities; under each are tasks and story cards; horizontal lines slice releases. Answers "what does the user want to achieve, which features support it, and in what order do we build?". Great for MVP definition.

## When to use / when NOT
- **Use** in early product/feature/release planning to keep user-flow context and prioritize by value; ideal for defining MVP.
- **NOT** for detailed scheduling (→ `gantt`), technical design, or work not organized around user activities. For a dateless high-level view without user flow, a Now/Next/Later roadmap fits better.

## Element vocabulary
| Element | Meaning | Rules |
|---|---|---|
| Wide rectangle (top row) | **User Activity (backbone)** | High-level user goal ("Browse products"). Placed left-to-right in journey order; same abstraction level. |
| Box (2nd row) | **Task / Step** | A user task under an activity. Belongs to exactly one activity. |
| Card | **User Story** | "As a [user], I want [goal]". Stacked vertically under its task; higher = higher priority. |
| Horizontal line | **Release Slice** | Groups a row of stories into a release across all columns. Top slice = walking skeleton (MVP). |

## Composition rules
- Backbone activities left-to-right in narrative order (never reordered).
- Under each activity: its tasks; under each task: story cards stacked by **decreasing priority** (top = must-have/MVP).
- Release lines run **horizontally across all columns** — "slice, don't layer".
- Every release slice includes ≥1 story per activity (first slice = a minimal end-to-end path).
- Horizontal axis = user journey; vertical axis = priority/value. The backbone itself is never prioritized.

## Canonical structure
```
[Activity1] — [Activity2] — [Activity3]     ← backbone (left→right)
   Task1         Task2         Task3         ← tasks
[Story]       [Story]       [Story]          ← top row = MVP slice
[Story]       [Story]       [Story]          ← Release 2
[Story]       [Story]       [Story]          ← Release 3
```
Horizontal slice lines separate MVP / Release 2 / ...

## Anti-patterns
- **Vertical slicing** — making a release one column instead of a horizontal band.
- Using the vertical axis for time or team instead of priority.
- No backbone (a flat backlog with no user-goal grouping).
- Wrong priority (low-value story in the MVP row).
- Incomplete first slice (missing an activity → no end-to-end MVP).
- Activities out of journey order.

## Rendering
- **Mermaid:** no story-map type — improvising is clumsy. Use Excalidraw.
- **Excalidraw:** a column per activity; colored header box (activity) on top, task boxes in the 2nd row, white/light story cards stacked below by priority. Horizontal colored bands/lines for release slices, labelled "MVP", "Release 2"... on the right. Colors: one for backbone headers, another for tasks, white for stories; highlight the MVP slice. Even column spacing; align rows.

## Required inputs
- Ordered user activities (journey order).
- Tasks/steps per activity.
- User stories per task, prioritized.
- Release plan (which stories are MVP / each slice).

## Worked example (structural)
E-commerce checkout:
- Backbone: `Search Products → Add to Cart → Checkout`.
- Tasks — Search: "Search by keyword", "Filter"; Cart: "Add item", "Change qty"; Checkout: "Shipping info", "Payment".
- Stories under "Search by keyword": (1) search by name *(MVP)*, (2) autocomplete.
- Stories under "Add item": (1) add to cart *(MVP)*, (2) change quantity.
- MVP slice line under the top row (search by name + add item + shipping) = minimal purchase path; Release 2 = the second story in each column.
