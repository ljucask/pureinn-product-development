# Pureinn Documentation

Pureinn is an AI-native product development framework for Claude Code. It covers the full product lifecycle - from the first idea to a shipped product - through 50 skills and a structured three-playbook engine.

---

## Install

```bash
/plugin marketplace add ljucask/pureinn-product-development
/plugin install pureinn-product-development@pureinn-product-development
```

Select **user scope** to make it available across all projects.

---

## Quick start

```bash
/pureinn "your product idea"
```

The engine scans your workspace, asks 9 intake questions, selects the right playbook, and presents an ordered skill queue. Run skills one at a time. Run `/pureinn` again after each phase to check the exit gate and advance.

```bash
/pureinn-resume [project-slug]    # resume a paused project (omit slug to list all)
/pureinn map                      # full framework overview - all playbooks, phases, skills
```

---

## Three playbooks

| Playbook | Use when |
|---|---|
| [Greenfield](playbook-greenfield.md) | New product, zero users, validating PMF |
| [Feature Implementation](playbook-feature.md) | Product exists, active users, adding new functionality |
| [Rebuild](playbook-rebuild.md) | Onboarding an existing product into Pureinn (legacy docs or clean) |

Run `/pureinn [product idea]` and the engine routes you automatically.

---

## Fast tracks

Skip phases you don't need.

**Greenfield Express** - validated idea, skip discovery:
```bash
/pureinn "your idea"          # workspace setup
/pm-entity-registry           # lean entity list
/pm-business-rules-library    # core rules, Draft mode
/pm-features-list             # feature inventory + FEAT-IDs
/pm-mvp-scope                 # MVP scope + Delivery Stripes
/pm-feature-design [ID]       # JIT spec per feature → build
```

**Feature Implementation - first run** on an existing codebase:
```bash
/pureinn [project]            # workspace setup
/common-ground                # tech context from existing code
/pm-reverse-extract           # bootstrap registers + feature inventory from codebase
/pm-feature-design [ID]       # JIT spec → build
```

---

## Stage shortcuts

Jump straight into one part of the framework:

```bash
/pureinn define                        # current project → Commercial Definition
/pureinn acme model                    # named project → Domain Modeling
/pureinn discover "food delivery app"  # fresh project → Discovery
```

| Keyword | Enters | You exit with |
|---|---|---|
| `setup` | Phase 1 - Foundation | Project skeleton |
| `discover` | Phase 2 - Discovery | Market / personas / JTBD / domain understanding |
| `validate` | Phase 3a - Validation | Go/No-Go verdict |
| `define` | Phase 3b - Commercial Definition | Value prop, business model, KPIs, PRD |
| `model` | Phase 4 - Domain Modeling | Entities, rules, flows blueprint |
| `plan` | Phase 5 - Feature Planning | Feature list, KANO/V×C, MVP scope |
| `build` | Phase 6+7 - JIT Delivery | Per-feature spec + delivery |

For a single artifact, run its skill directly - no stage keyword needed.

---

## Agent mode

Any skill accepts `--agent`. Instead of running interactively, the skill drafts the artifact autonomously from existing inputs and returns a short summary for your review.

```bash
/pm-prd --agent
/pm-market-analysis --agent
```

Missing inputs are never invented - they're marked `[ASSUMED]`. No flag = interactive (default). See [how it works](how-it-works.md#agent-mode).

---

## Framework phases

| Phase | What happens | Duration |
|---|---|---|
| [Phase 1 - Foundation](phase-1-foundation/index.md) | Project charter, team, stakeholders | ~1 day |
| [Phase 2 - Discovery](phase-2-discovery/index.md) | Market, tech, domain, customer research | 1-3 weeks |
| [Phase 3a - Validation](phase-3a-validation/index.md) | Hypothesis testing, Go/No-Go verdict | Externally paced |
| [Phase 3b - Commercial Definition](phase-3b-definition/index.md) | Business model, KPIs, PRD | Hours to a few sessions |
| [Phase 4 - Domain Modeling](phase-4-domain/index.md) | Entities, business rules, process flows | 3-5 days |
| [Phase 5 - Feature Planning](phase-5-planning/index.md) | Feature list, prioritization, MVP scope | 2-3 days |
| [Phase 6+7 - JIT Delivery](phase-6-build/index.md) | Per-feature spec + build cycle | Ongoing |
| [Cross-phase skills](cross-phase/index.md) | Prototype, stress-test, root-cause, audit, meeting, onboarding, diagrams, glossary, stripe | Any time |
| [Rebuild](rebuild/index.md) | Onboarding an existing product | Varies |

---

## Cross-phase skills at a glance

Skills that run at any point in any playbook - not tied to a phase:

| Skill | When to use |
|---|---|
| `/pm-prototype` | Before any build commitment - compile a tool-ready prompt for Lovable / v0 / Figma Make |
| `/pm-stress-test` | Before exec reviews, investor pitches, board meetings, or any room where you'll be challenged |
| `/pm-root-cause` | When a live metric drops, churn spikes, or a feature isn't being adopted |
| `/pm-audit` | After research injection, re-prioritization, or before a build commitment or pitch |
| `/pm-meeting` | After any meeting - generates structured summary + action items, pushes to Notion |
| `/pm-onboarding` | When a new team member joins - generates a role-specific onboarding brief |
| `/pm-diagrams` | When a visual is needed (user flow, architecture, ERD, JTBD forces) |
| `/pm-glossary` | Start early, update whenever new domain terminology surfaces |
| `/pm-stripe` | Orchestrate and monitor the JIT delivery cycle across all active Delivery Stripes |
