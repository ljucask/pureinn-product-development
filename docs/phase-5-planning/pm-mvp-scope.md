# pm-mvp-scope

> Phase 5 exit - MVP scope decision and Delivery Stripe assignment per feature

**Phase:** 5 - Planning (exit artifact)  
**Agent mode:** `decision` - drafts, then requires your review  
**Version:** 2.2.0  
**Triggers:** MVP scope, delivery stripes, MVP cut, feature prioritization, stripe assignment, workbench prototype phases, Phase 5

---

## When to use

Phase 5, after `pm-features-list` is approved and (optionally) `pm-prioritize` has run. This is the Phase 5 exit artifact. `pm-stripe` uses the output of this skill to orchestrate the JIT build cycle.

---

## What it produces

Two updates to existing artifacts (not new files):

1. **`phase` field per feature** in `feature_list.md` and each Feature Card frontmatter:
   - `MVP` (or project's first phase label, e.g. `P0`) = in scope for MVP
   - `MVP+` or later phase = post-MVP
   - Removed from list = cut

2. **`stripe` field per feature** in `feature_list.md` and each Feature Card frontmatter:
   - Assigns each feature to a Delivery Stripe (parallel development channel)
   - Example: `stripe-checkout`, `stripe-auth`, `stripe-notifications`
   - Stripe = domain-coherent delivery channel; one feature active per stripe at a time

After user approval: updates Notion Feature entries with `phase` and `stripe` values.

---

## How to invoke

```bash
/pm-mvp-scope           # interactive
/pm-mvp-scope --agent   # autonomous draft, requires review before finalizing
```

---

## The `phase` field is the single source of truth for MVP membership

**Never use a separate `mvp: true/false` flag.** MVP membership is recorded in `phase`. Two fields on the same axis drift apart.

| Value | Meaning |
|---|---|
| `MVP` (or project's P0/Phase 1) | In scope for MVP |
| `MVP+` (or Phase 2, Phase 3...) | Post-MVP |
| Feature removed | Cut - not building |

---

## Delivery Stripes

Stripes are parallel domain-focused development channels. Each stripe operates independently - one feature active per stripe at a time, progressing through the JIT cycle.

**Stripe assignment rules:**
- Features in one stripe must belong to a coherent domain slice
- A feature cannot be assigned to a stripe where one of its dependencies is in a different stripe still in progress
- Cross-stripe dependencies are surfaced as risks before finalizing assignment

**How stripes work in Phase 6:** `pm-stripe` orchestrates the JIT cycle per stripe - picking the next ready feature and routing it through `pm-feature-design` → build → review → shipped. See [docs/phase-6-build/pm-stripe.md](../phase-6-build/pm-stripe.md).

---

## When features already carry a `phase` (Rebuild)

If features already carry phase assignments from `pm-product-roadmap` (e.g., a Rebuild where roadmap split into P0 Pilot / P1 / P2):
- The MVP cut is already decided - do NOT re-litigate IN/POST
- This skill's job is only **stripe assignment**
- Confirm the phase-derived cut with the user, then assign stripes

---

## When a workbench prototype already made the cut

A prototype folder under `prototypes/` whose `meta.md` says `Purpose: workbench` was built wider than the MVP and then cut down by roadmap phase, so its `feature-plan-prt.md` already carries a phase per built feature. The skill detects it in the state check and reads that split as the **proposal** instead of deriving a cut from KANO/V×C from scratch.

| Feature is | Phase is read from | What happens |
|---|---|---|
| Promoted (Feature Card with `promoted_from:`) | Feature Card and `feature_list.md` | Phase read, stripe assigned |
| Still `PRT-`, built, phase set | `feature-plan-prt.md` | Shown as the proposed IN / later split; no stripe yet |
| Still `PRT-`, built, no phase | - | Undecided - routed to `/pm-prototype`, not placed here |
| `next` / `cut` in the plan | `feature-plan-prt.md` | Carried into Post-MVP / Cut with the recorded reason |
| No prototype counterpart | - | The normal cut |

- **Offered, not imposed** - the split is shown with the folder it came from and you confirm or change it.
- **Promotion does not happen here.** `PRT-` features become Feature Cards with real `FEAT-` IDs through `/pm-prototype`, phase by phase. A `PRT-` ID is never written into `feature_list.md`, a card, or a stripe; unpromoted first-phase features are listed as awaiting promotion and get their stripe on the re-run.
- **Matched by reference** (`promoted_from:` or the prototype's `targets`), never by a similar name.
- A workbench split is stakeholder alignment, not user evidence - the capacity check against team size and timeline still runs.

---

## Dependencies

**Required before running:**
- `pm-features-list` - must include Dependency Map, KANO Analysis, and V×C Matrix (all approved)

**Recommended:**
- `pm-prototype` (workbench) - if the MVP was cut down in a workbench prototype, its feature plan is the proposed phase split
- `pm-prioritize` - recommended to run before MVP scope if priority order has been updated
- `pm-kpis` - North Star and AARRR metrics validate MVP scope alignment
- `pm-business-case` - revenue model and runway inform how aggressive the MVP cut should be

**Produces for:**
- `features/feature_list.md` - `phase` and `stripe` updated per feature
- `/features/cards/FEAT-*.md` - `phase` and `stripe` fields updated in each Feature Card
- `pm-product-roadmap` (v3) - delivery view populated with stripe and phase data
- `pm-stripe` - uses stripe assignments to orchestrate the JIT cycle per stripe

**Related skills:** `pm-features-list`, `pm-prioritize`, `pm-product-roadmap`, `pm-stripe`, `pm-entity-registry`, `pm-prototype`
