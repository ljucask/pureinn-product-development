# Pureinn - Framework Guide

A complete reference for using the Pureinn product development framework. Covers playbook selection, the three playbooks, the shared JIT delivery engine, and a concept reference.

For installation, see [README](README.md).

The guide has four parts:

1. **[Which playbook?](#which-playbook)** - pick your entry path
2. **The three playbooks** - [Greenfield](#playbook-1-greenfield), [Rebuild](#playbook-2-rebuild), [Feature Implementation](#playbook-3-feature-implementation)
3. **[The JIT delivery engine](#the-jit-delivery-engine)** - shared by all playbooks once you reach build
4. **[Reference](#reference)** - concepts, artifact chain, workspace structure

---

## Which playbook?

Two questions route you to one of three entry paths.

```
                          Does the product already exist?
                                      │
              ┌───────────────────────┴───────────────────────┐
              │ No  /  yes but no users yet                    │ Yes, with active users
              ▼                                                ▼
       ┌─────────────┐                              What do you need to do?
       │ GREENFIELD  │                                         │
       │ Playbook 1  │                    ┌────────────────────┴────────────────────┐
       └─────────────┘                    │ Onboard it into Pureinn                 │ Add new
                                          │ (existing code + legacy docs)           │ functionality
                                          ▼                                         ▼
                                   ┌─────────────┐                          ┌──────────────────────┐
                                   │  REBUILD    │   ──── once onboarded ──► │ FEATURE              │
                                   │  Playbook 2 │                          │ IMPLEMENTATION       │
                                   └─────────────┘                          │ Playbook 3           │
                                    docs conflict → A1 reconcile            └──────────────────────┘
                                    docs clean    → A2 bootstrap
```

| Situation | Playbook |
|---|---|
| New product, 0 users, validating PMF | **[Greenfield](#playbook-1-greenfield)** |
| Existing product + legacy docs (BRD/FSD) that conflict with the code, onboarding to Pureinn | **[Rebuild → A1 Reconcile](#a1--reconcile-conflicting-docs)** |
| Existing product, docs clean or absent, just bootstrap into Pureinn | **[Rebuild → A2 Bootstrap](#a2--bootstrap-clean-or-no-docs)** |
| Already onboarded, adding new functionality | **[Feature Implementation](#playbook-3-feature-implementation)** |
| Two scenarios apply at once | **Hybrid** (run the primary, then the secondary) |

Greenfield and Rebuild are **entry paths** (how you get into the framework). Feature Implementation is the **ongoing delivery mode** both of them funnel into.

Run `/pureinn [product idea or name]` - the engine runs this decision tree automatically and routes you.

---

# Playbook 1: Greenfield

**Use when:** building a new product from scratch, zero users, need to validate PMF before building.

```
Phase 1       Phase 2       Phase 3a      Phase 3b       Phase 4        Phase 5       Phase 6+7
Foundation →  Discovery  →  Validation →  Commercial  →  Domain      →  Feature    →  JIT Delivery
                            ┃GO gate┃     Definition     + Registers    Planning      (per feature)
                            ┗━hard━━┛
```

## Express path (skip discovery/validation)

**Trigger:** validated idea, you know what to build, no discovery needed.

| Step | Skill | What it does |
|---|---|---|
| 1 | `/pureinn [idea]` | Workspace setup, 3 intake questions |
| 2 | `/pm-entity-registry` [lean] | Entity list + key states only - no full ERD |
| 3 | `/pm-business-rules-library` [lean] | Core rules in Draft - finalized JIT per feature |
| 4 | `/pm-features-list` | Feature inventory + FEAT-IDs + KANO + V×C |
| 5 | `/pm-mvp-scope` | MVP scope + Delivery Stripe assignment |
| 6+ | `/pm-feature-design [FEAT-ID]` | → [JIT delivery engine](#the-jit-delivery-engine) |

**Skips:** Phase 1, 2, 3a, 3b. **Never skips:** domain registers, feature list with FEAT-IDs (required by `pm-feature-design`).

## Full flow

### Phase 1 - Foundation (~1 day)

Scales by team size. Do not over-engineer for small teams.

| Team type | Skills to run |
|---|---|
| Solo | `/pm-project-charter` only |
| Small team (2-3) | `/pm-project-charter` → `/pm-team-roster` → `/pm-comms-charter` |
| Corporate | `/pm-stakeholder-map` → `/pm-project-charter` → `/pm-team-roster` → `/pm-comms-charter` |

**Artifacts:** Project Charter, Assumptions & Risks Register, Team Roster, Communication Charter

### Phase 2 - Discovery (1-3 weeks)

Four tracks run in parallel, converge at the end.

| Track | Before you run | Skill | Output |
|---|---|---|---|
| A - Tech | Perplexity / Tech Lead research | `/pm-tech-feasibility` | Tech Feasibility Report |
| B - Domain | Perplexity / domain + regulatory research | `/pm-domain-analysis` | Domain Analysis, Legal Requirements |
| C - Market | Perplexity / competitor research - or use Path C (AI-powered, no prep) | `/pm-market-analysis` | Market Size (TAM/SAM/SOM), Competitor Analysis, SWOT |
| D - Customer | ≥10 customer interviews | `/pm-personas` | Customer Segments, Personas, Early Adopters |
| D - JTBD | After pm-personas | `/jtbd-building` | JTBD Analysis, Forces Diagram |
| Convergence | All Track A-D outputs complete | `/pm-problem-validation` | Problem Validation Summary (Phase 2 exit) |

**"Bring your data" rule:** Claude structures and formalizes - it does not hallucinate market data or interview insights. Research is done externally first, then fed in. Exception: `/pm-market-analysis` Path C runs AI-powered web research via OpenAI (requires OPENAI_API_KEY in pureinn-variables.md).

### Phase 3a - Validation

**Character: externally-paced.** Tempo is set by the market. AI accelerates experiment design and hypothesis structuring, but the signal - whether people show up, convert, pre-order, confirm the pain - comes from the real world on its own schedule.

**Can start in parallel with late Phase 2** once the Problem Validation Summary exists.

**"Done elsewhere" rule:** if Design Thinking and hypothesis validation were done outside the framework, import results into `/pureinn` (Go/No-Go verdict, evidence per hypothesis, riskiest assumptions). Phase 3a is then complete.

| Step | Skill / Activity | Output |
|---|---|---|
| 1 | `/design-thinking` | Problem Statement, POV, HMW, Ideation synthesis, Elevator Pitch, Validation Hypotheses draft |
| 2 | `/pm-hypotheses` [Plan mode] | Hypothesis Register: ICP, assumption map, experiment plan, success criteria |
| 3 | 👤 Human: run experiments | Landing page / smoke test / pre-order / concierge MVP |
| 4 | `/pm-hypotheses` [Results mode] | Go/No-Go verdict: GO / PIVOT / STOP |

**Hard gate:** only GO advances to Phase 3b. PIVOT loops to targeted re-validation. STOP ends the project.

### Phase 3b - Commercial Definition

**Character: AI-assisted synthesis sprint.** Desk work synthesizing validated inputs into commercial strategy. With AI and clean Phase 3a outputs, hours to a few sessions - not weeks.

**Condition:** starts only after a GO verdict from Phase 3a. **"Done elsewhere":** bring an existing Lean Canvas / business model via Path A.

| Skill | Output |
|---|---|
| `/pm-kotler` | Product Definition - Kotler's Five Levels |
| `/pm-lean-canvas` | Lean Canvas (one-page, problem-focused - default for startups) |
| `/pm-business-model` | Business Model Canvas (fuller, operations-focused - optional alternative to Lean Canvas for established or more complex models) |
| `/pm-kpis` | North Star Metric, AARRR Funnel Metrics, OKRs |
| `/pm-business-case` | 3-year projections, unit economics, Go/No-Go |
| `/pm-product-roadmap` | Product Roadmap v1 |
| `/pm-prd` | PRD - Phase 3b exit artifact (synthesizes Phase 2+3a+3b) |
| `/pm-pitch-deck` | Pitch Deck content brief (optional - if raising capital) |

**Exit:** PRD frozen + Business Case complete + Roadmap v1 complete. `PRD_master.md` is immutable after this point.

### Phase 4 - Domain Modeling + Register Setup (3-5 days)

| Skill | Output |
|---|---|
| `/pm-domain-model` | Domain Model, ERD (optional higher-level companion to the entity registry; + Excalidraw if MCP connected) |
| `/pm-entity-registry` | entities.md - entity list + Mermaid state machines per entity (guard conditions added JIT) |
| `/pm-business-rules-library` | business_rules.md + decision_models.md in Draft (finalized JIT per feature) |
| `/pm-privacy-requirements` | PII Inventory, Privacy Requirements, GDPR Action Plan |
| `/pm-process-flows` | System user types + E2E process map per domain (business view) + per-user user flows connected to screens (designer brief, with UI/loading/empty states). Lean - references entity states by name, no duplication. Feeds pm-feature-design UX. |
| `/pm-product-roadmap` | Product Roadmap v2 (+ domain constraints) |

**The 4 Live Registers are initialized here and enriched continuously during Phase 6-7:**
- `entities.md` (Register 1): entity states + Mermaid `stateDiagram-v2`; guards TBD until JIT
- `business_rules.md` (Register 2): `BR-[DOMAIN]-[NUMBER]`; Draft until pm-feature-design finalizes JIT
- `decision_models.md` (Register 3): `TBL-[DOMAIN]-[NUMBER]`; decision tables in Draft

### Phase 5 - Feature Planning (2-3 days)

| Skill | Output | Notion |
|---|---|---|
| `/pm-features-list` | feature_list.md (Register 4, `FEAT-[DOMAIN]-[NUMBER]`, `FS-NN` Feature Sets), KANO, V×C + stub Feature Cards | Feature entries pushed (Status = Backlog, Priority from KANO+V×C) |
| `/pm-prioritize` | Re-runnable prioritization engine - basis: roadmap / directive / lens / propose. Dependency-reconciled, non-destructive. Any time priorities shift. | - |
| `/pm-mvp-scope` | MVP Scope (IN/POST-MVP/CUT), Delivery Stripes, Feature-to-Stripe assignment | Features enriched with Phase/Stripe |
| `/pm-product-roadmap` | Product Roadmap v3 (+ feature and delivery view) | - |

### Pre-Phase 6 - Technical Foundation

| Skill | Output |
|---|---|
| `/common-ground` | Tech stack decision, repo structure, COMMON-GROUND.md |

> `/common-ground` is part of the [fullstack-dev-skills](https://github.com/jeffallan/claude-skills) plugin. Pureinn pairs naturally with it - spec from Pureinn, execution from fullstack-dev-skills.

### Phase 6 + 7

Greenfield enters the shared **[JIT delivery engine](#the-jit-delivery-engine)** here - spec, build, ship, one feature at a time.

---

# Playbook 2: Rebuild

**Use when:** a product was built outside Pureinn (or under an older version), and you are onboarding it - especially after a team change, when legacy docs (BRD, FSD, domain/entity models, business rules) no longer match the code.

Two sub-paths, by the state of the legacy docs:

```
   Legacy docs exist AND conflict with code / each other?
            │
     ┌──────┴──────┐
     │ Yes         │ No (clean or absent)
     ▼             ▼
  A1 RECONCILE   A2 BOOTSTRAP
  /pm-reconcile  /pm-entity-registry + /pm-business-rules-library + /pm-reverse-extract
     │             │
     └──────┬──────┘
            ▼
   → Feature Implementation (JIT delivery)
```

## A1 - Reconcile (conflicting docs)

The full rebuild: reconcile the codebase against the legacy docs, produce a Reconciliation Report, and rebuild the registers + feature inventory clean. Run when docs are stale, contradictory, or the team is changing and needs one trustworthy source of truth.

```
PREP                    PLAN                EXECUTE per layer (multi-session)        VERIFY + HANDOFF
/pureinn                /pm-reconcile       ┌─ /pm-reconcile domain   ─┐             /pm-audit (form)
+ source/          →   → reconciliation  → ├─ /pm-reconcile rules    ─┤  →          /pm-reconcile verify
+ /common-ground          _plan.md          └─ /pm-reconcile features ─┘             (content + incorporate)
+ Notion URLs                                  ▲ check: /pm-reconcile-status ▲       → safe to archive source
                                               ▲ reconciliation_report.md grows ▲    → /pm-stripe (JIT)
```

**Source-of-truth model (the crux):** reconciliation is asymmetric.

| Layer | Source of truth | On mismatch |
|---|---|---|
| **Technical structure** - entity/attribute/enum/state names, state-machine shape, what is implemented | **Code** | Rewrite docs to match code, mechanically. Old name → glossary alias. |
| **Business intent** - rule values, decisions, *why* | **Legacy docs (BRD)** | If code implements a *different rule* → flag `DIV-NN` + **AskUserQuestion**. The team rules: code bug vs stale doc. |

Rules that follow: **code is never changed** (only documents); docs that run ahead of code → `specified, not implemented` (backlog). Business logic is migrated fully now; feature technical design stays JIT.

**Flow:**

| Phase | Command | What happens |
|---|---|---|
| Prep | `/pureinn` + `/common-ground` + put docs in `legacy-docs/` | Workspace, tech context, source docs in one folder |
| Plan | `/pm-reconcile` | Inspects docs + code surface, defines areas + order + targets → `reconciliation_plan.md` |
| Execute 1 | `/pm-reconcile domain` | Entities, attributes, enums, **state-machine structure** → `entities.md` (R1) + glossary aliases. Offers the cross-domain ERD / `domain-model.md` (the structural map for a new team). |
| Execute 2 | `/pm-reconcile rules` | Business rules, decision models, transition **guard conditions** → `business_rules.md` + `decision_models.md` (R2-3). Heaviest AskUserQuestion pass. |
| Execute 3 | `/pm-reconcile features` | Feature inventory (FDD grammar, FS-NN, Section 1 → BR-IDs) → `feature_list.md` (R4) + stub cards |
| Anytime | `/pm-reconcile-status` | Dashboard: done / pending areas, open divergences, disposal-readiness, next command |
| Verify | `/pm-reconcile verify` | Re-reads the source one last time, proves every unit was transposed, **incorporates the gaps** it finds, rules whether the source is safe to archive → `coverage_report.md`. The source-disposal gate. |
| Exit | review `reconciliation_report.md` with the team → `/pm-audit` (form) → `/pm-reconcile verify` (content) → `/pm-stripe` | Decide open `DIV-NN`, prove coverage, retire the source, then enter JIT delivery |

**Order is dependency-driven:** entities → rules → features (registers 1 → 2 → 3 → 4). Entities are the vocabulary everything references, so they become canonical first. On a large product, run domain-by-domain.

## A2 - Bootstrap (clean or no docs)

Docs are already clean or absent - just sync current state from the code. No reconciliation needed.

| Step | Skill | Output |
|---|---|---|
| 1 | `/pureinn` | Workspace setup, state.json, pureinn-variables.md |
| 2 | `/common-ground` | Technical context: stack, APIs, domain model, debt → COMMON-GROUND.md |
| 3 | `/impeccable document` | Design context: design system, UX patterns → PRODUCT.md + DESIGN.md |
| 4 | `/pm-glossary` | Domain glossary |
| 5 | `/pm-entity-registry` | entities.md (extracted from existing codebase) |
| 6 | `/pm-business-rules-library` | business_rules.md + decision_models.md (extracted rules) |
| 7 | `/pm-reverse-extract` | feature_list.md + Feature hierarchy → Notion; delivery-stripes.md for context |

`pm-reverse-extract` extracts what it can and shows the result before proceeding - you confirm or correct. Use it **instead of** `pm-features-list` + `pm-mvp-scope`.

**Both sub-paths then enter the [JIT delivery engine](#the-jit-delivery-engine).**

---

# Playbook 3: Feature Implementation

**Use when:** the product is onboarded (via Greenfield or Rebuild) and active - the goal is adding new functionality, one feature at a time.

```
Returning session:  /pureinn [slug] → /pm-feature-design [FEAT-ID] → JIT delivery
New feature:         Viability → Track A (or Track B discovery first) → JIT delivery
```

## Express path (returning session)

**Trigger:** Pureinn already ran on this project, `state.json` + domain registers exist.

| Step | Skill | What it does |
|---|---|---|
| 1 | `/pureinn [project-slug]` | Loads `state.json`, restores context |
| 2 | `/pm-feature-design [FEAT-ID]` | JIT spec directly - no setup |
| 3+ | → [JIT delivery engine](#the-jit-delivery-engine) | |

**If the FEAT-ID doesn't exist yet:** add an entry to `feature_list.md`, create a stub card at `features/cards/FEAT-[ID].md`, then `/pm-feature-design`. Or use `/pm-stripe` for the full delivery dashboard.

## Onboarding (Phase 0) - run once

Skip if all three context files exist from a prior session.

| Skill | Output | From |
|---|---|---|
| `/pureinn` | Product context: users, roadmap, known problems | Pureinn |
| `/common-ground` | Technical context → COMMON-GROUND.md | fullstack-dev-skills |
| `/impeccable document` | Design context → PRODUCT.md + DESIGN.md | impeccable |
| `/pm-glossary` | Domain glossary | Pureinn |

> First time on a product built outside the framework? Use the **[Rebuild playbook](#playbook-2-rebuild)** to onboard it, then return here for ongoing features.

## Per feature: Viability Assessment

Answer before writing a single line of spec:

1. Which segment / persona does this feature serve?
2. KANO: Must-be / Performance / Delighter / Indifferent?
3. V×C: Quick Win / Big Bet / Fill-in / Time Waster?
4. Demand signal: analytics, support tickets, feature requests?
5. If signal weak: run a lightweight experiment (fake door, mockup, landing page)
6. MDP: minimum delightful product version? What is deferred to V1.1?
7. Success metrics: depth of usage / behavior change / business impact (set before build)

## Track decision

- **Track A:** you know what to build → go directly to spec
- **Track B:** you know the area, not the solution → discovery first, then Track A

**Track B discovery:**

| Step | Activity / Skill | Output |
|---|---|---|
| 1 | Human: 5-10 user interviews (target segment) | Qualitative insight |
| 2 | Human: competitive analysis (if direction unclear) | Differentiation signal |
| 3 | Human: tech feasibility with existing stack | Candidate solution |
| 4 | `/pm-hypotheses` [Plan mode] | Feature hypothesis, experiment plan, criteria |
| 5 | Human: run experiments | Go/No-Go signal |
| 6 | `/pm-hypotheses` [Results mode] | Verdict: build / don't build / pivot |
| → | Apply KANO + V×C → enter Track A | |

## Track A - Spec

- Feature fits an existing domain → assign to its stripe, ready for JIT design
- New domain → run `/pm-entity-registry` + `/pm-business-rules-library` (Draft) for that domain first

Then enter the **[JIT delivery engine](#the-jit-delivery-engine)**.

---

# The JIT delivery engine

Phase 6 + 7. The shared build cycle that **all three playbooks funnel into**. Spec happens per Feature (not per Feature Set). The 4 Live Registers are the living source of truth. Orchestrated by `/pm-stripe`.

```
   ┌──────────────────── /pm-stripe orchestrates the lifecycle ────────────────────┐
   │                                                                                │
Viability      Spec            Design        Build         Review         Ship
(optional)  →  (JIT)        →  Inspection →  (code+tests)→ (code insp.) → (immutable)
pm-feature-    pm-feature-      pm-stripe                                  pm-stripe
 viability      design                                                       │
   │             │                                                           │
   ▼             ▼                                                           ▼
1_Backlog → 2_Spec_Done → 3_Ready_to_Build → 4_In_Build → 5_In_Review → 6_Shipped
```

## Cycle per feature

| Step | Status | Skill | Output |
|---|---|---|---|
| 0 (optional) | - | `/pm-feature-viability [FEAT-ID]` | KANO, MDP scope, success metrics. Skip if already scoped/committed. |
| 1 | → 2_Spec_Done | `/pm-feature-design [FEAT-ID]` | Commit 1: register finalization; Commit 2: Feature Card Sections 1-3 (Biznis Mantinely, ACs, sequence diagram, UX/UI) |
| 2 | → 3_Ready_to_Build | Design Inspection (`/pm-stripe`) | Team: review Sections 1-3; Solo: confirm |
| 3 | → 4_In_Build | Build skills (`/pm-stripe`) | Code + tests, reads Feature Card Section 3 as build spec |
| 4 | → 5_In_Review | Build complete (`/pm-stripe`) | Commits, tests, flag verification → Section 4 |
| 5 | → 6_Shipped | Code Inspection passed (`/pm-stripe`) | Final review done; Feature Card immutable after this |

**Spec gate (hard rule):** Sections 1-3 complete + status `3_Ready_to_Build` before any feature enters build.
**Atomic commit protocol:** register updates (`domain/*.md`) committed before code. One feature per stripe in active design/build at a time.

## Build skills (per feature, after the spec gate)

| Skill | From | Purpose |
|---|---|---|
| `/fullstack-guardian` | fullstack-dev-skills | Full-stack implementation (reads Feature Card Section 3) |
| `/impeccable-craft` | impeccable | Frontend UI implementation |
| `/test-master` | fullstack-dev-skills | Unit + integration tests |
| `/playwright-expert` | fullstack-dev-skills | E2E tests |
| `/code-reviewer` | fullstack-dev-skills | Code review |
| `/impeccable-harden` | impeccable | UI edge cases, error states, accessibility |
| `/security-reviewer` | fullstack-dev-skills | Security audit |
| `/devops-engineer` | fullstack-dev-skills | CI/CD, deployment |
| `/monitoring-expert` | fullstack-dev-skills | Observability, alerting |

Not every skill applies to every feature. Choose what fits.

**Optional spec support** (run when needed, not per feature): `/architecture-designer` (System Design, ADRs), `/api-designer` (API contracts, OpenAPI), `/impeccable document` (PRODUCT.md + DESIGN.md), `/impeccable-shape` (UX/UI shape brief).

## Delivery rules for existing products (Rebuild + Feature Implementation)

Mandatory when building onto a product that already has users. (Greenfield has no users to protect, so these relax until launch.)

| Rule | Detail |
|---|---|
| Feature flags | All new code wrapped (OFF by default), FE + BE |
| API changes | Additive only - no renames, no deletes, no breaking changes |
| DB changes | Additive only - new tables, new columns |
| Regression | Full suite per feature before merge |
| Performance gate | Feature adds ≤10% latency to existing API calls |
| Gradual rollout | Internal → 5% → 25% → 50% → 100% |
| Kill switch | Disable flag if error rate >5% |
| Post-launch monitoring | Minimum 4 weeks |

## Cross-phase skills (any time, any playbook)

| Skill | When |
|---|---|
| `/pm-glossary` | Start early, update when new terminology surfaces |
| `/pm-diagrams` | When a visual is needed (User Flow, Architecture, JTBD Forces) |
| `/pm-audit` | Workspace health check - scans Pureinn artifacts against current conventions, fixes drift/errors, migrates older-version workspaces. Run after reconcile/extract or any time before continuing. |

---

# Reference

## Impact over Activity

Pureinn measures progress by decisions made and validated - not by files generated.

- Every skill run must produce a decision, a validated assumption, or a delivery-ready artifact. If it produces none, skip it.
- More artifacts is not better. A 3-section document with real decisions beats a 12-section document with placeholders.
- Every skill surfaces its own skip condition and offers to route elsewhere when it is low-value.
- The highest-ROI next step is not always the next skill - sometimes it is talking to customers or making a team decision. Each skill's handoff reflects this.

Solo builder: `/pm-stakeholder-map`, `/pm-team-roster`, `/pm-comms-charter`, `/pm-pitch-deck` are all skippable with rationale. The orchestrator applies this at phase gates - it routes forward only when real criteria are met, not when documents exist.

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

For Rebuild, the chain starts from the code instead: `reconciliation_report.md` → registers (R1-3) → `feature_list.md` (R4) + cards → JIT cycle.

## Feature Set vs. Delivery Stripe vs. Feature Card

Three distinct concepts. Do not conflate.

| Concept | What it is | Role |
|---|---|---|
| **Feature Set** | Logical domain grouping (`FS-NN: name`). Grouping only - not a spec unit. | Organizing principle. Features are assigned to Feature Sets. No spec per FS. |
| **Delivery Stripe** | Domain-focused parallel channel (e.g. stripe-checkout). Not a time-box. | One stripe = one isolated development channel. Features processed one at a time per stripe in dependency order. |
| **Feature Card** | Atomic delivery unit. 6-state lifecycle 1_Backlog → 6_Shipped. Sections 1-3 written JIT by pm-feature-design; Section 4 after build. | Single deliverable feature. Build spec = Section 3. Immutable after 6_Shipped. |

Example: 50 MVP features across 25 Feature Sets → assigned to 3 parallel Delivery Stripes → each designed JIT just before build.

## KANO + Value vs. Complexity (Phase 5)

| Method | What it classifies | Output |
|---|---|---|
| KANO | Feature value type | Must-be / Performance / Delighter / Indifferent → what goes into MVP |
| V×C Matrix | Impact vs. effort | Quick Wins / Big Bets / Fill-ins / Time Wasters → order features enter Stripes |

Both run in `/pm-features-list`. Both are required - KANO without V×C doesn't give you a delivery order.

## Hypothesis validation (Phase 3a)

`/pm-hypotheses` is two-mode:

- **Plan mode** (after `/design-thinking`): structures Validation Hypotheses into a formal register with ICP, assumption map, experiment plan, and success criteria defined BEFORE experiments run.
- **Results mode** (after experiments): records results against pre-defined criteria, issues Go/No-Go (Go / Pivot / Stop).

The verdict is a hard gate. Only GO advances to Phase 3b. PIVOT loops to targeted re-validation. STOP terminates. No FORCE bypass.

## Human-in-the-loop & gate types

Every phase requires human approval before advancing - intentional, not optional. The engine routes, generates, structures. The human validates and decides. Run `/pureinn` after a phase to trigger its exit gate.

| Gate type | Phases | Behavior |
|---|---|---|
| **Hard gate** | Phase 3a (Go/No-Go), Phase 6 (Design Inspection) | Cannot be bypassed. No FORCE. Missing criteria = blocked. |
| **Soft gate + FORCE** | Phase 1, 2, 4, 5 | Criteria checked, gaps named. User can proceed by acknowledging risk. |
| **Implicit gate** | Phase 3b | Condition-based entry only (requires Phase 3a GO). Binary, no checklist. |

Hard gates exist where proceeding causes compounding, uncorrectable waste. Soft gates exist where partial inputs produce partial output and the team can consciously accept the gap.

## Workspace structure

Every project gets a workspace at `/pureinn`:

```
pureinn-workspace/
  [project-slug]/
    state.json                    - phase, playbook, completed phases, register flags, Notion IDs, reconcile status
    assessment.md                 - initial product assessment (read by /pureinn-resume)
    pureinn-variables.md          - Notion URLs per project (fill in once)
    glossary.md
    reconcile/                    - Rebuild playbook (A1) only
      reconciliation_plan.md      - areas, order, targets (pm-reconcile)
      reconciliation_report.md    - drift, divergences, decisions (living, appended per area)
    product/
      PRD_master.md               - pm-prd Phase 3b output (frozen, never overwritten)
    domain/                       - 4 living registers (source of truth in Phase 6-7)
      entities.md                 - Register 1 (pm-entity-registry)
      business_rules.md           - Register 2 (pm-business-rules-library)
      decision_models.md          - Register 3 (pm-business-rules-library)
    features/
      feature_list.md             - Register 4 (pm-features-list / pm-reverse-extract)
      cards/
        FEAT-[DOMAIN]-[NUMBER].md - Feature Cards (one per feature)
    initiatives/
      [initiative-slug]/          - separate folder per major initiative (FI Track B or scoped launch)
        discovery/                - Track B discovery outputs
        prd.md                    - Initiative PRD (scoped, living)
        kano-analysis.md
        value-complexity-matrix.md
    artifacts/
      phase-1-foundation/  phase-2-discovery/  phase-3-define/  phase-4-domain/  phase-5-planning/
```

`pureinn-variables.md` is human-editable - fill in the Notion URLs once; skills read it automatically and cache IDs in `state.json` (each DB fetched at most once). The `domain/` folder is the living source of truth during Phase 6-7. Fastest setup: duplicate the Pureinn Notion template, then paste the URLs - see [NOTION_TEMPLATE.md](NOTION_TEMPLATE.md).

---

## Works best with

Pureinn covers the product and spec layer. For the full stack, pair it with:

| Plugin / Skill | What it adds | Install |
|---|---|---|
| **fullstack-dev-skills** | 66+ specialist skills for implementation: backend, frontend, infra, testing, DevOps, security | `/plugin install fullstack-dev-skills@jeffallan` |
| **impeccable** | Production-grade UI/UX: shape briefs, frontend implementation, design system, accessibility | `/plugin install impeccable` |

- **Pureinn** - discovery, validation, domain modeling, feature planning, spec, reconciliation
- **fullstack-dev-skills** - technical context, implementation, testing, deployment
- **impeccable** - design context, UX shaping, frontend craft, UI hardening

## Acknowledgements

The build-phase skills referenced in the JIT delivery engine are part of two open-source projects:

- **[fullstack-dev-skills](https://github.com/jeffallan/claude-skills)** by [@jeffallan](https://github.com/jeffallan) - 66+ specialist skills across languages, frameworks, infrastructure, and workflows. `common-ground`, `fullstack-guardian`, `test-master`, `playwright-expert`, `code-reviewer`, `security-reviewer`, `devops-engineer`, and `monitoring-expert` are from this project.
- **[impeccable](https://github.com/impeccable-dev/impeccable)** - a production-grade frontend design skill. `impeccable document`, `impeccable-shape`, `impeccable-craft`, and `impeccable-harden` are from this project.

Pureinn focuses on what comes before the build: methodology, thinking, decisions, specifications. These two projects pick up where Pureinn ends. Credit where it is due.
