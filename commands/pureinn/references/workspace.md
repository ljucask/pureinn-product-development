# Pureinn - Workspace reference

> Reference for `commands/pureinn/COMMAND.md`. Workspace scaffolding, state.json, and pureinn-variables.md.

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
    scope_brief.md                               ← pm-scope-brief [commissioned builds - Phase 3b alternative]
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
    prep/                                        ← pm-discovery-interview (session agendas, created on demand)
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

## Repository

| Key | Value |
|---|---|
| github_repo_url | |
| local_repo_path | |

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

## Design context (cross-phase)

Not a Phase 6-7 setting. Design context is an input constraint - it applies from the moment anything visual is discussed. Sources combine; fill in whichever exist. See § Design context below for how they compose.

| Key | Description | Value |
|---|---|---|
| figma_project_url | Figma project URL - root of the product design file. Read by pm-feature-design when Figma MCP is connected. | |
| figma_design_system_url | Figma design system / component library URL (if separate from main project file). | |
| live_product_url | The product as it actually ships, if there is one. Browsable with Playwright. | |
| design_reference_urls | Products whose design is a deliberate reference or direction - not the product itself. Comma-separated. | |

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
Skills read pureinn-variables.md automatically. No need to re-enter URLs during skill runs.
```

Then use the AskUserQuestion tool to help the user connect Notion now (or defer):
- Question: "How do you want to connect Notion?"
  - Option A: "Use the Pureinn Notion template (Recommended)" — description: "Duplicate it to your workspace, then paste the URLs into pureinn-variables.md. Template + setup guide: see NOTION_TEMPLATE.md in the plugin folder."
  - Option B: "Use your own Notion setup" — description: "Open pureinn-variables.md and paste the URLs of your existing pages and databases."
  - Option C: "Skip for now" — description: "Leave rows blank - skills will ask when they first need each item."

**2d. Artifact language (asked once, stored in state.json)**

Use the AskUserQuestion tool:
- Question: "What language should generated artifact content be in?"
  - Option A: "English (Recommended)" — description: "Default. IDs, frontmatter keys, and section headers are always English regardless of this setting - only prose (descriptions, rationale, rule text) is affected."
  - Option B: "Other language - I'll name it" — description: "Prose content (descriptions, rationale, rule text) is written in that language. Structural elements - IDs, frontmatter keys/enum values, section headers, file names - stay English always, so skills can still parse them."

If B: capture the language name as free text, store it in `state.json` as `artifact_language`. If A or skipped: store `"English"`. This is asked once - not re-asked on resume.

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
| pm-discovery-interview | [YYYY-MM-DD]-[audience]-agenda.md | meetings/prep/ |
| pm-discovery-report | discovery-report.md (incremental, re-runnable) | artifacts/phase-2-discovery/ |
| pm-problem-validation | problem-validation-summary.md | artifacts/phase-2-discovery/ |
| design-thinking | design-thinking-synthesis.md | artifacts/phase-3-define/ |
| pm-hypotheses | hypothesis-register.md, go-no-go.md | artifacts/phase-3-define/ |
| pm-kotler | kotler-five-levels.md | artifacts/phase-3-define/ |
| pm-lean-canvas | lean-canvas.md | artifacts/phase-3-define/ |
| pm-business-model | business-model-canvas.md | artifacts/phase-3-define/ |
| pm-kpis | north-star-metric.md, aarrr-metrics.md, okrs.md | artifacts/phase-3-define/ |
| pm-business-case | business-case.md | artifacts/phase-3-define/ |
| pm-prd | PRD_master.md (Greenfield, frozen) / initiatives/[slug]/prd.md (FI Initiative mode) | product/ or initiatives/[slug]/ |
| pm-scope-brief | scope_brief.md (commissioned builds - Phase 3b exit alternative; Change Log after baseline) | product/ |
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
  "repo": {
    "present": "[local | remote | none_yet | none]",
    "local_path": "[absolute path, or null]",
    "url": "[git remote URL, or null]"
  },
  "artifact_language": "[English | other language name - default English]",
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
Note: `phase_3a_verdict` stores the Go/No-Go outcome: "GO", "PIVOT", or "STOP". Set by /pm-hypotheses [Results mode] or by "done elsewhere" import. Phase 3b entry is blocked until this field is "GO" - except commissioned builds (mandate given), where Phase 3a sits in `phases_skipped` and the field stays unset.
Note: `artifact_language` gates prose translation only (see CLAUDE.md "Artifact language" standard) - IDs, frontmatter keys/enum values, section headers, and file names stay English regardless of this setting. Set once at STEP 6, read by any skill carrying the "Artifact language" inline block; skills without that block yet just behave as English-default.

---

---

## Repo context

Set in **STEP 0f** and stored in `state.json` → `repo`. It is a routing signal, not decoration: several parts of the framework are only possible on one side of it, and offering them when they cannot work is how the engine wastes the user's time.

| `repo.present` | What it means | What it unlocks | What it rules out |
|---|---|---|---|
| `local` | Code is on this machine at `local_path` | `/pm-reverse-extract` (bootstrap registers from real code), `/pm-reconcile` (Rebuild), `/common-ground`, `/impeccable document` as the design-context source, in-repo prototypes, `mutex_tags` from real file contention | - |
| `remote` | A repository exists but is not checked out here | Reading the repo needs a clone first - offer that before anything that reads code | Everything in the `local` row, until it is cloned |
| `none_yet` | Greenfield; code will exist later | Full Greenfield path. Re-ask at Phase 6 entry, when a repo usually appears | Code-reading skills, in-repo prototypes |
| `none` | Research, strategy or a pitch with no build | Strategy and definition phases only | The whole Phase 6-7 delivery cycle - say so early rather than routing the user there |

**Rules:**
- Never offer a code-reading skill when `present` is `none_yet` / `none`, and never claim to have read code that is only a `remote` URL.
- When `present` is `remote` and something needs the code, offer the clone as an explicit step; do not silently clone.
- `none_yet` is not permanent. When a Phase 6 stripe opens and `repo.present` is still `none_yet`, ask again - that is the moment the answer usually changes.
- A wrong value here is worse than an empty one. If the user is unsure, record `none_yet` and re-ask rather than guessing a path.

---

---

## Design context

Design context is an **input constraint**, not a build-time detail: the moment anything visual is discussed - a prototype, a screen in a Feature Card, a pitch - the answer depends on what the product already looks like and what it is allowed to look like. That is why the variables sit in a cross-phase section rather than under Phase 6-7.

**Sources compose - this is not a choice between them.** A real design context is usually assembled: a reference site for direction, a screenshot of one screen someone sent, tokens read out of the codebase, a Figma library for the intended system. Each source answers a different question, so use every one that exists and say which part came from where.

| Source | Answers | How to get it | Available when |
|---|---|---|---|
| Codebase | What the product *is* - tokens actually in use, real components, real constraints | `/impeccable document` → PRODUCT.md + DESIGN.md; or read the theme/token files directly | `repo.present` = `local` |
| Figma | What the product is *meant to be* - the intended system, states not built yet | Figma MCP via `figma_project_url` / `figma_design_system_url` | a design file exists |
| Live product | What actually *ships* - real layout, spacing, interaction, copy | Playwright: browse `live_product_url`, capture screens, inspect computed styles | there is a public/reachable product |
| Screenshot / image | One specific screen, or a direction someone showed you | attach the file where it is needed (pm-prototype and pm-feature-design both accept images) | someone sent one |
| Reference products | Direction and taste - what "good" means here | Playwright over `design_reference_urls`, or screenshots | the user named references |
| Claude Design | Producing or iterating the design when there is nothing to read yet | the `design` skill / canvas | greenfield, or a redesign |

**Rules for composing:**
- **Mark provenance.** "Spacing scale from the codebase, colour direction from the reference site" is usable; a merged description with no source attached is not - the next person cannot tell what is fact and what is aspiration.
- **When sources disagree, name the conflict, do not average it.** Code says one thing and Figma another is the normal case (design drift), and it is information: `[CONFLICT - code ships X / Figma specifies Y]`. Apply the Deep source ingestion standard's reconciliation rule.
- **Codebase and live product are evidence. Figma and references are intent.** For "what does it look like today" trust the first two; for "what should it look like" trust the second two.
- **A reference is not the product.** Never fold `design_reference_urls` into the description of the product's own design - keep them in a separate line.
- **There is no automated extraction procedure here, and none is needed to start.** Point Playwright at the URL, look at the product, and write down what you find where it is used. If this becomes repetitive across projects, that is the signal to make it a skill - see BACKLOG.md.

---

Then read `references/dashboard.md` and run **STEP 7 (Dashboard and Routing)**.
