# Phase 5 - Feature Planning

Build the complete feature inventory, prioritize it, define the MVP scope, and assign features to Delivery Stripes. This phase closes the planning work and opens the door to the JIT build cycle.

**Duration:** 2-3 days · **Gate type:** Soft gate · **Playbooks:** Greenfield, Feature Implementation

---

## How to read this page

Four steps, run in this order the first time. `pm-prioritize` and `pm-mvp-scope` are also **re-runnable** later, whenever priorities shift - they don't have to wait for a full phase re-entry.

---

## When to enter this phase

Enter after Phase 4 (domain registers initialized). For Feature Implementation adding new features to an existing product, you may enter directly with `pm-features-list` if the registers already exist.

**What you need before entering:** `entities.md` (Register 1) must exist, `business_rules.md` (Register 2) at least in Draft, and a frozen PRD (Greenfield) or equivalent product context.

---

## Step 1 - Feature Inventory (R4)

- **When to run / skip:** always run - this is the phase's foundational artifact.
- **Gather first:** frozen PRD's Business Capabilities, Registers 1-2.
- **Command:** `/pm-features-list`
- **What you get:** `feature_list.md` (Register 4) - every feature gets a `FEAT-[DOMAIN]-[NUMBER]` ID, a Feature Set grouping (`FS-NN: name`), a KANO class (Must-be/Performance/Delighter/Indifferent - tells you *what* enters MVP), a V×C class (Quick Win/Big Bet/Fill-in/Time Waster - tells you *what order* features enter Delivery Stripes), plus a stub Feature Card at `features/cards/FEAT-[DOMAIN]-001.md` (status `1_Backlog`) and a Notion push.
- **What it does NOT give you:** a priority order across features - KANO and V×C classify, they don't sequence. That's Step 2.
- **Done when:** every feature from the PRD has a FEAT-ID, KANO class, and V×C class.

---

## Step 2 - Prioritization

- **When to run / skip:** run after Step 1, and **re-run any time** priorities shift (new features added, roadmap changed, a deadline appeared). Non-destructive - previous assignments are preserved and the delta is shown.
- **Gather first:** feature inventory (Step 1) and whichever basis applies:

| Basis | When to use |
|---|---|
| Roadmap | Align delivery order with roadmap phases |
| Directive | External constraint (deadline, regulatory, partner requirement) |
| Lens | Apply a specific thinking lens (user value, technical risk, revenue impact) |
| Propose | AI proposes order with rationale - you review and adjust |

- **Command:** `/pm-prioritize`
- **What you get:** an updated priority order in `feature_list.md`, dependency-reconciled.
- **What it does NOT give you:** MVP scope decisions (IN/POST-MVP/CUT) - that's Step 3. Priority order and MVP membership are different questions.
- **Done when:** every feature has a priority order consistent with its dependencies.

---

## Step 3 - MVP Scope + Delivery Stripes

- **When to run / skip:** always run after Step 2.
- **Gather first:** prioritized feature inventory (Step 2).
- **Command:** `/pm-mvp-scope`
- **What you get:** a scope decision per feature:

| Decision | Meaning |
|---|---|
| **IN** | In MVP scope - required for launch |
| **POST-MVP** | Not in MVP, but in V1.1 or later |
| **CUT** | Not planned - deferred indefinitely or dropped |

Plus Delivery Stripe assignment - parallel domain-focused development channels (e.g. `stripe-auth`, `stripe-checkout`, `stripe-reporting`). One feature is active per stripe at a time, processed in dependency order.

- **What it does NOT give you:** the feature spec itself - stripes and scope only decide *what* and *when*, not the design. That's Phase 6.
- **Done when:** every IN-scope feature has a Stripe assignment and a position in that Stripe's queue.

---

## Step 4 - Product Roadmap (v3)

- **When to run / skip:** always run, closing this phase.
- **Gather first:** MVP Scope + Delivery Stripes (Step 3).
- **Command:** `/pm-product-roadmap`
- **What you get:** Product Roadmap v3 - the final planning-phase roadmap, with full feature and delivery view.
- **What it does NOT give you:** anything beyond planning - from here, roadmap changes come from Impact Analysis in Phase 6-7, not a phase re-run.
- **Done when:** the roadmap reflects the actual Stripe queues, not a pre-planning estimate.

---

## What you exit with

- **feature_list.md** (Register 4) - complete feature inventory with FEAT-IDs, KANO, V×C, priorities
- **Stub Feature Cards** - one per feature at `features/cards/` with status `1_Backlog`
- **MVP Scope** - explicit IN / POST-MVP / CUT decisions
- **Delivery Stripes** - parallel build channels with feature assignments
- **Product Roadmap v3** - final planning-phase roadmap

---

## Phase exit gate

Run `/pureinn` to check the Phase 5 exit gate and advance to Phase 6.

**Gate type: Soft.** Requires: `feature_list.md` with FEAT-IDs, MVP scope defined, Delivery Stripes assigned. Missing items named - you can proceed acknowledging gaps.

After Phase 5, run `/common-ground` (from fullstack-dev-skills plugin) for the tech stack decision before entering the JIT build cycle.
