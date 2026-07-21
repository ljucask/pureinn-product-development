# 2×2 Matrix (generic) — composition reference

**Slug:** `matrix` · **Tool:** Excalidraw · **Phase:** various · **Source of truth:** user input / the analysis being plotted

## Purpose
Categorize and decide by plotting items against **two** dimensions. Answers "which quadrant does each item fall in?" (e.g. highest value at lowest effort). Common product variants: **Value vs Complexity**, **Impact vs Effort**, **Positioning/Perceptual map**.

## When to use / when NOT
- **Use** with exactly **two** key factors to compare (benefit vs cost, impact vs effort). Standard prioritization/risk tool.
- **NOT** with more than two factors, or when a dimension isn't ordinal/measurable. For >4 buckets use a 3×3 / Eisenhower matrix.

## Element vocabulary
| Element | Meaning | Rules |
|---|---|---|
| Horizontal arrow → | **X axis** | Dimension 1; value grows rightward. |
| Vertical arrow ↑ | **Y axis** | Dimension 2; value grows upward. |
| Crossing point | **Axis origin** | Splits the plane into 4 quadrants (a threshold, not necessarily zero). |
| Quadrant | **Quadrant** | Each of 4 regions has a name / recommendation. |
| Dot / marker | **Plotted item** | An item at its `(x, y)` coordinates. Must lie within the axes. |
| Text | **Labels** | Axis names + quadrant labels/actions. Concise, self-explaining. |

## Composition rules
- Orient axes so "better" values go **right** and **up** → the **top-right quadrant = best** (e.g. high value, low effort → put "low effort" on the right). State this explicitly.
- Draw one horizontal + one vertical line crossing at the center, each with an arrowhead in the growing direction.
- Four quadrants, each with a label and ideally an action ("Do it", "Improve", "Avoid").
- Plot each item at its `(x, y)`; nothing outside the axes.
- Label axes clearly (e.g. "Value ↑", "Effort →").

## Canonical structure
A balanced square. Top-right = highest X and Y; bottom-left = lowest. Each quadrant labelled; equal-size cells; thresholds set the center.
Variant conventions:
- **Value vs Complexity:** X = complexity (low→right), Y = value (high→up); top-right (high value, low complexity) = quick wins.
- **Impact vs Effort:** X = effort (low→right), Y = impact (high→up); top-right = do first.
- **Positioning map:** two brand attributes; competitors plotted as dots.

## Anti-patterns
- Unlabelled or wrongly oriented axes (best quadrant ends up in the wrong place).
- More or fewer than 4 quadrants.
- Quadrants with no action labels.
- Overcrowding one quadrant with too many points.
- Plotting without real X/Y data (it's not a text list).

## Rendering
- **Mermaid:** no clean 2×2 type (quadrant chart is limited/experimental). Approximate with a `graph` of four nodes if needed, but prefer Excalidraw for a real matrix.
- **Excalidraw:** two perpendicular arrowed axes crossing at center → 4 quadrants. Put a labelled text block in each quadrant. Optional background color (green = best quadrant, red = worst). Items as small dots/labels at their coordinates; distance from axis reflects relative value. Keep a clean, symmetric grid.

## Required inputs
- Axis names + what high/low means on each.
- Quadrant labels / action recommendations.
- Items to plot, each with `(x, y)` values (e.g. `[80% impact, 20% effort]`). Without coordinates the diagram is meaningless.

## Worked example (structural)
Value vs Complexity: X = complexity (low→right), Y = value (high→up).
- Top-right "Quick wins: high value, low complexity" — highest priority.
- Top-left "Big bets: high value, high complexity".
- Bottom-right "Nice-to-have: low value, low complexity".
- Bottom-left "Avoid: low value, high complexity".
Plot each feature as a dot at its measured coordinates.
