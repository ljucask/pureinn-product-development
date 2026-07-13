---
name: pm-mvp-scope
description: Define MVP scope and delivery plan from the prioritized FDD Feature List. Makes the IN/POST-MVP/CUT decision per feature (recorded in the single `phase` field, never a separate `mvp` flag), assigns each feature to a Delivery Stripe. Updates feature_list.md and Feature Card frontmatter (phase + stripe). If features already carry a phase (Rebuild where roadmap split phases), reads it instead of re-deciding the cut and only assigns stripes. After user approval, updates Notion Feature entries with phase and stripe assignment. Phase 5 exit artifact. Required input for pm-stripe JIT cycle.
license: MIT
metadata:
  agent-mode: decision
  author: https://github.com/ljucask
  version: "2.1.0"
  domain: product-management
  triggers: MVP scope, delivery stripes, MVP cut, feature prioritization, stripe assignment, Phase 5
  role: specialist
  scope: planning
  output-format: document
  related-skills: pm-features-list, pm-prioritize, pm-product-roadmap, pm-stripe, pm-entity-registry
---

# PM - MVP Scope


## Agent mode (`--agent`)

Supports `--agent`: runs autonomously in a subagent, drafts the artifact from existing inputs, and returns a short summary + coverage note.

- **No flag** → interactive (default); if inputs are heavy, offer agent mode.
- **`--agent`** → obey. First check inputs are complete. Anything missing: do NOT invent it - mark `[ASSUMED - what/why]` in the output and summary. Never hallucinate to fill a gap.
- **Review required:** the artifact contains commitments - after drafting, require the user's review before finalizing; do not close decisions autonomously.

---

## What this skill does

Phase 5 / Steps 4-5. Takes the prioritized, dependency-mapped FDD Feature List (Live Register 4, output of `pm-features-list`) and produces the delivery structure:

1. **MVP Scope Decision** - what is IN (MVP), what is POST-MVP, what is CUT. Decision is **per Feature** - not per Feature Set. Feature Sets are grouping only and do not affect the MVP cut. **MVP membership is recorded in the `phase` field, NOT a separate `mvp` boolean** - see the next section.
2. **Delivery Stripes** - parallel development tracks (not time-boxed sprints). Each stripe is an isolated channel for a coherent domain slice (e.g., stripe-checkout, stripe-auth). Features are assigned to stripes based on domain affinity and dependencies.
3. **Stripe assignment** - updates `stripe:` field in each Feature Card frontmatter and in feature_list.md.

After user approval: update Notion Feature entries with phase and stripe assignment.

### `phase` is the single axis for MVP membership - no separate `mvp` flag

The canonical Feature Card carries one field for this: **`phase`** (`MVP` / `MVP+` / `Phase 1` / … - or a project's own labels like `P0` / `P1`). MVP membership **is** the phase value: IN-MVP = `phase: MVP` (or the project's first/`P0` phase); POST-MVP = a later phase; CUT = removed / `What we are NOT building`. **Never write a separate `mvp: true/false` (or `roadmap_phase`) field** - that duplicates `phase` on the same axis and the two drift apart. One field, one source of truth.

**If features already carry a `phase` (a Rebuild where `/pm-product-roadmap` already split phases, e.g. P0 Pilot = MVP):** the cut is already decided - **read it, do not re-litigate IN/POST**. This skill's remaining job is then only **stripe assignment** (delivery channels + dependency order). Confirm the phase-derived cut with the user, then assign stripes.

This is the Phase 5 exit artifact. pm-stripe uses this structure to orchestrate the JIT cycle - picking the next ready feature in each stripe and routing to pm-feature-design + build.

---

## Dependencies

**Required before running:**
- `pm-features-list` - must include completed Dependency Map, KANO Analysis, and V×C Matrix
- All four artifacts from pm-features-list must be approved by user before running this skill

**Recommended before running:**
- `pm-kpis` - North Star and AARRR metrics validate MVP scope alignment
- `pm-business-case` - revenue model and runway inform how aggressive the MVP cut should be

**Produces artifacts used by:**
- `features/feature_list.md` - updated with `phase` and stripe per feature
- `/features/cards/FEAT-*.md` - `phase:` and `stripe:` fields updated in each stub Feature Card
- `pm-product-roadmap` v3 - delivery view populated
- `pm-stripe` - uses stripe assignments to orchestrate JIT cycle per feature
- Notion - Feature entries enriched with phase and stripe assignment

---

## Step 0: Current state check

Check for existing artifacts:
- MVP Scope decision (in feature_list.md MVP column)
- Delivery Stripe assignments (in feature_list.md and Feature Card frontmatter)

Also check: does `features/feature_list.md` exist with KANO and V×C? Stub Feature Cards created? This skill cannot run without them.

Look for: MVP scope that's too large (more than 3-4 months of work), no explicit out-of-scope list, features assigned to stripes that violate dependencies (blocked feature in Stripe 1, blocker in Stripe 2), domain boundary confusion across stripes (mixing unrelated domains in one stripe creates parallel conflict risk).

**Interaction:** Group related questions (2-4 per round) and confirm before moving on. For any A/B/C/D choice, use the AskUserQuestion tool with one option marked **(Recommended)** - never print options as plain text. Keep open-ended questions free-text (don't fake options). If the user is unsure, propose 3-4 concrete options plus "Other". Surface an assumption the moment you make one; never fabricate to fill a gap. (Full standard: CLAUDE.md.)

---

## Step 1: Gather inputs

Ask questions in 2 groups. Group 1 drives strategic alignment - Claude shows a preliminary MVP cut after it. Group 2 sets execution parameters.

---

### Group 1 of 2 - Strategic alignment

Ask as plain text:

What is the single most important thing the MVP must prove? Complete this sentence: "We will consider MVP successful if we prove that..." (e.g., "hosts will pay for automated property management", "users can complete a booking end-to-end without human intervention")

Are there any features that must be in MVP regardless of KANO/V×C scoring? Why are they non-negotiable? (technical dependency, contractual requirement, customer commitment, other)

Are there any features that must NOT be in MVP - explicitly excluded for technical, strategic, or resource reasons?

Then use AskUserQuestion tool:

What matters most for this MVP?

  A) User experience quality - the product must feel polished and intuitive from day one (Recommended if B2C or high-competition market)
  B) Revenue validation - proving people will pay, even if experience is rough
  C) Technical foundation - building the right architecture first, even if MVP is lean
  D) Speed to market - ship as fast as possible, iterate based on real feedback

After receiving Group 1 answers, Claude does the following before asking Group 2:

1. Read the KANO + V×C output from pm-features-list in context
2. Apply MVP hypothesis, non-negotiables, exclusions, and priority value to the feature list
3. Show a preliminary MVP cut with explicit trade-offs:

```
Based on your MVP hypothesis and priorities, here is my initial reading:

IN (recommended):
  - [feature] - [KANO: M / V×C: Quick Win] → why it's in
  - [feature] - [KANO: P / V×C: Big Bet] → worth the complexity because [reason]

BORDERLINE (discuss):
  - [feature] - [KANO/V×C score] → Trade-off: including this adds ~[X] to scope but [benefit]. Excluding means [cost/risk].

OUT (deferred):
  - [feature] - [reason: Delighter / Indifferent / too complex / explicit exclusion]

Override check:
  Any features in OUT that belong IN for reasons KANO/V×C doesn't capture?
  (customer commitment, competitive parity, sales dependency, personal priority)
```

Wait for response. Adjust the cut if needed - user's judgment overrides the framework's suggestion. Then proceed to Group 2.

---

### Group 2 of 2 - Execution parameters

Use AskUserQuestion tool for these two questions:

What is the approximate team size for development?

  A) Solo developer
  B) 2 developers
  C) 3-4 developers
  D) 5+ developers

What is the MVP timeline constraint?

  A) Hard deadline - specific date or event (describe)
  B) Runway-constrained - must launch before runway runs out (how many months?)
  C) Milestone-driven - launch when PMF signal is achieved, no fixed date
  D) No constraint - launch when it's ready

Then ask as plain text:

Are Notion Feature entries already created from pm-features-list? (yes / no - if yes, I'll update existing entries; if no, Notion update is skipped)

**Capacity reconciliation (run before finalizing - this is where most MVPs actually blow their timeline):** cross-check the Group 1 IN-list size against Group 2's team size and timeline constraint. Rough heuristic: a solo developer clears roughly 2-4 Quick-Win-sized features per week, less for Big Bets; scale with team size but apply a coordination discount (a 4-person team is not 4x a solo dev - closer to 2.5-3x once integration and review overhead is counted). If the IN-list divided by this rate exceeds the stated deadline or runway, say so explicitly and force a second cut pass before generating the artifact: "At [team size], this MVP list is ~[X] weeks of work against a [Y]-week constraint. Which gives: cut more features, extend timeline, or add capacity?" Do not generate an MVP Scope that is silently unrealistic against its own stated constraint - that is the single most common way MVPs slip.

After answers, show the finalized MVP scope proposal combining Group 1 alignment + Group 2 constraints. Ask for final confirmation before generating the full MVP Scope artifact with Feature Sets and Delivery Stripes.

---

## Step 2: Generate MVP Scope

---

### ARTIFACT 1: MVP Scope

```markdown
# MVP Scope - [Product Name]

> **Phase:** 5 - Feature Planning
> **Date:** [date]
> **MVP definition:** The minimum set of features that delivers the core value proposition
>                    to the primary persona and enables the first paying customers.

---

## MVP Definition

**What MVP must prove:** [Single hypothesis]

**Success signal:** [Specific, measurable - e.g., "20 paying customers, D30 retention > 40%, NPS > 30"]

**Primary persona served:** [Persona name from pm-personas]

---

## In MVP

| Feature | ID | KANO | V×C | Delivery Stripe |
|---|---|---|---|---|
| [Feature name] | FEAT-[DOMAIN]-001 | Must-be | Quick Win | Stripe 1 |
| [Feature name] | FEAT-[DOMAIN]-011 | Must-be | Big Bet | Stripe 2 |

**MVP total:** [X] features across [Y] stripes ([Z] weeks)

---

## Post-MVP

| Feature | ID | KANO | Reason deferred | Target phase |
|---|---|---|---|---|
| [Feature name] | FEAT-[DOMAIN]-006 | Performance | Not blocking core value | MVP+ |
| [Feature name] | FEAT-[DOMAIN]-040 | Performance | Nice-to-have | Phase 2 |

---

## Cut (Not building)

| Feature | ID | Reason |
|---|---|---|
| [Feature name] | F-050 | Indifferent per KANO - no customer asked for it |
```

---

---

## Step 3: Generate Delivery Stripes + Stripe Assignment

---

### ARTIFACT 2: Delivery Stripes

```markdown
# Delivery Stripes - [Product Name]

> **Phase:** 5 - Feature Planning
> **Date:** [date]
> **Definition:** A Delivery Stripe is an isolated development channel for a coherent domain slice.
>                MVP cut and stripe assignment are per Feature - not per Feature Set.
>                Feature Sets are grouping only. JIT design and build operate at Feature level.

---

## Stripe Overview

| Stripe ID | Name | Domain focus | MVP Features | Goal |
|---|---|---|---|---|
| stripe-checkout | Checkout | Order + Payment | FEAT-ORD-001, FEAT-ORD-002, FEAT-PAY-001 | [Customer can place and pay for an order] |
| stripe-auth | Authentication | User / Auth | FEAT-USR-001, FEAT-USR-002 | [User can register and log in] |
| stripe-[name] | [Name] | [Domain] | [FEAT-IDs] | [Goal] |

**MVP features total:** [X] across [Y] stripes
**Post-MVP backlog:** [X] features (stripe TBD)

---

## Stripe Design Rules

- Each stripe covers a coherent domain slice (minimizes register conflicts between parallel agents)
- No feature is assigned to a stripe if its dependencies are in a different stripe that hasn't started
- Feature Sets span multiple stripes - that is expected and correct
- JIT design (pm-feature-design) runs per feature, per stripe, just before build
- Stripes can run in parallel (different Claude agents / Class Owners per stripe)

---

## Feature-to-Stripe Assignment

| FEAT-ID | Feature | MVP | Stripe | Dependency on |
|---|---|---|---|---|
| FEAT-ORD-001 | [Create] [draft order] [from cart] | true | stripe-checkout | none |
| FEAT-ORD-002 | [Confirm] [order] [after payment] | true | stripe-checkout | FEAT-ORD-001, FEAT-PAY-001 |
| FEAT-PAY-001 | [Validate] [card payment] [for order] | true | stripe-checkout | FEAT-ORD-001 |
| FEAT-USR-001 | [Register] [new account] [with email] | true | stripe-auth | none |

---

## Dependency Sequencing per Stripe

For each stripe, list the execution order based on dependencies:

**stripe-checkout:**
1. FEAT-ORD-001 (no deps)
2. FEAT-PAY-001 (needs FEAT-ORD-001)
3. FEAT-ORD-002 (needs FEAT-ORD-001 + FEAT-PAY-001)

**stripe-auth:**
1. FEAT-USR-001 (no deps)
2. FEAT-USR-002 (needs FEAT-USR-001)
```

---

## Step 4: Update Feature Cards and feature_list.md

After user approves the MVP Scope and Stripe assignment:

1. For each feature, update the `stripe:` field **and the `phase:` field** in the Feature Card frontmatter at `/features/cards/[FEAT-ID].md`. The MVP decision is written as the `phase` value (`MVP` / `MVP+` / `Phase N` - or the project's `P0`/`P1`…), **not** a separate `mvp` field.
2. Update `features/feature_list.md` - fill in the Stripe column and the `phase` value per feature. **Do not add a separate MVP true/false column** - `phase` carries it (IN-MVP = first/`MVP`/`P0` phase). If the list already has a stray `mvp` or `roadmap_phase` column, collapse it into `phase`.

---

## Step 5: Notion update

**Runs after user approves both artifacts.**

If no Notion Feature entries exist (pm-features-list was not pushed to Notion): skip this step.

### 5a. Get Notion connection

1. Read `pureinn-variables.md` key "Feature Backlog" → get URL
2. Check `state.json notion_ids.feature_backlog` → if set, use it directly
3. If not cached: call `mcp__claude_ai_Notion__notion-fetch` with the URL, extract data source ID, save to `state.json notion_ids.feature_backlog`

### 5b. Enrich Feature entries

For each Feature, update the existing Notion entry via `mcp__claude_ai_Notion__notion-update-page`.

**Only update MVP and POST-MVP features. Do NOT push CUT features - they remain in local feature_list.md only.**

| Property | Value | Source |
|---|---|---|
| `Phase` | `"MVP"` (MVP features) / `"MVP+"` (POST-MVP features) | Artifact 1 MVP decision |
| `Dev Stripe` | `"Stripe 1"` / `"Stripe 2"` / ... / `"Stripe 7"` | Artifact 2 stripe number (Stripe 1 = first stripe defined, Stripe 2 = second, etc.) |
| `FEAT-ID` | `FEAT-[DOMAIN]-[NUMBER]` | feature_list.md |

**Dev Stripe mapping:** Named stripes (e.g., `stripe-auth`, `stripe-payments`) map to Notion's numbered options by position in the delivery plan. The first stripe defined = `Stripe 1`, second = `Stripe 2`, etc. The domain name is preserved in local Feature Card frontmatter and `feature_list.md`.

### 5c. Confirm

After all updates: report counts (Features enriched, errors). Remind user that pm-stripe will orchestrate the JIT cycle - picking the next ready feature per stripe when build starts.

---

## Internal completeness checklist

<!-- Claude reference only -->

**MVP Scope must cover:**
- [ ] MVP hypothesis stated
- [ ] MVP success signal defined (measurable)
- [ ] In MVP list with stripe assignment
- [ ] Post-MVP list with reason for deferral and target phase
- [ ] Cut list with rationale
- [ ] MVP size is realistic vs. team and timeline

**Delivery Stripes must cover:**
- [ ] Each stripe has a coherent domain focus (minimizes register conflicts)
- [ ] Each stripe has a named goal (testable outcome)
- [ ] No feature assigned to a stripe that violates its dependency order
- [ ] Dependency sequencing per stripe is explicit
- [ ] Stripes can run in parallel without register conflicts

**For SaaS/AI products:**
- [ ] Onboarding flow is in Stripe 1 or 2
- [ ] Payment integration is in MVP stripes (if paid product)
- [ ] AI features have a fallback plan if AI output quality isn't ready
- [ ] Data pipeline features are before AI features in stripe order
- [ ] Account deletion (GDPR) is before launch stripe
- [ ] Admin/support tooling has at least a minimal stripe in MVP

---

## Save to

```
pureinn-workspace/[project-slug]/artifacts/phase-5-planning/mvp-scope.md
pureinn-workspace/[project-slug]/artifacts/phase-5-planning/delivery-stripes.md
pureinn-workspace/[project-slug]/features/feature_list.md         (updated: MVP + stripe columns)
pureinn-workspace/[project-slug]/features/cards/FEAT-*.md         (updated: stripe field in frontmatter)
```

---

## Handoff

**Čo si teraz má:** MVP Scope (IN/POST-MVP/CUT per feature) + Delivery Stripes - jasné čo sa stavia a v akých paralelných kanáloch. Phase 5 exit.

**Ďalší krok:** `/pm-stripe` — spusti JIT delivery cyklus, rieši features jednu po druhej per stripe v dependency poradí.

**Môžeš preskočiť ak:** Pred buildom ešte potrebuješ technický základ - najprv `/common-ground` (stack, repo štruktúra).
