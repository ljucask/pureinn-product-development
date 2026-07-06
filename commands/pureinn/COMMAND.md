---
description: Pureinn workflow engine entry point. Reads existing documents, evaluates current state, maps to phases, and routes to the correct starting point. Run with a product idea or name to start. Run with 'map' for the full framework overview. Run with a known project slug to resume. Run with a stage keyword (setup / discover / validate / define / model / plan / build) to jump straight into that part of the framework - scaffolds a workspace first if none exists.
argument-hint: "[product idea | stage keyword | map | help | project-slug]"
---

# Pureinn - Workflow Engine

## Input

$ARGUMENTS

---

## Usage Patterns

### Greenfield - new product from scratch
```
/pureinn "B2B SaaS pre správu projektov v konštrukčných firmách"
/pureinn "marketplace pre freelancerov a klientov"
```
Engine spustí intake (9 otázok), nascanuje existujúce dokumenty, vyberie Greenfield playbook, ukáže dashboard s Phase 1 skills queue.

### Greenfield - máš research alebo čiastočné materiály
```
/pureinn "food delivery app" [+ vlož interview notes, research docs do working directory]
```
Engine prečíta dokumenty, zmapuje ich na fázy, identifikuje kde si, preskočí pokryté fázy.

### Feature Implementation - pridávaš feature do existujúceho produktu
```
/pureinn "Acme CRM - chceme pridať AI asistenta do reportingu"
/pureinn "náš e-shop, potrebujeme loyalty program"
```
Engine vyberie Feature playbook. Ak Phase 0 nie je hotová, začne kontextovým setupom (pureinn + common-ground + impeccable document). Ak Phase 0 existuje, smeruje priamo na Feature Viability Assessment.

### Pokračovanie v rozpracovanom projekte
```
/pureinn acme-crm
/pureinn-resume acme-crm
```
Engine prečíta `state.json`, obnoví kontext z `assessment.md`, zobrazí dashboard s aktuálnou fázou.

### Skok do konkrétnej časti (stage shortcut)
```
/pureinn define                       # aktuálny projekt: skoč do Commercial Definition
/pureinn vezmee model                 # projekt vezmee: skoč do Domain Modeling
/pureinn discover "food delivery app" # nový projekt: rovno do Discovery (Pureinn založí workspace)
```
Keywordy: `setup` · `discover` · `validate` · `define` · `model` · `plan` · `build` (+ aliasy). Engine rozlíši keyword, over si podklad pre danú časť (ak chýba, ponúkne možnosti - nikdy nezablokuje), a ak workspace ešte neexistuje, najprv ho celý založí. Pre jeden konkrétny artefakt spusti priamo daný skill (`/jtbd-building`, `/pm-features-list`) - stage netreba.

### Prehľad celého frameworku
```
/pureinn map
/pureinn help
```
Zobrazí Framework Map - všetky playbooki, fázy, skills a artifact chains na jednom mieste.

---

## Special Commands

Evaluate `$ARGUMENTS` in this order (first match wins):

1. **`map` / `help`** → Skip all steps. Go directly to **FRAMEWORK MAP** at the bottom of this skill.

2. **First token is a stage/playbook keyword** (see Stage Keyword Resolver below) → Go to **STEP 1C (Stage Entry)**.
   The keyword may stand alone (`/pureinn define`), be preceded by a project slug (`/pureinn vezmee define`), or be followed by a fresh product idea (`/pureinn discover "food delivery app"`).

3. **Matches a known project slug with an existing `state.json`** → Go to **STEP 1B (Resume path)**.

4. **Otherwise** → Go to **STEP 1A (New / intake path)**.

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

---

## STEP 1B - Resume Path

A state.json exists for this project. Read it and go directly to **STEP 7 (Dashboard)**.

---

## STEP 1C - Stage Entry

The user jumped straight to a part of the framework via a stage keyword (e.g. `/pureinn define`). Goal: get them into that stage cleanly, with a fully-formed workspace behind them - never a half-set-up project. This reuses existing logic; it does not duplicate the engine.

**a) Resolve the keyword** → target phase (Stage Keyword Resolver above). For playbook keywords (`reconcile` / `bootstrap` / `feature`), route to that playbook's entry instead of a phase.

**b) Establish workspace context:**

- **A `state.json` exists** (current dir, or the named slug) → read it. Load context as in STEP 1B.
- **No workspace exists yet** (fresh project + stage - a first-class path, e.g. "I already have my own research, I just want to use Pureinn for `define`"):
  1. Run a **minimal intake** - only what this stage needs: product name/slug, and "Do you have research or inputs for this stage? Point me at them." Do NOT run the full 9-question intake.
  2. **Scaffold the full workspace** exactly as STEP 6 does: create `pureinn-workspace/[slug]/` with the complete tree (`domain/`, `features/`, `product/`, `artifacts/`, `initiatives/`), `state.json`, `pureinn-variables.md`, `assessment.md`. The project must be fully operational for everything downstream - not a partial folder.
  3. In `state.json`: set `playbook` (infer from context - default Greenfield), `starting_phase` = the entered phase, and record every phase *before* it in `phases_skipped`.
  4. **Deep-ingest** whatever the user pointed at (apply the Deep source ingestion standard - full recursive read), so the stage has real inputs, not emptiness.

**c) PREREQ check for the target phase** (graceful degradation - never hard-block):

| Stage | Requires upstream | If missing |
|---|---|---|
| `setup` / `discover` | nothing | proceed |
| `validate` | Problem Validation Summary | offer options below |
| `define` | Phase 3a GO verdict + validated inputs | offer options below |
| `model` | PRD frozen | offer options below |
| `plan` | entities.md + business_rules.md | offer options below |
| `build` | feature_list.md + registers | offer options below |

When upstream is missing or thin, use **AskUserQuestion**:
- A) Proceed in [stage] now - treat skipped upstream as "done elsewhere" / imported from the ingested research, mark genuine gaps `[ASSUMED - replace when real data available]` *(Recommended when the user brought their own research for this stage)*
- B) Jump back to [upstream stage] to build the missing input first
- C) Proceed anyway, I accept the risk

This is the existing **"done elsewhere"** rule (used for Phase 3a) generalized to stage entry: if work was genuinely done outside the framework, collect the minimum evidence to confirm the exit criteria, mark the phase complete, and continue. Do not force re-running skills for work already done. Note the hard gate still holds: `define` (Phase 3b) requires a GO verdict - if none exists, collect it via the "done elsewhere" import (verdict + evidence) before proceeding.

**d) Set state + hand off:** write `current_phase_name` (and `current_phase_index` aligned to the existing scheme) to `state.json`, then go to **STEP 7 (Dashboard)**. The dashboard already renders the phase, its skills queue, and the guidance intro - no new dashboard logic.

---

## STEP 2 - Document Scan and Intake

First, scan the entire working directory recursively for any existing documents (.md, .txt, .pdf, .docx, .csv, notes, research files - anything that could be product or research material). Exclude code files, system files, and this framework's own files (`.claude/`, `Framework know-how/`, `docs - product framing/`, `pureinn-workspace/`).

**If documents are found outside the framework:**

Read them. Then inform the user:

```
I found the following files that may be relevant:

  [list of files with paths]

I'll include these in the analysis. If you have additional documents
not yet in the directory, add them now and let me know - otherwise
we'll proceed with what's here.
```

**If no documents found:**

```
I don't see any existing documents in the directory.

If you have research notes, specs, interview transcripts, or anything
else relevant - add them anywhere in this directory and let me know.

If you're starting from scratch, say "nothing" and we'll go from there.
```

Wait for confirmation. If user adds files, read them. If "nothing", proceed to Step 3 with no documents.

---

## STEP 3 - Intake Questions

Ask these questions regardless of whether documents were found. Documents give Claude the written record; these questions capture current thinking, intent, and product shape that documents often don't contain.

Questions are grouped into 3 rounds. Each round: ask questions, then show a summary and wait for confirmation before moving to the next round.

**How to ask questions within a round:**
- Questions with predefined answer options (A/B/C/D) - ask all of them together in one interactive call
- Questions that require free-text input - ask as plain text, one at a time
- Within a single round: ask free-text questions first, then ask the option-based questions together

---

### Group 1 of 3 - What you're building

**Free text (ask first):**

What are you building? Describe it in 2-3 sentences.

Wait for the user's answer, then use the AskUserQuestion tool with both questions together:

- Question 1: "What type of product is it?"
  - A: "SaaS web application"
  - B: "Mobile application (iOS / Android / both)"
  - C: "Marketplace or platform"
  - D: "Something else (internal tool, API)"

- Question 2: "Who is it for?"
  - A: "External customers (product for sale)"
  - B: "Internal team only"
  - C: "Both"

After receiving all answers for Group 1, output a summary block:

```
Here's what I understand so far:
- [1-sentence summary of what they're building]
- Product type: [type]
- Target: [users]

Is this correct, or do you want to change anything before we continue?
```

Wait for confirmation. If corrections needed, update and re-confirm. Then proceed to Group 2.

---

### Group 2 of 3 - Product shape

No free-text questions in this group. Use the AskUserQuestion tool with both questions together:

- Question 1: "What is the primary experience?"
  - A: "Mobile first" — description: "Main value delivered on mobile"
  - B: "Desktop first" — description: "Web/desktop: CRM, dashboard, admin tool"
  - C: "Both equally" — description: "Full parity across mobile and web"
  - D: "Not sure yet"

- Question 2: "Will the product be paid?"
  - A: "Yes - paid from day one" — description: "Subscription, one-time, or usage-based"
  - B: "Freemium" — description: "Free tier + paid upgrade"
  - C: "Free / internal" — description: "No revenue target"
  - D: "Not decided yet"

After receiving answers, output a summary block:

```
Adding to the picture:
- Platform: [platform]
- Business model: [model]

Does this match your intent, or anything to adjust?
```

Wait for confirmation. If corrections needed, update and re-confirm. Then proceed to Group 3.

---

### Group 3 of 3 - Context and starting point

Use the AskUserQuestion tool with both questions together first, then ask free-text questions:

- Question 1: "Where are you now?"
  - A: "Idea only" — description: "Nothing validated yet, starting from scratch"
  - B: "Have some research" — description: "Early customer insights or market knowledge"
  - C: "Validated problem" — description: "Ready to define strategy, problem is confirmed"
  - D: "Have strategy or specs" — description: "Moving to execution, know what to build"

- Question 2: "Who is building this?"
  - A: "Solo" — description: "Just me, no team"
  - B: "Small founding team" — description: "2-3 people, wearing multiple hats"
  - C: "Team with defined roles" — description: "PM, developers, designer"
  - D: "Corporate / enterprise team" — description: "Multiple stakeholders"

Wait for answers, then ask the following two free-text questions:

**Free text (ask after options):**

What matters most right now? What is the single most important thing you need to produce or figure out? (e.g., "validate whether the problem is real", "define MVP scope", "get to a spec I can build from")

Any constraints that shape how we approach this? (e.g., 3-month runway, regulated industry, must integrate with existing system, specific tech stack). Say "none" if not applicable.

After receiving all answers for Group 3, output a final summary block:

```
Complete picture:
- [1-sentence product description]
- Type: [type] | Platform: [platform] | Business model: [model]
- Target users: [users]
- Current stage: [stage]
- Priority: [what matters most]
- Team: [team type]
- Constraints: [constraints or none]

Ready to continue with this? Or anything to correct first?
```

Wait for final confirmation before proceeding to Step 4.

---

**Why these questions matter downstream:**
- Product type and platform strategy affect tech stack recommendations, Phase 6 approach, and which skills apply
- Internal vs. external changes compliance scope, pricing model, and go-to-market
- Business model (paid/free) drives KPI selection and exit gate criteria
- Team structure determines which Phase 1 skills are relevant (see Phase 1 adaptation rules below)
- Current stage determines starting phase directly

---

### Phase 1 Adaptation by Team Structure

Phase 1 skills are not all relevant for every team type. Apply these rules:

**Solo builder:**
- Skip: `/pm-stakeholder-map` (no stakeholders), `/pm-team-roster` (no team), `/pm-comms-charter` (no team communication)
- Keep: `/pm-project-charter` - simplified: assumptions, risks, personal constraints, success definition
- Phase 1 for solo = one skill

**Small founding team (2-3 people):**
- Skip: `/pm-stakeholder-map` (unless external investors or advisors are involved)
- Simplify: `/pm-team-roster` (decision rights matter, skill gaps matter - RACI overkill)
- Keep: `/pm-project-charter`, `/pm-comms-charter` (even 2 people need alignment on how they work)
- Phase 1 for small team = 2-3 skills

**Team with defined roles:**
- Run all 4 Phase 1 skills
- Full RACI and stakeholder map are worth the time

**Corporate / enterprise team:**
- Run all 4 Phase 1 skills
- Stakeholder map and escalation tree are critical - political complexity is real

---

## STEP 3B - Assessment

Combine documents (if any) with intake answers to produce a unified picture of the current state.

If documents exist: for each one, identify content type, phase mapping, and quality signals.

Then synthesize everything - documents + intake answers - into a structured assessment. This is the most important output of the entry point.

---

### Assessment Output Format

**1. Brief context** (2-3 sentences)
What Claude sees, the general picture, what kind of project and stage this appears to be - based on documents and intake answers combined.

**2. Document inventory** (skip section if no documents found)

```
| Document | Content type | Maps to | Quality |
|---|---|---|---|
| [filename or "intake answers"] | [e.g., Interview transcripts] | Phase 2 - Discovery (Track D) | ✅ Good / ⚠️ Partial / ❌ Thin |
```

**3. Phase coverage**

```
| Phase | Coverage | Source | Confidence |
|---|---|---|---|
| Phase 1 - Foundation         | ✅ / ⚠️ / ❌ | [document / intake / none] | High / Med / Low |
| Phase 2 - Discovery          | ✅ / ⚠️ / ❌ | | |
| Phase 3a - Validation        | ✅ / ⚠️ / ❌ | | |
| Phase 3b - Commercial Def.   | ✅ / ⚠️ / ❌ | | |
| Phase 4 - Domain             | ✅ / ⚠️ / ❌ | | |
| Phase 5 - Features           | ✅ / ⚠️ / ❌ | | |
```

**4. What Claude understands about this product**

Synthesize the actual product/market/customer picture. Be specific. Clearly mark the difference between **conclusions** (from documents or explicit user statements) and **assumptions** (inferred by Claude).

```
PROBLEM
  - [Conclusion] [what the problem is, from documents or stated by user]
  - [Assumption] [what Claude is inferring that wasn't explicitly stated]

CUSTOMER
  - [Conclusion] [who the primary customer is]
  - [Assumption] [...]

MARKET
  - [Conclusion] [what market context is established]
  - [Assumption] [...]

BUSINESS MODEL
  - [Conclusion] [revenue logic that's visible]
  - [Assumption] [...]

OPEN QUESTIONS
  - [What is unclear, missing, or contradictory - and why it matters]
```

**5. Confirmation**

```
Review the above. For each section:

  ✅ Confirm - correct
  ✗  Reject   - wrong, here's what's right: [correction]
  ~  Adjust   - partially right, here's the nuance: [adjustment]

Add anything I missed.
```

Wait for user response. Update the assessment based on corrections before proceeding.

After confirmation, save the finalized assessment to:
`pureinn-workspace/[slug]/assessment.md`

**5. Confirmation prompt**

```
Review the above. For each section:

  ✅ Confirm - this is correct
  ✗ Reject - this is wrong, here's what's correct: [correction]
  ~ Adjust - partially right, here's the nuance: [adjustment]

You can also add anything I missed.
```

Wait for user confirmation. Update the assessment based on their corrections before proceeding.

After confirmation, save the finalized assessment to:
`pureinn-workspace/[slug]/assessment.md`

---

## STEP 3C - Fast Track Detection

After assessment is confirmed, evaluate whether the user qualifies for a fast track. Check all three conditions independently.

---

### Fast Track 1 - Greenfield Express

**Triggers (all must be true):**
- Playbook = Greenfield
- Current stage (from intake Group 3) = "Validated problem, ready to define strategy" OR "Have a strategy or specs, moving to execution"
- Assessment shows: no significant unknown gaps in problem/customer/market understanding

**If triggered, surface proactively:**

```
Vyzerá to, že discovery a validáciu nepotrebuješ.

Express cesta:
  1. /pm-entity-registry     [lean] → entity list + základné stavy
  2. /pm-business-rules-library [lean] → kľúčové pravidlá, Draft mode
  3. /pm-features-list       → feature inventory + FEAT-IDs
  4. /pm-mvp-scope           → MVP scope + Delivery Stripes
  5. /pm-feature-design [FEAT-ID] → JIT spec, opakuj per feature
  → Build → Test → Release

Preskočíme: Phase 1 (Foundation), Phase 2 (Discovery), Phase 3a/3b (Validation + Commercial).

Use the AskUserQuestion tool:
- Question: "Ktorú cestu zvoliť?"
- Option A: "Express - preskočiť Discovery a Validation (Recommended)" — description: "Lean domain registers → feature list → JIT delivery"
- Option B: "Štandardný flow" — description: "Všetky fázy vrátane Discovery a Validation"
- Option C: "Čiastočný Discovery" — description: "Niektoré Phase 2 tracky chcem prejsť"
```

**Express lean mode rules:**
- `pm-entity-registry` lean: entity list + key states only, no full ERD, no Excalidraw
- `pm-business-rules-library` lean: core rules only, all Draft, finalize JIT per feature
- Skip: pm-domain-model, pm-privacy-requirements (unless regulated industry), pm-product-roadmap

---

### Fast Track 2 - Feature Implementation: First Run

**Triggers (all must be true):**
- Playbook = Feature Implementation
- No `state.json` exists for this project (first time with Pureinn on this product)

**If triggered, surface proactively:**

```
Existujúci produkt, prvý run s Pureinn.

Express cesta:
  1. /common-ground           → tech context z existujúceho kódu → COMMON-GROUND.md
  2. /pm-reverse-extract      → bootstrap z kódu:
                                 - extrahuje entities + business rules do registrov
                                 - generuje feature inventory (FDD formát)
                                 - pushne feature hierarchiu do Notion
                                 → ukáže čo našiel, ty opravíš ak treba
  3. /pm-feature-design [FEAT-ID] → JIT spec pre konkrétnu feature
  → Build → Test → Release (FI delivery pravidlá platia vždy)

Use the AskUserQuestion tool:
- Question: "Ktorú cestu zvoliť?"
- Option A: "Express - pm-reverse-extract bootstrap (Recommended)" — description: "Extrahuje entity, business rules a feature inventory priamo z kódu"
- Option B: "Štandardný Phase 0 onboarding" — description: "Manuálny setup: common-ground + impeccable document + pm-glossary + registre"
```

**Note on pm-reverse-extract bootstrap:** Extrahuje čo môže z kódu. Výsledok ukáže pred pokračovaním - user potvrdí alebo opraví. Štandardný PREREQ pattern.

**FI delivery rules vždy platia bez výnimky:**
- Feature flags (OFF by default), FE + BE
- Additive-only API + DB changes
- Full regression suite
- Performance gate (≤10% latency overhead)
- Gradual rollout: Internal → 5% → 25% → 50% → 100%
- Kill switch ak error rate >5%

---

### Fast Track 3 - Feature Implementation: Returning Session

**Triggers (all must be true):**
- Playbook = Feature Implementation
- `state.json` exists (Pureinn already ran on this project)
- Context files exist: `COMMON-GROUND.md` + domain registers

**If triggered, surface proactively:**

```
Kontext existuje z predošlej session.

Express cesta:
  → /pm-feature-design [FEAT-ID] priamo

Ktorú feature ideme špecifikovať?
(alebo: /pm-stripe pre delivery dashboard ak chceš vidieť stav všetkých stripes)
```

**Note:** Ak FEAT-ID ešte neexistuje (nová feature nie je v `feature_list.md`):
1. Pridaj feature do `feature_list.md` manuálne (FEAT-[DOMAIN]-[NUMBER] formát)
2. Vytvor stub Feature Card v `features/cards/`
3. Potom spusti `/pm-feature-design [FEAT-ID]`

---

## STEP 4 - Playbook Selection

If not already determined from document analysis, use the AskUserQuestion tool:

- Question: "Does the product already exist in any form?"
  - A: "No - building from scratch"
  - B: "Yes, but no active users yet"
  - C: "Yes, with active users - adding features" (Recommended if product exists)
  - D: "Yes, with active users - rebuilding or migrating from old docs" — description: "Existing code + legacy docs (BRD/FSD/domain models) that need reconciling into a clean Pureinn structure"

Map to playbook:
- A or B → **Greenfield**
- C → **Feature**
- D → **Rebuild**

**Feature playbook note:**
Feature Implementation does not start at Phase 1. It starts at Phase 0 (context setup).
Phase 0 runs once per project onboarding - not per feature. After Phase 0, each feature goes through Feature Viability Assessment before any spec work begins.
If Phase 0 is already done (context exists from a prior session), skip to Feature Viability Assessment.

**Rebuild playbook note:**
Rebuild is for an existing product onboarded to Pureinn where legacy docs and the codebase disagree. Route by what the user has:
```
- Existing code + legacy docs (BRD/FSD/domain models) that may conflict with the code:
  → /pm-reconcile  (first plans which areas to reconcile and in what order, then reconciles
                    per layer: /pm-reconcile domain → rules → features. Produces a living
                    Reconciliation Report and rebuilds the registers + feature inventory clean.
                    Track multi-session progress with /pm-reconcile-status. Old docs become reference only.)
- Existing code, docs already clean or absent (just need to bootstrap from code):
  → naive migration path: /pm-entity-registry + /pm-business-rules-library + /pm-reverse-extract
- Greenfield rewrite (throwing the code away): → Greenfield playbook
```
Confirm which case fits, then route. For the first case, `/pm-reconcile` is the entry point.

---

## STEP 5 - Starting Phase Determination

Based on the document analysis and confirmed assessment, determine the starting phase:

- Phase covered with high confidence → mark as done, skip
- Phase covered but partial or low confidence → flag gaps, user decides: fill gaps first or proceed with acknowledged risk
- Phase not covered → must be done

Starting phase = lowest incomplete phase.

If guidance mode is ON, before announcing the starting phase add:

```
[Phase N] - [Phase Name] is where we start because [1-2 sentences explaining
what this phase accomplishes and why it's the right entry point given what you have].
```

---

## STEP 6 - Workspace Setup

If no state.json exists yet:

1. Derive `project-slug`: lowercase, kebab-case, max 30 chars.
2. Create the artifact folder structure (playbook-aware):

**Greenfield:**
```
pureinn-workspace/[slug]/
  state.json
  assessment.md
  glossary.md                                    ← pm-glossary (cross-phase)
  product/
    PRD_master.md                                ← pm-prd [Product PRD - frozen after Phase 3b]
  domain/                                        ← 4 living registers (append per initiative)
    entities.md                                  ← pm-entity-registry (Live Register 1)
    business_rules.md                            ← pm-business-rules-library (Live Register 2)
    decision_models.md                           ← pm-business-rules-library (Live Register 3)
  features/
    feature_list.md                              ← pm-features-list (Live Register 4 - append per initiative)
    cards/                                       ← Feature Cards (one per feature)
  initiatives/                                   ← one subfolder per major domain initiative
    [initiative-slug]/                           ← e.g., ai-onboarding
      discovery/                                 ← Track B outputs for this initiative
      prd.md                                     ← pm-prd [Initiative PRD, scoped to this domain]
      kano-analysis.md                           ← pm-features-list (initiative-scoped)
      value-complexity-matrix.md                 ← pm-features-list (initiative-scoped)
  artifacts/
    phase-1-foundation/_index.md                 ← Foundation & Collaboration Setup
    phase-2-discovery/_index.md                  ← Ideation & Discovery
    phase-3-define/_index.md                     ← Define & Validation
    phase-4-domain/_index.md                     ← Domain Modeling + Register Setup
    phase-5-planning/_index.md                   ← Feature Planning
  team/                                          ← operational, created on demand
    onboarding/                                  ← pm-onboarding (role-specific briefs)
  meetings/                                      ← pm-meeting (per-meeting notes, created on demand)
  prototypes/                                    ← pm-prototype (prototype specs + results, created on demand)
  stress-tests/                                  ← pm-stress-test (pushback rehearsals + prep summaries, created on demand)
  root-cause/                                    ← pm-root-cause (anomaly investigations, created on demand)
```

`team/`, `meetings/`, `prototypes/`, `stress-tests/` and `root-cause/` are cross-cutting operational folders - created on demand by `pm-onboarding` / `pm-meeting` / `pm-prototype` / `pm-stress-test` / `pm-root-cause`, not part of the phase artifact flow.

**Feature Implementation:**
```
pureinn-workspace/[slug]/
  state.json
  assessment.md
  glossary.md
  domain/
    entities.md                                  ← append per initiative
    business_rules.md                            ← append per initiative
    decision_models.md                           ← append per initiative
  features/
    feature_list.md                              ← append per initiative
    cards/
  initiatives/
    [initiative-slug]/
      discovery/
      prd.md
      kano-analysis.md
      value-complexity-matrix.md
```

Each `_index.md` is a one-line placeholder: `# [Phase Name] - artifacts will appear here.`
This creates the folder and makes the structure visible in any file explorer.

**2b. Create `_archive/` folder and `.claudeignore`**

Create `_archive/` in the project root (alongside the working directory, not inside pureinn-workspace):
```
_archive/
  .gitkeep
```

Create `.claudeignore` in the project root:
```
_archive/
```

Tell the user:
```
_archive/ vytvorený - sem presúvaj staré FSD/BRD/feature cards pred tým ako spustíš pm-reverse-extract.
.claudeignore vytvorený - Claude _archive/ pri skenovaní preskočí.
```

**2c. Create pureinn-variables.md**

Create `pureinn-workspace/[project-slug]/pureinn-variables.md` with the following content (all URLs blank - user fills them in):

```markdown
# pureinn-variables.md - [Project Name]
# Edit this file to connect Notion to this project.
# Skills read these URLs automatically. Leave blank to be asked when needed.
# DB = database (push supported). Page = single Notion page (referenced/linked).

## Core

| Key | Type | URL |
|---|---|---|
| Dashboard | Page | |
| Feature Backlog | DB | |

## Product (Phase 2-3)

| Key | Type | Skill | URL |
|---|---|---|---|
| PRD Master | Page | pm-prd | |
| Product Roadmap | Page | pm-product-roadmap | |
| Elevator Pitch | Page | design-thinking | |
| Lean Canvas | Page | pm-lean-canvas | |
| Business Model Canvas | Page | pm-business-model | optional |
| Kotler Five Levels | Page | pm-kotler | |
| Competitor Analysis | Page | pm-market-analysis | |
| SWOT Analysis | Page | pm-market-analysis | |

## Research (Phase 2)

| Key | Type | Skill | URL |
|---|---|---|---|
| Customer Personas | Page | pm-personas | |
| Customer Discovery | Page | pm-problem-validation | |
| Customer Interviews | DB | pm-personas | |
| Research Lab | DB | pm-market-analysis | |

## Validation (Phase 3a)

| Key | Type | Skill | URL |
|---|---|---|---|
| Hypothesis Validation | Page | pm-hypotheses | |

## Commercial Definition (Phase 3b)

| Key | Type | Skill | URL |
|---|---|---|---|
| OKRs | Page | pm-kpis | |
| KPIs | DB | pm-kpis | |
| Investor Pitch | Page | pm-pitch-deck | |

## Engineering (Phase 4-6)

| Key | Type | Skill | URL |
|---|---|---|---|
| Domain Model | Page | pm-domain-model | |
| Entity Registry | Page | pm-entity-registry | |
| Business Rules Library | Page | pm-business-rules-library | |
| Architecture | Page | architecture-designer | |
| Diagrams | Page | pm-diagrams | |

## Business Logic DBs (Phase 4-6)

| Key | Type | Skill | URL |
|---|---|---|---|
| Business Rules | DB | pm-business-rules-library | |
| Decision Models | DB | pm-business-rules-library | |
| Event Catalogue | DB | pm-domain-model | |

## Domain Model DBs (Phase 4)

| Key | Type | Skill | URL |
|---|---|---|---|
| Internal Entity Catalogue | DB | pm-domain-model | |
| External Entity Catalogue | DB | pm-domain-model | |
| Data Sensitivity Map | DB | pm-privacy-requirements | |

## Knowledge

| Key | Type | Skill | URL |
|---|---|---|---|
| Glossary | DB | pm-glossary | |
| Meetings | DB | pm-meeting | |
| Open Questions | DB | pm-hypotheses | |

## Design (Phase 6-7)

| Key | Description | Value |
|---|---|---|
| figma_project_url | Figma project URL - root of the product design file. Read by pm-feature-design when Figma MCP is connected. | |
| figma_design_system_url | Figma design system / component library URL (if separate from main project file). | |

## Prototyping (cross-phase)

Prototyping tool endpoints read by pm-prototype. You may configure more than one - pm-prototype lets you pick which to target per run. Leave blank to use manual copy-paste (spec is always paste-ready).

| Key | Description | Value |
|---|---|---|
| lovable_mcp | Lovable MCP endpoint (https://mcp.lovable.dev) - functional full-stack prototypes. Live account access + real credits. | |
| v0_mcp | v0 / Vercel endpoint - fast UI generation + deploy URL. | |
| figma_make_mcp | Figma Make endpoint - design-native prototypes. | |
| prototype_default_tool | Which tool pm-prototype should suggest first (lovable / v0 / figma_make). | |

## AI Research

| Key | Description | Value |
|---|---|---|
| OPENAI_API_KEY | OpenAI API key - required for Path C (AI-powered market research) in pm-market-analysis | |
```

After creating the file, tell the user:

```
pureinn-variables.md created.

To connect Notion, you have two options:

  A) Use the Pureinn Notion template (recommended)
     Duplicate it to your workspace, then paste the URLs here.
     Template + setup guide: see NOTION_TEMPLATE.md in the plugin folder.

  B) Use your own Notion setup
     Open pureinn-variables.md and paste the URLs of your existing pages and databases.
     Leave rows blank - skills will ask when they first need each item.

Skills read pureinn-variables.md automatically. No need to re-enter URLs during skill runs.
```

**How skills read pureinn-variables.md:**

When a skill needs a Notion URL, it:
1. Reads `pureinn-workspace/[slug]/pureinn-variables.md`
2. Finds the row matching the Key it needs (e.g., "Glossary", "Feature Backlog")
3. Uses the URL in that row
4. If URL is blank: asks the user, then saves the provided URL back to pureinn-variables.md
5. For DBs: checks `state.json` for a cached data_source_id before calling notion-fetch

**state.json caches notion data source IDs** (so notion-fetch is called at most once per DB per project):

```json
"notion_ids": {
  "feature_backlog": null,
  "glossary": null,
  "kpis": null,
  "business_rules": null,
  "decision_models": null,
  "event_catalogue": null,
  "internal_entity_catalogue": null,
  "external_entity_catalogue": null,
  "data_sensitivity_map": null,
  "customer_interviews": null,
  "research_lab": null,
  "meetings": null,
  "open_questions": null
}
```

**Artifact save paths by skill (reference for all skills in this project):**

| Skill | Artifact | Path |
|---|---|---|
| pm-stakeholder-map | stakeholder-map.md, raci-matrix.md, escalation-tree.md | artifacts/phase-1-foundation/ |
| pm-project-charter | project-charter.md, assumptions-risks-register.md | artifacts/phase-1-foundation/ |
| pm-team-roster | team-roster.md, decision-rights-matrix.md, skill-gap-assessment.md | artifacts/phase-1-foundation/ |
| pm-comms-charter | communication-charter.md, meeting-rhythm.md | artifacts/phase-1-foundation/ |
| pm-tech-feasibility | tech-feasibility-report.md | artifacts/phase-2-discovery/ |
| pm-domain-analysis | domain-analysis-report.md, legal-regulatory-requirements.md | artifacts/phase-2-discovery/ |
| pm-market-analysis | market-size-analysis.md, competitor-analysis.md, swot-analysis.md, market-timing-rationale.md | artifacts/phase-2-discovery/ |
| pm-personas | customer-segments.md, personas.md, early-adopters-profile.md | artifacts/phase-2-discovery/ |
| jtbd-building | jtbd-analysis.md | artifacts/phase-2-discovery/ |
| pm-problem-validation | problem-validation-summary.md | artifacts/phase-2-discovery/ |
| design-thinking | design-thinking-synthesis.md | artifacts/phase-3-define/ |
| pm-hypotheses | hypothesis-register.md, go-no-go.md | artifacts/phase-3-define/ |
| pm-kotler | kotler-five-levels.md | artifacts/phase-3-define/ |
| pm-lean-canvas | lean-canvas.md | artifacts/phase-3-define/ |
| pm-business-model | business-model-canvas.md | artifacts/phase-3-define/ |
| pm-kpis | north-star-metric.md, aarrr-metrics.md, okrs.md | artifacts/phase-3-define/ |
| pm-business-case | business-case.md | artifacts/phase-3-define/ |
| pm-prd | PRD_master.md (Greenfield, frozen) / initiatives/[slug]/prd.md (FI Initiative mode) | product/ or initiatives/[slug]/ |
| pm-product-roadmap | product-roadmap-v1.md | artifacts/phase-3-define/ |
| pm-pitch-deck | pitch-deck-brief.md | artifacts/phase-3-define/ |
| pm-domain-model | domain-model.md | artifacts/phase-4-domain/ |
| pm-entity-registry | entities.md | domain/ (Live Register 1) |
| pm-business-rules-library | business_rules.md, decision_models.md | domain/ (Live Registers 2+3) |
| pm-privacy-requirements | pii-inventory.md, privacy-requirements.md, gdpr-action-plan.md | artifacts/phase-4-domain/ |
| pm-product-roadmap | product-roadmap-v2.md | artifacts/phase-4-domain/ |
| pm-features-list | feature_list.md + stub FEAT-*.md cards | features/ + features/cards/ (Live Register 4) |
| pm-mvp-scope | mvp-scope.md, delivery-stripes.md | artifacts/phase-5-planning/ |
| pm-reverse-extract | feature_list.md, delivery-stripes.md | features/ (migration path - updates root state.json) |
| pm-product-roadmap | product-roadmap-v3.md | artifacts/phase-5-planning/ |
| pm-feature-design | (updates Feature Card Sections 1-3 + domain registers in place) | features/cards/ + domain/ |
| pm-feature-card | FEAT-[DOMAIN]-[NUMBER].md | features/cards/ |
| pm-stripe | (orchestration only - updates Feature Card frontmatter status) | features/cards/ |
| pm-glossary | glossary.md | [slug]/ root |

3. Write `pureinn-workspace/[project-slug]/state.json`:

```json
{
  "project": "[human-readable name]",
  "slug": "[project-slug]",
  "created": "[ISO 8601 date]",
  "guidance_mode": true,
  "playbook": "[Greenfield | Feature | Rebuild]",
  "starting_phase": [N],
  "current_phase_index": [N],
  "current_phase_name": "[name]",
  "phases_completed": [],
  "phases_skipped": [],
  "phase_3a_verdict": null,
  "input": "[original user input]",
  "product_shape": {
    "type": "[SaaS | Mobile | Marketplace | Internal | API | Other]",
    "audience": "[External | Internal | Both]",
    "platform_strategy": "[Mobile first | Desktop first | Both | Unknown]",
    "business_model": "[Paid | Freemium | Free | Unknown]"
  },
  "team_structure": "[Solo | Small founding team | Team with roles | Corporate]",
  "documents_found": ["[list of filenames read]"],
  "assessment_file": "assessment.md",
  "current_stripes": [],
  "registers": {
    "entities_initialized": false,
    "business_rules_initialized": false,
    "decision_models_initialized": false,
    "feature_list_initialized": false
  },
  "notion_ids": {
    "feature_backlog": null,
    "glossary": null,
    "kpis": null,
    "business_rules": null,
    "decision_models": null,
    "event_catalogue": null,
    "internal_entity_catalogue": null,
    "external_entity_catalogue": null,
    "data_sensitivity_map": null,
    "customer_interviews": null,
    "research_lab": null,
    "meetings": null,
    "open_questions": null
  }
}
```

Notion integration uses two files:
- `pureinn-variables.md` - human-editable URLs per project (created at init, user fills in)
- `state.json notion_ids` - cached data source IDs fetched from Notion (never edit manually)

Skills always read the URL from pureinn-variables.md first, then check notion_ids for a cached ID. If no cached ID, they call notion-fetch and save the result.

Fields updated by `/pm-stripe` during Phase 6-7:
- `current_stripes` - array of active Stripe names (parallel stripes supported)

Note: individual feature status is tracked in Feature Card frontmatter (`status` field) and `feature_list.md`, not state.json.
Note: `registers` flags are set to `true` by pm-entity-registry and pm-business-rules-library after first initialization.
Note: `phases_completed` uses string identifiers - "1", "2", "3a", "3b", "4", "5", "6-7". Phase 3 split is tracked as two separate entries.
Note: `phase_3a_verdict` stores the Go/No-Go outcome: "GO", "PIVOT", or "STOP". Set by /pm-hypotheses [Results mode] or by "done elsewhere" import. Phase 3b entry is blocked until this field is "GO".

---

## STEP 7 - Dashboard and Routing

Display the project dashboard. Phase status display depends on playbook:

**Greenfield dashboard:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROJECT: [Product Name]
PLAYBOOK: Greenfield
GUIDANCE: [On / Off]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PHASE STATUS
  Phase 1 - Foundation & Collaboration          [✅ Done / ⏭ Skipped / 🔲 To do]
  Phase 2 - Discovery                           [✅ Done / ⚠️ Partial / ⏭ Skipped / 🔲 To do]
  Phase 3a - Validation                         [✅ Done / ⚠️ Partial / ⏭ Skipped / 🔲 To do]
  Phase 3b - Commercial Definition              [✅ Done / ⚠️ Partial / ⏭ Skipped / 🔲 To do]
  Phase 4 - Domain Modeling + Register Setup    [🔲 To do]
  Phase 5 - Feature Planning                    [🔲 To do]
  Phase 6 + 7 - Delivery Cycle (JIT)            [🔲 To do]

STARTING FROM: Phase [N] - [Phase Name]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Feature Implementation dashboard:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROJECT: [Product Name]
PLAYBOOK: Feature Implementation
GUIDANCE: [On / Off]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PHASE STATUS
  Phase 0 - Context Setup                [✅ Done / 🔲 To do]
             (pureinn + common-ground + impeccable document - runs once)
  Feature Viability Assessment           [runs per feature]
             (KANO + V×C + demand validation + MDP + success metrics)
  Track A / Track B                      [determined per feature]
  JIT Design (/pm-feature-design)        [Feature Card Sections 1-3 + register finalization per feature]
  Delivery Cycle (Phase 6 + 7)           [🔲 To do]
             (same as Greenfield JIT + backward compat + feature flags + regression)

CURRENT FEATURE: [feature name or "none - viability assessment pending"]
ACTIVE STRIPE: [stripe name or "none"]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Rebuild dashboard:** entry point is `/pm-reconcile` (plan, then per-layer reconcile: domain → rules → features). Show reconcile progress via `/pm-reconcile-status`. After all areas are done, the project drops into the Phase 6 JIT delivery cycle - show the standard stripe/feature queue.

Then show the skills queue for the current phase.

If guidance mode is ON, precede the queue with the phase purpose:

```
PHASE [N] - [PHASE NAME]
[2-3 sentences: what this phase is trying to achieve, what the output is, why it matters for what comes next]
```

Then always show:

```
SKILLS FOR THIS PHASE (run in order):

  1. /[skill-name]
     → Produces: [artifacts]
     → Input needed: [what to prepare or bring]

  2. /[skill-name]
     → Produces: [artifacts]
     → Input needed: [what to prepare or bring]

  [👤 Human activity: e.g., conduct interviews]
     → Before running /[next-skill]

  3. /[skill-name]
     → Produces: [artifacts]

Each skill checks your current state when you run it.
Run /pureinn again after this phase is complete to advance.
```

---

## Phase → Skills Reference

### Phase 1 - Foundation & Collaboration Setup
```
Skills shown depend on team structure (set during intake):

Solo builder:
  /pm-project-charter    → Project Charter (simplified: assumptions, risks, success definition)

Small founding team:
  /pm-project-charter    → Project Charter, Assumptions & Risks Register
  /pm-team-roster        → Decision Rights, Skill Gap Assessment (RACI skipped)
  /pm-comms-charter      → Communication Charter, Meeting Rhythm

Team with defined roles / Corporate:
  /pm-stakeholder-map    → Stakeholder Map, RACI, Escalation Tree
  /pm-project-charter    → Project Charter, Assumptions & Risks Register
  /pm-team-roster        → Team Roster, Decision Rights, Skill Gap Assessment
  /pm-comms-charter      → Communication Charter, Meeting Rhythm
```

### Phase 2 - Ideation & Discovery
```
/pm-tech-feasibility   → Tech Feasibility Report
                         [🔍 Before: research with Perplexity / Tech Lead input]
/pm-domain-analysis    → Domain Analysis, Legal Requirements
                         [🔍 Before: Perplexity research on domain + regulations]
/pm-market-analysis    → Market Size, Competitor Analysis, SWOT, Market Timing
                         [🔍 Before: Perplexity market data + competitor research]
/pm-personas           → Customer Segments, Personas, Early Adopters Profile
                         [👤 Before: ≥10 customer interviews / SynthFolk / ChatGPT]
/jtbd-building         → JTBD Analysis
                         [Run after /pm-personas - uses personas as input]
/pm-problem-validation → Problem Validation Summary (Phase 2 exit artifact)
                         [Synthesizes all Track A-D outputs - run last in Phase 2]
```

### Phase 3a - Validation
```
Character: externally-paced. AI accelerates structuring, not signal collection.
Can start: once Problem Validation Summary exists (parallel with late Phase 2 is fine).

"Done elsewhere" path: if Design Thinking + hypothesis validation were done outside
this framework (Miro, workshop, other tool), run /pureinn and say "Phase 3a done elsewhere."
The orchestrator will collect: Go/No-Go verdict, key evidence per hypothesis type,
riskiest assumptions tested. Phase 3a is then marked complete and 3b can start.

/design-thinking       → Problem Statement, POV, HMW, Ideation synthesis, Elevator Pitch
                         [Outputs Validation Hypotheses draft → feeds into /pm-hypotheses]
/pm-hypotheses         → Hypothesis Register: ICP, assumption map, experiment plan, success criteria
  [Plan mode]            [Run immediately after /design-thinking]
                         [Assigns experiment type per hypothesis - Problem / Customer / Solution / Market]
                         [Success criteria defined BEFORE experiments run]
[👤 Experiments run]   → Landing page / Smoke test / Pre-order / Rapid Prototype / Concierge MVP
                         [Human activity - execute the experiment plan from /pm-hypotheses]
/pm-hypotheses         → Go/No-Go Decision (Go / Pivot / Stop)
  [Results mode]         [Run after all assigned experiments complete]
                         [HARD GATE: GO required to enter Phase 3b. PIVOT loops back. STOP ends project.]
```

### Phase 3b - Commercial Definition
```
Character: AI-assisted synthesis sprint. With clean Phase 3a inputs, this is
Quality depends entirely on Phase 3a rigor.
Condition: only starts after GO verdict from Phase 3a. No FORCE bypass for this gate.

"Done elsewhere" path: if you already have a Lean Canvas, financial model, or
existing commercial strategy artifacts, bring them via Path A in each skill.
State "Phase 3b partially done elsewhere" and list which artifacts exist.

/pm-kotler             → Product Definition (5 levels: Core / Basic / Expected / Augmented / Potential)
/pm-lean-canvas        → Lean Canvas (one-page, problem-focused - default for startups)
/pm-business-model     → Business Model Canvas (optional fuller alternative - established or complex operational models)
/pm-kpis               → North Star Metric, AARRR, OKRs
/pm-business-case      → Business Case (3-year projections, Go/No-Go)
/pm-product-roadmap    → Product Roadmap v1
/pm-prd                → PRD - Phase 3b exit artifact (synthesizes all Phase 2+3a+3b)
                         [PRD_master.md is frozen after creation - immutable from this point]
/pm-pitch-deck         → Pitch Deck content brief (slide-by-slide spec → Gamma visual deck)
                         [Optional - run if raising capital, selling to customers, or pitching partners]
                         [Requires: pm-lean-canvas + pm-business-case + pm-problem-validation]
                         [Gamma MCP required for visual output; skill outputs content brief if Gamma not connected]
```

### Phase 4 - Domain Modeling + Register Setup (FDD Stage 1)
```
/pm-domain-model            → Domain Model, ERD + optional Excalidraw domain diagram
/pm-entity-registry         → entities.md: entity list + Mermaid state machines per entity
                               (guard conditions TBD - added JIT by pm-feature-design)
/pm-business-rules-library  → business_rules.md + decision_models.md (Draft mode)
                               (rules finalized JIT by pm-feature-design before each feature build)
/pm-privacy-requirements    → PII Inventory, Privacy Requirements, GDPR action plan
/pm-product-roadmap         → Product Roadmap v2 (update with domain constraints)
```

### Phase 5 - Feature Planning (FDD Stage 2)
```
/pm-features-list      → feature_list.md (FDD Feature List - Live Register 4)
                          → FEAT-[DOMAIN]-[NUMBER] ID format
                          → KANO Analysis + V×C Matrix
                          → Stub Feature Cards created in features/cards/
                          → Notion push: Feature entries (Status=Backlog, Priority from KANO+V×C)
/pm-mvp-scope          → MVP Scope (IN/POST-MVP/CUT), Delivery Stripes (domain-focused channels)
                          → Feature-to-Stripe assignment, dependency sequencing per stripe
                          → Updates stripe: field in each Feature Card frontmatter
                          → Notion: enrich Features with Phase/Stripe
/pm-product-roadmap    → Product Roadmap v3 (update with feature and delivery view)
```

### Pre-Phase 6 - Technical Foundation
```
/common-ground         → Tech stack, repo structure, COMMON-GROUND.md
[👤 Architecture decisions, infrastructure setup]
```

---

### Cross-Phase Skills (run at any time)
> These skills are not tied to a specific phase. Run them progressively throughout the project or on demand.

```
/pm-glossary           → Project Glossary (terms, entities, artifacts, abbreviations)
                         [Continuous - run after each phase or when new terminology surfaces]
                         [Also run on demand: /pm-glossary add "term1, term2"]

/pm-diagrams           → Visual diagrams (two rendering modes)
                         [Mermaid.js - primary for Claude Code: state machines (entities.md),
                          sequence diagrams (Feature Card Section 3)]
                         [Excalidraw - secondary for human communication: Domain Model Overview,
                          User Flow, Business Process Model, System Architecture, JTBD Four Forces]
                         [Excalidraw types require: Excalidraw MCP connected]
```

---

### Feature Implementation - Phase Sequence
> Use this section when playbook = Feature. Replaces Phases 1-5 entirely.

```
MIGRATION PATH (existing product built outside the framework)
  /pureinn              → always first: workspace setup, state.json, pureinn-variables.md
  /common-ground        → technical context (stack, APIs, debt) → COMMON-GROUND.md
  /impeccable document     → design context (design system, components) → PRODUCT.md + DESIGN.md
  /pm-glossary          → start domain glossary

  TWO SUB-PATHS:

  A) Legacy docs exist and may conflict with the code (old BRD/FSD/domain models),
     and/or the team is changing - you need one reconciled source of truth:
     /pm-reconcile       → scans code, parses old docs, reconciles (code = structural truth,
                            docs = business logic, conflicts → AskUserQuestion)
                          → Reconciliation Report (the team's "where are we" brief)
                          → then orchestrates the rebuild below in reconciled mode.
                          This is the entry point - run it instead of the three skills standalone.

  B) Docs already clean or absent - just bootstrap from code:
     /pm-entity-registry   → entities.md (extract from existing codebase/docs)
     /pm-business-rules-library → business_rules.md + decision_models.md (extract existing rules)
     /pm-reverse-extract   → reads existing Feature Cards/codebase
                          → extracts feature inventory in FDD format (FEAT-[DOMAIN]-[NUMBER])
                          → Notion: creates Feature hierarchy (primary: team visibility)
                          → generates feature_list.md, delivery-stripes.md
                          Use INSTEAD of pm-features-list + pm-mvp-scope.

  Both then proceed to Phase 6 + 7 (JIT per feature) directly.

─────────────────────────────────────────────

PHASE 0 - CONTEXT SETUP  [runs once per project onboarding, not per feature]
  /pureinn              → Product context (users, roadmap, known problems, workarounds)
  /common-ground        → Technical context (stack, domain model, APIs, debt) → COMMON-GROUND.md
  /impeccable document     → Design context (design system, UX patterns, components) → PRODUCT.md + DESIGN.md

  Exit: All three dimensions covered. Team has shared product understanding.
  Skip if already done (context files exist from a prior session).

─────────────────────────────────────────────

FEATURE VIABILITY ASSESSMENT  [runs per feature, before any spec work]

  Feature Target Profile
    → Which existing segment/persona does this serve?
    → KANO: Must-be / Performance / Delighter / Indifferent
    → V×C: Quick Win / Big Bet / Fill-in / Time Waster
    → Usage frequency + % of user base

  Demand Validation
    → Existing signal: analytics, support tickets, feature requests
    → Lightweight experiments if signal weak: fake door, mockup test, landing page
    → B2B: pilot commitment or letter of intent

  Strategic Alignment
    → Core vs. Adjacent: build vs. buy vs. integrate
    → Business impact: revenue / churn / support / strategic

  MDP Definition
    → Minimum Delightful Product: core value only
    → What is explicitly deferred to V1.1

  Success Metrics  [defined before build, dashboard set up before code is written]
    → Depth of usage (return rate, consistency)
    → Behavior change (does it shift workflow?)
    → Business impact (retention, conversion, support cost)
    → Avoid vanity metrics (raw clicks, impressions, DAU without depth)

─────────────────────────────────────────────

TRACK A - KNOW WHAT WE WANT  [skip Track B if here]

  Feature Set Assignment (grouping only - no longer a spec unit):
    Existing FS → feature is added to feature_list.md with existing stripe assignment
    New domain  → run /pm-entity-registry + /pm-business-rules-library (Draft mode) for that domain

  JIT Design (one feature at a time, per stripe):
    /pm-feature-design [FEAT-ID]  → Sections 1-3 of Feature Card + register finalization
                                    (scans existing codebase before generating sequence diagram)
    [Design Inspection]           → Team review (or solo confirm)
    Build skills                  → reads Feature Card Section 3 as build spec

─────────────────────────────────────────────

TRACK B - KNOW THE AREA, NOT THE SOLUTION  [discovery needed, output → Track A]

  Save all discovery outputs to: initiatives/[initiative-slug]/discovery/

  [👤 Human] User research (5-10 interviews, target segment only)
  [👤 Human] Competitive analysis (if solution direction unclear)
  [👤 Human] Tech feasibility (with existing stack)
  /pm-business-case   → Feature Business Case (revenue/retention impact, ROI, Go/No-Go)
  /pm-kpis            → Feature Success Metrics (depth / behavior / business impact)

  After discovery - if new domain is involved (new entities, new business rules):
  /pm-prd [Initiative mode] → initiatives/[slug]/prd.md (Business Capabilities for this domain)
  /pm-entity-registry       → domain/entities.md (append mode - new domain entities)
  /pm-business-rules-library → domain/business_rules.md + decision_models.md (append mode)
  /pm-features-list [FI append] → features/feature_list.md (append) + stubs in features/cards/
                                   KANO + V×C saved to initiatives/[slug]/

  Apply KANO + V×C to defined features → enter Track A.

─────────────────────────────────────────────

DELIVERY CYCLE  [same JIT per Feature as Greenfield Phase 6+7, with FI additions]
  /pm-stripe + /pm-feature-design + build skills (see Phase 6+7 section below)
  Feature Implementation additions per feature:
    ⚠️ All new code wrapped in feature flag (OFF by default), FE + BE both respect flag
    ⚠️ API changes: additive only, or v2 alongside v1 with deprecation timeline
    ⚠️ DB changes: additive only (new tables, new columns) - no renames, no deletes
    ⚠️ Full regression suite per feature before merge
    ⚠️ Performance gate: feature adds ≤10% latency to existing API calls
    ⚠️ Gradual rollout: Internal → 5% → 25% → 50% → 100%
    ⚠️ Kill switch: disable flag if error rate >5%
```

---

### Phase 6 + 7 - FDD Delivery Cycle (JIT per Feature, Stripe-based)

Phase 6 and 7 run as an integrated JIT cycle. Spec and build happen per Feature, not per Feature Set.
Each Delivery Stripe = a domain-focused parallel channel (not a time-box).
Feature status is tracked in Feature Card frontmatter and feature_list.md.
Domain registers (entities.md, business_rules.md, decision_models.md) are the living source of truth.

```
STRIPE ORCHESTRATION (use for every Stripe)
/pm-stripe             → Stripe dashboard, advance next feature, mark Design Inspection passed,
                          mark feature Promoted, run Impact Analysis when BR changes

JIT CYCLE PER FEATURE (orchestrated by /pm-stripe)
Step 0 (optional): /pm-feature-viability [FEAT-ID]
          → KANO classification, MDP scope, success metrics
          → Skip if feature already scoped, committed, or in validated roadmap

Step 1: /pm-feature-design [FEAT-ID]
          → Pre-step (Feature Implementation mode only): scan real service files
          → Commit 1: spec([FEAT-ID]): guard conditions + rule finalization
            - entities.md: guard conditions added to state transitions
            - business_rules.md: Draft rules updated to Final
            - decision_models.md: decision table rows finalized
          → Commit 2: spec([FEAT-ID]): feature design complete
            - Feature Card Section 1 (Biznis Mantinely - BR-IDs, entity guard conditions)
            - Feature Card Section 2 (Acceptance Criteria)
            - Feature Card Section 3 (Mermaid sequenceDiagram + files to modify + UX/UI context)
          → Status: 2_Spec_Done

Step 2: Design Inspection (/pm-stripe) [Team mode: human review of Sections 1-3]
          → Status: 3_Ready_to_Build
          [Solo mode: AI generates, human confirms - same gate, lighter ritual]

Step 3: BUILD SKILLS (/pm-stripe → Phase 7)
          → Status: 4_In_Build (set when build skills start)
/fullstack-guardian    → BE implementation (reads Feature Card Section 3)
/impeccable-craft      → FE implementation (reads Feature Card Section 3)
/test-master           → Unit + integration tests
/playwright-expert     → E2E tests
/code-reviewer         → Code review
/impeccable-audit      → Code quality review
/impeccable-harden     → Security hardening
/security-reviewer     → Security audit
/devops-engineer       → CI/CD, deployment
/monitoring-expert     → Observability, alerting

Step 4: Feature Card Section 4 (Realizacny Protokol) filled
          → Commits, test files, flag OFF verification
          → Status: 5_In_Review (set when build complete, before final review)
          → Code Inspection result recorded
          → Status: 6_Shipped (Feature Card immutable after this)

SPEC GATE (hard rule, enforced by /pm-stripe before routing to build):
  Feature Card Sections 1-3 must be complete
  Status must be 3_Ready_to_Build

ATOMIC COMMIT PROTOCOL (parallel stripe safety):
  Register updates (entities.md, business_rules.md, decision_models.md) committed BEFORE code
  Two commits per feature: register update first, Feature Card update second
  One feature at a time per stripe in active design/build (prevents register conflicts)

OPTIONAL SPEC SUPPORT
/architecture-designer → System Design Blueprint, ADRs (if needed)
/api-designer          → API contracts, OpenAPI spec (if needed)
/impeccable document   → PRODUCT.md + DESIGN.md [run once at Phase 6 start]
/impeccable-shape      → UX/UI shape brief per feature
```

---

## Exit Gate (when user runs /pureinn after completing a phase)

Check state.json: if `current_phase_index` has increased or user states a phase is done, run exit gate.

Read exit gate thresholds from the relevant playbook file.

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EXIT GATE - Phase [N]: [Phase Name]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Show quantitative thresholds from playbook]

For each threshold, did you meet it? (yes / no / unknown)
```

If all critical thresholds met:
```
Exit gate passed. Phase [N] complete.

Type GO to advance to Phase [N+1], or tell me what to revisit first.
```

If thresholds not met:
```
Exit gate not passed. Conditions unmet:
  ❌ [Condition 1] - [brief note on what's missing]
  ❌ [Condition 2]

Options:
  A) Go back and address the gaps (recommended skills: [list])
  B) Proceed anyway - I acknowledge the risk (FORCE)
```

On GO or FORCE: update state.json - add phase to `phases_completed`, advance `current_phase_index`.

**Special rule - Phase 3a → 3b transition:**
This gate cannot be bypassed with FORCE. The Go/No-Go verdict from /pm-hypotheses [Results mode] is the only valid exit from Phase 3a. If the verdict is PIVOT or STOP, Phase 3b cannot start. If user attempts to proceed to Phase 3b without a GO verdict, block with:
```
Phase 3b requires a GO verdict from Phase 3a hypothesis validation.
Current status: [PIVOT / STOP / not run]

Phase 3b is commercial commitment work - business case, roadmap, and PRD.
Starting it without validated problem-market fit means those documents are built on unconfirmed assumptions.

Options:
  A) Return to Phase 3a - run /pm-hypotheses [Results mode] with your experiment data
  B) Phase 3a was done outside this framework - provide Go/No-Go verdict and evidence
```

**"Done elsewhere" handler (for any phase):**
If user states a phase was done outside this framework, collect the minimum evidence needed to confirm the phase exit criteria were met, then mark it complete. For Phase 3a specifically: collect Go/No-Go verdict + which hypothesis types were tested + key evidence signal per type. Do not require re-running skills if the work was genuinely done.

---

## FRAMEWORK MAP

> Shown when user runs `/pureinn map` or `/pureinn help`

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PUREINN - FRAMEWORK MAP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Three entry points:
  /pureinn [idea or product name]  Start or continue a project
  /pureinn map                     This view - full framework overview
  /common-ground                   Technical setup (Pre-Phase 6)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Then display each phase as a block:

```
PHASE 1 - FOUNDATION & COLLABORATION SETUP
Goal: Align on context, assumptions, and constraints before discovery begins.
Output: Scales by team size - from a single project charter to full governance setup.
─────────────────────────────────────────────
  /pm-project-charter   [all team types]
    Input:  Project context, goals, constraints, risks, success definition
    Output: Project Charter, Assumptions & Risks Register

  /pm-team-roster       [small team / full team / corporate]
    Input:  Team members, roles, skill inventory
    Output: Team Roster, Decision Rights Matrix, Skill Gap Assessment
    Note:   Skip for solo builders. RACI simplified for small founding teams.

  /pm-comms-charter     [small team / full team / corporate]
    Input:  Team preferences, meeting cadence, tools
    Output: Communication Charter, Meeting Rhythm
    Note:   Skip for solo builders.

  /pm-stakeholder-map   [full team / corporate only]
    Input:  Product idea, team structure, organization context
    Output: Stakeholder Map, RACI Matrix, Escalation Tree
    Note:   Skip for solo and small founding teams unless external investors/board involved.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PHASE 2 - IDEATION & DISCOVERY
Goal: Validate the problem, customer, market, and technical feasibility.
Output: Problem Validation Summary (synthesizes all 4 tracks).
Four parallel tracks - can run simultaneously.
─────────────────────────────────────────────
  TRACK A - Tech Feasibility
  /pm-tech-feasibility
    Input:  Tech research (Perplexity / Tech Lead), stack assumptions
    Output: Tech Feasibility Report

  TRACK B - Domain & Legal
  /pm-domain-analysis
    Input:  Domain research (Perplexity), regulatory landscape
    Output: Domain Analysis Report, Legal & Regulatory Requirements

  TRACK C - Market
  /pm-market-analysis
    Input:  Market data (Perplexity), competitor research
    Output: Market Size (TAM/SAM/SOM), Competitor Analysis, SWOT, Market Timing

  TRACK D - Voice of Customer
  👤 Human: ≥10 customer interviews (or SynthFolk / ChatGPT synthetic)
  /pm-personas
    Input:  Interview transcripts, survey data, observations
    Output: Customer Segments, Personas, Early Adopters Profile
  /jtbd-building
    Input:  Personas + interview data
    Output: JTBD Analysis, Forces Diagram

  CONVERGENCE
  /pm-problem-validation
    Input:  All Track A-D outputs
    Output: Problem Validation Summary (Phase 2 exit artifact)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PHASE 3a - VALIDATION
Goal: Validate core assumptions about problem, customer, and market before committing to strategy.
Character: externally-paced - tempo set by market, not by you. Can start parallel with late Phase 2.
Output: Go/No-Go verdict (hard gate - only GO unlocks Phase 3b).
"Done elsewhere": accepted - provide Go/No-Go verdict + key evidence to /pureinn directly.
─────────────────────────────────────────────
  /design-thinking
    Input:  Problem Validation Summary, Personas
    Output: Problem Statement, POV, HMW Questions, Ideation Synthesis, Elevator Pitch,
            Validation Hypotheses draft

  /pm-hypotheses  [Plan mode]
    Input:  Validation Hypotheses draft, Phase 2 evidence (JTBD, Personas, Problem Validation)
    Output: Hypothesis Register (ICP definition, assumption map, experiment plan, success criteria)

  [👤 Experiments - human activity]
    Input:  Experiment plan from /pm-hypotheses
    Activity: Landing page, smoke test, targeted ads, pre-order, rapid prototype - based on plan
    Budget: €100-300 for quantitative experiments

  /pm-hypotheses  [Results mode]
    Input:  Experiment results vs. pre-defined success criteria
    Output: Hypothesis Register (updated), Go/No-Go Decision (Go / Pivot / Stop)
    Note:   HARD GATE - GO required to enter Phase 3b. PIVOT loops back. STOP ends project.
            No FORCE bypass on this gate.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PHASE 3b - COMMERCIAL DEFINITION
Goal: Translate validated problem-market fit into commercial strategy and product specification.
Character: AI-assisted synthesis sprint. Quality of output depends entirely on Phase 3a signal quality.
Condition: Phase 3a GO verdict required. Non-negotiable.
Output: PRD (frozen after creation) + Business Case + Roadmap v1.
"Done elsewhere": accepted - bring existing Lean Canvas, financial model, or strategy artifacts via Path A.
─────────────────────────────────────────────
  /pm-kotler
    Input:  High-level Feature Vision (from design-thinking), JTBD, Personas
    Output: Product Definition - 5 levels (Core Benefit / Basic / Expected / Augmented / Potential)

  /pm-lean-canvas
    Input:  Design Thinking outputs, Kotler Product Definition, Phase 2 research
    Output: Lean Canvas (one-page business model: Problem / Solution / UVP / Unfair Advantage /
            Customer Segments / Key Metrics / Channels / Cost Structure / Revenue Streams)

  /pm-kpis
    Input:  Lean Canvas (Key Metrics block), Problem Validation
    Output: North Star Metric, AARRR Funnel Metrics, OKRs

  /pm-business-case
    Input:  Lean Canvas, KPIs, Market Analysis
    Output: Business Case (3-year projections, unit economics, Go/No-Go)

  /pm-product-roadmap  [v1]
    Input:  Problem Validation, Lean Canvas, KPIs
    Output: Product Roadmap v1 (vision + strategic phases)

  /pm-prd  [Phase 3b exit artifact]
    Input:  All Phase 2 + Phase 3a + Phase 3b outputs
    Output: PRD (full product-level consolidation document - frozen after creation)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PHASE 4 - DOMAIN MODELING + REGISTER SETUP  [FDD Stage 1]
Goal: Model the domain, initialize the 4 living registers. Registers are the source of truth for AI throughout Phase 6-7.
─────────────────────────────────────────────
  /pm-domain-model
    Input:  PRD Business Capabilities, domain knowledge
    Output: Domain Model, ERD, Ubiquitous Language Glossary
            + optional Excalidraw domain overview

  /pm-entity-registry
    Input:  PRD Business Capabilities, Domain Model
    Output: entities.md - entity list + Mermaid stateDiagram-v2 per entity
            States and transitions defined; guard conditions left TBD (added JIT by pm-feature-design)
            Events use past tense dot notation (e.g., order.confirmed)
    Saves:  domain/entities.md (Live Register 1)

  /pm-business-rules-library
    Input:  PRD Business Capabilities, entities.md
    Output: business_rules.md + decision_models.md in Draft mode
            Rules finalized JIT by pm-feature-design before each feature build
    Saves:  domain/business_rules.md (Live Register 2), domain/decision_models.md (Live Register 3)
    IDs:    BR-[DOMAIN]-[NUMBER], TBL-[DOMAIN]-[NUMBER]

  /pm-privacy-requirements
    Input:  Domain Model, Legal Requirements, product description
    Output: PII Inventory, Privacy Requirements, GDPR Action Plan

  /pm-product-roadmap  [v2 update]
    Input:  Roadmap v1, Domain Model constraints
    Output: Product Roadmap v2 (+ domain constraints layer)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PHASE 5 - FEATURE PLANNING  [FDD Stage 2]
Goal: Define the feature inventory, prioritize, assign to Delivery Stripes.
─────────────────────────────────────────────
  /pm-features-list
    Input:  PRD Business Capabilities, Domain Model, user research
    Output: feature_list.md - FDD Feature List (FEAT-[DOMAIN]-[NUMBER] IDs)
            KANO Analysis + V×C Matrix
            Stub Feature Cards (status: 1_Backlog) in features/cards/
    Saves:  features/feature_list.md (Live Register 4), features/cards/FEAT-*.md
    Notion: Feature entries pushed (Status=Backlog, Priority from KANO+V×C)

  /pm-mvp-scope
    Input:  feature_list.md, business priorities
    Output: MVP Scope (IN/POST-MVP/CUT), Delivery Stripes (domain-focused channels)
            Feature-to-Stripe assignment + dependency sequencing per stripe
            Updates stripe: field in Feature Card frontmatter
    Saves:  artifacts/phase-5-planning/mvp-scope.md, artifacts/phase-5-planning/delivery-stripes.md
    Notion: enrich Features with Phase/Stripe

  /pm-product-roadmap  [v3 update]
    Input:  Roadmap v2, MVP Scope, Delivery Stripes
    Output: Product Roadmap v3 (+ feature and delivery view)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PRE-PHASE 6 - TECHNICAL FOUNDATION
─────────────────────────────────────────────
  /common-ground
    Input:  PRD, Domain Model, team tech preferences
    Output: Tech Stack Decision, Repo Structure, COMMON-GROUND.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PHASE 6 + 7 - FDD DELIVERY CYCLE  [FDD Stages 3 + 4 - JIT per Feature]
Goal: Deliver working features, Stripe by Stripe, JIT spec just before each feature enters build.
Domain registers are the living source of truth. Feature Cards are the atomic delivery unit.
─────────────────────────────────────────────
  STRIPE ORCHESTRATION (orchestrates the full JIT cycle)
  /pm-stripe
    Input:  feature_list.md, Feature Card frontmatter status
    Output: Stripe dashboard, advance feature, run Impact Analysis, mark Promoted

  JIT CYCLE PER FEATURE (phases 6+7 integrated per feature)
  /pm-feature-design [FEAT-ID]
    Input:  Feature Card stub, entities.md, business_rules.md, decision_models.md,
            PRD section (prd_ref from frontmatter)
    Pre-step (Feature Implementation mode): scan real service/class files first
    Output: Commit 1 - register updates (guard conditions, rule finalization)
            Commit 2 - Feature Card Sections 1-3 (Biznis Mantinely, ACs, sequence diagram)
    Status: 2_Spec_Done

  [Design Inspection]
    Team: human review of Feature Card Sections 1-3 → 3_Ready_to_Build
    Solo: human confirm → 3_Ready_to_Build

  SPEC GATE (hard rule - /pm-stripe enforces before routing to build):
    Feature Card Sections 1-3 populated + status: 3_Ready_to_Build

  BUILD (Phase 7 - per feature, after spec gate)
  /fullstack-guardian    → BE implementation (reads Feature Card Section 3)
  /impeccable-craft      → FE implementation (reads Feature Card Section 3)
  /test-master           → Unit + integration tests
  /playwright-expert     → E2E tests
  /code-reviewer         → Code review
  /impeccable-audit      → Code quality
  /impeccable-harden     → Security hardening
  /security-reviewer     → Security audit
  /devops-engineer       → CI/CD, deployment
  /monitoring-expert     → Observability, alerting
                           → Feature Card Section 4 filled, status: 6_Shipped

  OPTIONAL SPEC SUPPORT (run when needed, not per feature)
  /architecture-designer → System Design Blueprint, ADRs
  /api-designer          → API contracts, OpenAPI spec
  /impeccable document   → PRODUCT.md, DESIGN.md [once at Phase 6 start]
  /impeccable-shape      → UX/UI shape brief per feature

  ATOMIC COMMIT PROTOCOL (parallel stripe safety):
    Register commits (entities.md, business_rules.md, decision_models.md) before code commits
    One feature per stripe in active design/build at any time

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

GREENFIELD - RUNNING THIS PLAYBOOK
Use when: building a new product from scratch, 0 active users, validating PMF.
─────────────────────────────────────────────
ONCE AT START
  /pureinn [idea]         → intake, document scan, playbook selection, dashboard
  /pm-glossary            → start domain glossary; update continuously

PHASE 1 - FOUNDATION  (scales by team size)
  Solo:  /pm-project-charter
  Team:  /pm-project-charter → /pm-team-roster → /pm-comms-charter
  Corp:  + /pm-stakeholder-map first
  Run /pureinn when done to advance.

PHASE 2 - DISCOVERY  (four parallel tracks)
  🔍 → /pm-tech-feasibility      (tech feasibility)
  🔍 → /pm-domain-analysis       (domain + legal)
  🔍 → /pm-market-analysis       (market + competitors)
  👤 ≥10 interviews → /pm-personas → /jtbd-building  (customer + JTBD)
  Converge: /pm-problem-validation  (Phase 2 exit artifact)
  Run /pureinn when done to advance.

PHASE 3 - DEFINE & VALIDATION
  /design-thinking          → Problem Statement, HMW, Elevator Pitch,
                              Validation Hypotheses draft
  /pm-hypotheses [Plan]     → Hypothesis Register (ICP, experiments, success
                              criteria set BEFORE running)
  👤 Run experiments        → landing page / smoke test / pre-order / concierge
  /pm-hypotheses [Results]  → Go/No-Go verdict
  HARD GATE: GO advances. PIVOT re-validates. STOP ends project.

  After GO:
  /pm-kotler             → Product Definition (5 levels)
  /pm-lean-canvas        → Lean Canvas (default)
  /pm-business-model     → Business Model Canvas (optional fuller alternative)
  /pm-kpis               → North Star Metric, AARRR, OKRs
  /pm-business-case      → 3-year projections, Go/No-Go
  /pm-product-roadmap    → Roadmap v1
  /pm-prd                → PRD (Phase 3b exit artifact - frozen after creation)
  /pm-pitch-deck         → Pitch Deck (optional)
  Run /pureinn when done to advance.

PHASE 4 - DOMAIN MODELING + REGISTER SETUP
  /pm-domain-model            → Domain Model, ERD
  /pm-entity-registry         → entities.md (entity states + Mermaid state machines)
  /pm-business-rules-library  → business_rules.md + decision_models.md (Draft mode)
  /pm-privacy-requirements    → PII Inventory, GDPR action plan
  /pm-product-roadmap         → Roadmap v2 (+ domain constraints)
  Run /pureinn when done to advance.

PHASE 5 - FEATURE PLANNING  [2-3 days]
  /pm-features-list    → feature_list.md (FDD Feature List), KANO, V×C
                         → Stub Feature Cards in features/cards/
                         → Notion: Feature entries pushed
  /pm-mvp-scope        → MVP Scope, Delivery Stripes (domain-focused channels)
                         → Feature-to-Stripe assignment + dependency sequencing
                         → Updates stripe: in Feature Card frontmatter
                         → Notion: Features enriched with Phase/Stripe
  /pm-product-roadmap  → Roadmap v3 (+ feature + delivery view)
  Run /pureinn when done to advance.

PRE-PHASE 6
  /common-ground       → Tech stack decision, repo structure → COMMON-GROUND.md

PHASE 6 + 7 - DELIVERY  [JIT per Feature, repeats per Stripe]
  /pm-stripe           → Stripe dashboard, advance next feature, route to design or build
  Per feature (JIT spec):
    /pm-feature-design [FEAT-ID]  → Sections 1-3 of Feature Card + register finalization
    Design Inspection             → human review (team) or confirm (solo)
    Spec gate: Sections 1-3 complete + status: 3_Ready_to_Build
  Per feature (build):
    /fullstack-guardian → /impeccable-craft → /test-master → /playwright-expert
    → /code-reviewer → /impeccable-harden → /devops-engineer → /monitoring-expert
    → Feature Card Section 4 filled → status: 6_Shipped → next feature

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FEATURE IMPLEMENTATION PLAYBOOK
Use when: product exists, users are active, goal is adding new functionality.
Does NOT follow Phase 1-5. Has its own entry sequence.
─────────────────────────────────────────────
MIGRATION PATH  [product built outside the framework - run once]
  /pureinn             → always first: workspace setup, state.json, pureinn-variables.md
  /common-ground       → technical context (stack, APIs, debt) → COMMON-GROUND.md
  /impeccable document    → design context (design system, components) → PRODUCT.md + DESIGN.md
  /pm-glossary         → start domain glossary
  /pm-entity-registry  → entities.md (extract from existing codebase/docs)
  /pm-business-rules-library → business_rules.md + decision_models.md (extract existing rules)
  /pm-reverse-extract  → reads existing Feature Cards/codebase
                         → extracts feature inventory in FDD format (FEAT-[DOMAIN]-[NUMBER])
                         → derives Feature hierarchy with status
                         → pushes full structure to Notion (primary: team visibility)
                         → generates feature_list.md, delivery-stripes.md (secondary: Claude context)
  → proceed to Phase 6 + 7 (JIT per feature)

─────────────────────────────────────────────
STANDARD PATH  [onboarding a new feature project]
  PHASE 0 - CONTEXT SETUP  [once per project onboarding]
  /pureinn           → Product context (users, roadmap, problems, workarounds)
  /common-ground     → Technical context → COMMON-GROUND.md
  /impeccable document  → Design context → PRODUCT.md + DESIGN.md

  FEATURE VIABILITY ASSESSMENT  [per feature, before spec]
  Feature Target Profile:
    - Target segment + KANO classification (Must-be / Performance / Delighter / Indifferent)
    - V×C Matrix (Quick Win / Big Bet / Fill-in / Time Waster)
    - Usage frequency + % of user base
  Demand Validation:
    - Existing signal: analytics, support tickets, requests
    - Lightweight experiments if signal weak (fake door, mockup, landing page)
    - B2B: pilot commitment or letter of intent
  Strategic Alignment: Core vs. Adjacent
  MDP Definition: minimum delightful product scope
  Success Metrics: depth of usage / behavior change / business impact (set before build)

  TRACK A - KNOW WHAT WE WANT
    Feature Set assignment (grouping only)
    New domain? → /pm-entity-registry + /pm-business-rules-library (Draft mode) first
    JIT design per feature:
    /pm-feature-design [FEAT-ID]  → Feature Card Sections 1-3 + register finalization
                                    (scans existing codebase before generating sequence diagram)
    Design Inspection             → team review or solo confirm
    Build skills                  → reads Feature Card Section 3 as build spec

  TRACK B - KNOW THE AREA, NOT THE SOLUTION
    👤 User research (5-10 interviews), competitive analysis, tech feasibility
    Feature Value Prop, Business Case, Success Metrics
    → Converges into Track A after discovery

  DELIVERY CYCLE  [same as Phase 6+7 below, plus FI-specific rules]
    Feature flags mandatory (all new code OFF by default)
    Backward compat: API and DB changes additive only
    Regression suite per feature (≤10% latency increase gate)
    Gradual rollout: Internal → 5% → 25% → 50% → 100%
    Kill switch: disable flag if error rate >5%
    Post-launch: minimum 4 weeks monitoring

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LEGEND
  👤 Human activity - done outside Claude (interviews, Figma, domain research)
  🔍 External AI - Perplexity, ChatGPT - results brought in as skill input
  🤖 AI Skill - Claude generates the artifact

ARTIFACT CHAIN - GREENFIELD
  Phase 2  → Problem Validation Summary
  Phase 3a → Go/No-Go verdict (hard gate before 3b)
  Phase 3b → PRD frozen (product-level consolidation, Business Capabilities section drives Phase 4+)
  Phase 4  → Domain Model + entities.md + business_rules.md + decision_models.md (Draft)
  Phase 5  → feature_list.md + MVP Scope + Delivery Stripes + Stub Feature Cards
  Phase 6 (JIT) → Feature Card Sections 1-3 + register finalization (per feature, per stripe)
  Phase 7 → Working software + Feature Card Section 4 (per feature, Promoted status)

ARTIFACT CHAIN - FEATURE IMPLEMENTATION
  Phase 0 → Product + Technical + Design context (COMMON-GROUND.md, PRODUCT.md, DESIGN.md)
  Per feature → Feature Target Profile + Demand Validation + MDP + Success Metrics
  JIT per feature → Feature Card Sections 1-3 + register updates (entities.md, business_rules.md)
  Per Stripe → Build → Regression → Review → Deploy (feature-flagged)
  Per feature → Gradual rollout (Internal → 5% → 25% → 50% → 100%)
  Post-launch → 4 weeks monitoring

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

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
