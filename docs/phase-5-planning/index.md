# Phase 5 - Feature Planning

Build the complete feature inventory, prioritize it, define the MVP scope, and assign features to Delivery Stripes. This phase closes the planning work and opens the door to the JIT build cycle.

**Duration:** 2-3 days  
**Gate type:** Soft gate  
**Playbooks:** Greenfield, Feature Implementation

---

## When to enter this phase

Enter Phase 5 after Phase 4 (domain registers initialized). For Feature Implementation adding new features to an existing product, you may enter directly with `pm-features-list` if the registers already exist.

---

## What you need before entering

- `entities.md` (Register 1) - entity list must exist
- `business_rules.md` (Register 2) - at least Draft
- Frozen PRD (for Greenfield) or equivalent product context

---

## Skills in this phase

| Skill | What it does | Output |
|---|---|---|
| [pm-features-list](pm-features-list.md) | Builds the complete feature inventory with FEAT-IDs, KANO classification, V×C matrix, Feature Set grouping, and stub Feature Cards | `feature_list.md` (Register 4) + stub Feature Cards |
| [pm-prioritize](pm-prioritize.md) | Re-runnable prioritization engine - ranks the backlog by roadmap, directive, lens, or AI proposal. Dependency-reconciled, non-destructive. | Updated priority order in `feature_list.md` |
| [pm-mvp-scope](pm-mvp-scope.md) | Defines MVP scope (IN / POST-MVP / CUT), Delivery Stripes, and Feature-to-Stripe assignment | MVP Scope + `delivery-stripes.md` |
| [pm-product-roadmap](pm-product-roadmap.md) | Phase 5 update: roadmap with full feature and delivery view | Product Roadmap v3 |

**Order:**
```
pm-features-list → pm-prioritize → pm-mvp-scope → pm-product-roadmap (v3)
```

---

## pm-features-list: what it produces

The master feature inventory (Register 4). For each feature:

- **FEAT-ID** (`FEAT-[DOMAIN]-[NUMBER]`) - stable identifier referenced by Feature Cards and Notion
- **Feature Set assignment** (`FS-NN: name`) - logical domain grouping
- **KANO classification** - Must-be / Performance / Delighter / Indifferent
- **V×C classification** - Quick Win / Big Bet / Fill-in / Time Waster
- **Stub Feature Card** created at `features/cards/FEAT-[DOMAIN]-001.md` (status: 1_Backlog)
- **Notion push** - features pushed to Notion with Status = Backlog, Priority from KANO+V×C

KANO tells you *what* enters the MVP. V×C tells you *in what order* features enter Delivery Stripes.

---

## pm-prioritize: re-runnable engine

Prioritization is not a one-time event. `pm-prioritize` can be re-run any time priorities shift:

| Basis | When to use |
|---|---|
| Roadmap | Align delivery order with roadmap phases |
| Directive | External constraint (deadline, regulatory, partner requirement) |
| Lens | Apply a specific thinking lens (user value, technical risk, revenue impact) |
| Propose | AI proposes order with rationale - you review and adjust |

Non-destructive: previous priority assignments are preserved and delta is shown explicitly.

---

## pm-mvp-scope: MVP vs. POST-MVP vs. CUT

`pm-mvp-scope` makes three calls per feature:

| Decision | Meaning |
|---|---|
| **IN** | In MVP scope - required for launch |
| **POST-MVP** | Not in MVP, but in V1.1 or later |
| **CUT** | Not planned - either deferred indefinitely or dropped |

After scope decisions, features are assigned to **Delivery Stripes** - parallel domain-focused development channels. Example: stripe-auth, stripe-checkout, stripe-reporting.

One feature is active per stripe at a time, processed in dependency order.

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
