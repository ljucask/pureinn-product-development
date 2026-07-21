---
name: pm-diagrams
description: Generate any of 17 diagram types across 6 categories (domain/data, process/behavior, UX, architecture, planning/delivery, strategic). Two rendering modes - Mermaid.js (primary, embedded in markdown registers) and Excalidraw (visual overviews). Call with a slug for a specific diagram (`/pm-diagrams bpmn`, `/pm-diagrams erd`, `/pm-diagrams journey`...) or with no argument for a context-aware recommendation based on workspace state. Each type has a composition reference in references/[slug].md that the skill reads before drawing. Cross-phase - callable at any point.
license: MIT
metadata:
  agent-mode: synthesis
  author: https://github.com/ljucask
  version: "3.0.0"
  domain: product-management
  triggers: diagrams, visual diagram, state machine, sequence diagram, ERD, entity relationship, domain model, user flow, flowchart, BPMN, business process, customer journey, wireflow, screen flow, system architecture, C4, dependency graph, story map, gantt, roadmap timeline, JTBD forces, 2x2 matrix, Kano, SWOT, Excalidraw, Mermaid
  role: specialist
  scope: visualization
  output-format: diagram
  related-skills: pm-entity-registry, pm-feature-design, jtbd-building, pm-features-list, pm-product-roadmap, pm-market-analysis
---

# PM - Diagrams

## Agent mode (`--agent`)

Supports `--agent`: runs autonomously in a subagent, drafts the diagram from existing inputs, and returns a short summary + coverage note.

- **No flag** → interactive (default); if inputs are heavy, offer agent mode.
- **`--agent`** → obey. First check inputs are complete. Anything missing: do NOT invent it - mark `[ASSUMED - what/why]` in the output and summary. Never hallucinate to fill a gap.

---

## What this skill does

Generates visual diagrams. It is a **rendering engine + composition knowledge** utility: it owns *how each diagram type is correctly composed*, not the analysis behind it. The correct composition rules for every type live in **`references/[slug].md`** - the skill reads the relevant reference before drawing, so it never renders from memory.

**Two rendering modes:**
- **Mermaid.js** (primary, Claude Code workflow) - rendered inline in markdown, embedded in live registers and Feature Cards. Claude reads Mermaid natively. Use for anything that must be read as a specification.
- **Excalidraw** (secondary, human communication) - hand-drawn visual overviews for stakeholders. Use for high-level maps where the value is visual, not machine-readable.

### The 17-type catalogue (slug → type)

| Slug | Type | Primary tool | Phase | Ownership |
|---|---|---|---|---|
| **Domain / data** |
| `state` | Entity State Machine | Mermaid | 4 | pm-diagrams |
| `domain` | Domain Model Overview | Excalidraw | 4 | pm-diagrams |
| `erd` | ERD (crow's-foot) | Mermaid | 4 | pm-diagrams |
| **Process / behavior** |
| `sequence` | Sequence Diagram | Mermaid | 6 JIT | pm-diagrams |
| `flow` | User Flow / Flowchart | Mermaid/Excalidraw | 2, 6 | pm-diagrams |
| `bpmn` | Business Process (BPMN 2.0) | Excalidraw | 2, FI | pm-diagrams |
| `journey` | Customer Journey Map | Excalidraw | 2 | pm-diagrams |
| **UX / design** |
| `wireflow` | Wireflow / Screen Flow | Excalidraw | 6 | pm-diagrams |
| **Architecture** |
| `architecture` | System Architecture | Excalidraw | 4, 6 | pm-diagrams |
| `c4` | C4 (Context + Container) | Mermaid | 4 | pm-diagrams |
| **Planning / delivery** |
| `dependency` | Dependency Graph | Mermaid | 5 | render for pm-features-list |
| `storymap` | User Story Map | Excalidraw | 5 | pm-diagrams |
| `gantt` | Gantt / Timeline Roadmap | Mermaid | 3b, 5 | render for pm-product-roadmap |
| **Strategic** |
| `jtbd` | JTBD Four Forces | Excalidraw | 2 | pm-diagrams |
| `matrix` | 2×2 Matrix (generic) | Excalidraw | various | pm-diagrams |
| `kano` | Kano Model | Excalidraw | 5 | render for pm-features-list |
| `swot` | SWOT | Excalidraw | 2 | render for pm-market-analysis |

**"Render for" ownership (`dependency`, `gantt`, `kano`, `swot`):** the analysis is owned by another skill. This skill only *renders* it. Read the data from the owning artifact; if the analysis does not exist yet, **route to the owning skill** rather than inventing the analysis. Never fabricate a Kano classification, SWOT factors, dependency edges, or a dated plan.

---

## Step 0: Route by argument

**If a slug was passed** (`/pm-diagrams bpmn`, `/pm-diagrams erd`, ...): skip the menu. Go straight to Step 1 for that type. If the slug is unknown, show the catalogue and ask which was meant.

**If no argument was passed:** run the **context-aware recommendation** below - do not dump a generic menu.

### Context-aware recommendation (no argument)

1. Read `state.json` (or scan the workspace) → current phase + which artifacts exist.
2. Detect **visual gaps** - an artifact exists but its diagram does not:

| Signal in the workspace | Recommend |
|---|---|
| `entities.md` exists, entity has no state machine | `state` |
| domain model exists, no ERD | `erd` |
| Phase 2 + personas exist, no journey map | `journey` |
| `feature_list.md` has dependencies, no dependency graph | `dependency` |
| Phase 5, no story map | `storymap` |
| Phase 6, a feature is in design | `sequence` |
| JTBD analysis exists, no Four Forces | `jtbd` |
| market analysis exists, no SWOT visual | `swot` |
| architecture discussed, nothing drawn | `architecture` / `c4` |

3. Rank by proximity to the current phase (closest to active work first).
4. Use the AskUserQuestion tool: offer the **top 3** context-relevant recommendations, each with the reason it fits the current state, plus an **"Other - pick from the full catalogue"** option. Mark the highest-ROI one **(Recommended)**.

This is the active form of the "situation-aware + proactive" standard: read state, propose the highest-value visual for the current position, never a fixed script. (Full interaction standard: CLAUDE.md.)

---

## Step 1: Load the composition reference

Before gathering inputs or drawing, **read `references/[slug].md`** for the selected type. It carries the element vocabulary, composition rules, canonical structure, anti-patterns, Mermaid/Excalidraw rendering notes, required inputs, and a worked example. Compose strictly to that reference - it is the source of correctness for the diagram's form.

For **"render for" types** (`dependency`, `gantt`, `kano`, `swot`): also locate the owning artifact named in the reference's "Source of truth". If it is missing, route to the owning skill instead of inventing the analysis.

---

## Step 2: Gather inputs

Use the **Required inputs** list in the loaded reference. Gather them from:
1. The **source-of-truth artifact** first (see rule below), then
2. The user, for anything not in an artifact.

**Interaction:** group related questions (2-4 per round) and confirm before drawing. For any A/B/C/D choice, use the AskUserQuestion tool with one option marked **(Recommended)** - never print options as plain text. Keep open-ended questions free-text. If the user is unsure, propose 3-4 concrete options plus "Other". Surface an assumption the moment you make one; never fabricate to fill a gap. (Full standard: CLAUDE.md.)

**Source-of-truth rule:** when the content being diagrammed lives in a register (`entities.md`, `business_rules.md`, `feature_list.md`, process-flows, roadmap), read the register first and diagram what it says - never render from memory or from the user's paraphrase alone. If the user's description conflicts with the register, flag the divergence before drawing; a polished diagram of stale content is worse than no diagram, because people trust visuals more than they trust files.

---

## Step 3: Generate the diagram

Render per the reference's **Rendering notes**:
- **Mermaid** types → emit a fenced ```mermaid block. Optionally validate/repair with the mermaid MCP (`mcp__mermaid__validate_and_render_mermaid_diagram`) before finalizing.
- **Excalidraw** types → render with the Excalidraw MCP (`mcp__claude_ai_Excalidraw__create_view`) if available; otherwise fall back to the Mermaid approximation named in the reference and note that Excalidraw was unavailable.

Follow the reference's element vocabulary, composition rules, and color semantics exactly. Order Excalidraw elements for clean streaming (background zone → shape → label → arrow).

---

## Step 4: Export / checkpoint (optional, Excalidraw only)

After rendering an Excalidraw diagram, use the AskUserQuestion tool:
- Option A: "Export to excalidraw.com - shareable link for editing"
- Option B: "Save checkpoint - continue editing in a future session (Recommended)"
- Option C: "Done"

If A: call `mcp__claude_ai_Excalidraw__export_to_excalidraw` and return the URL.
If B: note the checkpoint ID from `create_view`; it can be restored with `/pm-diagrams` later.

Mermaid diagrams are already embedded in markdown - no export step needed.

---

## Notion push

After generating a diagram, update the Diagrams page in Notion.

1. Read `pureinn-variables.md` key `"Diagrams"` → get Page URL.
2. If blank: skip, remind user to add URL to pureinn-variables.md.
3. Call `mcp__claude_ai_Notion__notion-update-page` with `command: "insert_content"`:

```
## [Diagram Name] — [date]

**Type:** [type] (`[slug]`)
**Feature/Context:** [FEAT-ID or phase context]

[Mermaid code block, or Excalidraw URL / "Excalidraw checkpoint"]
```

Keeps the Diagrams page as a running catalogue of all generated visuals.

---

## Internal completeness checklist

<!-- Claude reference only -->

**Before generating:**
- [ ] Slug resolved (argument) or recommended from workspace state (no argument)
- [ ] `references/[slug].md` read
- [ ] For "render for" types: owning artifact located, or routed to owning skill
- [ ] Required inputs gathered from source-of-truth first, then user
- [ ] Correct tool (Mermaid vs Excalidraw) per the reference

**After generating:**
- [ ] Composition matches the reference (vocabulary, rules, structure)
- [ ] All elements labeled and readable (Excalidraw font ≥ 16)
- [ ] Mermaid validated (if MCP available)
- [ ] Notion push done (or skipped with reason)

---

## Handoff

**Čo si teraz má:** Konkrétny diagram ([type]) zložený podľa správneho notačného štandardu - použiteľný v dokumentácii, registri alebo na komunikáciu.

**Ďalší krok:** Pokračuj v aktuálnej fáze - `/pm-diagrams` je cross-phase utilita, spúšťaj ho kedykoľvek treba vizuál (`/pm-diagrams [slug]` pre konkrétny typ). `/pureinn` ukáže ďalší krok podľa fázy.

**Môžeš preskočiť ak:** diagram daného typu už existuje a je aktuálny - regeneruj len keď sa zmenil zdrojový register.
