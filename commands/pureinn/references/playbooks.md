# Pureinn - Playbooks reference

> Reference for `commands/pureinn/COMMAND.md`. Playbook selection, starting phase, and the phase skill catalogue.

## STEP 4 - Playbook Selection

If not already determined from document analysis, use the AskUserQuestion tool:

- Question: "Does the product already exist in any form?"
  - A: "No - building from scratch"
  - B: "Yes, but no active users yet"
  - C: "Yes, with active users - adding features" (Recommended if product exists)
  - D: "Yes, with active users - rebuilding or migrating from old docs" — description: "Existing code + legacy docs (BRD/FSD/domain models) that need reconciling into a clean Pureinn structure"

Map to playbook:
- A or B → **Greenfield**
- C → **Feature**
- D → **Rebuild**

**Cross-check against repo context** (`state.json` → `repo`, set in STEP 0f). Feature and Rebuild both read real code; a mismatch here produces a playbook that cannot execute its first step:

| Answer | `repo.present` | What to do |
|---|---|---|
| C or D | `local` | Proceed - the playbook has what it needs |
| C or D | `remote` | Offer to clone first; the entry skill (`/pm-reverse-extract`, `/pm-reconcile`) cannot read a URL |
| C or D | `none_yet` / `none` | Stop and reconcile the contradiction before routing: the product exists but no code is reachable. Either the code is somewhere not yet named (update `repo`), or "exists" means a live product they cannot access - in which case say plainly that Feature/Rebuild degrade to what can be inferred from documents and the live product, not from code |
| A or B | `local` | Worth one question - existing code with a from-scratch answer usually means a prototype or a predecessor system that is worth reading before deciding |

Never route into a code-reading playbook while claiming code access the project does not have.

**Feature playbook note:**
Feature Implementation does not start at Phase 1. It starts at Phase 0 (context setup).
Phase 0 runs once per project onboarding - not per feature. After Phase 0, each feature goes through Feature Viability Assessment before any spec work begins.
If Phase 0 is already done (context exists from a prior session), skip to Feature Viability Assessment.

**Rebuild playbook note:**
Rebuild is for an existing product onboarded to Pureinn where legacy docs and the codebase disagree. Route by what the user has:
```
- Existing code + legacy docs (BRD/FSD/domain models) that may conflict with the code:
  → /pm-reconcile  (first plans which areas to reconcile and in what order, then reconciles
                    per layer: /pm-reconcile domain → rules → features. Produces a living
                    Reconciliation Report and rebuilds the registers + feature inventory clean.
                    Track multi-session progress with /pm-reconcile-status. Old docs become reference only.)
- Existing code, docs already clean or absent (just need to bootstrap from code):
  → naive migration path: /pm-entity-registry + /pm-business-rules-library + /pm-reverse-extract
- Greenfield rewrite (throwing the code away): → Greenfield playbook
```
Confirm which case fits, then route. For the first case, `/pm-reconcile` is the entry point.

---

## STEP 5 - Starting Phase Determination

Based on the document analysis and confirmed assessment, determine the starting phase:

- Phase covered with high confidence → mark as done, skip
- Phase covered but partial or low confidence → flag gaps, user decides: fill gaps first or proceed with acknowledged risk
- Phase not covered → must be done

Starting phase = lowest incomplete phase.

If guidance mode is ON, before announcing the starting phase add:

```
[Phase N] - [Phase Name] is where we start because [1-2 sentences explaining
what this phase accomplishes and why it's the right entry point given what you have].
```

Then read `references/workspace.md` and run **STEP 6 (Workspace Setup)**.

---

## Phase → Skills Reference

### Phase 1 - Foundation & Collaboration Setup
```
Skills shown depend on team structure (set during intake):

Solo builder:
  /pm-project-charter    → Project Charter (simplified: assumptions, risks, success definition)

Small founding team:
  /pm-project-charter    → Project Charter, Assumptions & Risks Register
  /pm-team-roster        → Decision Rights, Skill Gap Assessment (RACI skipped)
  /pm-comms-charter      → Communication Charter, Meeting Rhythm

Team with defined roles / Corporate:
  /pm-stakeholder-map    → Stakeholder Map, RACI, Escalation Tree
  /pm-project-charter    → Project Charter, Assumptions & Risks Register
  /pm-team-roster        → Team Roster, Decision Rights, Skill Gap Assessment
  /pm-comms-charter      → Communication Charter, Meeting Rhythm
```

### Phase 2 - Ideation & Discovery
```
/pm-tech-feasibility   → Tech Feasibility Report
                         [🔍 Before: research with Perplexity / Tech Lead input]
/pm-domain-analysis    → Domain Analysis, Legal Requirements
                         [🔍 Before: Perplexity research on domain + regulations]
/pm-market-analysis    → Market Size, Competitor Analysis, SWOT, Market Timing
                         [🔍 Before: Perplexity market data + competitor research]
/pm-personas           → Customer Segments, Personas, Early Adopters Profile
                         [👤 Before: ≥10 customer interviews / SynthFolk / ChatGPT]
/jtbd-building         → JTBD Analysis
                         [Run after /pm-personas - uses personas as input]
/pm-problem-validation → Problem Validation Summary (Phase 2 exit artifact)
                         [Synthesizes all Track A-D outputs - run last in Phase 2]

Client discovery layer (commissioned builds - someone else defines what gets built):
/pm-discovery-interview → Session agenda before each live client/user session
                          [Reads meetings/ + artifacts, targets biggest gaps; the full
                           question bank is embedded inline in the skill - self-contained]
/pm-meeting             → Client Discovery type - structured capture after each session
                          [References classified directive/hypothesis, constraints,
                           [CANDIDATE-BR] exceptions, [CLIENT-ASSERTED] user claims]
/pm-discovery-report    → Client-facing "what we heard, what we recommend"
                          [Incremental across sessions; narrative companion to the
                           internal Problem Validation Summary. If mandate is given,
                           feeds /pm-scope-brief directly - Phase 3a skipped]
```

### Phase 3a - Validation
```
Character: externally-paced. AI accelerates structuring, not signal collection.
Can start: once Problem Validation Summary exists (parallel with late Phase 2 is fine).

"Done elsewhere" path: if Design Thinking + hypothesis validation were done outside
this framework (Miro, workshop, other tool), run /pureinn and say "Phase 3a done elsewhere."
The orchestrator will collect: Go/No-Go verdict, key evidence per hypothesis type,
riskiest assumptions tested. Phase 3a is then marked complete and 3b can start.

/design-thinking       → Problem Statement, POV, HMW, Ideation synthesis, Elevator Pitch
                         [Outputs Validation Hypotheses draft → feeds into /pm-hypotheses]
/pm-hypotheses         → Hypothesis Register: ICP, assumption map, experiment plan, success criteria
  [Plan mode]            [Run immediately after /design-thinking]
                         [Assigns experiment type per hypothesis - Problem / Customer / Solution / Market]
                         [Success criteria defined BEFORE experiments run]
[👤 Experiments run]   → Landing page / Smoke test / Pre-order / Rapid Prototype / Concierge MVP
                         [Human activity - execute the experiment plan from /pm-hypotheses]
/pm-hypotheses         → Go/No-Go Decision (Go / Pivot / Stop)
  [Results mode]         [Run after all assigned experiments complete]
                         [HARD GATE: GO required to enter Phase 3b. PIVOT loops back. STOP ends project.]
```

### Phase 3b - Commercial Definition
```
Character: AI-assisted synthesis sprint. With clean Phase 3a inputs, this is
Quality depends entirely on Phase 3a rigor.
Condition: only starts after GO verdict from Phase 3a. No FORCE bypass for this gate.
(Exception: commissioned builds skip 3a - mandate given - and run /pm-scope-brief here.)

"Done elsewhere" path: if you already have a Lean Canvas, financial model, or
existing commercial strategy artifacts, bring them via Path A in each skill.
State "Phase 3b partially done elsewhere" and list which artifacts exist.

/pm-kotler             → Product Definition (5 levels: Core / Basic / Expected / Augmented / Potential)
/pm-lean-canvas        → Lean Canvas (one-page, problem-focused - default for startups)
/pm-business-model     → Business Model Canvas (optional fuller alternative - established or complex operational models)
/pm-kpis               → North Star Metric, AARRR, OKRs
/pm-business-case      → Business Case (3-year projections, Go/No-Go)
/pm-product-roadmap    → Product Roadmap v1
/pm-prd                → PRD - Phase 3b exit artifact (synthesizes all Phase 2+3a+3b)
                         [PRD_master.md is frozen after creation - immutable from this point]
/pm-scope-brief        → Scope Brief - Phase 3b exit ALTERNATIVE for commissioned builds
                         [mandate already given (client/exec decided): Phase 3a skipped, canvas/KPI
                          skills optional. Business Capabilities section = same downstream contract
                          as PRD Section 7; Phase 4-5 consume it identically. Change Log after baseline]
/pm-pitch-deck         → Pitch Deck content brief (slide-by-slide spec → Gamma visual deck)
                         [Optional - run if raising capital, selling to customers, or pitching partners]
                         [Requires: pm-lean-canvas + pm-business-case + pm-problem-validation]
                         [Gamma MCP required for visual output; skill outputs content brief if Gamma not connected]
```

### Phase 4 - Domain Modeling + Register Setup (FDD Stage 1)
```
/pm-domain-model            → Domain Model, ERD + optional Excalidraw domain diagram
/pm-entity-registry         → entities.md: entity list + Mermaid state machines per entity
                               (guard conditions TBD - added JIT by pm-feature-design)
/pm-business-rules-library  → business_rules.md + decision_models.md (Draft mode)
                               (rules finalized JIT by pm-feature-design before each feature build)
/pm-privacy-requirements    → PII Inventory, Privacy Requirements, GDPR action plan
/pm-product-roadmap         → Product Roadmap v2 (update with domain constraints)
```

### Phase 5 - Feature Planning (FDD Stage 2)
```
/pm-features-list      → feature_list.md (FDD Feature List - Live Register 4)
                          → FEAT-[DOMAIN]-[NUMBER] ID format
                          → KANO Analysis + V×C Matrix
                          → Stub Feature Cards created in features/cards/
                          → Notion push: Feature entries (Status=Backlog, Priority from KANO+V×C)
/pm-mvp-scope          → MVP Scope (IN/POST-MVP/CUT), Delivery Stripes (domain-focused channels)
                          → Feature-to-Stripe assignment, dependency sequencing per stripe
                          → Updates stripe: field in each Feature Card frontmatter
                          → Notion: enrich Features with Phase/Stripe
/pm-product-roadmap    → Product Roadmap v3 (update with feature and delivery view)
```

### Pre-Phase 6 - Technical Foundation
```
/common-ground         → Tech stack, repo structure, COMMON-GROUND.md
[👤 Architecture decisions, infrastructure setup]
```

---

### Cross-Phase Skills (run at any time)
> These skills are not tied to a specific phase. Run them progressively throughout the project or on demand.

```
/pm-glossary           → Project Glossary (terms, entities, artifacts, abbreviations)
                         [Continuous - run after each phase or when new terminology surfaces]
                         [Also run on demand: /pm-glossary add "term1, term2"]

/pm-diagrams           → Visual diagrams (two rendering modes)
                         [Mermaid.js - primary for Claude Code: state machines (entities.md),
                          sequence diagrams (Feature Card Section 3)]
                         [Excalidraw - secondary for human communication: Domain Model Overview,
                          User Flow, Business Process Model, System Architecture, JTBD Four Forces]
                         [Excalidraw types require: Excalidraw MCP connected]

/pm-process-flows      → System user types + business process maps (2A) + per-user screen-connected
                         user flows (2B, designer brief)
                         [Phase 4-5 bridge into design - re-runnable per domain/module]
                         [Feeds pm-feature-design's UX context (Section 3b) and the designer]

/pm-prioritize         → Re-runnable backlog prioritization engine (align to roadmap / your directive /
                          a named lens / propose-and-confirm), dependency-reconciled, non-destructive
                         [Run any time priorities shift - after pm-features-list, after MVP cut, or later]

/pm-audit              → Workspace health check - Tier 1 form (IDs, naming, cross-refs, lifecycle,
                          version drift) auto-fixed + Tier 2 strategic consistency (read-only, routes conflicts)
                         [Optional area argument: /pm-audit domain | rules | features | strategy]
                         [Run after pm-reconcile/pm-reverse-extract, after a framework version upgrade,
                          or any time to confirm the workspace is internally consistent]

/pm-onboarding         → Role-specific Onboarding Brief for a new team member (Developer / PM / Designer /
                          Stakeholder), distilled from the existing workspace
                         [Run when a new person joins. Skip if solo builder with no team.]

/pm-meeting            → Structured meeting notes, decisions log, and tagged action items from raw
                          notes or a transcript
                         [Run after any meeting where notes or a transcript exist]

/pm-prototype          → Tool-ready prototype spec (Lovable / v0 / Figma Make) to validate a flow, UX
                          hypothesis, or concept before real build; result mode feeds back to the
                          Feature Card / hypothesis register
                         [Cross-phase - use anytime there is genuine uncertainty worth de-risking cheaply]

/pm-stress-test        → Adversarial stakeholder pushback simulator (investor / CFO / board / CTO / DPO...)
                         [Run before any exec review, investor pitch, board meeting, or contentious push]

/pm-root-cause         → Diagnostic engine for an in-flight anomaly (metric dropped, churn spiked,
                          feature not adopted) - drills to the real root cause, ends with testable hypotheses
                         [Cross-phase - feeds /pm-hypotheses]

/pm-feature-viability  → Lightweight KANO/MDP/success-metric check before a new feature enters JIT design
                         [Skip if the feature is already scoped, committed, or in a validated roadmap]

/pm-decision-model     → JIT helper - add a single decision table (TBL-ID) to decision_models.md
                          without re-running the full pm-business-rules-library skill
                         [Typically triggered from pm-feature-design when a multi-condition decision surfaces]

/pm-business-rule-core / -critical / -governance
                       → JIT helpers - add a single business rule (operational / critical invariant /
                          compliance) to business_rules.md by priority class, without re-running the
                          full pm-business-rules-library skill
                         [Typically triggered from pm-feature-design when a rule not yet in the register surfaces]
```

---

### Feature Implementation - Phase Sequence
> Use this section when playbook = Feature. Replaces Phases 1-5 entirely.

```
MIGRATION PATH (existing product built outside the framework)
  /pureinn              → always first: workspace setup, state.json, pureinn-variables.md
  /common-ground        → technical context (stack, APIs, debt) → COMMON-GROUND.md
  /impeccable document     → design context (design system, components) → PRODUCT.md + DESIGN.md
  /pm-glossary          → start domain glossary

  TWO SUB-PATHS (reference only - resolved interactively in STEP 4's Rebuild playbook note):

  - Legacy docs exist and may conflict with the code (old BRD/FSD/domain models),
    and/or the team is changing - you need one reconciled source of truth:
    /pm-reconcile       → scans code, parses old docs, reconciles (code = structural truth,
                           docs = business logic, conflicts → AskUserQuestion)
                         → Reconciliation Report (the team's "where are we" brief)
                         → then orchestrates the rebuild below in reconciled mode.
                         This is the entry point - run it instead of the three skills standalone.

  - Docs already clean or absent - just bootstrap from code:
    /pm-entity-registry   → entities.md (extract from existing codebase/docs)
    /pm-business-rules-library → business_rules.md + decision_models.md (extract existing rules)
    /pm-reverse-extract   → reads existing Feature Cards/codebase
                         → extracts feature inventory in FDD format (FEAT-[DOMAIN]-[NUMBER])
                         → Notion: creates Feature hierarchy (primary: team visibility)
                         → generates feature_list.md, delivery-stripes.md
                         Use INSTEAD of pm-features-list + pm-mvp-scope.

  Both then proceed to Phase 6 + 7 (JIT per feature) directly.

─────────────────────────────────────────────

PHASE 0 - CONTEXT SETUP  [runs once per project onboarding, not per feature]
  /pureinn              → Product context (users, roadmap, known problems, workarounds)
  /common-ground        → Technical context (stack, domain model, APIs, debt) → COMMON-GROUND.md
  /impeccable document     → Design context (design system, UX patterns, components) → PRODUCT.md + DESIGN.md

  Exit: All three dimensions covered. Team has shared product understanding.
  Skip if already done (context files exist from a prior session).

─────────────────────────────────────────────

FEATURE VIABILITY ASSESSMENT  [runs per feature, before any spec work]

  Feature Target Profile
    → Which existing segment/persona does this serve?
    → KANO: Must-be / Performance / Delighter / Indifferent
    → V×C: Quick Win / Big Bet / Fill-in / Time Waster
    → Usage frequency + % of user base

  Demand Validation
    → Existing signal: analytics, support tickets, feature requests
    → Lightweight experiments if signal weak: fake door, mockup test, landing page
    → B2B: pilot commitment or letter of intent

  Strategic Alignment
    → Core vs. Adjacent: build vs. buy vs. integrate
    → Business impact: revenue / churn / support / strategic

  MDP Definition
    → Minimum Delightful Product: core value only
    → What is explicitly deferred to V1.1

  Success Metrics  [defined before build, dashboard set up before code is written]
    → Depth of usage (return rate, consistency)
    → Behavior change (does it shift workflow?)
    → Business impact (retention, conversion, support cost)
    → Avoid vanity metrics (raw clicks, impressions, DAU without depth)

─────────────────────────────────────────────

TRACK A - KNOW WHAT WE WANT  [skip Track B if here]

  Feature Set Assignment (grouping only - no longer a spec unit):
    Existing FS → feature is added to feature_list.md with existing stripe assignment
    New domain  → run /pm-entity-registry + /pm-business-rules-library (Draft mode) for that domain

  JIT Design (one feature at a time, per stripe):
    /pm-feature-design [FEAT-ID]  → Sections 1-3 of Feature Card + register finalization
                                    (scans existing codebase before generating sequence diagram)
    [Design Inspection]           → Team review (or solo confirm)
    Build skills                  → reads Feature Card Section 3 as build spec

─────────────────────────────────────────────

TRACK B - KNOW THE AREA, NOT THE SOLUTION  [discovery needed, output → Track A]

  Save all discovery outputs to: initiatives/[initiative-slug]/discovery/

  [👤 Human] User research (5-10 interviews, target segment only)
  [👤 Human] Competitive analysis (if solution direction unclear)
  [👤 Human] Tech feasibility (with existing stack)
  /pm-business-case   → Feature Business Case (revenue/retention impact, ROI, Go/No-Go)
  /pm-kpis            → Feature Success Metrics (depth / behavior / business impact)

  After discovery - if new domain is involved (new entities, new business rules):
  /pm-prd [Initiative mode] → initiatives/[slug]/prd.md (Business Capabilities for this domain)
  /pm-entity-registry       → domain/entities.md (append mode - new domain entities)
  /pm-business-rules-library → domain/business_rules.md + decision_models.md (append mode)
  /pm-features-list [FI append] → features/feature_list.md (append) + stubs in features/cards/
                                   KANO + V×C saved to initiatives/[slug]/

  Apply KANO + V×C to defined features → enter Track A.

─────────────────────────────────────────────

DELIVERY CYCLE  [same JIT per Feature as Greenfield Phase 6+7, with FI additions]
  /pm-stripe + /pm-feature-design + build skills (see Phase 6+7 section below)
  Feature Implementation additions per feature:
    ⚠️ All new code wrapped in feature flag (OFF by default), FE + BE both respect flag
    ⚠️ API changes: additive only, or v2 alongside v1 with deprecation timeline
    ⚠️ DB changes: additive only (new tables, new columns) - no renames, no deletes
    ⚠️ Full regression suite per feature before merge
    ⚠️ Performance gate: feature adds ≤10% latency to existing API calls
    ⚠️ Gradual rollout: Internal → 5% → 25% → 50% → 100%
    ⚠️ Kill switch: disable flag if error rate >5%
```

---

### Phase 6 + 7 - FDD Delivery Cycle (JIT per Feature, Stripe-based)

Phase 6 and 7 run as an integrated JIT cycle. Spec and build happen per Feature, not per Feature Set.
Each Delivery Stripe = a domain-focused parallel channel (not a time-box).
Feature status is tracked in Feature Card frontmatter and feature_list.md.
Domain registers (entities.md, business_rules.md, decision_models.md) are the living source of truth.

```
STRIPE ORCHESTRATION (use for every Stripe)
/pm-stripe             → Stripe dashboard, advance next feature, mark Design Inspection passed,
                          mark feature Promoted, run Impact Analysis when BR changes

JIT CYCLE PER FEATURE (orchestrated by /pm-stripe)
Step 0 (optional): /pm-feature-viability [FEAT-ID]
          → KANO classification, MDP scope, success metrics
          → Skip if feature already scoped, committed, or in validated roadmap

Step 1: /pm-feature-design [FEAT-ID]
          → Pre-step (Feature Implementation mode only): scan real service files
          → Commit 1: spec([FEAT-ID]): guard conditions + rule finalization
            - entities.md: guard conditions added to state transitions
            - business_rules.md: Draft rules updated to Final
            - decision_models.md: decision table rows finalized
          → Commit 2: spec([FEAT-ID]): feature design complete
            - Feature Card Section 1 (Biznis Mantinely - BR-IDs, entity guard conditions)
            - Feature Card Section 2 (Acceptance Criteria)
            - Feature Card Section 3 (Mermaid sequenceDiagram + files to modify + UX/UI context)
          → Status: 2_Spec_Done

Step 2: Design Inspection (/pm-stripe) [Team mode: human review of Sections 1-3]
          → Status: 3_Ready_to_Build
          [Solo mode: AI generates, human confirms - same gate, lighter ritual]

Step 3: BUILD SKILLS (/pm-stripe → Phase 7)
          → Status: 4_In_Build (set when build skills start)
/fullstack-guardian    → BE implementation (reads Feature Card Section 3)
/impeccable-craft      → FE implementation (reads Feature Card Section 3)
/test-master           → Unit + integration tests
/playwright-expert     → E2E tests
/code-reviewer         → Code review
/impeccable-audit      → Code quality review
/impeccable-harden     → Security hardening
/security-reviewer     → Security audit
/devops-engineer       → CI/CD, deployment
/monitoring-expert     → Observability, alerting

Step 4: Feature Card Section 4 (Realizacny Protokol) filled
          → Commits, test files, flag OFF verification
          → Status: 5_In_Review (set when build complete, before final review)
          → Code Inspection result recorded
          → Status: 6_Shipped (Feature Card immutable after this)

SPEC GATE (hard rule, enforced by /pm-stripe before routing to build):
  Feature Card Sections 1-3 must be complete
  Status must be 3_Ready_to_Build

ATOMIC COMMIT PROTOCOL (parallel stripe safety):
  Register updates (entities.md, business_rules.md, decision_models.md) committed BEFORE code
  Two commits per feature: register update first, Feature Card update second
  One feature at a time per stripe in active design/build (prevents register conflicts)

OPTIONAL SPEC SUPPORT
/architecture-designer → System Design Blueprint, ADRs (if needed)
/api-designer          → API contracts, OpenAPI spec (if needed)
/impeccable document   → PRODUCT.md + DESIGN.md [run once at Phase 6 start]
/impeccable-shape      → UX/UI shape brief per feature
```

---

