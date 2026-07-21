# pm-diagrams

> Generate any of 17 diagram types across 6 categories - domain/data, process/behavior, UX, architecture, planning/delivery, strategic

**Phase:** Any (cross-phase)
**Agent mode:** `synthesis` - runs fully autonomously
**Version:** 3.0.0
**Triggers:** diagrams, visual diagram, state machine, sequence diagram, ERD, entity relationship, domain model, user flow, flowchart, BPMN, business process, customer journey, wireflow, screen flow, system architecture, C4, dependency graph, story map, gantt, roadmap timeline, JTBD forces, 2x2 matrix, Kano, SWOT, Excalidraw, Mermaid

---

## When to use

Whenever a visual is needed - architecture, domain structure, user flow, entity states, a business process, a journey map, or a strategic framework diagram. Call at any phase, with a specific type or with no argument for a recommendation.

Note: state machines (per entity) and sequence diagrams (per feature) are generated automatically within `pm-entity-registry` and `pm-feature-design` respectively. Use this skill for standalone diagram needs or to regenerate/update a diagram independently.

---

## Two rendering tools

**Mermaid.js (primary - Claude Code workflow)**
Rendered inline in markdown, embedded directly in live registers and Feature Cards. Claude Code reads and understands Mermaid syntax natively.

**Excalidraw (secondary - human communication)**
Hand-drawn visual style for team and stakeholder communication. Rendered inline in conversation, exportable to excalidraw.com.

---

## The 17-type catalogue

Each type has a dedicated composition reference (`references/[slug].md`) that the skill reads before drawing - the element vocabulary, composition rules, canonical structure, anti-patterns, and rendering notes for that specific notation.

| Slug | Type | Tool | Best used in |
|---|---|---|---|
| **Domain / data** |
| `state` | Entity State Machine | Mermaid | Phase 4 (`entities.md`) |
| `domain` | Domain Model Overview | Excalidraw | Phase 4 |
| `erd` | ERD (crow's-foot) | Mermaid | Phase 4 |
| **Process / behavior** |
| `sequence` | Sequence Diagram | Mermaid | Phase 6 JIT (Feature Card Section 3) |
| `flow` | User Flow / Flowchart | Mermaid or Excalidraw | Phase 2, Phase 6 |
| `bpmn` | Business Process (BPMN 2.0) | Excalidraw | Phase 2, Feature Implementation |
| `journey` | Customer Journey Map | Excalidraw | Phase 2 |
| **UX / design** |
| `wireflow` | Wireflow / Screen Flow | Excalidraw | Phase 6 |
| **Architecture** |
| `architecture` | System Architecture | Excalidraw | Phase 4, Phase 6 |
| `c4` | C4 (Context + Container) | Mermaid | Phase 4 |
| **Planning / delivery** |
| `dependency` | Dependency Graph | Mermaid | Phase 5 |
| `storymap` | User Story Map | Excalidraw | Phase 5 |
| `gantt` | Gantt / Timeline Roadmap | Mermaid | Phase 3b, Phase 5 |
| **Strategic** |
| `jtbd` | JTBD Four Forces | Excalidraw | Phase 2 |
| `matrix` | 2×2 Matrix (generic) | Excalidraw | Various |
| `kano` | Kano Model | Excalidraw | Phase 5 |
| `swot` | SWOT | Excalidraw | Phase 2 |

Four types (`dependency`, `gantt`, `kano`, `swot`) render an analysis owned by another skill (`pm-features-list`, `pm-product-roadmap`, `pm-market-analysis`). If that analysis doesn't exist yet, `pm-diagrams` routes there instead of inventing one.

---

## How to invoke

```bash
/pm-diagrams                          # no argument - context-aware recommendation
/pm-diagrams bpmn                     # specific type by slug - skips the menu
/pm-diagrams erd
/pm-diagrams --agent                  # autonomous draft from existing artifacts
```

---

## How it works

1. **With a slug argument:** skips straight to gathering inputs for that type.
2. **With no argument:** reads workspace state (`state.json`, existing artifacts) and detects "visual gaps" - e.g. entities without a state machine, a feature list with dependencies but no graph - then recommends the top 3 highest-value diagrams for the current phase.
3. Loads the composition reference (`references/[slug].md`) for the selected type.
4. Reads the relevant source artifact first (entities.md, feature_list.md, JTBD analysis, market analysis...), then asks the user for anything missing.
5. Generates the diagram per the reference's rendering notes (Mermaid or Excalidraw).
6. For Mermaid: embeds in the relevant document (or outputs standalone).
7. For Excalidraw: renders inline + offers export/checkpoint.

---

## Dependencies

**No hard dependencies.** Works from whatever artifacts are available; for the four "render for" types it routes to the owning skill if no analysis exists yet.

**Best inputs per diagram type:**
- State Machine / ERD / Domain Overview: `entities.md` (`pm-entity-registry`)
- Sequence Diagram: Feature Card Section 3 context (`pm-feature-design`)
- Dependency Graph / Kano: `feature_list.md` (`pm-features-list`)
- Gantt: `pm-product-roadmap` output
- JTBD Forces: JTBD Analysis output (`jtbd-building`)
- SWOT: `pm-market-analysis` output

**Related skills:** `pm-entity-registry`, `pm-feature-design`, `jtbd-building`, `pm-features-list`, `pm-product-roadmap`, `pm-market-analysis`
