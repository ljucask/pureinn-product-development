# Kano Model — composition reference

**Slug:** `kano` · **Tool:** Excalidraw (Mermaid unsuitable) · **Phase:** 5 · **Source of truth:** `pm-features-list` KANO analysis / Kano survey data

## Purpose
Classify product features by their effect on customer satisfaction. Plots which features are Must-be (basic), Performance (linear), Attractive (delighters), Indifferent, or Reverse. Answers "how does the level of implementation of a feature change customer satisfaction?".

## When to use / when NOT
- **Use** in feature planning to separate "wow" features from baseline expectations, and to decide what to expand/improve/drop.
- **NOT** for process/internal analysis (it's the customer-satisfaction perspective) or purely technical qualities the end user doesn't perceive.

> The KANO analysis is owned by `pm-features-list`. Plot from its output / survey data; if none exists, route there rather than guessing categories.

## Element vocabulary
| Element | Meaning | Rules |
|---|---|---|
| X axis → | **Functionality** | Level of implementation/investment. Left = absent, right = fully implemented. |
| Y axis ↑ | **Satisfaction** | Bottom = very dissatisfied, top = very satisfied. |
| Rising-then-flat curve | **Must-be (Basic)** | Absence angers; presence only reaches neutral. Never enters the delight region. |
| Straight diagonal | **Performance (One-dimensional)** | More functionality → linearly more satisfaction. From bottom-left to top-right. |
| Steep rising curve | **Attractive (Delighter)** | Absence causes no dissatisfaction; presence sharply raises satisfaction. Starts at origin, no negative part. |
| Flat line at Y≈0 | **Indifferent** | No effect on satisfaction. |
| Descending line | **Reverse** | More functionality lowers satisfaction for some users. |

## Composition rules
- Fixed axes: **X = implementation (0→100%)**, **Y = satisfaction (dissatisfied↓ / satisfied↑)**. Never flip.
- Draw at least the three core curves (Must-be, Performance, Attractive); add Indifferent/Reverse as reference lines.
- Must-be stays below/at the satisfaction axis (never rises into delight); Attractive never dips below zero.
- Label each curve (legend) and differentiate by color/line style.

## Canonical structure
An XY plot; axes cross at origin. Bottom-left = max dissatisfaction, top-right = max satisfaction. Must-be curve from lower-left toward the neutral region; Performance a straight diagonal; Attractive a curve rising steeply from the origin; Indifferent a flat line near Y=0; optional Reverse descending.

## Anti-patterns
- Confused axes (satisfaction on the wrong axis).
- Wrong curve shapes — swapping Must-be and Attractive, or drawing a delighter below the axis.
- Omitting Indifferent/Reverse without a note.
- Cryptic labels (M/O/A) with no legend — not machine-interpretable.
- "Plotting" with no real data (Kano needs survey classification, else it's just an illustration).

## Rendering
- **Mermaid:** no Kano curve type; any hack is meaningless (no continuous curves). Use Excalidraw.
- **Excalidraw:** draw standard axes (X right = "None → Full implementation", Y up = "Dissatisfied → Satisfied"). Then the curves: Must-be (from lower-left, rising steeply then flattening near neutral, never above 0), Performance (straight diagonal lower-left → upper-right), Attractive (from origin curving steeply up-right), Indifferent (flat at Y=0), optional Reverse (descending). Distinct color per curve + legend: e.g. Must-be grey, Performance blue, Attractive green, Indifferent silver, Reverse red. Classify features onto curves rather than plotting bare points.

## Required inputs
- Axis labels + extremes (Absent vs Full; Frustrated vs Delighted).
- Set of features being evaluated.
- Customer feedback / Kano survey answers to classify each feature.
- Which features map to which curve (for the legend).
- Definitions of "satisfaction" (rating scale) and "functionality".

## Worked example (structural)
- X: "None → Fully implemented"; Y: "Dissatisfied → Satisfied".
- **Must-be**: starts below the satisfaction axis, ends near neutral (never above).
- **Performance**: straight from lower-left (dissatisfied at 0%) to upper-right (satisfied at 100%).
- **Attractive**: from origin, rising steeply to (100%, high satisfaction).
- Indifferent: flat mid-line. Features get classified onto these curves from survey data.
