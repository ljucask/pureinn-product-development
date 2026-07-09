# How Pureinn Works

A reference for the concepts, mechanics, and rules that govern the framework.

---

## Which playbook?

Two questions route you to the right entry path:

```
Does the product already exist?
            │
┌───────────┴───────────────────────────┐
│ No / yes but no users yet             │ Yes, with active users
▼                                       ▼
GREENFIELD                    What do you need to do?
                                        │
                        ┌───────────────┴──────────────────┐
                        │ Onboard it into Pureinn           │ Add new functionality
                        ▼                                   ▼
                     REBUILD                     FEATURE IMPLEMENTATION
```

| Situation | Playbook |
|---|---|
| New product, 0 users, validating PMF | Greenfield |
| Existing product + legacy docs (BRD/FSD) that conflict with code | Rebuild → A1 Reconcile |
| Existing product, docs clean or absent | Rebuild → A2 Bootstrap |
| Already onboarded, adding new functionality | Feature Implementation |

Run `/pureinn [product idea or name]` and the engine runs this decision tree automatically.

---

## Stage shortcuts

You don't have to start at Phase 1. A stage keyword jumps straight into one part of the framework - useful when you only need Pureinn for a slice.

```bash
/pureinn define                        # current project → Commercial Definition
/pureinn vezmee model                  # named project → Domain Modeling
/pureinn discover "food delivery app"  # fresh project → straight into Discovery
```

**How it behaves:** the engine resolves the keyword to its phase, checks what inputs that phase needs. If something upstream is missing, it offers options: proceed with `[ASSUMED]` markers, jump back to build the input, or proceed anyway. It never hard-blocks except at the Phase 3a GO gate.

If no workspace exists yet, it scaffolds the full project first (folder tree + `state.json` + variables) so everything downstream works.

---

## Agent mode

Any skill accepts `--agent`. The skill runs autonomously in a subagent - keeping your main session clean - drafts the artifact from existing inputs, and returns a short summary you review afterward.

```bash
/pm-prd --agent
/pm-market-analysis --agent
```

Each skill declares its `agent-mode`:

| agent-mode | Skills | `--agent` behavior |
|---|---|---|
| `synthesis` | Assemble/structure existing artifacts (PRD, market analysis, roadmap, pitch deck...) | Runs fully, drafts + returns summary |
| `decision` | You commit to something (personas, JTBD, lean canvas, MVP scope, feature design...) | Drafts, then **requires your review** before anything is final |
| `never` | Value is the live dialogue (stress-test, root-cause, reconcile, hypotheses...) | Declines `--agent`, warns once, proceeds interactively |

**Two rules hold across all modes:**
- **The flag is obeyed.** No flag = interactive default. `--agent` = run autonomously.
- **Missing inputs are never invented.** A subagent can't ask you, so any gap is marked `[ASSUMED - what/why]` in the output. Use `--agent` when you have solid inputs and want a fast first draft.

---

## Phase gates

Every phase requires human approval before advancing. Run `/pureinn` after a phase to trigger its exit gate.

| Gate type | Phases | Behavior |
|---|---|---|
| **Hard gate** | Phase 3a (Go/No-Go), Phase 6 (Design Inspection) | Cannot be bypassed. Missing criteria = blocked. |
| **Soft gate + FORCE** | Phase 1, 2, 4, 5 | Criteria checked, gaps named. You can proceed by acknowledging risk. |
| **Implicit gate** | Phase 3b | Condition-based entry only (requires Phase 3a GO verdict). |

Hard gates exist where proceeding causes compounding, uncorrectable waste. Soft gates exist where partial inputs produce partial output and you can consciously accept the gap.

---

## Key concepts

### Live Registers

Four living documents that are the source of truth throughout Phase 4-7. Initialized in Phase 4, enriched continuously during the JIT build cycle.

| Register | File | Content |
|---|---|---|
| R1 | `entities.md` | Entity list, states, Mermaid state machines; guard conditions added JIT |
| R2 | `business_rules.md` | Business rules (`BR-[DOMAIN]-[NUMBER]`); Draft until pm-feature-design finalizes JIT |
| R3 | `decision_models.md` | Decision tables (`TBL-[DOMAIN]-[NUMBER]`); Draft until finalized JIT |
| R4 | `feature_list.md` | Feature inventory (`FEAT-[DOMAIN]-[NUMBER]`), KANO, V×C, Feature Set grouping |

### Feature Card

The atomic delivery unit. One Feature Card per feature, six-state lifecycle:

```
1_Backlog → 2_Spec_Done → 3_Ready_to_Build → 4_In_Build → 5_In_Review → 6_Shipped
```

- **Sections 1-3** written JIT by `/pm-feature-design` just before build
- **Section 4** written after build completes
- **Immutable after 6_Shipped**

### Feature Set vs. Delivery Stripe vs. Feature Card

| Concept | What it is | Role |
|---|---|---|
| **Feature Set** | Logical domain grouping (`FS-NN: name`) | Organizing principle only - not a spec unit |
| **Delivery Stripe** | Domain-focused parallel development channel | One stripe = one isolated channel; one feature active at a time |
| **Feature Card** | Atomic delivery unit, 6-state lifecycle | The build spec. Section 3 = what developers read |

Example: 50 MVP features across 25 Feature Sets → assigned to 3 parallel Delivery Stripes → each designed JIT just before build.

### KANO + Value vs. Complexity

Both run in `/pm-features-list`. Both are required - KANO without V×C doesn't give you a delivery order.

| Method | What it classifies | Output |
|---|---|---|
| KANO | Feature value type | Must-be / Performance / Delighter / Indifferent → what enters MVP |
| V×C Matrix | Impact vs. effort | Quick Wins / Big Bets / Fill-ins / Time Wasters → delivery order |

### JIT Design

Features are designed Just-In-Time - one feature, immediately before it enters build. Not upfront per Feature Set.

| Upfront approach (not used) | JIT approach (Pureinn) |
|---|---|
| Feature-Set-level design, written upfront | Feature-level design, written just before build |
| Standalone design document | Register updates + sequence diagram embedded in Feature Card |
| Written for entire Feature Set before the Stripe | Written for one Feature just before build |

---

## Artifact chain

Artifacts are not independent documents. Each phase feeds the next:

```
Phase 2 (JTBD, Personas, Market Analysis, Problem Validation)
  ↓
Phase 3a (Design Thinking, Go/No-Go verdict)
  ↓
Phase 3b (Lean Canvas, KPIs, Business Case)
  ↓
PRD - consolidates Phase 2+3a+3b; Business Capabilities drive Phase 4+
  ↓
Product Roadmap v1  →  Domain Model + ERD
  ↓
entities.md (R1) + business_rules.md (R2) + decision_models.md (R3) + PII Inventory
  ↓
Product Roadmap v2  →  feature_list.md (R4) + KANO + V×C → Notion
  ↓
Stub Feature Cards (1_Backlog) + MVP Scope + Delivery Stripes → Notion
  ↓
Product Roadmap v3
  ↓
[Per Stripe, per Feature - JIT cycle]
  pm-feature-design → Feature Card Sections 1-3 + register finalization
  Design Inspection → Build → Test → Deploy → Section 4 → 6_Shipped
  ↓
Alpha → Beta → V1.0 Launch → Scale
```

For Rebuild, the chain starts from the code: `reconciliation_report.md` → registers (R1-3) → `feature_list.md` (R4) + cards → JIT cycle.

---

## Workspace structure

Every project gets a workspace scaffolded at the start:

```
pureinn-workspace/[project-slug]/
  state.json                          # project state, Notion IDs, phase progress
  pureinn-variables.md                # Notion URLs, API keys, project metadata
  domain/
    entities.md                       # Register 1 - entity states + state machines
    business_rules.md                 # Register 2 - business rules
    decision_models.md                # Register 3 - decision tables
    glossary.md
  artifacts/
    phase-1-foundation/               # project-charter.md, team-roster.md...
    phase-2-discovery/                # market-analysis.md, personas.md...
    phase-3a-validation/              # hypotheses.md, go-no-go.md...
    phase-3b-definition/              # lean-canvas.md, kpis.md, prd.md...
    phase-4-domain/                   # domain-model.md, process-flows.md...
    phase-5-planning/                 # feature-list.md, mvp-scope.md...
  features/
    feature_list.md                   # Register 4 - feature inventory
    delivery-stripes.md               # Stripe assignments
    cards/
      FEAT-[DOMAIN]-001.md            # Feature Cards
```

---

## Impact over Activity

Pureinn measures progress by decisions made and validated - not by files generated.

- Every skill run must produce a decision, a validated assumption, or a delivery-ready artifact. If it produces none, skip it.
- More artifacts is not better. A 3-section document with real decisions beats a 12-section document with placeholders.
- Every skill surfaces its own skip condition and routes elsewhere when it is low-value.
- The highest-ROI next step is not always the next skill - sometimes it is talking to customers. Each skill's handoff reflects this.

**Skippable for solo builders:** `/pm-stakeholder-map`, `/pm-team-roster`, `/pm-comms-charter`, `/pm-pitch-deck` - the orchestrator surfaces these conditions at phase gates.
