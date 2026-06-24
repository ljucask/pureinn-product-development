<p align="center">
  <img src="assets/pureinn-cover.png" width="100%" alt="Pureinn - AI PM Workflow Engine"/>
</p>

# Pureinn - AI Product Development Framework

A structured methodology for building products - from zero to launch. Implemented as a Claude Code plugin running an AI-native execution engine.

---

## Install

```bash
/plugin marketplace add ljucask/pureinn-product-development
/plugin install pureinn-product-development@pureinn-product-development
```

---

## What this is

**39 active skills + 2 commands** covering the full product lifecycle: discovery, validation, domain modeling, feature planning, FDD delivery, reconciliation-based rebuild, and workspace health-check.

Three playbooks:

| Playbook | Use when |
|---|---|
| Greenfield | New product, zero users, validating PMF |
| Feature Implementation | Product exists, active users, adding functionality |
| Rebuild | Product exists, active users, technical transformation *(coming soon)* |

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

## Fast Track

Skip upstream phases and go straight to spec + build. The engine detects the right path automatically after intake - or you can declare it explicitly.

### Greenfield Express
Use when: you have a validated idea, know the problem and customer, and don't need discovery.

```
/pureinn "your idea"     → workspace setup (3 questions)
/pm-entity-registry      → lean entity list + key states
/pm-business-rules-library → core rules, Draft mode
/pm-features-list        → feature inventory + FEAT-IDs
/pm-mvp-scope            → MVP scope + Delivery Stripes
/pm-feature-design [ID]  → JIT spec per feature
→ Build → Test → Release
```

Skips: Phase 1 (Foundation), Phase 2 (Discovery), Phase 3a/3b (Validation + Commercial).

---

### Feature Implementation - First Run
Use when: existing product, first time using Pureinn on this codebase.

```
/pureinn [project]       → workspace setup
/common-ground           → tech context from existing code
/pm-reverse-extract      → bootstrap domain registers + feature inventory from codebase
                           (shows what it found - you confirm or correct)
/pm-feature-design [ID]  → JIT spec for the feature you want to build
→ Build → Test → Release
```

FI delivery rules always apply: feature flags, regression suite, gradual rollout.

---

### Feature Implementation - Returning Session
Use when: Pureinn already ran on this project, context files exist.

```
/pureinn [project-slug]  → loads state.json + context
/pm-feature-design [ID]  → JIT spec directly
→ Build → Test → Release
```

If FEAT-ID doesn't exist yet: add it to `feature_list.md`, create stub card, then run `pm-feature-design`.

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
| `/pm-market-analysis` | Market Size (TAM/SAM/SOM), Competitor Analysis, SWOT - three input paths: paste research (A), guided elicitation (B), AI-powered via OpenAI (C) |
| `/pm-personas` | Customer Segments, Personas, Early Adopters Profile |
| `/jtbd-building` | JTBD Analysis, Forces Diagram |
| `/pm-problem-validation` | Problem Validation Summary (Phase 2 exit) |

### Phase 3a - Validation
| Skill | Output |
|---|---|
| `/design-thinking` | Problem Statement, POV, HMW, Elevator Pitch, Validation Hypotheses draft |
| `/pm-hypotheses` | Hypothesis Register + Go/No-Go Decision (hard gate - GO required for Phase 3b) |

### Phase 3b - Commercial Definition
| Skill | Output |
|---|---|
| `/pm-kotler` | Product Definition - Kotler's Five Levels |
| `/pm-lean-canvas` | Lean Canvas (problem-focused, startups) |
| `/pm-business-model` | Business Model Canvas (optional fuller alternative for established/complex models) |
| `/pm-kpis` | North Star Metric, AARRR, OKRs |
| `/pm-business-case` | Business Case (3-year projections, Go/No-Go) |
| `/pm-product-roadmap` | Product Roadmap v1 |
| `/pm-prd` | PRD - Phase 3b exit artifact (frozen after creation) |
| `/pm-pitch-deck` | Pitch Deck content brief (+ Gamma visual deck if MCP connected) |

### Phase 4 - Domain Modeling + Register Setup
| Skill | Output |
|---|---|
| `/pm-domain-model` | Domain Model, ERD (+ Excalidraw diagram if MCP connected) |
| `/pm-entity-registry` | entities.md - entity states + Mermaid state machines (Live Register 1) |
| `/pm-business-rules-library` | business_rules.md + decision_models.md in Draft mode (Live Registers 2+3) |
| `/pm-privacy-requirements` | PII Inventory, Privacy Requirements, GDPR Action Plan |
| `/pm-product-roadmap` | Product Roadmap v2 |

### Phase 5 - Feature Planning
| Skill | Output |
|---|---|
| `/pm-features-list` | feature_list.md (FDD Feature List, Live Register 4), KANO Analysis, V×C Matrix + stub Feature Cards |
| `/pm-mvp-scope` | MVP Scope, Delivery Stripes (domain-focused channels), Feature-to-Stripe assignment |
| `/pm-product-roadmap` | Product Roadmap v3 |

### Phase 6 + 7 - FDD Delivery (JIT per Feature)
| Skill | Output |
|---|---|
| `/pm-stripe` | Session orchestrator - stripe dashboard, advance feature through lifecycle (1_Backlog → 6_Shipped), Impact Analysis |
| `/pm-feature-viability` | Feature Viability Assessment (optional) - KANO, MDP scope, success metrics before JIT design |
| `/pm-feature-design` | Feature Card Sections 1-3 (JIT, per feature) - Biznis Mantinely, ACs, sequence diagram, UX/UI context |

### Cross-phase
| Skill | When |
|---|---|
| `/pm-glossary` | Start in Phase 1, update continuously |
| `/pm-diagrams` | Any phase - Domain Model Overview, User Flow, System Architecture, JTBD Forces |

### Feature Implementation - migration path
| Skill | Purpose |
|---|---|
| `/pm-reconcile` | **Rebuild playbook.** Existing code + legacy docs (BRD/FSD/domain models) that conflict with each other and the code. First plans (which areas, what order, target structure), then reconciles per layer - `/pm-reconcile domain` → `rules` → `features` - with code = structural truth, docs = business logic, real conflicts asked. Produces a living Reconciliation Report and rebuilds the registers + feature inventory clean. Entry point when docs are stale or the team is changing. |
| `/pm-reconcile-status` | Read-only progress dashboard for a multi-session reconcile: which areas are done/pending, open divergences awaiting a team decision, next area command. |
| `/pm-entity-registry` | Extracts entity states from existing codebase into entities.md |
| `/pm-business-rules-library` | Extracts business rules from existing codebase into business_rules.md + decision_models.md |
| `/pm-reverse-extract` | Extracts feature inventory from an existing product into Notion + local artifacts. Run instead of pm-features-list + pm-mvp-scope for products built outside the framework. |
| `/pm-audit` | **Workspace health check.** Scans the Pureinn artifacts against current conventions, finds drift/errors, fixes mechanical ones, asks about judgment calls. Migrates older-version workspaces. Run after reconcile/extract, on an older workspace, or any time before continuing. |

---

## MCP integrations

| MCP | Skills | Without MCP |
|---|---|---|
| Notion | `pm-features-list`, `pm-mvp-scope`, `pm-glossary`, `pm-domain-model`, `pm-kpis`, `pm-privacy-requirements`, `pm-reverse-extract`, `pm-reconcile`, `pm-feature-card` | Markdown artifacts only, Notion push skipped |
| Figma | `pm-feature-design` | Paste Figma URL or attach screenshot manually |
| Excalidraw | `pm-diagrams`, `pm-domain-model` | Mermaid.js output only (state machines, sequence diagrams always available) |
| Gamma | `pm-pitch-deck` | Slide content brief only |

Connect via `/mcp` in Claude Code.

**Notion setup:** Duplicate the Pureinn Notion template to your workspace, then paste the URLs into `pureinn-variables.md` when the engine creates it. See [NOTION_TEMPLATE.md](NOTION_TEMPLATE.md) for the setup guide and template link.

---

## Project output structure

```
pureinn-workspace/
  [project-slug]/
    state.json              - Current phase, playbook, completed phases, register init flags
    assessment.md           - Initial product assessment
    pureinn-variables.md    - Notion URLs per project (fill in once)
    glossary.md
    product/
      PRD_master.md         - pm-prd Phase 3b output (frozen after creation, never overwritten)
    domain/                 - Living registers (source of truth for AI during Phase 6-7)
      entities.md           - Entity states + Mermaid state machines (Live Register 1)
      business_rules.md     - Business Rules Library (Live Register 2)
      decision_models.md    - Decision Models Matrix (Live Register 3)
    features/
      feature_list.md       - FDD Feature List (Live Register 4)
      cards/
        FEAT-ORD-001.md     - Feature Cards (one per feature, 6-state lifecycle)
        FEAT-PAY-001.md
    initiatives/
      [initiative-slug]/    - One folder per major new initiative (FI Track B or scoped launch)
        discovery/          - Track B discovery outputs
        prd.md              - Initiative PRD (scoped, living)
        kano-analysis.md
        value-complexity-matrix.md
    artifacts/
      phase-1-foundation/
      phase-2-discovery/
      phase-3-define/
      phase-4-domain/
      phase-5-planning/
```

---

## Examples

The `examples/` folder contains realistic output samples showing what the framework produces in a real project scenario. Use them to calibrate expectations before running skills for the first time.

**Available examples:**

| Example | Playbook | Domain | What it shows |
|---|---|---|---|
| [saas-subscription/](examples/saas-subscription/) | Feature Implementation | Subscription Billing (Stripe) | Initiative PRD, full domain registers (entities, business rules, feature list), two Feature Cards at different lifecycle stages (6_Shipped + 3_Ready_to_Build) |

---

## Core principles

- **Impact over activity.** Decisions measured by outcome, not output.
- **Evidence over politics.** Validate before building. Research before deciding.
- **Human-in-the-loop.** Every phase requires human approval before advancing.
- **Bring your data.** Claude structures and formalizes - it does not hallucinate market data or domain facts.
- **Simplicity is a feature.** Remove everything that does not serve the user directly.
