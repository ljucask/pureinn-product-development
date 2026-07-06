---
name: pm-prioritize
description: Re-runnable prioritization engine for the feature backlog. Works at ANY point - after the feature list is created, after the MVP cut, or any time later when priorities shift. Takes flexible input - align to a roadmap, follow a directive you give ("X first", "revenue first"), apply a prioritization lens, or let the skill propose a basis with reasoning. Always reconciles with the dependency map (cannot rank a feature ahead of its blocker), is non-destructive (proposes, you confirm before it writes), and explains the rationale and trade-offs. The canonical prioritization logic that pm-features-list offers for the first-time scoring.
license: MIT
metadata:
  agent-mode: decision
  author: https://github.com/ljucask
  version: "1.0.0"
  domain: product-management
  triggers: prioritize, prioritization, reprioritize, re-order features, feature priority, backlog order, what to build first, sequence features
  role: specialist
  scope: planning
  output-format: document
  related-skills: pm-features-list, pm-mvp-scope, pm-product-roadmap, pm-stripe, pm-feature-viability
---

# PM - Prioritize (Backlog Prioritization Engine)


## Agent mode (`--agent`)

Supports `--agent`: runs autonomously in a subagent, drafts the artifact from existing inputs, and returns a short summary + coverage note.

- **No flag** → interactive (default); if inputs are heavy, offer agent mode.
- **`--agent`** → obey. First check inputs are complete. Anything missing: do NOT invent it - mark `[ASSUMED - what/why]` in the output and summary. Never hallucinate to fill a gap.
- **Review required:** the artifact contains commitments - after drafting, require the user's review before finalizing; do not close decisions autonomously.

---

## What this skill does

Prioritizes (or re-prioritizes) the feature backlog at **any point in the lifecycle**, on a basis you choose or one it proposes. It is the canonical prioritization engine - `pm-features-list` offers it for the first-time scoring, and you re-run it standalone whenever priorities shift (new market signal, investor input, strategy change, a fresh roadmap).

It is deliberately **agile, not waterfall** (per the Adaptive-execution standard in CLAUDE.md): it does not auto-impose a default order - it **offers** a basis (and proposes one with reasoning when you are unsure), reconciles against dependencies, shows the rationale and trade-offs, and only writes after you confirm. Re-running it iterates the order; it never destroys the KANO/V×C scores or the feature data.

**Produces:** an updated priority / sequence on `features/feature_list.md` (Priority column + explicit order), optional Delivery-Stripe re-assignment suggestions, and a logged prioritization entry (date + basis + rationale).

---

## Relationship to the other prioritization touchpoints

| Skill | Role |
|---|---|
| `pm-features-list` | Creates the inventory + Dependency Map; **offers** the first-time prioritization (this engine's basis-selection), with KANO + V×C as the default lens |
| **pm-prioritize** | The re-runnable engine - apply any basis at any time, dependency-reconciled, explainable |
| `pm-mvp-scope` | Uses the prioritized order to make the IN/POST/CUT cut + stripe assignment |
| `pm-stripe` | Processes features in dependency order within each stripe |

KANO and V×C are prioritization **methods** (lenses) this engine can apply - not separate steps. This skill orchestrates them alongside roadmap alignment, your directives, and dependency constraints.

---

## What this skill does NOT do

- Change the feature inventory (add/remove/rename features) - that is `pm-features-list`
- Make the MVP IN/POST/CUT decision - that is `pm-mvp-scope` (it consumes this order)
- Overwrite KANO/V×C scores - it re-sequences on top of them, non-destructively

---

## Dependencies

- `features/feature_list.md` exists (created by `pm-features-list` or `pm-reverse-extract`) with a Dependency Map.
- Optional inputs that strengthen the result: a roadmap (`pm-product-roadmap`), KANO/V×C scores, `pm-feature-viability` outputs.

If no feature list exists, route to `pm-features-list` first.

---

## Step 0: Current state check

Read `features/feature_list.md`: features, current Priority, the **Dependency Map / Critical Path**, KANO/V×C scores (if present), MVP flags and stripe assignments (if any). Note whether a roadmap exists and whether it has phases/functional decomposition.

Show a short state table (N features, has dependency map?, has KANO/V×C?, has roadmap?, current ordering basis if logged). **Interaction:** Group related questions (2-4 per round) and confirm before moving on. For any A/B/C/D choice, use the AskUserQuestion tool with one option marked **(Recommended)** - never print options as plain text. Keep open-ended questions free-text (don't fake options). If the user is unsure, propose 3-4 concrete options plus "Other". Surface an assumption the moment you make one; never fabricate to fill a gap. (Full standard: CLAUDE.md.)

---

## Step 1: Choose the basis (offer, don't impose)

Use AskUserQuestion - this is the core "offer, don't impose" moment:

- Question: "On what basis should I prioritize?"
  - Option A: "**Align to the roadmap**" - re-order features to match the roadmap's phases / functional decomposition (only offer if a roadmap exists; recommended when it does)
  - Option B: "**Follow my directive**" - you state it ("payments first", "reduce churn first", "fastest path to revenue"); I map it to features and order accordingly
  - Option C: "**Apply a lens**" - I order by a named method: Value-first (KANO + business impact) / Quick-wins (V×C) / Risk-reduction / Unblock-dependencies
  - Option D: "**You decide and propose**" - I analyse the backlog and recommend a basis, with the reasoning, then you confirm

**Proactive partner (Option D, or when the user is unsure / context is thin):** do not stall. Analyse what is available (KANO/V×C spread, dependency clusters, roadmap phases, stated goals) and **propose 2-3 concrete candidate bases with a recommended one and the why** - e.g. "Your dependency map has a long critical path through Payments, and most P1s sit there - I recommend Unblock-dependencies first, then Value. Agree, or pick another?" Always include an "Other / I'll describe" path.

If Option B (directive): capture it as free text, then restate how you interpreted it before applying ("'revenue first' → I'll rank features that directly enable a paid transaction highest - correct?").

---

## Step 2: Apply the basis + reconcile dependencies

Apply the chosen basis to produce a ranked order. Then **reconcile against the Dependency Map - this is a hard constraint:**

- A feature can never rank ahead of a feature it depends on. If the chosen basis would do that, the blocker is pulled forward and the conflict is surfaced.
- Flag every conflict explicitly: *"You ranked FEAT-X high, but it depends on FEAT-Y (currently P3) - Y must come first, or be re-prioritized too."*
- Where the basis is silent (ties), break by dependency depth, then by V×C, then by KANO.

Map the resulting order onto Priority bands (P1/P2/P3) and an explicit sequence.

---

## Step 3: Present + confirm (non-destructive)

Show the proposed prioritization before writing anything:

```
PROPOSED PRIORITIZATION - basis: [chosen basis]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Order  FEAT-ID         Feature                 Priority  Why (per basis)
 1     FEAT-PAY-001    [Validate card payment]  P1       blocker for checkout; revenue-critical
 2     FEAT-ORD-001    [Create draft order]     P1       ...
 ...

DEPENDENCY CONFLICTS RESOLVED
  - FEAT-X pulled ahead of FEAT-Z to respect dependency

TRADE-OFFS
  - This basis defers [feature] - acceptable? (it was P1 under the previous basis)

CHANGES FROM CURRENT ORDER
  - [N features moved up, M moved down]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Use AskUserQuestion: "Apply this prioritization, adjust, or try a different basis?" Iterate until confirmed. Nothing is written until the user confirms.

---

## Step 4: Write + log

On confirmation:
- Update the **Priority** column and the **order** in `features/feature_list.md`.
- If features are in delivery, surface (do not auto-apply) suggested **Delivery-Stripe** re-assignments where the new order crosses stripe boundaries - the user confirms stripe moves.
- Append a **Prioritization log** entry to `feature_list.md`: `| [date] | [basis] | [one-line rationale] | [N features re-ranked] |`.

KANO/V×C scores and feature data are left intact - only Priority/order changes.

---

## Save to

```
pureinn-workspace/[project-slug]/features/feature_list.md   (Priority + order updated, prioritization log appended)
```

---

## Handoff

**Čo si teraz má:** Backlog prioritizovaný na zvolenom základe, zladený so závislosťami, s logom prečo. Nedeštruktívne - skóre a dáta features ostali.

**Ďalší krok:**
- Pred MVP: `/pm-mvp-scope` — spraví IN/POST/CUT cut na tomto poradí.
- Počas delivery: `/pm-stripe` — berie features v novom poradí per stripe.

**Môžeš preskočiť ak:** Poradie sa nezmenilo oproti aktuálnemu - reprioritizácia nepridáva hodnotu. Spusti znova kedykoľvek, keď sa priority posunú (nový signál, stratégia, roadmap).
