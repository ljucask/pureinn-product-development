# pm-diagrams

> Generate visual diagrams - state machines, sequence diagrams, domain overviews, user flows, architecture

**Phase:** Any (cross-phase)  
**Agent mode:** `synthesis` - runs fully autonomously  
**Version:** 2.0.0  
**Triggers:** diagrams, visual diagram, state machine, sequence diagram, domain model diagram, user flow, architecture, JTBD forces, Excalidraw, Mermaid

---

## When to use

Whenever a visual is needed to communicate architecture, domain structure, user flow, or entity states. Can be called at any phase.

Note: state machines (per entity) and sequence diagrams (per feature) are generated automatically within `pm-entity-registry` and `pm-feature-design` respectively. Use this skill for standalone diagram needs or to regenerate/update a diagram independently.

---

## Two rendering tools

**Mermaid.js (primary - Claude Code workflow)**  
Rendered inline in markdown, embedded directly in live registers and Feature Cards. Claude Code reads and understands Mermaid syntax natively.

**Excalidraw (secondary - human communication)**  
Hand-drawn visual style for team and stakeholder communication. Rendered inline in conversation, exportable to excalidraw.com.

---

## Diagram types

| Type | Tool | Best used in | Primary input |
|---|---|---|---|
| Entity State Machine | Mermaid.js | Phase 4 (`entities.md`) | `pm-entity-registry` output |
| Sequence Diagram | Mermaid.js | Phase 6 JIT (Feature Card Section 3) | `pm-feature-design` |
| Domain Model Overview | Excalidraw | Phase 4 | `entities.md` |
| User Flow | Excalidraw or Mermaid | Phase 2, Phase 6 | Feature description |
| Business Process Model | Excalidraw | Phase 2, FI | Process steps, actors |
| System Architecture | Excalidraw | Phase 4, Phase 6 | Tech stack, components |
| JTBD Four Forces | Excalidraw | Phase 2 | JTBD Analysis output |

---

## How to invoke

```bash
/pm-diagrams                          # interactive - asks what type of diagram
/pm-diagrams --agent                  # autonomous draft from existing artifacts
```

---

## How it works

1. Asks which diagram type is needed (or detects from context)
2. Reads the relevant source artifacts (entities.md, feature card, JTBD analysis, etc.)
3. Selects the appropriate tool (Mermaid vs. Excalidraw) based on diagram type and use case
4. Generates the diagram
5. For Mermaid: embeds in the relevant document (or outputs standalone)
6. For Excalidraw: renders inline + provides export instructions

---

## Dependencies

**No hard dependencies.** Works from whatever artifacts are available.

**Best inputs per diagram type:**
- State Machine: `entities.md` (pm-entity-registry)
- Sequence Diagram: Feature Card Section 3 context (pm-feature-design)
- Domain Overview: `entities.md` + `domain-model.md`
- JTBD Forces: JTBD Analysis output (jtbd-building)

**Related skills:** `pm-entity-registry`, `pm-feature-design`, `jtbd-building`
