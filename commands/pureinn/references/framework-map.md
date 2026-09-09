# Pureinn - Framework map reference

> Reference for `commands/pureinn/COMMAND.md`. Shown on `/pureinn map` and `/pureinn help`.

## FRAMEWORK MAP

> Shown when user runs `/pureinn map` or `/pureinn help`

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PUREINN - FRAMEWORK MAP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Three entry points:
  /pureinn [idea or product name]  Start or continue a project
  /pureinn map                     This view - full framework overview
  /common-ground                   Technical setup (Pre-Phase 6)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Then display each phase as a block:

```
PHASE 1 - FOUNDATION & COLLABORATION SETUP
Goal: Align on context, assumptions, and constraints before discovery begins.
Output: Scales by team size - from a single project charter to full governance setup.
─────────────────────────────────────────────
  /pm-project-charter   [all team types]
    Input:  Project context, goals, constraints, risks, success definition
    Output: Project Charter, Assumptions & Risks Register

  /pm-team-roster       [small team / full team / corporate]
    Input:  Team members, roles, skill inventory
    Output: Team Roster, Decision Rights Matrix, Skill Gap Assessment
    Note:   Skip for solo builders. RACI simplified for small founding teams.

  /pm-comms-charter     [small team / full team / corporate]
    Input:  Team preferences, meeting cadence, tools
    Output: Communication Charter, Meeting Rhythm
    Note:   Skip for solo builders.

  /pm-stakeholder-map   [full team / corporate only]
    Input:  Product idea, team structure, organization context
    Output: Stakeholder Map, RACI Matrix, Escalation Tree
    Note:   Skip for solo and small founding teams unless external investors/board involved.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PHASE 2 - IDEATION & DISCOVERY
Goal: Validate the problem, customer, market, and technical feasibility.
Output: Problem Validation Summary (synthesizes all 4 tracks).
Four parallel tracks - can run simultaneously.
─────────────────────────────────────────────
  TRACK A - Tech Feasibility
  /pm-tech-feasibility
    Input:  Tech research (Perplexity / Tech Lead), stack assumptions
    Output: Tech Feasibility Report

  TRACK B - Domain & Legal
  /pm-domain-analysis
    Input:  Domain research (Perplexity), regulatory landscape
    Output: Domain Analysis Report, Legal & Regulatory Requirements

  TRACK C - Market
  /pm-market-analysis
    Input:  Market data (Perplexity), competitor research
    Output: Market Size (TAM/SAM/SOM), Competitor Analysis, SWOT, Market Timing

  TRACK D - Voice of Customer
  👤 Human: ≥10 customer interviews (or SynthFolk / ChatGPT synthetic)
  /pm-personas
    Input:  Interview transcripts, survey data, observations
    Output: Customer Segments, Personas, Early Adopters Profile
  /jtbd-building
    Input:  Personas + interview data
    Output: JTBD Analysis, Forces Diagram

  CONVERGENCE
  /pm-problem-validation
    Input:  All Track A-D outputs
    Output: Problem Validation Summary (Phase 2 exit artifact)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PHASE 3a - VALIDATION
Goal: Validate core assumptions about problem, customer, and market before committing to strategy.
Character: externally-paced - tempo set by market, not by you. Can start parallel with late Phase 2.
Output: Go/No-Go verdict (hard gate - only GO unlocks Phase 3b).
"Done elsewhere": accepted - provide Go/No-Go verdict + key evidence to /pureinn directly.
─────────────────────────────────────────────
  /design-thinking
    Input:  Problem Validation Summary, Personas
    Output: Problem Statement, POV, HMW Questions, Ideation Synthesis, Elevator Pitch,
            Validation Hypotheses draft

  /pm-hypotheses  [Plan mode]
    Input:  Validation Hypotheses draft, Phase 2 evidence (JTBD, Personas, Problem Validation)
    Output: Hypothesis Register (ICP definition, assumption map, experiment plan, success criteria)

  [👤 Experiments - human activity]
    Input:  Experiment plan from /pm-hypotheses
    Activity: Landing page, smoke test, targeted ads, pre-order, rapid prototype - based on plan
    Budget: €100-300 for quantitative experiments

  /pm-hypotheses  [Results mode]
    Input:  Experiment results vs. pre-defined success criteria
    Output: Hypothesis Register (updated), Go/No-Go Decision (Go / Pivot / Stop)
    Note:   HARD GATE - GO required to enter Phase 3b. PIVOT loops back. STOP ends project.
            No FORCE bypass on this gate. (Commissioned builds skip Phase 3a entirely -
            mandate given - so this gate is never evaluated for them.)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PHASE 3b - COMMERCIAL DEFINITION
Goal: Translate validated problem-market fit into commercial strategy and product specification.
Character: AI-assisted synthesis sprint. Quality of output depends entirely on Phase 3a signal quality.
Condition: Phase 3a GO verdict required. Non-negotiable for speculative products.
           (Commissioned builds enter directly - Phase 3a skipped, mandate given.)
Output: PRD (frozen after creation) + Business Case + Roadmap v1.
        Commissioned builds: Scope Brief baselined (product/scope_brief.md) instead.
"Done elsewhere": accepted - bring existing Lean Canvas, financial model, or strategy artifacts via Path A.
─────────────────────────────────────────────
  /pm-kotler
    Input:  High-level Feature Vision (from design-thinking), JTBD, Personas
    Output: Product Definition - 5 levels (Core Benefit / Basic / Expected / Augmented / Potential)

  /pm-lean-canvas
    Input:  Design Thinking outputs, Kotler Product Definition, Phase 2 research
    Output: Lean Canvas (one-page business model: Problem / Solution / UVP / Unfair Advantage /
            Customer Segments / Key Metrics / Channels / Cost Structure / Revenue Streams)

  /pm-kpis
    Input:  Lean Canvas (Key Metrics block), Problem Validation
    Output: North Star Metric, AARRR Funnel Metrics, OKRs

  /pm-business-case
    Input:  Lean Canvas, KPIs, Market Analysis
    Output: Business Case (3-year projections, unit economics, Go/No-Go)

  /pm-product-roadmap  [v1]
    Input:  Problem Validation, Lean Canvas, KPIs
    Output: Product Roadmap v1 (vision + strategic phases)

  /pm-prd  [Phase 3b exit artifact]
    Input:  All Phase 2 + Phase 3a + Phase 3b outputs
    Output: PRD (full product-level consolidation document - frozen after creation)

  /pm-scope-brief  [Phase 3b exit alternative - commissioned builds]
    Input:  Discovery Report (primary), client-discovery meeting notes, Track artifacts
    Output: Scope Brief (product/scope_brief.md) - what exactly gets built: Business
            Capabilities (same downstream contract as PRD Section 7), scope IN/OUT/deferred,
            edge cases [CANDIDATE-BR], acceptance criteria + Change Log after baseline
    Note:   Used when the mandate is already given (client/exec decided) - Phase 3a is
            skipped and the canvas/KPI/business-case skills are optional. Phase 4-5
            consume the Scope Brief exactly as they consume a PRD.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PHASE 4 - DOMAIN MODELING + REGISTER SETUP  [FDD Stage 1]
Goal: Model the domain, initialize the 4 living registers. Registers are the source of truth for AI throughout Phase 6-7.
─────────────────────────────────────────────
  /pm-domain-model
    Input:  PRD Business Capabilities, domain knowledge
    Output: Domain Model, ERD, Ubiquitous Language Glossary
            + optional Excalidraw domain overview

  /pm-entity-registry
    Input:  PRD Business Capabilities, Domain Model
    Output: entities.md - entity list + Mermaid stateDiagram-v2 per entity
            States and transitions defined; guard conditions left TBD (added JIT by pm-feature-design)
            Events use past tense dot notation (e.g., order.confirmed)
    Saves:  domain/entities.md (Live Register 1)

  /pm-business-rules-library
    Input:  PRD Business Capabilities, entities.md
    Output: business_rules.md + decision_models.md in Draft mode
            Rules finalized JIT by pm-feature-design before each feature build
    Saves:  domain/business_rules.md (Live Register 2), domain/decision_models.md (Live Register 3)
    IDs:    BR-[DOMAIN]-[NUMBER], TBL-[DOMAIN]-[NUMBER]

  /pm-privacy-requirements
    Input:  Domain Model, Legal Requirements, product description
    Output: PII Inventory, Privacy Requirements, GDPR Action Plan

  /pm-product-roadmap  [v2 update]
    Input:  Roadmap v1, Domain Model constraints
    Output: Product Roadmap v2 (+ domain constraints layer)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PHASE 5 - FEATURE PLANNING  [FDD Stage 2]
Goal: Define the feature inventory, prioritize, assign to Delivery Stripes.
─────────────────────────────────────────────
  /pm-features-list
    Input:  PRD Business Capabilities, Domain Model, user research
    Output: feature_list.md - FDD Feature List (FEAT-[DOMAIN]-[NUMBER] IDs)
            KANO Analysis + V×C Matrix
            Stub Feature Cards (status: 1_Backlog) in features/cards/
    Saves:  features/feature_list.md (Live Register 4), features/cards/FEAT-*.md
    Notion: Feature entries pushed (Status=Backlog, Priority from KANO+V×C)

  /pm-mvp-scope
    Input:  feature_list.md, business priorities
    Output: MVP Scope (IN/POST-MVP/CUT), Delivery Stripes (domain-focused channels)
            Feature-to-Stripe assignment + dependency sequencing per stripe
            Updates stripe: field in Feature Card frontmatter
    Saves:  artifacts/phase-5-planning/mvp-scope.md, artifacts/phase-5-planning/delivery-stripes.md
    Notion: enrich Features with Phase/Stripe

  /pm-product-roadmap  [v3 update]
    Input:  Roadmap v2, MVP Scope, Delivery Stripes
    Output: Product Roadmap v3 (+ feature and delivery view)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PRE-PHASE 6 - TECHNICAL FOUNDATION
─────────────────────────────────────────────
  /common-ground
    Input:  PRD, Domain Model, team tech preferences
    Output: Tech Stack Decision, Repo Structure, COMMON-GROUND.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PHASE 6 + 7 - FDD DELIVERY CYCLE  [FDD Stages 3 + 4 - JIT per Feature]
Goal: Deliver working features, Stripe by Stripe, JIT spec just before each feature enters build.
Domain registers are the living source of truth. Feature Cards are the atomic delivery unit.
─────────────────────────────────────────────
  STRIPE ORCHESTRATION (orchestrates the full JIT cycle)
  /pm-stripe
    Input:  feature_list.md, Feature Card frontmatter status
    Output: Stripe dashboard, advance feature, run Impact Analysis, mark Promoted

  JIT CYCLE PER FEATURE (phases 6+7 integrated per feature)
  /pm-feature-design [FEAT-ID]
    Input:  Feature Card stub, entities.md, business_rules.md, decision_models.md,
            PRD section (prd_ref from frontmatter)
    Pre-step (Feature Implementation mode): scan real service/class files first
    Output: Commit 1 - register updates (guard conditions, rule finalization)
            Commit 2 - Feature Card Sections 1-3 (Biznis Mantinely, ACs, sequence diagram)
    Status: 2_Spec_Done

  [Design Inspection]
    Team: human review of Feature Card Sections 1-3 → 3_Ready_to_Build
    Solo: human confirm → 3_Ready_to_Build

  SPEC GATE (hard rule - /pm-stripe enforces before routing to build):
    Feature Card Sections 1-3 populated + status: 3_Ready_to_Build

  BUILD (Phase 7 - per feature, after spec gate)
  /fullstack-guardian    → BE implementation (reads Feature Card Section 3)
  /impeccable-craft      → FE implementation (reads Feature Card Section 3)
  /test-master           → Unit + integration tests
  /playwright-expert     → E2E tests
  /code-reviewer         → Code review
  /impeccable-audit      → Code quality
  /impeccable-harden     → Security hardening
  /security-reviewer     → Security audit
  /devops-engineer       → CI/CD, deployment
  /monitoring-expert     → Observability, alerting
                           → Feature Card Section 4 filled, status: 6_Shipped

  OPTIONAL SPEC SUPPORT (run when needed, not per feature)
  /architecture-designer → System Design Blueprint, ADRs
  /api-designer          → API contracts, OpenAPI spec
  /impeccable document   → PRODUCT.md, DESIGN.md [once at Phase 6 start]
  /impeccable-shape      → UX/UI shape brief per feature

  ATOMIC COMMIT PROTOCOL (parallel stripe safety):
    Register commits (entities.md, business_rules.md, decision_models.md) before code commits
    One feature per stripe in active design/build at any time

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

GREENFIELD - RUNNING THIS PLAYBOOK
Use when: building a new product from scratch, 0 active users, validating PMF.
─────────────────────────────────────────────
ONCE AT START
  /pureinn [idea]         → intake, document scan, playbook selection, dashboard
  /pm-glossary            → start domain glossary; update continuously

PHASE 1 - FOUNDATION  (scales by team size)
  Solo:  /pm-project-charter
  Team:  /pm-project-charter → /pm-team-roster → /pm-comms-charter
  Corp:  + /pm-stakeholder-map first
  Run /pureinn when done to advance.

PHASE 2 - DISCOVERY  (four parallel tracks)
  🔍 → /pm-tech-feasibility      (tech feasibility)
  🔍 → /pm-domain-analysis       (domain + legal)
  🔍 → /pm-market-analysis       (market + competitors)
  👤 ≥10 interviews → /pm-personas → /jtbd-building  (customer + JTBD)
  Converge: /pm-problem-validation  (Phase 2 exit artifact)
  Run /pureinn when done to advance.

PHASE 3 - DEFINE & VALIDATION
  /design-thinking          → Problem Statement, HMW, Elevator Pitch,
                              Validation Hypotheses draft
  /pm-hypotheses [Plan]     → Hypothesis Register (ICP, experiments, success
                              criteria set BEFORE running)
  👤 Run experiments        → landing page / smoke test / pre-order / concierge
  /pm-hypotheses [Results]  → Go/No-Go verdict
  HARD GATE: GO advances. PIVOT re-validates. STOP ends project.

  After GO:
  /pm-kotler             → Product Definition (5 levels)
  /pm-lean-canvas        → Lean Canvas (default)
  /pm-business-model     → Business Model Canvas (optional fuller alternative)
  /pm-kpis               → North Star Metric, AARRR, OKRs
  /pm-business-case      → 3-year projections, Go/No-Go
  /pm-product-roadmap    → Roadmap v1
  /pm-prd                → PRD (Phase 3b exit artifact - frozen after creation)
  /pm-pitch-deck         → Pitch Deck (optional)
  Run /pureinn when done to advance.

PHASE 4 - DOMAIN MODELING + REGISTER SETUP
  /pm-domain-model            → Domain Model, ERD
  /pm-entity-registry         → entities.md (entity states + Mermaid state machines)
  /pm-business-rules-library  → business_rules.md + decision_models.md (Draft mode)
  /pm-privacy-requirements    → PII Inventory, GDPR action plan
  /pm-product-roadmap         → Roadmap v2 (+ domain constraints)
  Run /pureinn when done to advance.

PHASE 5 - FEATURE PLANNING  [2-3 days]
  /pm-features-list    → feature_list.md (FDD Feature List), KANO, V×C
                         → Stub Feature Cards in features/cards/
                         → Notion: Feature entries pushed
  /pm-mvp-scope        → MVP Scope, Delivery Stripes (domain-focused channels)
                         → Feature-to-Stripe assignment + dependency sequencing
                         → Updates stripe: in Feature Card frontmatter
                         → Notion: Features enriched with Phase/Stripe
  /pm-product-roadmap  → Roadmap v3 (+ feature + delivery view)
  Run /pureinn when done to advance.

PRE-PHASE 6
  /common-ground       → Tech stack decision, repo structure → COMMON-GROUND.md

PHASE 6 + 7 - DELIVERY  [JIT per Feature, repeats per Stripe]
  /pm-stripe           → Stripe dashboard, advance next feature, route to design or build
  Per feature (JIT spec):
    /pm-feature-design [FEAT-ID]  → Sections 1-3 of Feature Card + register finalization
    Design Inspection             → human review (team) or confirm (solo)
    Spec gate: Sections 1-3 complete + status: 3_Ready_to_Build
  Per feature (build):
    /fullstack-guardian → /impeccable-craft → /test-master → /playwright-expert
    → /code-reviewer → /impeccable-harden → /devops-engineer → /monitoring-expert
    → Feature Card Section 4 filled → status: 6_Shipped → next feature

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FEATURE IMPLEMENTATION PLAYBOOK
Use when: product exists, users are active, goal is adding new functionality.
Does NOT follow Phase 1-5. Has its own entry sequence.
─────────────────────────────────────────────
MIGRATION PATH  [product built outside the framework - run once]
  /pureinn             → always first: workspace setup, state.json, pureinn-variables.md
  /common-ground       → technical context (stack, APIs, debt) → COMMON-GROUND.md
  /impeccable document    → design context (design system, components) → PRODUCT.md + DESIGN.md
  /pm-glossary         → start domain glossary
  /pm-entity-registry  → entities.md (extract from existing codebase/docs)
  /pm-business-rules-library → business_rules.md + decision_models.md (extract existing rules)
  /pm-reverse-extract  → reads existing Feature Cards/codebase
                         → extracts feature inventory in FDD format (FEAT-[DOMAIN]-[NUMBER])
                         → derives Feature hierarchy with status
                         → pushes full structure to Notion (primary: team visibility)
                         → generates feature_list.md, delivery-stripes.md (secondary: Claude context)
  → proceed to Phase 6 + 7 (JIT per feature)

─────────────────────────────────────────────
STANDARD PATH  [onboarding a new feature project]
  PHASE 0 - CONTEXT SETUP  [once per project onboarding]
  /pureinn           → Product context (users, roadmap, problems, workarounds)
  /common-ground     → Technical context → COMMON-GROUND.md
  /impeccable document  → Design context → PRODUCT.md + DESIGN.md

  FEATURE VIABILITY ASSESSMENT  [per feature, before spec]
  Feature Target Profile:
    - Target segment + KANO classification (Must-be / Performance / Delighter / Indifferent)
    - V×C Matrix (Quick Win / Big Bet / Fill-in / Time Waster)
    - Usage frequency + % of user base
  Demand Validation:
    - Existing signal: analytics, support tickets, requests
    - Lightweight experiments if signal weak (fake door, mockup, landing page)
    - B2B: pilot commitment or letter of intent
  Strategic Alignment: Core vs. Adjacent
  MDP Definition: minimum delightful product scope
  Success Metrics: depth of usage / behavior change / business impact (set before build)

  TRACK A - KNOW WHAT WE WANT
    Feature Set assignment (grouping only)
    New domain? → /pm-entity-registry + /pm-business-rules-library (Draft mode) first
    JIT design per feature:
    /pm-feature-design [FEAT-ID]  → Feature Card Sections 1-3 + register finalization
                                    (scans existing codebase before generating sequence diagram)
    Design Inspection             → team review or solo confirm
    Build skills                  → reads Feature Card Section 3 as build spec

  TRACK B - KNOW THE AREA, NOT THE SOLUTION
    👤 User research (5-10 interviews), competitive analysis, tech feasibility
    Feature Value Prop, Business Case, Success Metrics
    → Converges into Track A after discovery

  DELIVERY CYCLE  [same as Phase 6+7 below, plus FI-specific rules]
    Feature flags mandatory (all new code OFF by default)
    Backward compat: API and DB changes additive only
    Regression suite per feature (≤10% latency increase gate)
    Gradual rollout: Internal → 5% → 25% → 50% → 100%
    Kill switch: disable flag if error rate >5%
    Post-launch: minimum 4 weeks monitoring

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LEGEND
  👤 Human activity - done outside Claude (interviews, Figma, domain research)
  🔍 External AI - Perplexity, ChatGPT - results brought in as skill input
  🤖 AI Skill - Claude generates the artifact

ARTIFACT CHAIN - GREENFIELD
  Phase 2  → Problem Validation Summary
  Phase 3a → Go/No-Go verdict (hard gate before 3b)
  Phase 3b → PRD frozen (product-level consolidation, Business Capabilities section drives Phase 4+)
  Phase 4  → Domain Model + entities.md + business_rules.md + decision_models.md (Draft)
  Phase 5  → feature_list.md + MVP Scope + Delivery Stripes + Stub Feature Cards
  Phase 6 (JIT) → Feature Card Sections 1-3 + register finalization (per feature, per stripe)
  Phase 7 → Working software + Feature Card Section 4 (per feature, Promoted status)

ARTIFACT CHAIN - FEATURE IMPLEMENTATION
  Phase 0 → Product + Technical + Design context (COMMON-GROUND.md, PRODUCT.md, DESIGN.md)
  Per feature → Feature Target Profile + Demand Validation + MDP + Success Metrics
  JIT per feature → Feature Card Sections 1-3 + register updates (entities.md, business_rules.md)
  Per Stripe → Build → Regression → Review → Deploy (feature-flagged)
  Per feature → Gradual rollout (Internal → 5% → 25% → 50% → 100%)
  Post-launch → 4 weeks monitoring

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

