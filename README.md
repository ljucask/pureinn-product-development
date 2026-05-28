# Pureinn - AI Product Development Framework

A structured methodology for building products - from zero to launch. Implemented as a Claude Code plugin running an AI-native execution engine.

---

## Install

```bash
/plugin marketplace add ljucask/pureinn-product-development
/plugin install pureinn-product-development@ljucask
```

---

## What this is

**34 skills + 2 commands** covering the full product lifecycle: discovery, validation, domain modeling, feature planning, and FDD delivery.

Three playbooks:

| Playbook | Use when |
|---|---|
| Greenfield | New product, zero users, validating PMF |
| Feature Implementation | Product exists, active users, adding functionality |
| Rebuild | Product exists, active users, technical transformation |

---

## Quick start

```bash
/pureinn "your product idea"
```

Engine scans existing documents, asks 9 intake questions, selects playbook, and shows a dashboard with the ordered skills queue. Run skills one at a time. Run `/pureinn` again after each phase to advance.

```bash
/pureinn-resume [project-slug]
```

Resume a paused project. Omit slug to list all available projects.

```bash
/pureinn map
```

Full framework overview - all playbooks, phases, skills, and artifact chains.

---

## Skill map

### Phase 1 - Foundation
| Skill | Output |
|---|---|
| `/pm-project-charter` | Project Charter, Assumptions & Risks Register |
| `/pm-team-roster` | Team Roster, Decision Rights Matrix, Skill Gap Assessment |
| `/pm-comms-charter` | Communication Charter, Meeting Rhythm |
| `/pm-stakeholder-map` | Stakeholder Map, RACI Matrix, Escalation Tree |

### Phase 2 - Discovery
| Skill | Output |
|---|---|
| `/pm-tech-feasibility` | Tech Feasibility Report |
| `/pm-domain-analysis` | Domain Analysis, Legal & Regulatory Requirements |
| `/pm-market-analysis` | Market Size (TAM/SAM/SOM), Competitor Analysis, SWOT |
| `/pm-personas` | Customer Segments, Personas, Early Adopters Profile |
| `/jtbd-building` | JTBD Analysis, Forces Diagram |
| `/pm-problem-validation` | Problem Validation Summary (Phase 2 exit) |

### Phase 3 - Define & Validation
| Skill | Output |
|---|---|
| `/design-thinking` | Problem Statement, POV, HMW, Elevator Pitch, Validation Hypotheses draft |
| `/pm-hypotheses` | Hypothesis Register + Go/No-Go Decision (hard gate) |
| `/pm-kotler` | Product Definition - Kotler's Five Levels |
| `/pm-lean-canvas` | Lean Canvas |
| `/pm-kpis` | North Star Metric, AARRR, OKRs |
| `/pm-business-case` | Business Case (3-year projections, Go/No-Go) |
| `/pm-product-roadmap` | Product Roadmap v1 |
| `/pm-prd` | PRD - Phase 3 exit artifact |
| `/pm-pitch-deck` | Pitch Deck content brief (+ Gamma visual deck if MCP connected) |

### Phase 4 - Domain Modeling
| Skill | Output |
|---|---|
| `/pm-domain-model` | Domain Model, ERD (+ Excalidraw diagram if MCP connected) |
| `/pm-privacy-requirements` | PII Inventory, Privacy Requirements, GDPR Action Plan |
| `/pm-brd` | BRD Skeleton |
| `/pm-product-roadmap` | Product Roadmap v2 |

### Phase 5 - Feature Planning
| Skill | Output |
|---|---|
| `/pm-features-list` | Features List (FDD format), KANO Analysis, V×C Matrix |
| `/pm-mvp-scope` | MVP Scope, Feature Sets (MFS→FS), Delivery Stripes |
| `/pm-product-roadmap` | Product Roadmap v3 |

### Phase 6 + 7 - FDD Delivery
| Skill | Output |
|---|---|
| `/pm-stripe` | Stripe Kickoff, routing per feature, Stripe Close |
| `/pm-feature-set-overview` | Feature Set scope overview |
| `/pm-brd` | Full BRD per Feature Set |
| `/pm-fsd` | Functional Specification per Feature Set |
| `/pm-business-rule-critical` | RULE-A: Critical Invariants |
| `/pm-business-rule-core` | RULE-B: Core Business Rules |
| `/pm-business-rule-governance` | RULE-C: Governance / Policy / UX Rules |

### Cross-phase
| Skill | When |
|---|---|
| `/pm-glossary` | Start in Phase 1, update continuously |
| `/pm-diagrams` | Any phase - Domain Model Overview, User Flow, System Architecture, JTBD Forces |

### Feature Implementation - migration path
| Skill | Purpose |
|---|---|
| `/pm-reverse-extract` | Extracts feature inventory from an existing product into Notion + local artifacts. Run instead of pm-features-list + pm-mvp-scope for products built outside the framework. |

---

## MCP integrations

| MCP | Skills | Without MCP |
|---|---|---|
| Notion | `pm-features-list`, `pm-mvp-scope`, `pm-glossary`, `pm-domain-model`, `pm-kpis`, `pm-brd`, `pm-privacy-requirements`, `pm-reverse-extract` | Markdown artifacts only, Notion push skipped |
| Excalidraw | `pm-diagrams`, `pm-domain-model` | Mermaid text output only |
| Gamma | `pm-pitch-deck` | Slide content brief only |

Connect via `/mcp` in Claude Code.

---

## Project output structure

```
pureinn-workspace/
  [project-slug]/
    state.json              - Current phase, playbook, completed phases
    assessment.md           - Initial product assessment
    pureinn-variables.md    - Notion URLs per project (fill in once)
    glossary.md
    artifacts/
      phase-1/
      phase-2/
      phase-3/
      phase-4/
      phase-5/
      phase-6/
        [fs-id]-overview.md
        [fs-id]-brd.md
        [fs-id]-fsd.md
        feature-cards/
      phase-7/
```

---

## Core principles

- **Impact over activity.** Decisions measured by outcome, not output.
- **Evidence over politics.** Validate before building. Research before deciding.
- **Human-in-the-loop.** Every phase requires human approval before advancing.
- **Bring your data.** Claude structures and formalizes - it does not hallucinate market data or domain facts.
- **Simplicity is a feature.** Remove everything that does not serve the user directly.
