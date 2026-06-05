# Pureinn - Framework Guide

A complete reference for using the Pureinn product development framework. Covers playbook selection, phase structure, skill sequences, and the artifact chain.

For installation, see [README](README.md).

---

## Which playbook?

Three questions determine the right path.

**1. Does the product exist?**
- No - Greenfield
- Yes, no active users yet - Greenfield
- Yes, with active users - continue

**2. What is the primary goal?**
- Add new functionality - Feature Implementation
- Technical transformation (replatforming, migration) - Rebuild *(coming soon)*
- Both - Hybrid (identify primary + secondary)

| Situation | Playbook |
|---|---|
| New product, 0 users, validating PMF | **Greenfield** |
| Product exists, active users, adding functionality | **Feature Implementation** |
| Product exists, active users, technical transformation | **Rebuild** *(coming soon)* |
| Product built outside the framework, starting to use Pureinn | **Feature Implementation - Migration Path** |
| Two scenarios apply simultaneously | **Hybrid** (primary + secondary playbook) |

Run `/pureinn [product idea or name]` - the engine runs the decision tree automatically.

---

## Fast Track

Three paths that skip upstream phases and go straight to spec + build. The engine detects the right path after intake and surfaces it proactively. You can also declare it explicitly.

**When fast track applies:**
- You already have validated knowledge (no need for discovery/validation)
- You know exactly what to build
- You want to move from idea → spec → build with minimal ceremony

**What fast track never skips:**
- Domain registers (`entities.md`, `business_rules.md`) - required by `pm-feature-design`
- Feature list with FEAT-IDs - required for JIT cycle
- FI delivery rules (feature flags, regression, gradual rollout) - always apply

---

### Fast Track 1 - Greenfield Express

**Trigger:** New product, validated idea, no discovery needed.

| Step | Skill | What it does |
|---|---|---|
| 1 | `/pureinn [idea]` | Workspace setup, 3 intake questions |
| 2 | `/pm-entity-registry` [lean] | Entity list + key states only - no full ERD |
| 3 | `/pm-business-rules-library` [lean] | Core rules in Draft mode - finalized JIT per feature |
| 4 | `/pm-features-list` | Feature inventory + FEAT-IDs + KANO + V×C |
| 5 | `/pm-mvp-scope` | MVP scope + Delivery Stripe assignment |
| 6+ | `/pm-feature-design [FEAT-ID]` | JIT spec per feature → Build → Test → Release |

**Skips:** Phase 1 (Foundation), Phase 2 (Discovery), Phase 3a (Validation), Phase 3b (Commercial Definition).

**Lean mode:** `pm-entity-registry` and `pm-business-rules-library` run in condensed mode - bare minimum to enable JIT spec. Registers are enriched continuously as features are designed.

---

### Fast Track 2 - Feature Implementation: First Run

**Trigger:** Existing product, first time running Pureinn on this codebase.

| Step | Skill | What it does |
|---|---|---|
| 1 | `/pureinn [project]` | Workspace setup |
| 2 | `/common-ground` | Tech context from existing code → `COMMON-GROUND.md` |
| 3 | `/pm-reverse-extract` | Reads existing code/docs → extracts entities, business rules, feature inventory → bootstraps all domain registers → pushes to Notion → shows result for confirmation |
| 4 | `/pm-feature-design [FEAT-ID]` | JIT spec for the target feature |
| 5+ | Build → Test → Release | FI delivery rules always apply |

**`pm-reverse-extract` bootstrap:** Extracts what it can from existing code. Shows result before proceeding - you confirm or correct. If code is poorly structured, you fill the gaps manually.

**FI delivery rules (non-negotiable):**

| Rule | Detail |
|---|---|
| Feature flags | All new code wrapped (OFF by default), FE + BE |
| API changes | Additive only - no renames, no deletes |
| DB changes | Additive only - new tables, new columns |
| Regression | Full suite per feature before merge |
| Performance gate | Feature adds ≤10% latency to existing API calls |
| Gradual rollout | Internal → 5% → 25% → 50% → 100% |
| Kill switch | Disable flag if error rate >5% |

---

### Fast Track 3 - Feature Implementation: Returning Session

**Trigger:** Pureinn already ran on this project, `state.json` + domain registers exist.

| Step | Skill | What it does |
|---|---|---|
| 1 | `/pureinn [project-slug]` | Loads `state.json`, restores context |
| 2 | `/pm-feature-design [FEAT-ID]` | JIT spec directly - no setup needed |
| 3+ | Build → Test → Release | FI delivery rules always apply |

**If FEAT-ID doesn't exist yet** (new feature not in `feature_list.md`):
1. Add entry to `features/feature_list.md` (format: `FEAT-[DOMAIN]-[NUMBER]`)
2. Create stub Feature Card at `features/cards/FEAT-[ID].md`
3. Run `/pm-feature-design [FEAT-ID]`

Or use `/pm-stripe` for a full delivery dashboard showing all active stripes and their current state.

---

## Greenfield

Use when: building a new product from scratch, zero users, need to validate PMF before building.

The full lifecycle: Foundation → Discovery → Validation → Domain Modeling → Feature Planning → FDD Delivery.

### Phase 1 - Foundation (~1 day)

Scales by team size. Do not over-engineer for small teams.

| Team type | Skills to run |
|---|---|
| Solo | `/pm-project-charter` only |
| Small team (2-3) | `/pm-project-charter` → `/pm-team-roster` → `/pm-comms-charter` |
| Corporate | `/pm-stakeholder-map` → `/pm-project-charter` → `/pm-team-roster` → `/pm-comms-charter` |

**Artifacts:** Project Charter, Assumptions & Risks Register, Team Roster, Communication Charter

---

### Phase 2 - Discovery (1-3 weeks)

Four tracks run in parallel. Converge at the end.

| Track | Before you run | Skill | Output |
|---|---|---|---|
| A - Tech | Perplexity / Tech Lead research | `/pm-tech-feasibility` | Tech Feasibility Report |
| B - Domain | Perplexity / domain + regulatory research | `/pm-domain-analysis` | Domain Analysis, Legal Requirements |
| C - Market | Perplexity / competitor research - or use Path C (AI-powered, no prep needed) | `/pm-market-analysis` | Market Size (TAM/SAM/SOM), Competitor Analysis, SWOT |
| D - Customer | ≥10 customer interviews | `/pm-personas` | Customer Segments, Personas, Early Adopters |
| D - JTBD | After pm-personas | `/jtbd-building` | JTBD Analysis, Forces Diagram |
| Convergence | All Track A-D outputs complete | `/pm-problem-validation` | Problem Validation Summary (Phase 2 exit) |

**"Bring your data" rule:** Claude structures and formalizes - it does not hallucinate market data or interview insights. Research must be done externally first (Perplexity, interviews, surveys), then fed into the skill. Exception: `/pm-market-analysis` Path C runs AI-powered web research automatically via OpenAI (requires OPENAI_API_KEY in pureinn-variables.md).

---

### Phase 3a - Validation

**Character: externally-paced.** Tempo is set by the market, not by you. AI accelerates experiment design and hypothesis structuring, but the signal itself - whether people show up, convert, pre-order, or confirm the pain - comes from the real world on its own schedule.

**Can start in parallel with late Phase 2** once Problem Validation Summary exists. You do not need all Phase 2 tracks complete before beginning design-thinking or structuring hypotheses.

**"Done elsewhere" rule:** If Design Thinking and hypothesis validation were done outside this framework (workshop, Miro, other tool), you can import results directly into /pureinn. The orchestrator will ask for: Go/No-Go verdict, key evidence per hypothesis type, and riskiest assumptions tested. Phase 3a is then marked complete and 3b can start.

| Step | Skill / Activity | Output |
|---|---|---|
| 1 | `/design-thinking` | Problem Statement, POV, HMW, Ideation synthesis, Elevator Pitch, Validation Hypotheses draft |
| 2 | `/pm-hypotheses` [Plan mode] | Hypothesis Register: ICP, assumption map, experiment plan, success criteria |
| 3 | 👤 Human: run experiments | Landing page / smoke test / pre-order / concierge MVP - based on experiment plan |
| 4 | `/pm-hypotheses` [Results mode] | Go/No-Go verdict: GO / PIVOT / STOP |

**Hard gate:** only GO advances to Phase 3b. PIVOT loops back to targeted re-validation. STOP ends the project.

---

### Phase 3b - Commercial Definition

**Character: AI-assisted synthesis sprint.** This is desk work synthesizing validated inputs into commercial strategy. With AI and clean Phase 3a outputs, this is hours to a few focused sessions - not weeks. The bottleneck is not cognitive capacity here; it is the quality of what came out of Phase 3a.

**Condition:** Phase 3b only starts after a GO verdict from Phase 3a. No exceptions.

**"Done elsewhere" rule:** If you already have an existing Lean Canvas, business model, or financial model from another tool or previous iteration, bring it. Skills will accept existing artifacts via Path A (import) rather than generating from scratch.

| Skill | Output |
|---|---|
| `/pm-kotler` | Product Definition - Kotler's Five Levels (Core / Basic / Expected / Augmented / Potential) |
| `/pm-lean-canvas` | Lean Canvas (one-page business model) |
| `/pm-kpis` | North Star Metric, AARRR Funnel Metrics, OKRs |
| `/pm-business-case` | 3-year projections, unit economics, Go/No-Go |
| `/pm-product-roadmap` | Product Roadmap v1 |
| `/pm-prd` | PRD - Phase 3b exit artifact (synthesizes all Phase 2+3a+3b) |
| `/pm-pitch-deck` | Pitch Deck content brief (optional - if raising capital or pitching) |

**Phase 3b exit:** PRD frozen + Business Case complete + Roadmap v1 complete. PRD_master.md is immutable after this point.

---

### Phase 4 - Domain Modeling + Register Setup (3-5 days)

| Skill | Output |
|---|---|
| `/pm-domain-model` | Domain Model, ERD (+ Excalidraw diagram if MCP connected) |
| `/pm-entity-registry` | entities.md - entity list + Mermaid state machines per entity (guard conditions added JIT) |
| `/pm-business-rules-library` | business_rules.md + decision_models.md in Draft mode (finalized JIT per feature) |
| `/pm-privacy-requirements` | PII Inventory, Privacy Requirements, GDPR Action Plan |
| `/pm-product-roadmap` | Product Roadmap v2 (+ domain constraints) |

**Living registers initialized here, enriched continuously during Phase 6-7.**
- entities.md (Live Register 1): entity states + Mermaid stateDiagram-v2; guard conditions left TBD until JIT design
- business_rules.md (Live Register 2): BR-[DOMAIN]-[NUMBER] format; Draft status until pm-feature-design finalizes JIT
- decision_models.md (Live Register 3): TBL-[DOMAIN]-[NUMBER] format; decision tables in Draft mode

---

### Phase 5 - Feature Planning (2-3 days)

| Skill | Output | Notion |
|---|---|---|
| `/pm-features-list` | feature_list.md (FDD Feature List, FEAT-[DOMAIN]-[NUMBER] IDs), KANO Analysis, V×C Matrix + stub Feature Cards in features/cards/ | Feature entries pushed (Status = Backlog, Priority from KANO+V×C) |
| `/pm-mvp-scope` | MVP Scope (IN/POST-MVP/CUT), Delivery Stripes (domain-focused channels), Feature-to-Stripe assignment | Features enriched with Phase/Stripe |
| `/pm-product-roadmap` | Product Roadmap v3 (+ feature and delivery view) | - |

---

### Pre-Phase 6 - Technical Foundation

| Skill | Output |
|---|---|
| `/common-ground` | Tech stack decision, repo structure, COMMON-GROUND.md |

> `/common-ground` is part of the [fullstack-dev-skills](https://github.com/jeffallan/claude-skills) plugin. Pureinn pairs naturally with it - spec and product definition from Pureinn, technical execution from fullstack-dev-skills. Install both for the full stack.

---

### Phase 6 + 7 - FDD Delivery (JIT per Feature, Stripe-based)

Phase 6 and 7 are integrated into a JIT cycle - spec happens per Feature, not per Feature Set. Domain registers (entities.md, business_rules.md, decision_models.md) are the living source of truth.

**JIT cycle per feature (orchestrated by `/pm-stripe`):**

| Step | Status | Skill | Output |
|---|---|---|---|
| 0 (optional) | - | `/pm-feature-viability [FEAT-ID]` | KANO, MDP scope, success metrics. Skip if feature already scoped/committed. |
| 1 | → 2_Spec_Done | `/pm-feature-design [FEAT-ID]` | Commit 1: register finalization; Commit 2: Feature Card Sections 1-3 (Biznis Mantinely, ACs, sequence diagram, UX/UI context) |
| 2 | → 3_Ready_to_Build | Design Inspection (`/pm-stripe`) | Team: review Sections 1-3; Solo: confirm |
| 3 | → 4_In_Build | Build skills (`/pm-stripe`) | Code + tests, reads Feature Card Section 3 as build spec |
| 4 | → 5_In_Review | Build complete (`/pm-stripe`) | Commits, tests, flag verification recorded in Section 4 |
| 5 | → 6_Shipped | Code Inspection passed (`/pm-stripe`) | Final review done; Feature Card immutable after this |

**Spec gate (hard rule):** Feature Card Sections 1-3 complete + status 3_Ready_to_Build before any feature enters build.

**Atomic commit protocol:** Register updates (domain/*.md) committed before code. One feature per stripe in active design/build at any time.

**Build (per feature, after spec gate):**

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

**Optional spec support (not per feature - run when needed):**

| Skill | Purpose |
|---|---|
| `/architecture-designer` | System Design Blueprint, ADRs |
| `/api-designer` | API contracts, OpenAPI spec |
| `/impeccable document` [once] | PRODUCT.md + DESIGN.md |
| `/impeccable-shape` [per feature] | UX/UI shape brief |

---

### Cross-phase skills (run at any time)

| Skill | When |
|---|---|
| `/pm-glossary` | Start in Phase 1, update after each phase or when new terminology surfaces |
| `/pm-diagrams` | When a visual diagram is needed (User Flow, Architecture, JTBD Forces) |

---

## Feature Implementation

Use when: product exists, active users, goal is adding new functionality.

### Option A - Migration path (product built outside the framework)

Run once to sync current state into Notion and generate Claude context:

| Skill | Output | From |
|---|---|---|
| `/pureinn` | Workspace setup, state.json, pureinn-variables.md | Pureinn |
| `/common-ground` | Technical context: stack, APIs, domain model, debt → COMMON-GROUND.md | fullstack-dev-skills |
| `/impeccable document` | Design context: design system, UX patterns → PRODUCT.md + DESIGN.md | impeccable |
| `/pm-glossary` | Domain glossary | Pureinn |
| `/pm-entity-registry` | entities.md (extracted from existing codebase/docs) | Pureinn |
| `/pm-business-rules-library` | business_rules.md + decision_models.md (extracted existing rules) | Pureinn |
| `/pm-reverse-extract` | feature_list.md + Feature hierarchy pushed to Notion; delivery-stripes.md for Claude context | Pureinn |

Then proceed directly to Phase 6 + 7 (JIT per feature).

---

### Option B - Standard onboarding (Phase 0)

Run once per project - not per feature:

| Skill | Output | From |
|---|---|---|
| `/pureinn` | Product context: users, roadmap, known problems, workarounds | Pureinn |
| `/common-ground` | Technical context: stack, domain model, APIs, debt → COMMON-GROUND.md | fullstack-dev-skills |
| `/impeccable document` | Design context: design system, UX patterns, components → PRODUCT.md + DESIGN.md | impeccable |
| `/pm-glossary` | Domain glossary | Pureinn |

Skip if all three context files exist from a prior session.

---

### Per feature: Viability Assessment (before any spec work)

Answer before writing a single line of spec:

1. Which segment / persona does this feature serve?
2. KANO: Must-be / Performance / Delighter / Indifferent?
3. V×C: Quick Win / Big Bet / Fill-in / Time Waster?
4. Demand signal: analytics, support tickets, feature requests?
5. If signal weak: run lightweight experiment (fake door, mockup, landing page)
6. MDP: what is the minimum delightful product version? What is deferred to V1.1?
7. Success metrics: depth of usage / behavior change / business impact (set before build)

---

### Track decision

- **Track A:** you know what to build → go directly to spec
- **Track B:** you know the area, not the solution → run discovery first, then enter Track A

**Track B discovery:**

| Step | Activity / Skill | Output |
|---|---|---|
| 1 | Human: 5-10 user interviews (target segment only) | Qualitative insight |
| 2 | Human: competitive analysis (if solution direction unclear) | Differentiation signal |
| 3 | Human: tech feasibility with existing stack | Candidate solution |
| 4 | `/pm-hypotheses` [Plan mode] | Feature hypothesis, experiment plan, success criteria |
| 5 | Human: run experiments | Go/No-Go signal |
| 6 | `/pm-hypotheses` [Results mode] | Verdict: build / don't build / pivot |
| → | Apply KANO + V×C → enter Track A | |

---

### Track A - Spec

Feature Set assignment (grouping only - no longer a spec unit):
- Feature fits existing domain → assign to existing stripe, feature is ready for JIT design
- New domain → run `/pm-entity-registry` + `/pm-business-rules-library` (Draft mode) for that domain first

JIT design per feature (one at a time, per stripe):

| Skill | Output |
|---|---|
| `/pm-feature-design [FEAT-ID]` | Feature Card Sections 1-3 + register finalization (pre-step: scans existing codebase before generating sequence diagram) |
| Design Inspection | Team review or solo confirm → status: 3_Ready_to_Build |
| Build skills | Read Feature Card Section 3 as build spec |

---

### Delivery additions (mandatory for Feature Implementation)

| Rule | Detail |
|---|---|
| Feature flags | All new code wrapped in flag (OFF by default), both FE and BE |
| API changes | Additive only - no renames, no deletes, no breaking changes |
| DB changes | Additive only - new tables, new columns only |
| Regression | Full regression suite per feature before merge |
| Performance gate | Feature adds ≤10% latency to existing API calls |
| Gradual rollout | Internal → 5% → 25% → 50% → 100% |
| Kill switch | Disable flag if error rate >5% |
| Post-launch monitoring | Minimum 4 weeks |

---

## Key concepts

### Impact over Activity

Pureinn does not measure progress by files generated. It measures progress by decisions made and validated.

**What this means:**

- Every skill run must produce a decision, a validated assumption, or a delivery-ready artifact. If it produces none of these, it should be skipped.
- More artifacts is not better. A 3-section document with real decisions beats a 12-section document with placeholders.
- Every skill surfaces its own skip condition. If the context makes a skill low-value, the skill says so before generating anything and offers to route elsewhere.
- The highest-ROI next step is not always the next skill in sequence. Sometimes it is talking to customers, running an experiment, or making a team decision. The handoff at the end of each skill reflects this.

**Practical application:**
- Solo builder: `/pm-stakeholder-map`, `/pm-team-roster`, `/pm-comms-charter`, `/pm-pitch-deck` are all skippable with explicit rationale
- No research available: skills offer assumption-based paths, never block
- Validated insight exists: skip the corresponding discovery skill, carry the insight forward

The orchestrator (`/pureinn`) applies this principle at phase gates - it only routes forward when real criteria are met, not when documents exist.

---

### Artifact chain

Artifacts are not independent documents. Each phase feeds the next:

```
Phase 2 outputs (JTBD, Personas, Market Analysis, Problem Validation)
  ↓
Phase 3a outputs (Design Thinking, Go/No-Go verdict)
  ↓
Phase 3b outputs (Lean Canvas, KPIs, Business Case)
  ↓
PRD - consolidation of Phase 2+3a+3b, Business Capabilities section drives Phase 4+
  ↓
Product Roadmap v1 (vision + segments + business model)
  ↓
Domain Model + ERD
entities.md (Live Register 1) + business_rules.md (Live Register 2) + decision_models.md (Live Register 3)
PII Inventory, Privacy Requirements
  ↓
Product Roadmap v2 (+ domain context)
  ↓
feature_list.md (Live Register 4) + KANO + V×C → Notion: Feature entries
Stub Feature Cards (status: 1_Backlog) + MVP Scope + Delivery Stripes → Notion: enriched
  ↓
Product Roadmap v3 (+ Feature and Delivery view)
  ↓
[Per Stripe, per Feature - JIT cycle]
  pm-feature-design → Feature Card Sections 1-3 + register finalization
  Design Inspection → Build → Test → Deploy → Feature Card Section 4 → Promoted
  ↓
Alpha → Beta → V1.0 Launch → Scale
```

---

### Feature Set vs. Delivery Stripe vs. Feature Card

Three distinct concepts. Do not conflate.

| Concept | What it is | Role |
|---|---|---|
| **Feature Set** | Logical domain grouping (e.g., "User Auth", "Booking Flow"). Grouping only - not a spec unit. | Organizing principle. Features are assigned to Feature Sets. No BRD or FSD per FS. |
| **Delivery Stripe** | Domain-focused parallel channel (e.g., stripe-checkout, stripe-auth). Not a time-box. | One stripe = one isolated development channel. Features are processed one at a time per stripe in dependency order. |
| **Feature Card** | Atomic delivery unit. 6-state lifecycle: 1_Backlog → 2_Spec_Done → 3_Ready_to_Build → 4_In_Build → 5_In_Review → 6_Shipped. Sections 1-3 written JIT by pm-feature-design; Section 4 filled after build. | Single deliverable feature. Build spec = Feature Card Section 3. Immutable after 6_Shipped. |

Example: 50 MVP features across 25 Feature Sets → assigned to 3 parallel Delivery Stripes → each feature designed JIT just before build.

---

### KANO + Value vs. Complexity (used together in Phase 5)

| Method | What it classifies | Output |
|---|---|---|
| KANO | Feature value type | Must-be / Performance / Delighter / Indifferent → determines what goes into MVP |
| V×C Matrix | Impact vs. effort | Quick Wins / Big Bets / Fill-ins / Time Wasters → determines in what order features enter Stripes |

Both methods run in `/pm-features-list`. Both are required - KANO without V×C doesn't give you a delivery order.

---

### Hypothesis validation (Phase 3a)

`/pm-hypotheses` is a two-mode skill:

- **Plan mode** - run after `/design-thinking`: structures Validation Hypotheses into a formal register with ICP definition, assumption map, experiment plan, and success criteria defined BEFORE experiments run
- **Results mode** - run after experiments complete: records results against pre-defined criteria, issues Go/No-Go verdict (Go / Pivot / Stop)

The Go/No-Go verdict is a hard gate. Only GO advances to Phase 3b (`/pm-kotler` and beyond). PIVOT loops back to targeted re-validation. STOP terminates the project. No FORCE bypass on this gate.

---

### Workspace structure

Every project gets a workspace folder created at `/pureinn`:

```
pureinn-workspace/
  [project-slug]/
    state.json                    - Phase, playbook, completed phases, register init flags, Notion IDs
    assessment.md                 - Initial product assessment (read by /pureinn-resume)
    pureinn-variables.md          - Notion URLs per project (fill in once)
    glossary.md
    product/
      PRD_master.md               - pm-prd Phase 3b output (frozen after creation, never overwritten)
    domain/                       - 4 living registers (source of truth for AI in Phase 6-7)
      entities.md                 - pm-entity-registry (Live Register 1, append per initiative)
      business_rules.md           - pm-business-rules-library (Live Register 2, append per initiative)
      decision_models.md          - pm-business-rules-library (Live Register 3, append per initiative)
    features/
      feature_list.md             - pm-features-list (Live Register 4, append per initiative)
      cards/
        FEAT-[DOMAIN]-[NUMBER].md - Feature Cards (one per feature)
    initiatives/
      [initiative-slug]/          - Separate folder per new major initiative (FI Track B or scoped launch)
        discovery/                - Track B discovery outputs (interviews, research)
        prd.md                    - Initiative PRD (scoped, living - separate from PRD_master)
        kano-analysis.md          - KANO scoped to this initiative
        value-complexity-matrix.md
    artifacts/
      phase-1-foundation/
      phase-2-discovery/
      phase-3-define/
      phase-4-domain/
      phase-5-planning/
```

`pureinn-variables.md` is human-editable. Fill in the Notion URLs once - skills read the file automatically and cache IDs in `state.json` so each Notion DB is fetched at most once per project.

The `domain/` folder is the living source of truth during Phase 6-7. Every pm-feature-design run updates these files before writing Feature Card Sections 1-3.

The fastest way to fill it in: duplicate the Pureinn Notion template to your workspace, then paste the URLs. See [NOTION_TEMPLATE.md](NOTION_TEMPLATE.md) for the template link and setup guide.

---

### Human-in-the-loop

Every phase requires human approval before advancing. This is intentional - not optional. The engine routes, generates, and structures. The human validates and decides.

Run `/pureinn` after completing a phase to trigger the exit gate. Exit gates have quantitative thresholds (e.g., "≥10 customer interviews complete", "Go/No-Go hypothesis verdict recorded"). Only when criteria are met does the engine advance.

**Gate types - there are three, and they behave differently:**

| Gate type | Phases | Behavior |
|---|---|---|
| **Hard gate** | Phase 3a (Go/No-Go), Phase 6 (Design Inspection) | Cannot be bypassed. No FORCE. Missing criteria = blocked until resolved. |
| **Soft gate + FORCE** | Phase 1, Phase 2, Phase 4, Phase 5 | Criteria checked, gaps named. User can proceed by acknowledging risk (FORCE). Output quality depends on what was skipped. |
| **Implicit gate** | Phase 3b | Condition-based entry only (requires Phase 3a GO verdict). No checklist - the condition is binary. |

Hard gates exist where proceeding without meeting them causes compounding waste downstream - not just lower quality output, but invalid decisions that cannot be corrected without going back. Soft gates exist where partial inputs produce partial output and the team can consciously decide whether the gap is acceptable. The difference is intentional, not an oversight.

---

## Works best with

Pureinn covers the product and spec layer. For the full development stack, pair it with:

| Plugin / Skill | What it adds | Install |
|---|---|---|
| **fullstack-dev-skills** | 66+ specialist skills for implementation: backend, frontend, infrastructure, testing, DevOps, security | `/plugin install fullstack-dev-skills@jeffallan` |
| **impeccable** | Production-grade UI/UX: shape briefs, frontend implementation, design system, accessibility, polish | `/plugin install impeccable` |

The combination covers the complete product development lifecycle:
- **Pureinn** - discovery, validation, domain modeling, feature planning, spec
- **fullstack-dev-skills** - technical context setup, implementation, testing, deployment
- **impeccable** - design context, UX shaping, frontend craft, UI hardening

---

## Acknowledgements

The build-phase skills referenced in Phase 6-7 are part of two excellent open-source projects:

- **[fullstack-dev-skills](https://github.com/jeffallan/claude-skills)** by [@jeffallan](https://github.com/jeffallan) - a comprehensive skill pack for full-stack development covering 66+ specialist skills across languages, frameworks, infrastructure, and workflows. The `common-ground`, `fullstack-guardian`, `test-master`, `playwright-expert`, `code-reviewer`, `security-reviewer`, `devops-engineer`, and `monitoring-expert` skills referenced in this guide are all from this project.

- **[impeccable](https://github.com/impeccable-dev/impeccable)** - a production-grade frontend design skill for Claude Code. The `impeccable document`, `impeccable-shape`, `impeccable-craft`, and `impeccable-harden` skills referenced in this guide are from this project.

Pureinn focuses on what comes before the build: the methodology, the thinking, the decisions, and the specifications. These two projects pick up where Pureinn ends and take the product into production. Credit where it is due.
