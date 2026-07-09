# pm-prioritize

> Re-runnable backlog prioritization engine - any basis, dependency-reconciled, non-destructive

**Phase:** 5 (initial); re-runnable at any point  
**Agent mode:** `decision` - drafts, then requires your review  
**Version:** 1.0.0  
**Triggers:** prioritize, prioritization, reprioritize, re-order features, feature priority, backlog order, what to build first, sequence features

---

## When to use

Whenever the feature order needs to change. Can run after the feature list is created, after the MVP cut, or any time priorities shift (new market signal, investor input, strategy change, a fresh roadmap). This is the canonical prioritization engine - `pm-features-list` uses it for first-time scoring; you re-run it standalone thereafter.

---

## What it produces

Updated **Priority column + explicit sequence** in `features/feature_list.md`:

- Priority bands: P1 / P2 / P3 per feature
- Explicit delivery order within each band
- Rationale per placement (traceable to the chosen basis)
- Optional: Delivery Stripe re-assignment suggestions if order change affects stripes

A logged prioritization entry is added: date + basis used + rationale summary.

---

## How to invoke

```bash
/pm-prioritize           # interactive
/pm-prioritize --agent   # autonomous prioritization, requires review before writing
```

---

## Four prioritization bases

At Step 0, the skill offers a basis selection (uses AskUserQuestion - never auto-imposes):

| Basis | When to use |
|---|---|
| **Align to roadmap** | A roadmap with defined phases exists - re-order features to match phase decomposition |
| **Follow my directive** | You state what matters most ("payments first", "revenue first", "reduce churn") - skill maps it to features |
| **Apply a lens** | Value-first (KANO + business impact) / Quick-wins (V×C) / Risk-reduction / Unblock-dependencies |
| **You decide and propose** | Skill analyses backlog and recommends a basis with reasoning; user confirms before applying |

---

## Dependency reconciliation (hard constraint)

After applying the chosen basis, the skill reconciles against the Dependency Map before writing:

- A feature can never rank ahead of a feature it depends on
- If the chosen basis would create such a conflict, the blocker is pulled forward
- Every conflict is surfaced explicitly: which feature was moved and why

---

## Non-destructive

This skill does NOT:
- Change the feature inventory (add/remove/rename features) - that is `pm-features-list`
- Make the MVP IN/POST/CUT decision - that is `pm-mvp-scope`
- Overwrite KANO/V×C scores - it re-sequences on top of them

The current KANO/V×C scores remain intact after every re-run.

---

## Relationship to other prioritization touchpoints

| Skill | Role |
|---|---|
| `pm-features-list` | Creates inventory + Dependency Map; offers first-time prioritization |
| **pm-prioritize** | Re-runnable prioritization - any basis, any time |
| `pm-mvp-scope` | Consumes the prioritized order to make MVP cut + stripe assignment |
| `pm-stripe` | Processes features in dependency order within each stripe |

---

## Dependencies

**Required before running:**
- `pm-features-list` - `feature_list.md` must exist with a Dependency Map

**Recommended:**
- `pm-product-roadmap` - roadmap phases inform the "align to roadmap" basis
- `pm-feature-viability` - viability assessments may override priority

**Produces for:**
- `pm-mvp-scope` - updated priority order is the input for MVP cut
- `pm-stripe` - stripe-level sequence follows from priority order

**Related skills:** `pm-features-list`, `pm-mvp-scope`, `pm-product-roadmap`, `pm-stripe`, `pm-feature-viability`
