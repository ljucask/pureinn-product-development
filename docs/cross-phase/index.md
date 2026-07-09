# Cross-phase skills

Skills that run at any point in any playbook - not tied to a specific phase. Each addresses a distinct need that can arise throughout the product lifecycle.

---

## Skills overview

| Skill | When to run |
|---|---|
| [pm-prototype](pm-prototype.md) | Before any build commitment - validate a feature, initiative, or product slice |
| [pm-stress-test](pm-stress-test.md) | Before any room where you'll be challenged |
| [pm-root-cause](pm-root-cause.md) | When a live metric behaves unexpectedly |
| [pm-audit](pm-audit.md) | After research injection, re-prioritization, reconcile/extract, or before a build commitment or pitch |
| [pm-meeting](pm-meeting.md) | After any meeting with notes or a transcript |
| [pm-onboarding](pm-onboarding.md) | When a new team member joins |
| [pm-diagrams](pm-diagrams.md) | When a visual diagram is needed |
| [pm-glossary](pm-glossary.md) | Start early, update whenever new terminology surfaces |
| [pm-stripe](pm-stripe.md) | Orchestrating and monitoring the JIT delivery cycle |

---

## pm-prototype

**When to use:** before committing to build - to validate a feature, a PRD initiative, or a product slice with real users.

Runs an intent gate first: is a prototype worth it, or go straight to build? If yes, it ingests ACs / flows / process maps / Feature Card / persona / brain dump and compiles a **tool-ready build prompt** with the Lovable Prompting Bible baked in:
- Front-load + book-end structure
- Mandatory in/out-of-scope fence
- Explicit stack declaration
- Flow narrative
- Plan-first instruction
- Fidelity calibration

Targets **Lovable / v0 / Figma Make** via MCP (user picks per run; multiple endpoints configurable in `pureinn-variables.md`) or produces a paste-ready block.

Writes a prototype reference back into the Feature Card. On re-run (result mode) captures the verdict and cascades to the hypothesis register.

**Agent mode:** `never` - the value is the live dialogue.

---

## pm-stress-test

**When to use:** before any room where you'll be challenged - exec/product-council review, investor pitch, board meeting, budget defense, security/legal review, contentious feature push.

Adversarial pushback simulator. You paste the proposal/decision/view; the skill plays a specific skeptical stakeholder and attacks it in **multiple rounds**, in that persona's real voice.

Built-in capabilities:
- **15 stakeholder profiles** - investor, CFO, board, CTO, CPO, CRO, legal, compliance, security, DPO, COO, user advocate, procurement, and more
- **Challenge-question bank** across 13 dimensions
- **12 adversarial methods** - pre-mortem, red team, murder board, 5 Whys, falsification, outside-view, and more
- **Real-room bars** - VC due diligence, board review, stage-gate, CFO, GDPR/EU AI Act, GTM, pricing
- **12-item weakness catalogue**

Process: runs a silent weakness diagnosis first, then attacks in rounds, ends with a prep summary - held / thin / unresolved blind spots / robustness score / pre-meeting checklist.

Two modes: **live iterative rehearsal** (back-and-forth) or **one-pass written gauntlet**.

Does not fabricate your facts - it challenges the gaps.

**Agent mode:** `never` - the value is the live adversarial dialogue.

---

## pm-root-cause

**When to use:** when a live metric behaves unexpectedly - a metric dropped, churn spiked, feature not adopted, conversion fell, tickets rising.

In-flight diagnostic engine (distinct from `pm-problem-validation` which is foundational, and `pm-stress-test` which is adversarial).

Structured flow:
1. Is it real or a measurement artifact?
2. Localize (segment / funnel / version)
3. What changed?
4. Candidate causes across categories
5. 5-Whys to an actionable root cause
6. Separate evidence from guess
7. Cheapest confirmation test

Built-in capabilities:
- **11 diagnostic methods** with a selection guide - 5 Whys, Ishikawa, issue tree/MECE, change analysis, cohort/segmentation, funnel, Pareto, fault tree, DMAIC, Kepner-Tregoe, correlation-vs-causation/Simpson
- **12-anomaly candidate-cause differential library** - cause · category · data signature · fastest test · frequency
- **Measurement-trap catalogue**
- **12-item bias catalogue**
- **Pre-acceptance validation checklist**

Hard rules: don't stop at the first plausible cause; correlation ≠ causation; symptom ≠ root cause.

Two modes: **guided investigation** or **quick differential**.

Ends with testable hypotheses that feed `pm-hypotheses`.

**Agent mode:** `never` - the value is the live diagnostic dialogue.

---

## pm-audit

**When to use:** after research injection or re-prioritization, after reconcile/extract, or before a build commitment or pitch.

Two tiers:

**Tier 1 - Form check:** scans Pureinn artifacts against current conventions, fixes naming drift and metadata errors, migrates older-version workspaces to the current schema.

**Tier 2 - Strategic consistency:** cross-checks PRD ↔ personas ↔ roadmap ↔ market ↔ business model ↔ feature phases. Surfaces contradictions read-only and routes each fix to its authoring skill (which re-runs in delta mode).

```bash
/pm-audit              # both tiers
/pm-audit strategy     # Tier 2 only
```

**Agent mode:** `synthesis` - runs fully autonomously.

---

## pm-meeting

**When to use:** after any meeting with notes or a transcript.

Detects meeting type and applies the right summary template. Tags action items by destination: Notion Task / Feature Card / follow-up meeting / Pureinn skill. Pushes to Notion Meetings DB with linked tasks.

**Agent mode:** `synthesis` - runs fully autonomously from the transcript.

---

## pm-onboarding

**When to use:** when a new team member joins.

Reads the existing workspace and generates a role-specific Onboarding Brief:
- Product context (what we're building, why, for whom)
- Settled decisions (what is not up for debate)
- Artifact map (where things live, what each document means)
- Current delivery state (what's in each Stripe, what's being built)
- Who to ask about what

Roles: Developer, PM, Designer, Stakeholder.

**Skip if:** solo builder (no team to onboard).

**Agent mode:** `synthesis` - runs fully autonomously from the workspace.

---

## pm-diagrams

**When to use:** when a visual diagram is needed to communicate architecture, user flow, domain model, or JTBD forces.

Generates Mermaid.js diagrams. Types supported:
- User Flow diagrams
- Architecture diagrams
- JTBD Forces Diagram
- ERD (Entity-Relationship Diagram)
- Sequence diagrams (also generated within `pm-feature-design`)

**Agent mode:** `synthesis`.

---

## pm-glossary

**When to use:** start early (Phase 1 or 4), update continuously as new domain terminology surfaces.

Maintains a consistent domain glossary. New terms added JIT when they surface in any artifact. Prevents terminology drift across the team and between documents.

During Rebuild (A1 Reconcile), the glossary captures entity name aliases - the old name from legacy docs mapped to the canonical name from code.

**Agent mode:** `synthesis`.

---

## pm-stripe

**When to use:** orchestrating and monitoring the JIT delivery cycle across all active Delivery Stripes.

Provides a delivery dashboard: feature status per stripe, dependency graph, what's blocked, what's next. Drives the Feature Card lifecycle transitions (Design Inspection → 3_Ready_to_Build, Code Inspection → 6_Shipped).

**Agent mode:** `synthesis`.
