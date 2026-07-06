---
name: pm-product-roadmap
description: Generate or update the Product Roadmap. Living document - v1 created in Phase 3b (vision + problem + business model), v2 updated in Phase 4 (domain constraints), v3 updated in Phase 5 (feature and delivery view). Run this skill at each update point.
license: MIT
metadata:
  agent-mode: synthesis
  author: https://github.com/ljucask
  version: "1.2.0"
  domain: product-management
  triggers: product roadmap, roadmap, strategic roadmap, roadmap v1 v2 v3, delivery plan
  role: specialist
  scope: planning
  output-format: document
  related-skills: pm-prd, pm-mvp-scope, pm-features-list, pm-prioritize, pm-kpis
---

# PM - Product Roadmap


## Agent mode (`--agent`)

Supports `--agent`: runs autonomously in a subagent, drafts the artifact from existing inputs, and returns a short summary + coverage note.

- **No flag** → interactive (default); if inputs are heavy, offer agent mode.
- **`--agent`** → obey. First check inputs are complete. Anything missing: do NOT invent it - mark `[ASSUMED - what/why]` in the output and summary. Never hallucinate to fill a gap.

---

## What this skill does

Creates and maintains the Product Roadmap - a living strategic document that evolves across phases:

- **v1 (Phase 3b):** Vision + validated problem + customer segments + business model horizon. No features yet - strategic direction only.
- **v2 (Phase 4):** Domain constraints and architecture decisions incorporated. Technical realities added. **Functional Decomposition** introduced - phases mapped to Domains and Feature Sets as the top-down input to the Feature Plan. Still no individual Features.
- **v3 (Phase 5):** Feature view added. Phases aligned with Feature Sets and Delivery Stripes. Delivery timeline visible.

This skill handles all three versions. Step 0 determines which version applies and what updates are needed.

**The roadmap and the feature list are iterative and bidirectional - not strictly top-down.** The v1/v2/v3 versions are a default rhythm, not a rigid waterfall (per the Adaptive-execution standard in CLAUDE.md). Two valid orderings, and you can mix them:

- **Top-down:** you have a notion of phases first (a partial roadmap - v1/v2, phases only, detail TBD). The feature list is derived from that, then the roadmap is **completed** (v3) once features exist.
- **Bottom-up:** you extract or propose features first (via `pm-features-list` / `pm-reverse-extract`), and the roadmap phases and sequencing are **filled in from them**.

So a partial roadmap is a valid, expected state - capture the phases you know, derive features, and return to complete the remaining parts. Features can drive phasing, not only reflect it. When you run this skill, detect what already exists (partial roadmap? feature list?) and adapt - complete what is missing rather than assuming a fixed order.

The roadmap is NOT a sprint backlog. It communicates strategic intent and phase sequencing - not implementation details.

---

## Dependencies

**Recommended before running v1 (Phase 3b):**
- `pm-problem-validation` - validated problem is the strategic foundation
- `pm-business-model` - revenue model and segments frame the roadmap horizon
- `pm-kpis` - success metrics anchor each roadmap phase

**Recommended before running v2 (Phase 4):**
- v1 roadmap must exist
- `pm-domain-model` - domain constraints affect phase ordering
- `pm-privacy-requirements` - compliance requirements may shift timelines

**Recommended before running v3 (Phase 5):**
- v2 roadmap must exist
- `pm-features-list` - feature inventory for the feature view
- `pm-mvp-scope` - MVP scope, Feature Sets, and Delivery Stripes define the delivery structure

**Produces artifacts used by:**
- `pm-prd` - roadmap is a required PRD section
- `pm-business-case` - roadmap phases inform investment staging
- All Phase 6 skills - roadmap v3 defines what gets built in which stripe

---

## Step 0: Current state check

Check for existing artifacts:
- Product Roadmap (any version)

If a roadmap exists: identify the current version (v1 / v2 / v3) and what phase we are in now. Determine what update is needed.

Also check: what Phase 3b artifacts exist (Business Model Canvas, KPIs, Business Case)? What Phase 4 artifacts exist (Domain Model)? What Phase 5 artifacts exist (Features List, MVP Scope)?

Look for: roadmap that jumps straight to features without strategic context, phases without success criteria, missing "not now" section, timeline without explicit assumptions, v1 being updated with feature detail before Phase 5 is complete.

**Interaction:** Group related questions (2-4 per round) and confirm before moving on. For any A/B/C/D choice, use the AskUserQuestion tool with one option marked **(Recommended)** - never print options as plain text. Keep open-ended questions free-text (don't fake options). If the user is unsure, propose 3-4 concrete options plus "Other". Surface an assumption the moment you make one; never fabricate to fill a gap. (Full standard: CLAUDE.md.)

---

### Re-run with new inputs (delta mode)

If a roadmap already exists and you are re-running it because new upstream evidence arrived (updated personas, market analysis, re-prioritization), do NOT rewrite from scratch. Operate in delta mode (on re-run: compare against the prior artifact, update only what new evidence supports, and show the delta before finalizing; never silently overwrite - full standard in CLAUDE.md) - this is distinct from the v1/v2/v3 version steps below, which add planned detail; delta mode re-validates existing strategic content against new research:

1. **Read the current roadmap first** and capture its claims in the sections most sensitive to the new input: Vision, Strategic Phases (Problem&Market context, Segments), phase success criteria, "What We Are Not Building".
2. **Re-validate against the new upstream sources:** `personas.md`, `market-analysis.md`, `PRD_master.md`, `business-model-canvas.md`, hypotheses register.
3. **Change only what the new evidence supports.** Mark each change `[UPDATED - previous: X / new: Y - reason: which input drove it]`; leave what the new input does not address `[UNCHANGED]`.
4. **Show the delta and wait for confirmation before writing** - never silently overwrite a prior strategic conclusion, and never re-assign phases/deliverables without explicit sign-off.
5. **Surface the cascade:** after updating, name the downstream artifacts now possibly inconsistent - `/pm-features-list` (feature `phase` assignments), `/pm-mvp-scope` (stripes), `/pm-prd` (roadmap summary section) - and recommend `/pm-audit strategy` to verify the whole strategic layer still agrees.

---

## Step 1: Gather inputs

The questions differ by version. After Step 0, Claude identifies which version and asks accordingly.

### For v1 (Phase 3b - new roadmap):

Ask questions in 2 groups. After each group show a summary and wait for confirmation before continuing.

**Group 1 of 2 - Vision and phases**

Ask all as plain text:

What is the 3-year product vision in one sentence? What does the world look like if you succeed?

What is the 12-month goal? Where do you want to be in a year - specific metrics or milestones?

How do you think about the product in strategic phases? Describe 2-4 phases with a name and primary goal for each. (e.g., "Phase 1: Prove value with early adopters → Phase 2: Scale core use case → Phase 3: Expand to adjacent segments")

What is the North Star Metric? (from pm-kpis if available) What is the success signal that exits each phase?

After answers, confirm: "Does this phase structure and success logic make sense?"

**Group 2 of 2 - Scope and risks**

Ask all as plain text:

What is explicitly out of scope for the first 12 months? What do customers ask for that you are choosing not to build, and why?

What external factors could shift the timeline? (regulation, funding, hiring, partnership) What is the biggest strategic risk to this roadmap?

After answers, show complete v1 inputs summary. Ask for final confirmation before generating the roadmap.

---

### For v2 (Phase 4 update):

Ask all as plain text in one group:

What did the Domain Model reveal about system complexity or data structure? Are there domain-driven constraints that affect phase ordering or timeline?

What technical decisions change what can be built when? Are there dependencies between technical capabilities that affect sequencing?

Any regulatory requirements from pm-privacy-requirements that add time to specific phases?

What changes from v1? (new phases, shifted timelines, dropped scope, new risks)

Confirm before updating.

---

### For v3 (Phase 5 update):

**First check the dependency:** the v3 delivery view (stripes + MVP cut) is downstream of `/pm-mvp-scope`. Look in `feature_list.md` for stripe assignments and an IN/POST-MVP cut. **If they are absent (mvp-scope has not run - common in a Rebuild where roadmap runs before features are carded), do not ask the user to invent them and do not fabricate them.** Finalize every other section, mark `MVP Delivery View` as `[TBD - pending /pm-mvp-scope]`, and tell the user to re-run this skill after mvp-scope. Only proceed with the questions below if mvp-scope output exists.

Ask all as plain text in one group:

What is in MVP? List the Feature Sets and their priority order. (from pm-mvp-scope if available)

What are the planned Delivery Stripes? How many for MVP? What does the post-MVP roadmap look like?

What changes from v2? (feature decisions that shift strategic direction, new risks, scope changes)

Confirm before updating.

---

## Step 2: Generate artifact

Generate in English.

---

### ARTIFACT: Product Roadmap

> The template below is for v1. Claude adapts for v2 (adds domain/technical layer) and v3 (adds feature/stripe view) based on the current version being created.

```markdown
# Product Roadmap - [Product Name]

> **Phase created:** 3 - Define & Validation
> **Current version:** v1 / v2 / v3
> **Last updated:** [date]
> **Next scheduled update:** Phase 4 (domain model complete) / Phase 5 (MVP scope defined)

---

## Vision

**3-year vision:**
[One sentence: what does the world look like if this product succeeds?]

**12-month goal:**
[What we want to achieve in the next 12 months - measurable direction, not a feature list]

**North Star Metric:** [NSM from pm-kpis]
**NSM Target (Month 12):** [X]

---

## Strategic Phases

> v1: strategic direction only. Feature detail comes in v3.

### Phase 1: [Name] - [Timeframe]
**Goal:** [What this phase achieves - one sentence]
**Focus:** [What we concentrate on]
**Key hypothesis being tested:** [The core assumption this phase validates]

**Success criteria (phase exit gate):**
- [ ] [Measurable condition 1 - e.g., 20 paying customers]
- [ ] [Measurable condition 2 - e.g., Day 30 retention > 40%]
- [ ] [Measurable condition 3]

**What we are NOT doing in this phase:**
- [Explicitly excluded scope]
- [Features deferred to Phase 2]

---

### Phase 2: [Name] - [Timeframe]
**Goal:** [What this phase achieves]
**Focus:** [What we concentrate on]
**Key hypothesis being tested:** [The core assumption]

**Unlock condition:** [What must be true before Phase 2 starts - exit gate from Phase 1]

**Success criteria:**
- [ ] [Condition 1]
- [ ] [Condition 2]

---

### Phase 3: [Name] - [Timeframe]
**Goal:** [What this phase achieves]
**Focus:** [Expansion / optimization / new segments]

**Unlock condition:** [Exit gate from Phase 2]

**Success criteria:**
- [ ] [Condition 1]

---

## Functional Decomposition (v2+ - top-down input to the Feature Plan)

> Added in v2 (once the Domain Model exists), refined in v3. This is the bridge from strategy to the Feature List: each strategic phase is decomposed into the functional areas (**Domains**) and capabilities (**Feature Sets, FS-NN**) it requires. `pm-features-list` consumes this map to derive **Features** top-down as the leaves. One consistent picture for both audiences - investor sees direction, dev team sees what gets built where.

| Strategic Phase | Domain | Feature Set (FS-NN) | Capability / business outcome |
|---|---|---|---|
| Phase 1: [Name] | [Order Management] | FS-01: [Order Processing] | [what this capability delivers for the client] |
| Phase 1: [Name] | [Payments] | FS-02: [Card Payments] | |
| Phase 2: [Name] | [Notifications] | FS-03: [Transactional Email] | |

**Derivation rules:**
- Features are **not** listed here - they are derived from these Feature Sets in `pm-features-list` (top-down, leaves last). This guarantees every Feature traces to a phase and a capability.
- 2-level hierarchy only: **Domain > Feature Set (FS-NN) > Feature**. The classic FDD "Major Feature Set" level is intentionally not used (lean / AI-first).
- FS-NN numbering is global and continues across domains.

---

## What We Are Not Building (Now)

These are features and capabilities we have explicitly decided not to build in the current horizon. This is a strategic choice, not a backlog.

| Item | Why deferred | Reconsider when |
|---|---|---|
| [Feature / capability] | [Too complex for MVP, wrong segment, unvalidated demand...] | [Phase 2 / after X customers / if Y signal appears] |
| [Feature 2] | | |
| [Feature 3] | | |

---

## Dependencies and Risks

| Dependency / Risk | Type | Impact | Mitigation |
|---|---|---|---|
| [e.g., Payment integration timeline] | External | Could delay Phase 1 by [X weeks] | [Start early, parallel track] |
| [e.g., Regulatory approval in SK] | Regulatory | Could block Phase 2 | [Legal track started in Phase 2] |
| [e.g., Hiring key engineer] | Internal | Phase 1 delayed if not hired by [date] | [Recruiting started now] |
| [e.g., AI API pricing increase] | Technical | Margin compression → repricing needed | [Cost model reviewed quarterly] |

---

## Roadmap Assumptions

The timeline in this roadmap assumes:
- [Assumption 1: e.g., Team of X fully onboarded by [date]]
- [Assumption 2: e.g., First paying customers acquired through founder-led sales]
- [Assumption 3: e.g., No major regulatory changes in target markets]
- [Assumption 4: e.g., AI API costs remain within ±20% of current rate card]

**If any of these change:** [Which phase gates should be reviewed and how]

---

## Version History

| Version | Date | Phase | Key changes |
|---|---|---|---|
| v1 | [date] | Phase 3b | Initial - strategic phases, vision, success criteria |
| v2 | [date] | Phase 4 | Domain constraints added, [X] timeline adjustments |
| v3 | [date] | Phase 5 | Feature view added, Delivery Stripes defined |
```

---

### v3 Additions (Phase 5 update)

When updating to v3, Claude adds the following section to the artifact:

```markdown
---

## MVP Delivery View (v3)

> Added in Phase 5 after MVP Scope is defined.

> **DEPENDENCY GUARD - do not fabricate this section.** Delivery Stripes and the MVP/POST-MVP cut are the **output of `/pm-mvp-scope`**, downstream of this skill. Before writing this section, check `feature_list.md` (and card frontmatter) for **stripe assignments and an IN/POST-MVP cut**. If they are absent - i.e. `/pm-mvp-scope` has not run yet (common when roadmap runs early, e.g. in a Rebuild before features are fully carded) - **do NOT invent stripes or an MVP cut.** Mark the whole section `[TBD - pending /pm-mvp-scope]` and finalize the other sections. Fabricating a delivery view that does not match the real cut violates the depth-over-breadth rule. Once `/pm-mvp-scope` has run, re-run this skill to mirror its result here (feature_list stays the source of truth; this section is a summary of it).

### Feature Sets (logical groupings)

| Feature Set | Description | Feature Cards Status | Priority |
|---|---|---|---|
| [FS-01: Name] | [What functional area this covers] | [Backlog / In Spec / Ready to Build] | P1 |
| [FS-02: Name] | | | P2 |
| [FS-03: Name] | | | P3 |

### Delivery Stripes (domain-focused parallel channels)

| Stripe | Domain focus | Features included | Feature Set(s) | Goal |
|---|---|---|---|---|
| Stripe 1 | [e.g., Auth + Onboarding] | [FEAT-AUTH-001, FEAT-AUTH-002] | FS-01 | [What this stripe proves or delivers] |
| Stripe 2 | [e.g., Payments] | [FEAT-PAY-001, FEAT-PAY-002] | FS-02 | |
| Stripe 3 | [e.g., Notifications] | [FEAT-NOT-001] | FS-03 | |
| ... | | | | |

**MVP completion:** [Stripe X - when last MVP feature reaches 6_Shipped]

### Post-MVP Roadmap

| Horizon | Focus | Feature Sets planned |
|---|---|---|
| Month 1-3 post-MVP | [Retention + activation optimization] | [FS-04, FS-05] |
| Month 4-6 post-MVP | [Expansion features] | [FS-06] |
| Month 7-12 post-MVP | [Scale and new segment] | [TBD based on data] |
```

---

## Internal completeness checklist

<!-- Claude reference only - not shown to user.
     Use in Step 0 to identify gaps in existing artifacts.
     Use in Step 2 to verify full coverage before finalizing output. -->

**v1 Product Roadmap must cover:**
- [ ] 3-year vision stated (direction, not feature list)
- [ ] 12-month goal stated (measurable direction)
- [ ] Strategic phases defined (2-4 phases, each with name + timeframe + goal)
- [ ] Success criteria per phase (measurable, specific - not "grow users")
- [ ] Unlock condition per phase (what must be true before phase starts)
- [ ] "What we are not building" section - explicit deferred scope
- [ ] Roadmap assumptions listed (what must hold for the timeline to be valid)
- [ ] North Star Metric stated with phase-aligned targets

**v2 additions must cover:**
- [ ] Domain constraints incorporated (any from Domain Model that affect sequencing)
- [ ] Technical dependencies added (architecture decisions that gate features)
- [ ] Compliance requirements reflected in timeline (GDPR, licensing, etc.)
- [ ] Version history updated

**v3 additions must cover:**
- [ ] Feature Sets listed with priority
- [ ] Delivery Stripes defined (domain-focused parallel channels, dependency-ordered)
- [ ] Each stripe has a stated goal (not just a feature list)
- [ ] MVP completion stripe identified
- [ ] Post-MVP roadmap direction stated
- [ ] Feature Card status per feature noted (spec gate: Sections 1-3 + 3_Ready_to_Build before build)
- [ ] Version history updated

**Living document quality:**
- [ ] Version number and date are current
- [ ] Assumptions section is up to date
- [ ] "What we are not building" is reviewed and reflects current decisions
- [ ] No outdated phase goals from earlier versions

**For SaaS/AI products:**
- [ ] Phase 1 explicitly targets early adopters (not general availability)
- [ ] AI feature maturity staged (MVP: basic AI → Phase 2: trained on customer data → Phase 3: advanced)
- [ ] Compliance phase included if GDPR / EU AI Act requirements need to be addressed before launch
- [ ] Freemium funnel is a strategic phase consideration (when to introduce free tier)

## Notion

Read `pureinn-variables.md` key "Product Roadmap" → if URL present, remind user after saving:
`Roadmap saved locally. Update Notion: [Product Roadmap URL]`

## Save to

```
pureinn-workspace/[project-slug]/artifacts/phase-3-define/product-roadmap-v1.md
pureinn-workspace/[project-slug]/artifacts/phase-4-domain/product-roadmap-v2.md
pureinn-workspace/[project-slug]/artifacts/phase-5-planning/product-roadmap-v3.md
```

---

## Handoff

**Čo si teraz má:** Product Roadmap - vízia a sekvencia v čase. (Beží 3x: v1 v Phase 3b, v2 po doméne v Phase 4, v3 po features v Phase 5.)

**Ďalší krok:** Podľa fázy - po v1: `/pm-prd` (exit Phase 3b). Po v2: `/pm-features-list`. Po v3: `/pm-mvp-scope`.

**Môžeš preskočiť ak:** Roadmapa sa pre dané kolo nezmenila - nový rez nepridáva hodnotu.
