# JTBD Four Forces — composition reference

**Slug:** `jtbd` · **Tool:** Excalidraw (Mermaid only crudely) · **Phase:** 2 · **Source of truth:** `jtbd-building` output / switch interviews · **Standard:** Bob Moesta's Forces of Progress

## Purpose
Show the forces that drive a customer to switch to a new solution versus those that hold them back. Progress happens only when the forces pushing forward (Push + Pull) outweigh those blocking (Anxiety + Habit). Explains why a customer leaves the current product for a new one.

## When to use / when NOT
- **Use** to analyze customer switching decisions (from JTBD interviews): what motivates the search for a new solution and what delays the change.
- **NOT** for org strategy or competitive analysis (→ `swot`). This evaluates one customer's decision, not a company's state. Not for internal process mapping.

## Element vocabulary
| Element | Meaning | Direction |
|---|---|---|
| Horizontal axis | **Timeline** | Current state (left) → new solution (right); the switch point in the middle. |
| Arrow → | **Push** (of the situation) | Frustrations with today driving the customer to look. Points **right** (toward switch). |
| Arrow → | **Pull** (of the new solution) | Attractions/benefits of the new solution. Points **right** (toward switch). |
| Arrow ← | **Anxiety** (of the new solution) | Fears/uncertainty about the new solution. Points **left** (against switch). |
| Arrow ← | **Habit / Inertia** (of the present) | Comfort, sunk cost, routine of the current solution. Points **left** (against switch). |

## Composition rules
- **Push** and **Pull** point right (driving forward); **Anxiety** and **Habit** point left (blocking).
- Read left-to-right as progress toward change. Left = reasons rooted in the current state; right = the new solution.
- **Decision rule to visualize:** switch happens iff `Push + Pull > Anxiety + Habit`.
- Always draw **all four** forces — omitting one (often Habit) makes it incomplete. Each force is its own labelled arrow.
- No sequential steps/loops — this is not a flow. Forces converge implicitly at the center; arrows shouldn't cross.

## Canonical structure
Four fields in two columns. Left column = current state, right = new solution:
- Top-left: **Push** (pressure of the current situation)
- Bottom-left: **Habit** (attachment to the status quo)
- Top-right: **Pull** (attraction of the new solution)
- Bottom-right: **Anxiety** (fear of the new solution)
Each arrow runs from its corner toward the central switch point; a horizontal axis joins the two sides.

## Anti-patterns
- Missing one of the four forces.
- Reversed arrows (Pull pointing left, Anxiety pointing right) — changes the meaning.
- Vertical axis / chained transitions / branches — it is not a sequential process.
- Renaming forces to non-standard terms ("Excitement" for Pull).
- Forces stated without concrete context (each should come from real findings, e.g. a switch interview).
- Styling it like a SWOT — fields must be named Push/Pull/Anxiety/Habit.

## Rendering
- **Mermaid:** no four-forces type. A `flowchart` with each force pointing at a central "Customer" node only conveys content, not the true layout, and can't color arrows. Use it only as a content mirror; prefer Excalidraw.
- **Excalidraw:** two horizontal regions — left "Current state", right "New solution". Two arrows on the left edge (Push, Habit) pointing right, two on the right (Pull, Anxiety) pointing left; all toward the center. Recommended colors: green = driving forces (Push/Pull), red = blocking forces (Anxiety/Habit). Label each arrow. Keep symmetry (Push opposite Pull top row, Habit opposite Anxiety bottom row); draw the axis line between regions.

## Required inputs
- Current state (current solution / habitual behavior).
- New solution / proposed change.
- Push list — concrete problems driving change.
- Pull list — attractive benefits of the new solution.
- Anxiety list — fears about adopting the new solution.
- Habit list — comforts/benefits of the current solution the user won't give up.

## Worked example (structural)
Switching from driving a car to an e-scooter:
- **Push:** high fuel cost, traffic jams.
- **Pull:** eco-friendly, cheaper, faster in the city.
- **Anxiety:** risk of falling, worries about securing the scooter.
- **Habit:** comfort of a personal car, carrying belongings.
Excalidraw: left "Current state" with Push (green, →) above Habit (red, ←); right "New solution" with Pull (green, ←... toward center) above Anxiety (red), all converging on the central switch point.
