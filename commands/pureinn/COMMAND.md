---
description: Pureinn workflow engine entry point. Reads existing documents, evaluates current state, maps to phases, and routes to the correct starting point. Run with a product idea or name to start. Run with 'map' for the full framework overview. Run with a known project slug to resume. Run with a stage keyword (setup / discover / validate / define / model / plan / build) to jump straight into that part of the framework - scaffolds a workspace first if none exists.
argument-hint: "[product idea | stage keyword | map | help | project-slug]"
---

# Pureinn - Workflow Engine

## Input

$ARGUMENTS

---

## Reference files

This file is the router. The engine's steps live in `references/` next to it. **Read the reference file for the path you are on before producing any output for that path** - never work from memory of what a step used to say. Read only the file the current path needs, not all of them.

Resolve a reference path in this order, stopping at the first that works:
1. `${CLAUDE_PLUGIN_ROOT}/commands/pureinn/references/[file]`
2. If that path did not resolve (the working directory is the user's product workspace, not the plugin, so a bare Glob will not find it), locate the plugin root once with Bash and reuse it for the rest of the session:
   ```bash
   find ~/.claude/plugins/cache ~/.claude/plugins/marketplaces -maxdepth 6 \
        -type d -path '*/commands/pureinn/references' 2>/dev/null | head -1
   ```
   (`find`, not a shell glob - a non-matching glob aborts the command in zsh. The installed copy under `cache/` is listed first and wins; `marketplaces/` is the fallback clone.)
3. Last resort - a dev checkout inside the working directory: Glob `**/commands/pureinn/references/[file]`

If none resolve, say so plainly and ask the user where the Pureinn plugin is installed. Never improvise a step's content from memory.

| Reference file | Contains | Read it when |
|---|---|---|
| `entry.md` | STEP 0a - Document Scan, STEP 0b - Explore mode | **every** path, at STEP 0 |
| `intake.md` | STEP 2 - Documents recap, STEP 3 - Intake Questions | new project (STEP 1A path) |
| `assessment.md` | STEP 3B - Assessment, STEP 3C - Fast Track Detection | after intake |
| `playbooks.md` | STEP 4 - Playbook Selection, STEP 5 - Starting Phase, Phase → Skills Reference | selecting a playbook, or listing a phase's skills |
| `workspace.md` | STEP 6 - Workspace Setup (tree, `state.json`, `pureinn-variables.md`) | scaffolding a workspace |
| `dashboard.md` | STEP 7 - Dashboard and Routing, Exit Gate Thresholds, Exit Gate | rendering the dashboard, running an exit gate |
| `framework-map.md` | FRAMEWORK MAP | `/pureinn map` or `/pureinn help` |

---

## STEP 0 - Intent Gate

**Hard rule: this step completes before any other output.** No dashboard, no intake question, no artifact, no advice - classify first. The engine's worst failure is answering a free-text brief conversationally and never entering the framework at all.

**a) Classify `$ARGUMENTS` into exactly one of five modes.** Evaluate in this order, first match wins:

| # | Mode | Trigger | Example | Goes to |
|---|---|---|---|---|
| 1 | `map` | `map` / `help` | `/pureinn map` | `references/framework-map.md`, nothing else |
| 2 | `stage` | The argument is a **bare** stage/playbook keyword (see resolver below), optionally preceded by a project slug or followed by a quoted product idea | `/pureinn define` · `/pureinn acme model` · `/pureinn discover "food delivery app"` | STEP 1C |
| 3 | `resume` | Matches a known project slug that has a `state.json` | `/pureinn acme-crm` | STEP 1B |
| 4 | `new` | A product idea, or an explicit ask to start/build something | `/pureinn "B2B SaaS pre správu projektov"` · `/pureinn "e-shop, potrebujeme loyalty program"` | STEP 1A |
| 5 | `explore` | The user is describing a situation, brief or problem out loud - thinking, not yet committing to a project | `/pureinn "máme 3 hodiny na take-home, brief je v prílohe - čo s tým"` | `references/entry.md` § STEP 0b |

The full user-facing usage patterns (what the engine does on each of these) live in `references/framework-map.md` - shown on `/pureinn map`. Do not restate them here; one list, one place.

**b) Stage keyword disambiguation - the rule that prevents false positives.** Stage keywords are common English words (`build`, `plan`, `research`, `test`, `scope`, `start`). A keyword only routes to `stage` when the whole argument is a bare command:

- at most 3 tokens, **and**
- no sentence punctuation (`.` `,` `?` `!` `:` `;`), **and**
- the keyword is the first or second token (a slug may precede it)

A keyword sitting inside a longer sentence is prose, not a command. `/pureinn build` is stage entry; `/pureinn "we need to build a loyalty program for our shop"` is not - it is `new` or `explore`. The one exception is a keyword followed by a quoted idea (`/pureinn discover "food delivery app"`), which stays stage entry by design.

**c) Distinguishing `new` from `explore`** - both are free text, and the difference is commitment, not length:

| Signal | Points to |
|---|---|
| Names a product or an idea to build, asks to start, uses "I want to build / we're making" | `new` |
| Describes a situation, an assignment, a client brief, a problem to think about; asks what to do; has a deadline attached; pastes material for an opinion | `explore` |

When genuinely ambiguous, treat it as `explore` - it can always route into `new` one step later, and it never creates a workspace the user did not ask for. The reverse mistake is expensive.

**d) Confirm before acting on free text.** If the input is free text longer than ~10 words, echo the classification back and confirm with **one** AskUserQuestion before proceeding - never a series. Show what you understood in one line, then offer the classified mode as the recommended option and the neighbouring mode as the alternative. Short, unambiguous inputs (`map`, a bare keyword, a known slug) are not confirmed - that would be friction with no benefit.

**e) Run the document scan.** Read `references/entry.md` § STEP 0a and run it at the depth its table gives for the classified mode. This runs on every path including resume and stage entry - not only on new-project intake.

**f) Establish repo context.** Whether a codebase exists is a **routing signal**, not a config detail - it decides whether the code can be read at all, which design-context source is available, and whether anything can be built in-repo. Ask once per project, never on every run:

| Mode | What to do |
|---|---|
| `map` | skip |
| `resume`, `stage` with a `state.json` | read `repo` from it. Only if the key is absent (project predates this field) ask once and write it |
| `new`, `explore` | ask as part of this gate |

Use **AskUserQuestion**, one question - "Is there a codebase for this?":
- **Local path** - the code is on this machine *(recommend when the product already exists)*; capture the path
- **Remote URL only** - a repository exists but is not checked out here; capture the URL
- **None yet** - greenfield, code will exist later *(recommend for a new product)*
- **None, and there won't be** - research, strategy or a pitch with no build

Record the answer in `state.json` → `repo` and in `pureinn-variables.md` (both shapes in `references/workspace.md`). In `explore` mode, hold the answer in the session only - explore writes no files. What each answer unlocks is in `references/workspace.md` § Repo context; do not re-derive it here.

**One follow-up, only when it applies:** if the product exists but the code is not reachable (`remote`, `none`), ask for the live product URL and record it as `live_product_url`. That is the one case where the product's design can be read from nowhere else - see `references/workspace.md` § Design context. Do not ask this on a greenfield run; there is nothing to look at yet.

Only then continue to the step the mode points at.

### Stage Keyword Resolver

A stage keyword is a user-facing shortcut into one part of the framework. It never changes the engine - it resolves to an existing phase and hands control to the normal dashboard/routing. Match case-insensitively; accept any alias.

| Keyword (+ aliases) | Resolves to |
|---|---|
| `setup` · foundation · kickoff · start | Phase 1 - Foundation |
| `discover` · discovery · research | Phase 2 - Discovery |
| `validate` · validation · test | Phase 3a - Validation |
| `define` · definition · prd | Phase 3b - Commercial Definition |
| `model` · domain · modeling · domain modeling · build domain model · erd | Phase 4 - Domain Modeling |
| `plan` · planning · features · scope | Phase 5 - Feature Planning |
| `build` · deliver · ship · jit | Phase 6 + 7 - JIT Delivery |
| `reconcile` | Rebuild playbook A1 (entry: `/pm-reconcile`) |
| `bootstrap` | Rebuild playbook A2 (entry: `/pm-entity-registry` chain) |
| `feature` | Feature Implementation playbook |

**Two-tier model:** stage keywords enter a whole *chunk* of work. For a single artifact (just JTBD, just KANO), the user runs the existing per-skill command directly (`/jtbd-building`, `/pm-features-list`) - no stage needed. Do not invent cross-phase stages; the per-skill commands already cover pinpoint needs.

---

## First-Run Orientation

If no `state.json` exists for this project (new start, not a resume), display the following before asking about guidance mode:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PUREINN - AI Product Development Framework
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

I'll ask you 9 questions in 3 groups to understand what you're building.
I'll also scan your directory for existing research, notes, or specs.
Then I'll select the right playbook and show you exactly which skills to run.

Run one skill at a time. Each skill tells you what's next when it finishes.
Type /pureinn map at any point to see the full framework overview.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Then proceed to Guidance Mode Check.

---

## STEP 1A - Guidance Mode Check

Use the AskUserQuestion tool:

- Question: "Do you want guidance throughout the workflow?"
- Option A: "Yes - explain the why" (Recommended) — description: "Before each phase and skill, adds 2-3 sentences of context: what it achieves, what to watch out for."
- Option B: "No - just tell me what to run" — description: "Pure routing. Dashboard + skills queue only."

Store the answer. Save as `"guidance_mode": true` or `false` in state.json.

**What guidance mode means:**
- ON: Before each phase and before recommending each skill, Claude adds 2-3 sentences of context - what this phase is trying to achieve, what to watch out for, common mistakes. Applied consistently throughout the workflow, not just at the start.
- OFF: Pure routing. Dashboard + skills queue, no explanatory text.

Then read `references/intake.md` and run **STEP 2 (Documents recap)** - the scan itself already ran in STEP 0.

---

## STEP 1B - Resume Path

A state.json exists for this project. Read it, then read `references/dashboard.md` and go to **STEP 7 (Dashboard)**. If the STEP 0 delta scan found new material, surface it before the dashboard - new inputs can change what the right next action is.

---

## STEP 1C - Stage Entry

The user jumped straight to a part of the framework via a stage keyword (e.g. `/pureinn define`). Goal: get them into that stage cleanly, with a fully-formed workspace behind them - never a half-set-up project. This reuses existing logic; it does not duplicate the engine.

**a) Resolve the keyword** → target phase (Stage Keyword Resolver above). For playbook keywords (`reconcile` / `bootstrap` / `feature`), route to that playbook's entry instead of a phase.

**b) Establish workspace context:**

- **A `state.json` exists** (current dir, or the named slug) → read it. Load context as in STEP 1B.
- **No workspace exists yet** (fresh project + stage - a first-class path, e.g. "I already have my own research, I just want to use Pureinn for `define`"):
  1. Run a **minimal intake** - only what this stage needs: product name/slug, and "Do you have research or inputs for this stage? Point me at them." Do NOT run the full 9-question intake.
  2. **Scaffold the full workspace** exactly as STEP 6 in `references/workspace.md` does: create `pureinn-workspace/[slug]/` with the complete tree (`domain/`, `features/`, `product/`, `artifacts/`, `initiatives/`), `state.json`, `pureinn-variables.md`, `assessment.md`. The project must be fully operational for everything downstream - not a partial folder.
  3. In `state.json`: set `playbook` (infer from context - default Greenfield), `starting_phase` = the entered phase, and record every phase *before* it in `phases_skipped`.
  4. **Deep-ingest** whatever the user pointed at (apply the Deep source ingestion standard - full recursive read), so the stage has real inputs, not emptiness.

**c) PREREQ check for the target phase** (graceful degradation - never hard-block):

| Stage | Requires upstream | If missing |
|---|---|---|
| `setup` / `discover` | nothing | proceed |
| `validate` | Problem Validation Summary | offer options below |
| `define` | Phase 3a GO verdict + validated inputs — OR a given mandate (commissioned build: client/exec decided) + Discovery Report → route to `/pm-scope-brief` | offer options below |
| `model` | PRD frozen — or Scope Brief baselined (`product/scope_brief.md`, commissioned builds) | offer options below |
| `plan` | entities.md + business_rules.md | offer options below |
| `build` | feature_list.md + registers | offer options below |

When upstream is missing or thin, use **AskUserQuestion**:
- A) Proceed in [stage] now - treat skipped upstream as "done elsewhere" / imported from the ingested research, mark genuine gaps `[ASSUMED - replace when real data available]` *(Recommended when the user brought their own research for this stage)*
- B) Jump back to [upstream stage] to build the missing input first
- C) Proceed anyway, I accept the risk

This is the existing **"done elsewhere"** rule (used for Phase 3a) generalized to stage entry: if work was genuinely done outside the framework, collect the minimum evidence to confirm the exit criteria, mark the phase complete, and continue. Do not force re-running skills for work already done. Note the hard gate still holds: `define` (Phase 3b) requires a GO verdict - if none exists, collect it via the "done elsewhere" import (verdict + evidence) before proceeding. **Exception - commissioned builds:** when the mandate is already given (a client commissioned the build, an exec directed it), the GO gate does not apply - the market risk sits with the commissioner. Phase 3a is skipped (record it in `phases_skipped` with reason "mandate given") and Phase 3b runs as `/pm-scope-brief` instead of the canvas → PRD chain.

**d) Set state + hand off:** write `current_phase_name` (and `current_phase_index` aligned to the existing scheme) to `state.json`, then read `references/dashboard.md` and go to **STEP 7 (Dashboard)**. The dashboard already renders the phase, its skills queue, and the guidance intro - no new dashboard logic.

---

## Behavioral Rules

- Never execute skill logic. Route to the right skill, let the user invoke it.
- Document analysis (Step 3) is the primary assessment mechanism - not a questionnaire. Read first, ask second.
- Conclusions and assumptions must be explicitly separated in the assessment. Never mix them.
- User confirmation of the assessment is mandatory before routing. They confirm, reject, or adjust each section.
- Guidance mode is persistent throughout the workflow - not a one-time intro.
- If guidance is ON: always add phase purpose before the skills queue. Never skip it.
- Phase skipping is allowed for phases with confirmed coverage. Record in state.json.
- One phase at a time in the dashboard. Show only the current phase skills queue in detail.
- If user asks to pause: save state and say "Run /pureinn [slug] to continue."
