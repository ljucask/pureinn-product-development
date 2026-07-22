---
name: pm-open-questions
description: Build and maintain the Open Questions & Decisions Register - Live Register 5 in the FDD+SDD framework. Centralizes every unresolved question, legacy-vs-code divergence, and concrete blocker across the whole project into one file (/domain/open_questions.md), each with a unique ID (OQ-/DIV-/BLK-{DOMAIN}-NN), full context, and an Open→Resolved audit trail. Replaces scattered per-artifact "Open Questions" sections (PRD, Roadmap, reconcile reports, Feature Cards) - there is exactly one place open items live. Callable at any phase; initializes on first use, at latest during Phase 4 (pm-domain-model or pm-reconcile). Other skills append directly to this register when they hit an unresolved item, instead of writing it into their own artifact. Handles migration scan for existing projects being onboarded to the framework.
license: MIT
metadata:
  agent-mode: decision
  author: https://github.com/ljucask
  version: "1.0.0"
  domain: product-management
  triggers: open questions, open question register, decisions log, unresolved question, blocker, divergence, OQ-ID, DIV-ID, BLK-ID, decision tracking, Live Register 5
  role: specialist
  scope: specification
  output-format: document
  related-skills: pm-reconcile, pm-domain-model, pm-prd, pm-product-roadmap, pm-features-list, pm-feature-design, pm-business-rules-library, pm-market-analysis, pm-audit
---

# PM - Open Questions & Decisions Register

## Agent mode (`--agent`)

Supports `--agent`: runs autonomously in a subagent, drafts the artifact from existing inputs, and returns a short summary + coverage note.

- **No flag** → interactive (default); if inputs are heavy, offer agent mode.
- **`--agent`** → obey. First check inputs are complete. Anything missing: do NOT invent it - mark `[ASSUMED - what/why]` in the output and summary. Never hallucinate to fill a gap.
- **Review required:** the artifact contains commitments (priority, owner, resolution) - after drafting, require the user's review before finalizing; do not close a question autonomously.

---

## What this skill does

Builds and maintains **Live Register 5**: the Open Questions & Decisions Register (`/domain/open_questions.md`).

**The problem this solves:** without one home for open questions, every skill that hits an unresolved item writes it wherever it happens to be working - a PRD section, a roadmap note, a reconcile report, a Notion comment. No one - human or skill - can answer "what are all the open questions on this project" without manually searching five or more places.

**The rule:** open questions, divergences, and blockers have **exactly one** home in the whole project. No other artifact (PRD, Roadmap, Feature Cards, reconcile reports) contains one or references its text - anyone looking for open items goes to `domain/open_questions.md`, always.

**Position in the 5-register architecture:**

| Register | File | Content |
|---|---|---|
| 1. Entity & State Registry | `/domain/entities.md` | Domain objects + state machines (pm-entity-registry) |
| 2. Business Rules Library | `/domain/business_rules.md` | Business rules catalog (pm-business-rules-library) |
| 3. Decision Models Matrix | `/domain/decision_models.md` | Decision tables (pm-business-rules-library) |
| 4. FDD Feature List | `/features/feature_list.md` | Feature hierarchy + planning (pm-features-list) |
| **5. Open Questions & Decisions** | `/domain/open_questions.md` | Unresolved questions, divergences, blockers (THIS SKILL) |

**When it is created:** at first occurrence of an open item in the project - at latest during `pm-reconcile` or `pm-domain-model` in Phase 4, but it can be created earlier if a question arises in Phase 2/3.

**Who writes to it:** any skill that encounters an unresolved question, a legacy-vs-code divergence, or a concrete blocker - directly, not via PRD/Roadmap/reports as a proxy. See "Producing skills" below.

---

## The three record types

Not every open item is the same kind of problem. Distinguishing them prevents a "fully-specified, just needs doing" blocker from being treated like a genuine judgment call - and vice versa.

| Type | Prefix | Resolves | Example |
|---|---|---|---|
| **Question** | `OQ-{DOMAIN}-NN` | Real alternatives exist; needs a judgment call | "Server-side or client-managed active-role?" |
| **Divergence** | `DIV-{DOMAIN}-NN` | Legacy documentation and code disagree; needs a ruling on which is true | "Legacy says X, code does Y - which is correct?" |
| **Blocker** | `BLK-{DOMAIN}-NN` | Something concrete is missing or broken; no ambiguity about what to do, just needs executing | "Shared submodule doesn't exist - needs restoring" |

`OQ-BIZ-NN` and `OQ-MVP-NN` are **domain-scoped variants of `OQ-`** (Type is still `Question`) - they change the namespace (business/strategic scope, MVP-exit-gate scope), not the record type. Never invent a 4th type; if an item doesn't fit Question/Divergence/Blocker, it's probably a task, not an open item - it belongs in the backlog (`feature_list.md`), not here.

**ID rule:** never recycle an ID across different questions, even if a slot looks free after a resolve. If unsure whether an ID was used, check the register - never assume.

---

## Producing skills (who writes here)

Any skill can append an entry when it hits an unresolved item. The framework wires this into:

- `pm-prd` - synthesis reveals an unresolved question or TBD value
- `pm-product-roadmap` - a phase decision is genuinely unresolved (not just an assumption)
- `pm-reconcile` - legacy-vs-code divergences (`DIV-`) and build blockers (`BLK-`) found during any area pass
- `pm-domain-model` - entity/boundary ambiguities during domain modeling
- `pm-features-list` - scope or prioritization judgment calls during feature decomposition
- `pm-feature-design` - JIT design surfaces a rule/guard-condition ambiguity
- `pm-business-rules-library` - a rule's exact formula or enforcement point is unresolved
- `pm-market-analysis` - a strategic/business question without technical domain context (`OQ-BIZ-`)

Each of these writes the entry **directly** to `domain/open_questions.md` following the schema below (creating the register first via this skill if it doesn't exist yet) - they do not write the question into their own artifact, and they do not route through this skill as a middle step for every single entry. This skill's job is to **own the register**: initialize it, assign IDs without collision, manage the Open→Resolved lifecycle, handle Notion sync, and run the migration scan. It is also directly callable to add, resolve, or query an entry standalone.

---

## Dependencies

**No hard dependency** - can be created standalone or by any producing skill above.

**Produces artifacts used by:**
- Every skill listed above (as a place to route unresolved items instead of embedding them)
- `pm-audit` - flags any open-question-like content duplicated outside the register as an anti-pattern
- `pm-stripe` / Phase 6 - Critical/High priority open items blocking a feature are visible before build starts

---

## Step 0: Current state check + mode detection

Check for `domain/open_questions.md` in the current project workspace.

**Mode detection:**

| Condition | Mode |
|---|---|
| File does NOT exist | **Initialize** - create the Open/Resolved skeleton, then proceed to whichever mode triggered the call |
| File EXISTS | Go straight to the requested mode below |

Use AskUserQuestion tool (skip if the caller already specified the action, e.g. a producing skill appending one entry):

- Question: "What do you want to do with the Open Questions Register?"
  - Option A: "Add a new entry (Recommended if a question/divergence/blocker just came up)"
  - Option B: "Resolve an existing entry"
  - Option C: "Migrate an existing project - scan for scattered open items and consolidate them here"
  - Option D: "Review - just show me the current Open items"

**Interaction:** Group related questions (2-4 per round) and confirm before moving on. For any A/B/C/D choice, use the AskUserQuestion tool with one option marked **(Recommended)** - never print options as plain text. Keep open-ended questions free-text (don't fake options). If the user is unsure, propose 3-4 concrete options plus "Other". Surface an assumption the moment you make one; never fabricate to fill a gap. (Full standard: CLAUDE.md.)

---

## Step 1: Gather inputs (Add mode)

Ask as plain text:

```
I need inputs for this open item.

1. THE ITEM ITSELF
   State it as a full sentence, not a fragment.
   Question example: "Should active-role state be tracked server-side or client-managed?"
   Divergence example: "Legacy BRD says refunds are manual-only; code has an auto-refund path - which is correct?"
   Blocker example: "The shared submodule referenced in the build config does not exist."

2. TYPE
   Question (needs a judgment call) / Divergence (legacy vs. code disagreement) /
   Blocker (concrete gap, no ambiguity about what to do)

3. CONTEXT (2-4 sentences)
   Why does this matter? What's already decided vs. not? What's the current state?
   (This is the field people skip - don't. A one-sentence question with no context
   is not enough to act on later.)

4. OPTIONS CONSIDERED (if Type = Question and real alternatives exist)
   List the alternatives with their trade-offs.

5. IMPACT IF UNRESOLVED
   What specifically does this block? FEAT-ID, phase, or risk.

6. DOMAIN CODE
   Which domain/pass does this belong to? (e.g. entity domain code from entities.md,
   or a pass code like a reconcile area or design pass)
```

Then use AskUserQuestion tool with:
- Question: "Priority?"
  - Option A: "Critical - blocks build/launch right now"
  - Option B: "High - must resolve before the relevant milestone (Recommended if unsure)"
  - Option C: "Medium - address before scale"
  - Option D: "Low - nice to resolve, nothing blocked"
- Question: "Owner?"
  - Option A: "PO"
  - Option B: "Tech lead"
  - Option C: "PO + Tech lead"

Ask as plain text: "Target - before which milestone or feature should this resolve?" and "Source - which artifact/pass/skill first surfaced this?"

---

## Step 2: Assign ID

1. Read `domain/open_questions.md` (Open + Resolved sections - an ID is never reused even after resolution).
2. Determine the prefix from Type: `OQ-` (Question), `DIV-` (Divergence), `BLK-` (Blocker). Business/strategic scope without a technical domain → `OQ-BIZ-`; MVP-scope/exit-gate questions → `OQ-MVP-`.
3. Find the next unused number for that `{PREFIX}-{DOMAIN}` combination. Never recycle a number that appears anywhere in the file, Open or Resolved.
4. If unsure whether a number was used - check the file, do not assume it's free.

---

## Step 3: Generate / append entry

---

### ARTIFACT: Open Questions & Decisions Register

Save to: `pureinn-workspace/[project-slug]/domain/open_questions.md`

```markdown
# Open Questions & Decisions Register
# Live Register 5 - FDD+SDD Framework

> **Product:** [Product Name]
> **Version:** 1.0
> **Last updated:** [date]
> **Maintained by:** pm-open-questions + any skill that surfaces an open item

---

> **How to read this register:**
> - This is the ONLY place open questions, divergences, and blockers live. No PRD, Roadmap,
>   Feature Card, or reconcile report duplicates their text.
> - Type: Question (judgment call) | Divergence (legacy vs. code ruling) | Blocker (concrete gap)
> - Entries move Open → Resolved. Never deleted - a resolved entry is the audit trail for why
>   something was decided, not just that it was.

---

## Open

### {ID}: {Question/divergence/blocker as a full sentence}

**Type:** Question | Divergence | Blocker
**Context:** [2-4 sentences - why it matters, what's already decided vs. not, current state]
**Options considered:** [if real alternatives exist - mainly for Type: Question]
**Impact if unresolved:** [what specifically blocks - FEAT-ID, phase, risk]
**Priority:** Critical | High | Medium | Low
**Owner:** PO | Tech lead | PO + Tech lead
**Target:** [before which milestone/feature]
**Source:** [which artifact/pass/skill first recorded it]

---

## Resolved

### {ID}: {Question/divergence/blocker as a full sentence}

**Type:** Question | Divergence | Blocker
**Context:** [preserved from when it was open]
**Resolved:** [date]
**Decision:** [what was decided, in full - not just "resolved"]
**Recorded in:** [artifact where the decision now lives, e.g. business-model-canvas.md, a specific BR-ID]
**Source:** [preserved from when it was open]

---

## Changelog

| Version | Date | Change | Reason |
|---|---|---|---|
| 1.0 | [date] | Register initialized | First open item on the project |
```

---

## Step 4: Resolve an entry

1. Locate the entry under **Open** by ID.
2. Move it to **Resolved**, adding: `Resolved` (date), `Decision` (the actual decision, in full - not "done"), `Recorded in` (the artifact where the decision now permanently lives, e.g. a BR-ID, a roadmap phase, `business-model-canvas.md`).
3. Never delete an entry, Open or Resolved. A future team member needs to know **why** something was decided, not just that it was.
4. **Duplicate/late-breaking check:** if a resolved question resurfaces elsewhere (e.g. re-raised in Notion, or a producing skill about to log what looks like the same item again) - do NOT silently overwrite the resolution with a "late-breaking" change. Mark the new occurrence as a duplicate/stale reference to the canonical ID and ask the user to confirm whether it should genuinely be reopened (moved back to Open with a new context note) before touching the resolved record.

---

## Step 5: Migration scan (existing project onboarding)

Run this when the framework is applied to an already-running project (typically triggered from `/pm-reconcile open-questions`, or standalone via `/pm-open-questions migrate`).

1. **Scan all `.md` artifacts + `state.json`** for patterns: `OQ-*`, `DIV-*`, `BLK-*`, "TBD", "open question". Follow the deep source ingestion standard (CLAUDE.md) - recursive, full depth, not just an index/summary file.
2. **Scan the existing Notion "Open Questions" DB, if one exists** - do not assume it is empty. Verify with an actual row count (`mcp__claude_ai_Notion__notion-query-database-view` or equivalent), not just by checking the schema exists.
3. **Cross-check for duplicates/conflicts** between what was found locally and what's in Notion before writing anything to the register.
4. **Flag conflicts to the user - never silently decide.** This is exactly the case where a human must rule: present each conflict (`local: X` vs `Notion: Y`) and let the user say which is canonical, or whether both are genuinely distinct items.
5. Once resolved, write the consolidated entries into `domain/open_questions.md` per the schema above, assigning IDs per Step 2 (never recycling any ID already visible in either source).

---

## Notion push

After saving/updating `domain/open_questions.md`, sync to Notion.

1. Read `pureinn-variables.md` key `"Open Questions"` → get DB URL.
2. If blank: skip, remind user to add URL to `pureinn-variables.md`.
3. Call `mcp__claude_ai_Notion__notion-fetch` → extract `data_source_id`, cache in `state.json notion_ids.open_questions`.
4. **If a DB already exists with a different (poorer) schema, extend it - do not create a new one.** The workspace register is the source of truth; Notion's schema adapts to it (same principle as the Feature Backlog DB).
5. For each new/updated entry, call `mcp__claude_ai_Notion__notion-create-pages` (new) or the update equivalent (status change):

```
properties:
  Question: [{ID}: {question/divergence/blocker text}]   (title)
  ID: [ID]
  Context: [Context]
  Impact if unresolved: [Impact]
  Priority: [Critical / High / Medium / Low]              (select)
  Owner: [PO / Tech lead / PO + Tech lead]                 (select)
  Deadline: [Target]
  Source: [Source]
  Type: [Question / Divergence / Blocker]                  (select)
  Status: [Open / Resolved]                                (select)
```

After push: report counts (entries pushed, status updates, errors).

---

## Internal completeness checklist

<!-- Claude reference only -->

**Every entry:**
- [ ] ID follows `{OQ|DIV|BLK}-{DOMAIN}-NN`, never recycled
- [ ] Type set and matches the prefix
- [ ] Context explains WHY, not just what (2-4 sentences, not a fragment)
- [ ] Impact if unresolved names something concrete (FEAT-ID, phase, or risk)
- [ ] Priority, Owner, Target, Source all filled

**Register-wide:**
- [ ] No open item's text is duplicated in PRD / Roadmap / Feature Cards / reconcile reports
- [ ] Resolved section never has a deleted entry - only moved-and-annotated ones
- [ ] Migration scan (if run) cross-checked Notion by count, not schema alone, and flagged conflicts rather than deciding them

---

## Save to

**Initialize (first entry on the project):**
```
pureinn-workspace/[project-slug]/domain/open_questions.md
```
State update → `state.json`: set `registers.open_questions_initialized` to `true`.

**Add mode (register already exists):**
- Append the new entry under `## Open`, in the correct ID sequence
- Update the Changelog

**Resolve mode:**
- Move the entry from `## Open` to `## Resolved` with the added fields
- Update the Changelog and `> Last updated`

---

## Handoff

**Čo si teraz má:** `open_questions.md` (Live Register 5) - jediné miesto, kde sa dá zistiť, čo je na projekte otvorené, prečo, a kto to má vyriešiť dokedy.

**Ďalší krok:** Späť do skillu/fázy, kde otázka vznikla - register je cross-cutting, nie vlastný krok v sekvencii. `/pm-audit` skontroluje, či sa niekde open-question obsah neduplikuje mimo registra.

**Môžeš preskočiť ak:** žiadny skill zatiaľ nenarazil na nezodpovedanú otázku - register sa vytvára až pri prvom výskyte, nikdy vopred naprázdno.
