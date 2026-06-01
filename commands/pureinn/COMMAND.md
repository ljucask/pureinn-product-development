---
description: Pureinn workflow engine entry point. Reads existing documents, evaluates current state, maps to phases, and routes to the correct starting point. Run with a product idea or name to start. Run with 'map' for the full framework overview. Run with a known project slug to resume.
argument-hint: "[product idea or name | map | help | project-slug]"
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
Engine vyberie Feature playbook. Ak Phase 0 nie je hotová, začne kontextovým setupom (pureinn + common-ground + impeccable-teach). Ak Phase 0 existuje, smeruje priamo na Feature Viability Assessment.

### Pokračovanie v rozpracovanom projekte
```
/pureinn acme-crm
/pureinn-resume acme-crm
```
Engine prečíta `state.json`, obnoví kontext z `assessment.md`, zobrazí dashboard s aktuálnou fázou.

### Prehľad celého frameworku
```
/pureinn map
/pureinn help
```
Zobrazí Framework Map - všetky playbooki, fázy, skills a artifact chains na jednom mieste.

---

## Special Commands

If $ARGUMENTS is `map` or `help`:
→ Skip all steps. Go directly to **FRAMEWORK MAP** at the bottom of this skill.

If $ARGUMENTS matches a known project slug and a `state.json` exists:
→ Go to **STEP 1B (Resume path)**.

Otherwise:
→ Go to **STEP 1A (New / intake path)**.

---

## STEP 1A - Guidance Mode Check

Ask the user:

```
Do you want guidance throughout the workflow?

  A) Yes - explain the why behind each phase and skill as we go
  B) No - just tell me what to run next
```

Store the answer. Save as `"guidance_mode": true` or `false` in state.json.

**What guidance mode means:**
- ON: Before each phase and before recommending each skill, Claude adds 2-3 sentences of context - what this phase is trying to achieve, what to watch out for, common mistakes. Applied consistently throughout the workflow, not just at the start.
- OFF: Pure routing. Dashboard + skills queue, no explanatory text.

---

## STEP 1B - Resume Path

A state.json exists for this project. Read it and go directly to **STEP 7 (Dashboard)**.

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

Wait for the user's answer, then ask the following two questions together:

**Options (ask together):**

What type of product is it?

  A) SaaS web application
  B) Mobile application (iOS / Android / both)
  C) Marketplace or platform (connects two or more sides)
  D) Something else (internal tool, API)

Who is it for?

  A) External customers (product for sale)
  B) Internal team only
  C) Both

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

No free-text questions in this group. Ask both together:

What is the primary experience?

  A) Mobile first - main value delivered on mobile
  B) Desktop first - web/desktop (CRM, dashboard, admin tool)
  C) Both equally - full parity across mobile and web
  D) Not sure yet

Will the product be paid?

  A) Yes - paid from day one (subscription, one-time, usage-based)
  B) Freemium - free tier + paid upgrade
  C) Free / internal - no revenue target
  D) Not decided yet

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

**Options (ask together first):**

Where are you now?

  A) Idea only - nothing validated yet
  B) Have some research or early customer insights
  C) Validated problem, ready to define strategy
  D) Have a strategy or specs, moving to execution

Who is building this?

  A) Solo - just me, no team
  B) Small founding team (2-3 people, wearing multiple hats)
  C) Team with defined roles (PM, developers, designer)
  D) Corporate / enterprise team (multiple stakeholders)

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
- Phase 1 for solo = one skill, ~30 minutes

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
| Phase 1 - Foundation | ✅ / ⚠️ / ❌ | [document / intake / none] | High / Med / Low |
| Phase 2 - Discovery  | ✅ / ⚠️ / ❌ | | |
| Phase 3 - Define     | ✅ / ⚠️ / ❌ | | |
| Phase 4 - Domain     | ✅ / ⚠️ / ❌ | | |
| Phase 5 - Features   | ✅ / ⚠️ / ❌ | | |
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

## STEP 4 - Playbook Selection

If not already determined from document analysis, ask:

```
One question to confirm the right playbook:

Does the product already exist in any form?
  A) No - building from scratch
  B) Yes, but no active users yet
  C) Yes, with active users - adding features
  D) Yes, with active users - rebuilding or migrating
```

Map to playbook:
- A or B → **Greenfield**
- C → **Feature**
- D → **Rebuild**

**Feature playbook note:**
Feature Implementation does not start at Phase 1. It starts at Phase 0 (context setup).
Phase 0 runs once per project onboarding - not per feature. After Phase 0, each feature goes through Feature Viability Assessment before any spec work begins.
If Phase 0 is already done (context exists from a prior session), skip to Feature Viability Assessment.

**Rebuild playbook note:**
Rebuild starts at Phase 1 (Foundation) but includes two additional Rebuild-only phases: R2 (Legacy Assessment) and R3 (Migration Strategy) before Phase 3. Do not skip these - poor legacy analysis is the primary cause of Rebuild failures.

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
    PRD_master.md                                ← pm-prd [Product PRD - frozen after Phase 3]
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
```

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

**2b. Create pureinn-variables.md**

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
| Product Roadmap | Page | pm-product-roadmap | |
| Elevator Pitch | Page | design-thinking | |
| Lean Canvas | Page | pm-lean-canvas | |
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

## Validation & Metrics (Phase 3)

| Key | Type | Skill | URL |
|---|---|---|---|
| Hypothesis Validation | Page | pm-hypotheses | |
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
| Meetings | DB | pm-comms-charter | |
| Open Questions | DB | pm-hypotheses | |

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
| pm-stakeholder-map | stakeholder-map.md, raci-matrix.md, escalation-tree.md | artifacts/phase-1/ |
| pm-project-charter | project-charter.md, assumptions-risks-register.md | artifacts/phase-1/ |
| pm-team-roster | team-roster.md, decision-rights-matrix.md, skill-gap-assessment.md | artifacts/phase-1/ |
| pm-comms-charter | communication-charter.md, meeting-rhythm.md | artifacts/phase-1/ |
| pm-tech-feasibility | tech-feasibility-report.md | artifacts/phase-2/ |
| pm-domain-analysis | domain-analysis-report.md, legal-regulatory-requirements.md | artifacts/phase-2/ |
| pm-market-analysis | market-size-analysis.md, competitor-analysis.md, swot-analysis.md, market-timing-rationale.md | artifacts/phase-2/ |
| pm-personas | customer-segments.md, personas.md, early-adopters-profile.md | artifacts/phase-2/ |
| jtbd-building | jtbd-analysis.md | artifacts/phase-2/ |
| pm-problem-validation | problem-validation-summary.md | artifacts/phase-2/ |
| design-thinking | design-thinking-synthesis.md | artifacts/phase-3/ |
| pm-hypotheses | hypothesis-register.md, go-no-go.md | artifacts/phase-3/ |
| pm-kotler | kotler-five-levels.md | artifacts/phase-3/ |
| pm-lean-canvas | lean-canvas.md | artifacts/phase-3/ |
| pm-kpis | north-star-metric.md, aarrr-metrics.md, okrs.md | artifacts/phase-3/ |
| pm-business-case | business-case.md | artifacts/phase-3/ |
| pm-prd | PRD.md (or PRD_[Domain].md for modular) | product/ |
| pm-product-roadmap | product-roadmap-v1.md | artifacts/phase-3/ |
| pm-pitch-deck | pitch-deck-brief.md | artifacts/phase-3/ |
| pm-domain-model | domain-model.md | artifacts/phase-4/ |
| pm-entity-registry | entities.md | domain/ (Live Register 1) |
| pm-business-rules-library | business_rules.md, decision_models.md | domain/ (Live Registers 2+3) |
| pm-privacy-requirements | pii-inventory.md, privacy-requirements.md, gdpr-action-plan.md | artifacts/phase-4/ |
| pm-product-roadmap | product-roadmap-v2.md | artifacts/phase-4/ |
| pm-features-list | feature_list.md + stub FEAT-*.md cards | features/ + features/cards/ (Live Register 4) |
| pm-mvp-scope | mvp-scope.md, delivery-stripes.md | artifacts/phase-5/ |
| pm-reverse-extract | feature_list.md, delivery-stripes.md | features/ (migration path - updates root state.json) |
| pm-product-roadmap | product-roadmap-v3.md | artifacts/phase-5/ |
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
  Phase 1 - Foundation & Collaboration   [✅ Done / ⏭ Skipped / 🔲 To do]
  Phase 2 - Discovery                    [✅ Done / ⚠️ Partial / ⏭ Skipped / 🔲 To do]
  Phase 3 - Define & Validation          [✅ Done / ⚠️ Partial / ⏭ Skipped / 🔲 To do]
  Phase 4 - Domain Modeling + Register Setup  [🔲 To do]
  Phase 5 - Feature Planning              [🔲 To do]
  Phase 6 + 7 - Delivery Cycle (JIT)     [🔲 To do]

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
             (pureinn + common-ground + impeccable-teach - runs once)
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

**Rebuild dashboard:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROJECT: [Product Name]
PLAYBOOK: Rebuild
GUIDANCE: [On / Off]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PHASE STATUS
  Phase 1 - Foundation & Collaboration   [✅ Done / ⏭ Skipped / 🔲 To do]
  Phase R2 - Legacy Assessment           [✅ Done / ⚠️ Partial / 🔲 To do]
  Phase R3 - Migration Strategy          [✅ Done / ⚠️ Partial / 🔲 To do]
  Phase 3 - Define & Scoping             [🔲 To do]
  Phase 4 - Domain Modeling + Register Setup  [🔲 To do]
  Phase 5 - Feature Planning             [🔲 To do]
  Phase 6 + 7 - Delivery Cycle (JIT)    [🔲 To do]
  Parallel Run + Cutover                 [🔲 To do]

STARTING FROM: Phase [N] - [Phase Name]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

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

### Phase 3 - Define & Validation
```
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
                         [Hard gate: only GO advances to /pm-kotler and beyond]
/pm-kotler             → Product Definition (5 levels: Core / Basic / Expected / Augmented / Potential)
/pm-lean-canvas        → Lean Canvas (one-page business model for startups)
                         [Replaces BMC - optimized for validation stage, not established operations]
/pm-kpis               → North Star Metric, AARRR, OKRs
/pm-business-case      → Business Case (3-year projections, Go/No-Go)
/pm-product-roadmap    → Product Roadmap v1
/pm-prd                → PRD - Phase 3 exit artifact (synthesizes all Phase 2+3)
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
  /pm-entity-registry   → entities.md (extract from existing codebase/docs)
  /pm-business-rules-library → business_rules.md + decision_models.md (extract existing rules)
  /pm-reverse-extract   → reads existing Feature Cards/codebase
                          → extracts feature inventory in FDD format (FEAT-[DOMAIN]-[NUMBER])
                          → Notion: creates Feature hierarchy (primary: team visibility)
                          → generates feature_list.md, delivery-stripes.md
                          Use INSTEAD of pm-features-list + pm-mvp-scope.
                          Then proceed to Phase 6 + 7 (JIT per feature) directly.

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

  [👤 Human] User research (5-10 interviews, target segment only)
  [👤 Human] Competitive analysis (if solution direction unclear)
  [👤 Human] Tech feasibility (with existing stack)
  /feature-value-prop → Feature Value Prop (WHO / WHAT / WHERE / WHEN / IMPACT)
  /pm-business-case   → Feature Business Case (revenue/retention impact, ROI, Go/No-Go)
  /pm-kpis            → Feature Success Metrics (depth / behavior / business impact)

  After discovery: apply KANO + V×C to defined feature → enter Track A.

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
Step 1: /pm-feature-design [FEAT-ID]
          → Pre-step (Feature Implementation mode only): scan real service files
          → Commit 1: spec([FEAT-ID]): guard conditions + rule finalization
            - entities.md: guard conditions added to state transitions
            - business_rules.md: Draft rules updated to Final
            - decision_models.md: decision table rows finalized
          → Commit 2: spec([FEAT-ID]): feature design complete
            - Feature Card Section 1 (Biznis Mantinely - BR-IDs, entity guard conditions)
            - Feature Card Section 2 (Acceptance Criteria)
            - Feature Card Section 3 (Mermaid sequenceDiagram + files to modify)
          → Status: 2_Design

Step 2: Design Inspection [Team mode: human review of Sections 1-3]
          → Status: 3_Design_Inspection_Passed
          [Solo mode: AI generates, human confirms - same gate, lighter ritual]

Step 3: BUILD SKILLS (Phase 7)
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
          → Commits, test files, flag OFF verification, Code Inspection result
          → Status: 6_Promoted_to_Build (Feature Card immutable after this)

SPEC GATE (hard rule, enforced by /pm-stripe before routing to build):
  Feature Card Sections 1-3 must be complete
  Status must be 3_Design_Inspection_Passed

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

PHASE 3 - DEFINE & VALIDATION
Goal: Define the strategy, validate core assumptions, and produce a Go/No-Go before building.
Output: PRD (consolidates all Phase 2+3 into one coherent document).
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
    Note:   Hard gate - only GO advances past this point

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

  /pm-prd  [Phase 3 exit artifact]
    Input:  All Phase 2 + Phase 3 outputs
    Output: PRD (full product-level consolidation document)

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
            Stub Feature Cards (status: 1_Walkthrough) in features/cards/
    Saves:  features/feature_list.md (Live Register 4), features/cards/FEAT-*.md
    Notion: Feature entries pushed (Status=Backlog, Priority from KANO+V×C)

  /pm-mvp-scope
    Input:  feature_list.md, business priorities
    Output: MVP Scope (IN/POST-MVP/CUT), Delivery Stripes (domain-focused channels)
            Feature-to-Stripe assignment + dependency sequencing per stripe
            Updates stripe: field in Feature Card frontmatter
    Saves:  artifacts/phase-5/mvp-scope.md, artifacts/phase-5/delivery-stripes.md
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
    Status: 2_Design

  [Design Inspection]
    Team: human review of Feature Card Sections 1-3 → 3_Design_Inspection_Passed
    Solo: human confirm → 3_Design_Inspection_Passed

  SPEC GATE (hard rule - /pm-stripe enforces before routing to build):
    Feature Card Sections 1-3 populated + status: 3_Design_Inspection_Passed

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
                           → Feature Card Section 4 filled, status: 6_Promoted_to_Build

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

PHASE 1 - FOUNDATION  [~1 day, scales by team size]
  Solo:  /pm-project-charter
  Team:  /pm-project-charter → /pm-team-roster → /pm-comms-charter
  Corp:  + /pm-stakeholder-map first
  Run /pureinn when done to advance.

PHASE 2 - DISCOVERY  [1-3 weeks, four parallel tracks]
  🔍 → /pm-tech-feasibility      (tech feasibility)
  🔍 → /pm-domain-analysis       (domain + legal)
  🔍 → /pm-market-analysis       (market + competitors)
  👤 ≥10 interviews → /pm-personas → /jtbd-building  (customer + JTBD)
  Converge: /pm-problem-validation  (Phase 2 exit artifact)
  Run /pureinn when done to advance.

PHASE 3 - DEFINE & VALIDATION  [2-4 weeks]
  /design-thinking          → Problem Statement, HMW, Elevator Pitch,
                              Validation Hypotheses draft
  /pm-hypotheses [Plan]     → Hypothesis Register (ICP, experiments, success
                              criteria set BEFORE running)
  👤 Run experiments        → landing page / smoke test / pre-order / concierge
  /pm-hypotheses [Results]  → Go/No-Go verdict
  HARD GATE: GO advances. PIVOT re-validates. STOP ends project.

  After GO:
  /pm-kotler             → Product Definition (5 levels)
  /pm-lean-canvas        → Lean Canvas
  /pm-kpis               → North Star Metric, AARRR, OKRs
  /pm-business-case      → 3-year projections, Go/No-Go
  /pm-product-roadmap    → Roadmap v1
  /pm-prd                → PRD (Phase 3 exit artifact)
  /pm-pitch-deck         → Pitch Deck (optional)
  Run /pureinn when done to advance.

PHASE 4 - DOMAIN MODELING + REGISTER SETUP  [3-5 days]
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
    Spec gate: Sections 1-3 complete + status: 3_Design_Inspection_Passed
  Per feature (build):
    /fullstack-guardian → /impeccable-craft → /test-master → /playwright-expert
    → /code-reviewer → /impeccable-harden → /devops-engineer → /monitoring-expert
    → Feature Card Section 4 filled → status: 6_Promoted_to_Build → next feature

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
  Phase 2 → Problem Validation Summary
  Phase 3 → PRD (product-level consolidation, Business Capabilities section drives Phase 4+)
  Phase 4 → Domain Model + entities.md + business_rules.md + decision_models.md (Draft)
  Phase 5 → feature_list.md + MVP Scope + Delivery Stripes + Stub Feature Cards
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
