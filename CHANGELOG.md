# Changelog

## [5.5.0] - 2026-06-25

### Changed

- **`pm-reconcile` domain pass now also offers the domain model.** Previously `/pm-reconcile domain` produced only `entities.md` (the operational register) - not `domain-model.md` (the cross-domain ERD and boundaries). For a rebuild, a new team benefits from both: the Reconciliation Report is the audit ("what conflicted, how we ruled"), the domain model is the structural map ("how it all fits together"). The domain pass now offers (default Yes) to also drive `/pm-domain-model` in reconciled mode, building the ERD from the same reconciled entities. Added a **Reconciled mode** note to `pm-domain-model` (builds from the reconciled `entities.md`, does not re-derive). Updated the reconcile invocation table, plan template, and the FRAMEWORK_GUIDE Rebuild A1 flow.

---


## [5.4.0] - 2026-06-24

### New Skill

- **pm-audit** (39th skill) - workspace health check. Scans the framework's own artifacts (the 4 Live Registers, feature_list, Feature Cards, roadmap, glossary, state.json) against the **current** Pureinn conventions, finds inconsistencies, drift, and errors, fixes the mechanical ones in place, and asks about the judgment calls via grouped AskUserQuestion. Detects **framework-version drift** (old lifecycle state names, old hierarchy terms, missing newer fields like `feature_set`/`estimate`/Subtasks, `notion.*` cache keys) and migrates older-version workspaces. Findings scored by severity (P0-P3). Distinct from pm-reconcile (code vs legacy docs) and pm-reverse-extract (code to inventory) - this checks Pureinn artifacts against Pureinn conventions. Run after reconcile/extract, on an older workspace, or any time before continuing. `pm-reconcile` now routes to it as its verification step. This productizes the manual consistency passes done in v4.11.0 / v5.0.0 / v5.2.0.

### Fixed

- **pm-features-list** internal checklist: replaced the leftover "deliverable in 2 weeks or less" with the semantic atomicity test (one coherent client-valued function with one result), aligning the checklist with the v5.3.0 reframe.

---


## [5.3.0] - 2026-06-24

JIT feature-design redesign - making feature design a guided deep-dive rather than a form to fill, grounded in an FDD feature-definition deep-research pass.

### Added

- **Discovery Interrogation (`pm-feature-design` Step 1.5).** The skill now actively interrogates to surface what the user did not yet know when writing the business logic - instead of passively asking "any edge cases?" and accepting "none". Adaptive depth calibrated to feature criticality (KANO, priority, touches money/PII, state-transition count). Probes happy path, state transitions, guard conditions, edge cases, hidden concerns (permissions, idempotency, audit, retention), and rule gaps. Uses the grouped question pattern + "I don't know" handling + assumption surfacing. Every finding is sorted into the right layer: business rule / decision table / acceptance criterion / subtask.
- **Subtask helper layer.** A new lightweight `## Subtasks` section on the Feature Card (canonical template + both stub creators + all Notion blocks). Subtasks are nuance/spec helpers for the developer - not deliverables, not sub-features; they never break feature atomicity. Captured during discovery, by the team, or folded from too-granular legacy features. A subtask that hardens becomes an AC or a business rule.
- **Roadmap Functional Decomposition (`pm-product-roadmap` v2+).** Maps strategic phases to Domains and Feature Sets as the explicit top-down input to the Feature Plan. One picture for both audiences - investor sees direction, dev team sees what gets built where.

### Changed

- **Atomicity is now a semantic test, not time-based.** Replaced the "≤2 weeks / 14 days" rule with: *a Feature is one coherent client-valued function with one result*. "...and..." → split; a detail → a subtask. The `estimate` field (S/M/L) is informational for the roadmap, not the gate - dev time compresses with AI agents.
- **`pm-features-list`** - explicit top-down derivation from the roadmap decomposition (Features are leaves, derived last); strengthened naming rules (strong-verb whitelist, vague-verb blacklist, object = entity from `entities.md`); the 7 FDD anti-patterns as validation checks.
- **`pm-feature-design`** - JIT rule enrichment loop made explicit (new rules surfaced in discovery added via the single-rule helpers); writes Subtasks; Notion push includes description + subtasks.
- **`pm-reconcile`** - legacy feature right-sizing: too-granular legacy "features" consolidate under one rightful Feature with the granular bits captured as Subtasks; too-big ones split. Recorded in the Reconciliation Report.
- **Hierarchy confirmed 2-level** (Domain > Feature Set > Feature, top-down). The classic FDD "Major Feature Set" level is intentionally not used (lean / AI-first). Feature ordering is driven by dependency + priority + Delivery Stripe, never by completing whole Feature Sets.

---


## [5.2.0] - 2026-06-24

Full pre-launch consistency audit across all 38 skills, relationships, naming, and usability.

### Changed

- **Handoff blocks added to all 38 skills.** Only 6 followed the mandated handoff format (`Čo si teraz má` / `Ďalší krok` / `Môžeš preskočiť ak`); 25 had no forward guidance at all and 7 used an ad-hoc format. Every skill now ends with a tailored handoff that routes to the highest-ROI next step with a concrete skip condition.
- **pm-business-model wired into Phase 3b.** It claimed "Phase 3b" but appeared in zero playbook/doc tables (orphaned alongside pm-lean-canvas). Added to FRAMEWORK_GUIDE, README, and the orchestrator as the optional fuller alternative to Lean Canvas. Removed the contradictory "Replaces BMC" line in the orchestrator.
- **Single-rule JIT helpers wired in.** `pm-business-rule-core`, `pm-business-rule-critical`, `pm-business-rule-governance` were referenced nowhere. Now surfaced from `pm-business-rules-library` and `pm-feature-design` as the way to append one rule by priority class without re-running the full library skill.

### Fixed

- **Public skill count 36 → 38** in plugin.json, marketplace.json, and README (the descriptions users see at install).
- Removed the stale `exclude: ./skills/deprecated/` from plugin.json (the folder was deleted in v5.0.0).

### Verified clean (no change needed)

- Folder name = frontmatter name (38/38), no dangling related-skills or body references, uniform ID formats (FEAT/BR/TBL/FS/DIV-[DOMAIN]-NNN), uniform lifecycle states (1_Backlog..6_Shipped), uniform Notion cache keys (`notion_ids.*`), PREREQ/dependencies present in all skills.

---


## [5.1.1] - 2026-06-24

### Docs

- **FRAMEWORK_GUIDE restructured** for clearer separation. Now three parallel, self-contained playbook sections - **Greenfield**, **Rebuild**, **Feature Implementation** - each with its own flow diagram and express path, funneling into a single shared **JIT delivery engine** section, followed by a **Reference** appendix.
- Added pseudo-diagrams (decision tree, per-playbook flows, JIT lifecycle, artifact chain, workspace tree) as an orientation aid alongside the prose.
- Documented the full **Rebuild / pm-reconcile flow** end to end (prep → plan → per-layer reconcile → status → handoff), giving the Rebuild playbook a proper home instead of being buried under Feature Implementation.
- Folded the standalone Fast Track section into each playbook as its "Express path".
- Consolidated content that was duplicated (delivery rules appeared twice; JIT delivery was split between Greenfield and Feature Implementation).
- Fixed the stale "Rebuild coming soon" references (the playbook shipped in v5.1.0).

---


## [5.1.0] - 2026-06-24

Fills the long-standing "Rebuild playbook coming soon" slot in the orchestrator.

### New Skills

- **pm-reconcile** - the Rebuild playbook for onboarding an existing product whose legacy docs (BRD, FSD, domain/entity models, business rules) conflict with the code and each other. Two-phase, argument-driven:
  - **Plan** (`/pm-reconcile`): inspects the docs + codebase surface, detects which areas exist, maps each to its target Pureinn artifact, and defines the order. Writes `reconciliation_plan.md` and initializes `state.json reconcile.areas[]`.
  - **Per-area execution** (`/pm-reconcile domain | rules | features | ...`): reconciles one layer at a time in dependency order (entities → rules → features = registers 1 → 2 → 3 → 4). State-machine **structure** reconciles in `domain`; transition **guard conditions** reconcile in `rules`.
  - Asymmetric source-of-truth model: **code = truth for structure** (names, shape, what is implemented - docs rewritten to match, mechanically); **docs = truth for business logic** (rule values, decisions - code divergences flagged as `DIV-NN` and asked via AskUserQuestion, never silently resolved). Docs ahead of code → `specified, not implemented` (backlog), not fabricated into the registers. Code never changes.
  - Appends to a living **Reconciliation Report** per area, then rebuilds that register via the existing register skills in reconciled mode. Business logic migrated fully now; feature technical design (Sections 2-3) stays JIT.
- **pm-reconcile-status** - read-only progress dashboard for the multi-session reconcile. Reads `reconciliation_plan.md` + `state.json`, shows which areas are done/in-progress/pending, surfaces open divergences awaiting a team decision, and routes to the next area command. The session re-entry tool for a long-running rebuild (the reconcile analogue of pm-stripe).

### Changed

- Orchestrator (`/pureinn`): the **Rebuild** route (Playbook D) is now live and points to `/pm-reconcile`. Migration path documented as two sub-paths - A1 reconcile (conflicting docs) vs A2 bootstrap (clean/absent docs). Updated in COMMAND.md, README.md, FRAMEWORK_GUIDE.md.
- `pm-entity-registry`, `pm-business-rules-library`, `pm-reverse-extract`: added a **reconciled mode** note - when a Reconciliation Report exists, it is the authoritative input; they do not re-question what it already settled.

---


## [5.0.0] - 2026-06-23

Framework-wide consistency audit (follow-up to the v4.11.0 Feature Card alignment).

### Breaking Changes

- **Removed deprecated skills** `pm-brd`, `pm-fsd`, `pm-feature-set-overview` (the entire `skills/deprecated/` folder). They have been non-functional since v4.0.0.
  - Migration: `pm-brd` → `pm-entity-registry` (entities + state machines) + `pm-business-rules-library` (rules + decision models). `pm-fsd` → `pm-feature-design` (JIT per-feature design). `pm-feature-set-overview` → `pm-feature-card` + `pm-prd`.

### Changed

- **pm-domain-model** repositioned as the optional higher-level companion to `pm-entity-registry` (cross-domain ERD + domain boundaries above the operational `entities.md` register). Removed the contradictory "Replaces pm-domain-model" wording from `pm-entity-registry`; the two are complementary, not alternatives.
- **Feature Set ID system (FS-NN):** Feature Sets now get a stable globally-sequential ID (`FS-01`, `FS-02`, ... continuing across domains). `pm-features-list` assigns them; `feature_set: "FS-NN: name"` added to the canonical Feature Card frontmatter (pm-feature-card, pm-features-list, pm-reverse-extract). All `[FS-ID]` references normalized to the `FS-NN: Name` format.
- Removed lingering deprecated-skill mentions from active skill descriptions (pm-feature-design, pm-business-rules-library) and CLAUDE.md examples. Historical CHANGELOG entries left intact.

### Fixed

- **pm-features-list** Notion cache key: `notion.product_features_data_source_id` → `notion_ids.feature_backlog` (now matches the convention used by all other Notion-pushing skills).

### Docs

- Documented workspace path conventions in CLAUDE.md: full no-leading-slash paths for file save locations, leading-slash workspace-root-relative paths for in-document cross-references.

---


## [4.11.0] - 2026-06-23

### Feature Card consistency: unified structure, headers, naming and placeholder text across pm-feature-card, pm-features-list, pm-feature-design and pm-reverse-extract (.md + Notion parity)

---


## [4.10.0] - 2026-06-15

### Audit and align all example documents with skills: bug fixes, missing sections, skill template updates (Section 1 table format, BC numbered format, Full ERD)

---


## [4.9.1] - 2026-06-15

### Fix product-roadmap-v3 example: full product Feature Sets, Version History moved to end, structure matches skill template

---


## [4.9.0] - 2026-06-15

### Added PRD_master and product-roadmap-v3 examples to saas-subscription showcase

---


## [4.8.1] - 2026-06-09

### Fix saas-subscription README - correct reading order, add domain_model and decision_models to workflow, remove stale 'not needed' note

---


## [4.8.0] - 2026-06-09

### Added domain_model.md and decision_models.md examples to saas-subscription showcase

---


## [4.7.2] - 2026-06-08

### pureinn-resume: explicit project root for _archive and .claudeignore creation

---


## [4.7.1] - 2026-06-08

### pureinn-resume creates _archive and .claudeignore if missing

---


## [4.7.0] - 2026-06-08

### Fix all remaining empty Notion pages + _archive/.claudeignore init + pm-diagrams Notion push

---


## [4.6.0] - 2026-06-08

### Replace template_id with inline content across all Notion push operations

---


## [4.5.1] - 2026-06-08

### Add template_id to pm-entity-registry and pm-business-rules-library Notion push

---


## [4.5.0] - 2026-06-08

### pm-business-rules-library Notion push to Business Rules DB and Decision Models DB

---


## [4.4.0] - 2026-06-08

### pm-entity-registry pushes to Notion Entity Catalogues; Event Catalogue added to variables template

---


## [4.3.0] - 2026-06-08

### pm-feature-design pushes Sections 1-3 to Notion after spec is complete

---


## [4.2.7] - 2026-06-08

### Feature Card stub includes description, current state and evidence from extraction

---


## [4.2.6] - 2026-06-08

### Explicit template_id lookup steps in pm-reverse-extract and pm-features-list Notion push

---


## [4.2.5] - 2026-06-08

### pm-reverse-extract: add template_id to Notion push so feature pages get Feature Card Template structure

---


## [4.2.4] - 2026-06-06

### Fix: all A/B/C/D option questions use AskUserQuestion tool instead of plain text

---


## [4.2.3] - 2026-06-06

### Deep Notion schema audit fixes: pm-features-list, pm-mvp-scope, pm-feature-card

---


## [4.2.2] - 2026-06-06

### pm-reverse-extract Notion push aligned to new DB schema (status values, FEAT-ID, Artefact Type)

---


## [4.2.1] - 2026-06-05

### Fast Track documented in README and FRAMEWORK_GUIDE

---


## [4.2.0] - 2026-06-05

### Notion sync in pm-stripe, three Fast Track paths, Rebuild coming soon

---


## [4.1.1] - 2026-06-05

### Pre-launch consistency audit: remove stale BRD/FSD/feature-forge/impeccable-teach/time-box references

---


## [4.1.0] - 2026-06-05

### User-centric onboarding: PREREQ+handoff patterns, Impact over Activity, first-run orientation, no time estimates

---


## [4.0.1] - 2026-06-04

### Post-audit fixes: example files state names, CHANGELOG v4.0.0 detail, CLAUDE.md version, pm-feature-viability in related-skills

---


## [4.0.0] - 2026-06-04

### Breaking Changes

**Feature Card lifecycle states renamed** - all 6 status values changed. Any project using Feature Card frontmatter `status:` fields must update to new names.

| Old | New |
|---|---|
| `1_Walkthrough` | `1_Backlog` |
| `2_Design` | `2_Spec_Done` |
| `3_Design_Inspection_Passed` | `3_Ready_to_Build` |
| `4_Build` | `4_In_Build` |
| `5_Code_Inspection` | `5_In_Review` |
| `6_Promoted_to_Build` | `6_Shipped` |

Applied across 9 framework files + all example files.

### New Skills

- **pm-feature-viability** - Feature Viability Assessment for Feature Implementation playbook. Optional Step 0 before JIT design. Produces KANO classification, MDP scope, and pre-defined success metrics. Explicitly skippable when feature is already scoped or committed.

### Skill Updates

**pm-stripe v3.0.0** - Complete rewrite:
- All 6 lifecycle states now have dedicated steps (was missing 4_In_Build, 5_In_Review, Design Inspection menu entry)
- Smart context detection on session start: detects mid-cycle features and surfaces next action
- Re-entry logic for interrupted sessions
- Explicit stripe closure step (Step 1G)
- State transition table added to skill overview

**pm-feature-design** - UX/UI context added:
- Step 1 now asks for UX/UI context for UI features: text description, screenshot, Figma URL, or Figma MCP
- Section 3b added to Feature Card template: placement in app, user-facing intent, design system reference, Figma link
- Figma MCP reads from `figma_project_url` in pureinn-variables.md when connected

**pm-mvp-scope** - Human-in-the-loop decision layer:
- New AskUserQuestion: what matters most for this MVP (UX quality / revenue validation / technical foundation / speed)
- Preliminary MVP cut now shows explicit trade-offs per feature
- Override check: user can move features against KANO/V×C recommendation
- User judgment explicitly overrides framework suggestion

### Integrations

**Figma MCP** - New integration:
- `pureinn-variables.md` template now includes `figma_project_url` and `figma_design_system_url`
- README MCP integrations table updated with Figma row
- pm-feature-design reads from Figma MCP when connected; falls back to URL paste or screenshot

### Documentation

- Skill count updated to 36 (35 + pm-feature-viability)
- FRAMEWORK_GUIDE Phase 6+7 JIT cycle table updated with Step 0 (optional viability)
- COMMAND.md Phase 6+7 routing updated
- Example files updated to new state names

---


## [3.1.1] - 2026-06-04

### Fix all audit findings: 4_Build state naming, skill counts 37→35, deprecated refs in pm-domain-model/pm-domain-analysis/pm-glossary/pm-prd, Subject Area removed from pm-prd checklist

---


## [3.1.0] - 2026-06-04

### Feature Card lifecycle complete (4_In_Build, 5_Code_Inspection), PIVOT escalation rule, gate types documented, KANO+VxC explained, deprecated skills moved, Feature Set clarified as grouping label, Subject Area removed

---


## [3.0.1] - 2026-06-04

### Fix all residual Phase 3 references across 15 files after 3.0.0 split

---


## [3.0.0] - 2026-06-04

### Breaking Changes

### Split Phase 3 into 3a (Validation) and 3b (Commercial Definition) - separate phases with hard gate, done-elsewhere support, and state.json tracking

---


## [2.4.2] - 2026-06-04

### Added specific downstream risk callouts to Path B in pm-problem-validation, pm-personas, design-thinking, and pm-hypotheses

---


## [2.4.1] - 2026-06-03

### Added recommended option rule (ROI-based, not easiest) and proactive assumption surfacing to skill question pattern

---


## [2.4.0] - 2026-06-03

### Updated all skills to use AskUserQuestion tool for option-based questions; added proactive I-dont-know handler to CLAUDE.md skill question pattern

---


## [2.3.0] - 2026-06-01

### Examples folder - realistic output showcase

**New: `examples/` folder in plugin repo:**
- Purpose: set correct user expectations with realistic output artifacts from an ideal FDD+SDD workflow run.
- First example: `examples/saas-subscription/` - Feature Implementation, subscription billing domain.
- Covers: Initiative PRD, full domain register set (entities, business rules, feature list), two Feature Cards at different lifecycle stages.

**FEAT-SUB-001.md (6_Promoted_to_Build - complete):**
- All 4 sections present: Biznis Mantinely, ACs, Technical Design, Realizacny Protokol.
- Section 3 includes full Mermaid sequenceDiagram (8 participants: Admin, FE, API, SubscriptionService, InvoiceService, Stripe, WebhookController, EmailService).
- Section 4 includes 7 commits with hashes, 10 test results, feature flag verification, Code Inspection sign-off.

**FEAT-SUB-003.md (3_Design_Inspection_Passed - pre-build):**
- Sections 1-3 complete. Section 4 empty (written just before build).
- Shows contrast with FEAT-SUB-001 to illustrate the 6-state Feature Card lifecycle.
- Covers two-direction flow: cancellation + reactivation path (BR-SUB-003 + BR-SUB-004).

**README.md updated:**
- Examples section added to plugin README with a reference table.

---

## [2.2.0] - 2026-06-01

### Comprehensive framework consistency pass + full-stack builder role

**AskUserQuestion - guided input collection:**
- Global CLAUDE.md skill interaction pattern updated: all decision points in Step 0 and Step 1 must use AskUserQuestion tool (not plain text prompts). Recommended option goes first.
- pm-prd, pm-entity-registry, pm-business-rules-library, pm-features-list: Step 0 mode detection updated to explicitly call for AskUserQuestion at key branch points.

**Full-stack builder role definition (CLAUDE.md):**
- New "Claude's role in this framework" section before skill interaction pattern.
- Defines Claude as PM + architect + developer + orchestrator.
- Instructs: reason like an implementer, proactively flag architectural implications, always close with next step + risk of skipping.

**pm-business-rule-core/critical/governance - repurposed as JIT helpers:**
- Complete rewrite of all 3 skills. Old RULE-A/B/C → BRD model removed.
- New: JIT helpers that add a single BR-[DOMAIN]-NNN rule to existing `domain/business_rules.md`.
- pm-business-rule-critical: Critical priority, hard invariants, no exceptions
- pm-business-rule-core: High/Medium priority, operational rules, may have exceptions
- pm-business-rule-governance: Compliance/Regulatory/Policy rules (GDPR, admin constraints)
- All 3 append to business_rules.md with correct format, domain section, and Changelog update.

**pm-feature-set-overview - deprecated:**
- Replaced by Feature Cards (pm-feature-card) + Initiative PRD (pm-prd Initiative mode).
- Deprecation notice added. Legacy content preserved.

**pm-reverse-extract - full rewrite (v1.x → v2.0.0):**
- Removed: BRD/FSD references, F-001 IDs, feature-sets.md artifact, MFS/FS hierarchy.
- Added: FEAT-[DOMAIN]-NNN IDs (domain code from entities.md), feature_list.md (Live Register 4), stub Feature Cards in features/cards/, Delivery Stripe assignment, post-extract JIT design queue.
- Run order documented: pm-entity-registry → pm-business-rules-library → pm-reverse-extract.
- State update: sets `registers.feature_list_initialized: true`, `current_phase_index: 6`.

**Feature ID examples updated:**
- pm-features-list: dependency matrix, critical path, KANO table, V×C table: F-001 → FEAT-[DOMAIN]-NNN
- pm-mvp-scope: MVP table, Post-MVP table: F-001 → FEAT-[DOMAIN]-NNN

**Metadata cleanup (related-skills):**
- pm-domain-analysis, pm-privacy-requirements, pm-domain-model, pm-glossary: pm-brd/pm-fsd references replaced with pm-entity-registry, pm-business-rules-library, pm-feature-design.
- pm-feature-set-overview: related-skills updated to pm-feature-card, pm-prd, pm-stripe.
- pm-business-rule-core/critical/governance: related-skills updated to pm-business-rules-library, pm-entity-registry, pm-feature-design.
- pm-reverse-extract: related-skills updated to pm-entity-registry, pm-business-rules-library, pm-feature-design, pm-stripe.

---

## [2.1.0] - 2026-06-01

### Phase folder naming, PRD_master, initiatives/ folder, universal append mode

**Workspace structure improvements:**
- Phase artifact folders renamed from `phase-N/` to `phase-N-name/` (e.g., `phase-3-define/`, `phase-4-domain/`, `phase-5-planning/`) for immediate context at a glance.
- New `initiatives/[slug]/` folder per project: separates discovery artifacts, Initiative PRD, and scoped KANO/V×C per initiative from the product-level workspace. Returning to a product after months with a new feature no longer pollutes the existing artifact structure.

**PRD dual mode (pm-prd updated):**
- Greenfield Phase 3 PRD renamed `PRD_master.md` (saved to `product/PRD_master.md`). Frozen after creation - never overwritten.
- New Initiative PRD mode: scope-limited document saved to `initiatives/[slug]/prd.md`. Living, updatable per initiative. Separate from PRD_master. Drives append mode for all 4 living registers.
- Mode detection in pm-prd Step 0: checks whether PRD_master exists to determine which mode to apply.

**Universal append mode for all 4 living registers:**
- `pm-entity-registry`: Create mode (first run) vs. Append mode (subsequent initiatives). New domain entities appended as new sections; existing entities untouched.
- `pm-business-rules-library`: Create mode vs. Append mode. New domain section added with `## [Domain] Rules (BR-[NEW-DOMAIN]-*)` header; no existing rule IDs modified.
- `pm-features-list`: Create mode vs. FI Append mode (Feature Implementation, per initiative). New FEAT-[NEW-DOMAIN]-* features appended; KANO + V×C saved to `initiatives/[slug]/` instead of overwriting Phase 5 master analysis.
- `decision_models.md`: same append pattern as business_rules.md (managed by pm-business-rules-library).

**Updated artifact paths:**
- pureinn-resume artifact expectation map updated to use named phase folders.
- FRAMEWORK_GUIDE.md and README.md workspace structure sections updated.

---

## [2.0.0] - 2026-06-01

### FDD+SDD hybrid redesign: 4 living registers, JIT per-feature design, atomic commit protocol

**Breaking changes:**
- `pm-brd` and `pm-fsd` are deprecated. Replaced by `pm-entity-registry`, `pm-business-rules-library`, and `pm-feature-design` (JIT).
- Feature Sets are no longer spec units. BRD and FSD per Feature Set are removed from Phase 6.
- Delivery Stripes are no longer time-boxes. They are domain-focused parallel channels.
- Feature IDs changed from `F-001` to `FEAT-[DOMAIN]-[NUMBER]` (e.g., FEAT-ORD-001).
- Workspace structure changed: `artifacts/phase-6/` replaced by `domain/`, `features/`, `features/cards/`.

**New skills:**
- `pm-entity-registry`: Live Register 1. Extracts entities from PRD Business Capabilities. Generates Mermaid stateDiagram-v2 per entity. Guard conditions left TBD for JIT finalization by pm-feature-design.
- `pm-business-rules-library`: Live Registers 2+3. Manages business_rules.md (BR-[DOMAIN]-[NUMBER]) and decision_models.md (TBL-[DOMAIN]-[NUMBER]). Draft mode in Phase 4, rules finalized JIT in Phase 6.
- `pm-feature-design`: JIT Design by Feature. Replaces pm-fsd. Per feature, per stripe, just before build. Two atomic commits: (1) register updates (guard conditions, rule finalization), (2) Feature Card Sections 1-3 (Biznis Mantinely, ACs, Mermaid sequenceDiagram + files to modify). Feature Implementation mode: scans real codebase before generating sequence diagram.

**Updated skills:**
- `pm-feature-card`: Complete rewrite. New 4-section template. Frontmatter: FEAT-[DOMAIN]-[NUMBER] ID, stripe, prd_ref, feature_flag. Section 1: Biznis Mantinely (BR-IDs, entity guard conditions). Section 2: Acceptance Criteria (happy path, guard failure, flag OFF). Section 3: JIT Technical Design (Mermaid sequenceDiagram, files to modify). Section 4: Realizacny Protokol (commits, tests, flag verification, Code Inspection - immutable after 6_Promoted_to_Build). 6-state lifecycle: 1_Walkthrough -> 2_Design -> 3_Design_Inspection_Passed -> 4_Build -> 5_Code_Inspection -> 6_Promoted_to_Build.
- `pm-features-list`: ID format FEAT-[DOMAIN]-[NUMBER]. Creates stub Feature Cards (status: 1_Walkthrough) automatically. Saves to features/feature_list.md (Live Register 4) + features/cards/.
- `pm-mvp-scope`: MVP Cut per Feature. Delivery Stripes = domain-focused channels. Feature-to-Stripe assignment. Updates stripe: field in Feature Card frontmatter. Removed feature-sets.md artifact.
- `pm-stripe`: Complete rewrite. JIT orchestrator. Step 0: Stripe Dashboard. Step 1A: advance next feature (READY = status 1_Walkthrough + all deps Promoted + one at a time per stripe). Step 1B: mark Design Inspection passed. Step 1C: mark feature Promoted (fills Section 4). Step 1D: Impact Analysis when BR-ID changes. Atomic commit protocol enforced.
- `pm-prd`: No User Stories (incompatible with FDD). Business Capabilities section mandatory (drives entity extraction and feature decomposition). Modular PRD option for large products: PRD.md + PRD_[Domain].md. prd_ref in Feature Card links to specific section.
- `pm-diagrams`: Mermaid.js as primary tool for Claude Code (state machines in entities.md, sequence diagrams in Feature Card Section 3). Excalidraw remains secondary for human communication.

**Deprecated skills (content preserved for legacy projects):**
- `pm-brd`: Deprecated. Content split into pm-entity-registry (state machines, entities) and pm-business-rules-library (rules, decision models).
- `pm-fsd`: Deprecated. Replaced by pm-feature-design (JIT per Feature).

**Documentation updated:**
- COMMAND.md: Phase 4-7 flow, dashboard, workspace structure, artifact paths, state.json, Framework Map.
- FRAMEWORK_GUIDE.md: Phase 4+5+6+7 sections, artifact chain, Feature Set vs Stripe vs Feature Card, workspace structure, migration path.
- README.md: Skill map Phase 4+5+6+7, project output structure, MCP table.

---

## [1.7.0] - 2026-06-01

### Add pm-feature-card skill; replace feature-forge references throughout

- New skill `pm-feature-card`: bridges FDD spec layer (FSD) to individual feature delivery
- Combines pureinn context (F-ID, FS-ID, RULE-ID traceability, FSD AC derivation, Stripe context) with feature-forge strengths (EARS requirements, implementation checklist)
- Template: Section 0 Feature Meta (F-ID, FS-ID, Stripe, flag name, BRD/FSD references), Section 1 Purpose & User Value, Section 2 EARS Functional Requirements (derived from FSD, includes feature flag FR), Section 3 State Interactions, Section 4 Acceptance Criteria (derived from FSD AC-XX, includes flag OFF scenario), Section 5 Error Handling (business-level only - no HTTP codes), Section 6 NFRs (feature-scoped + feature flag ON/OFF/kill switch/rollout), Section 7 Implementation Checklist (Backend/Frontend/Feature Flag/Testing/Post-launch monitoring), Section 8 Dependencies (depends on / blocks), Section 9 Definition of Done, Section 10 Open Questions
- Feature flag mandatory: default OFF, gradual rollout Internal→5%→25%→50%→100%, kill switch if error rate >5%, 4-week post-launch monitoring
- Definition of Done includes all ACs numbered, flag verified, regression test, monitoring active
- Notion push: updates Feature entry in Feature Backlog DB (Status→Ready for Dev, flag name, references) and pushes Feature Card as page body
- All `feature-forge` references in pm-stripe, pm-fsd, pm-feature-set-overview, COMMAND.md, FRAMEWORK_GUIDE.md updated to `pm-feature-card`
- COMMAND.md: artifact path updated to `[f-id]-feature-card.md` in `phase-6/feature-cards/`

---


## [1.6.0] - 2026-06-01

### pm-fsd: rewrite template to match reference FSD structure (11 sections)

- Section 0: Document Meta table (Feature Set, Version, Owner, Status, Related BRD Sections, Related Domain Entities)
- Section 1: Purpose & Context - 1.1 Purpose (business problems + BRD rules), 1.2 Business Context (process + affected lifecycles + downstream prerequisites), 1.3 In Scope / Out of Scope (detailed bullet lists, each out-of-scope item names responsible FS)
- Section 2: References & Dependencies - 2.1 Referenced Business Rules (Rule ID | Name | Why enforced here), 2.2 Referenced State Machines (per entity), 2.3 Referenced Domain Entities (Entity | Attributes Used | Access R/W), 2.4 Dependencies on Other Feature Sets (FS | Dependency Type | Description)
- Section 3: Responsibilities & Boundaries - 3.1 Core Responsibilities, 3.2 Explicit Non-Responsibilities (each names the FS that handles it instead), 3.3 Assumptions & Constraints
- Section 4: Functional Behavior (BUSINESS-LOGIC VIEW) - 4.1 Entry Points / Triggers table, 4.2 Main Business Flow (numbered, named steps), 4.3 Validations & Guards table, 4.4 Edge Cases & Exceptional Scenarios
- Section 5: Events & Reactions - 5.1 Events Produced (Canonical | When | Meaning as business fact), 5.2 Events Consumed (Canonical | Producer | Expected Context), 5.3 Idempotency (per-event table) + Ordering expectations (Entity/Lifecycle | Events | Expected order | What if out-of-order)
- Section 6: State Interactions (Entity | From | To | Condition with rule reference)
- Section 7: Acceptance Criteria - AC-01 to AC-N format (Given/When/Then/And), covers happy path, each validation failure, idempotency, expiry/housekeeping
- Section 8: Non-Functional Expectations - 8.1 Performance, 8.2 Latency, 8.3 Consistency, 8.4 Accuracy (each with business justification)
- Section 9: Operational & Observability Notes - 9.1 Business Signals table, 9.2 Key Metrics table, 9.3 Alert-Worthy Conditions table, 9.4 Operational Notes
- Section 10: Open Questions & Pending Decisions
- Section 11: Working Notes (Engineering Playground) - non-binding section for API drafts, diagrams, tech notes
- Step 1 intake: restructured into 3 groups covering scope/context, behavior/events, and non-functional/observability
- Completeness checklist: updated to cover all 11 sections with specific coverage requirements

---


## [1.5.0] - 2026-06-01

### pm-brd: rewrite Phase 4 Skeleton and Phase 6 Detail templates to match reference BRD structure

- Phase 4 Skeleton: 10-section structure (0: Document Meta, 1: System Boundary, 2: State Machines overview, 3: Processes & Orchestration, 4-10: placeholders)
- Section 0: purpose/scope, BRD vs. non-BRD, boundaries & relationships, audience, how-to-read, references, notation glossary, change log
- Section 1: Primary Roles table, Secondary Roles table, Motivations & Needs table, Multi-Role Logic; System Boundary (Inside/Outside/External Systems); Capability Map by domain; Responsibility Split
- Section 2: State Machine Overview table (Entity | States | Key transitions | Detailed in)
- Section 3: Process Overview table (PROC-IDs, Layer, Trigger, Goal, Affected Lifecycles) + Orchestration Principles (ordering, blocking, override, fallback/recovery)
- Sections 4-10: flat-table placeholders (Business Rules, Decision Models, Event Catalogue 6.1/6.2/6.3, Notifications, Policies, NFRs, Open Questions)
- Phase 6 Detail: rich state machine format per entity - States Catalogue (State | Description | Terminal? | Notes), Allowed Transitions (From | To | Trigger Type | Trigger Name | Conditions | Related RULE IDs | Notes), Illegal/Blocked Transitions table, Entry/Exit Semantics per state, Exception & Override Paths, Coverage & Gaps
- Phase 6 Section 4 update: flat Business Rules table (Name | Rule ID | Category | Affected Entity | Description | Domain | Priority) + RULE-A/B detail cards
- Phase 6 Section 5 update: Decision Models Catalogue with full column set (Type TBL/TRE/SCR, Produces, Used in Process, Where in lifecycle, Uses Rules/Models/Decisions)
- Phase 6 Section 6 update: Event Catalogue 6.2 (Name | Category | Aliases | Business Meaning | Consumers | Lifecycle+State | Primary Entity | Producer | Related Rules | Trigger Type) + Event Propagation Map 6.3 (Canonical Event | Producer | Primary Entity | Lifecycle Transition | Business Reaction | Triggered Decisions | Governing Rules) with Downstream effects
- Completeness checklist updated to match all new sections and table formats

---


## [1.4.9] - 2026-06-01

### pm-brd: full Notion push to all 4 connected databases

- BRD page content now pushed directly to Notion page (Phase 4: set; Phase 6: append per FS) - no more "paste manually"
- Event Catalogue DB push added: one entry per business event in the BRD Business Events section
- Data Sensitivity DB push added: one entry per RULE-C rule with compliance/data-retention context
- Business Rules DB and Decision Models DB pushes unchanged, now documented as numbered steps
- Updated "What this skill does" to list all 4 Notion targets
- Completeness checklist: added Notion push section

---


## [1.4.8] - 2026-06-01

### pm-reverse-extract: push BRD/FSD/Domain Model to Notion, add FS Overview and Feature Card content

- Step 4c: FS entries now include Feature Set Overview as Notion page body
- Step 4d: Feature entries now include Feature Card content as page body (full for Done/In Progress, stub for Planned)
- Step 4e (new): pushes existing local BRD/FSD/Domain Model files to Notion as pages; links FS entries via BRD/FSD URL properties; updates pureinn-variables.md with created page URLs
- Step 4f (renamed from 4e): updated confirmation summary to include new push counts
- Step 6 migration summary: updated to reflect FS Overview, Feature Card, and doc push results
- Notion section: clarified which pureinn-variables.md keys are used in which steps; removed stale manual reminder

---


## [1.4.7] - 2026-05-31

### Rename impeccable-teach to /impeccable document across all references

- COMMAND.md: all `/impeccable-teach` references updated to `/impeccable document`
- FRAMEWORK_GUIDE.md: all `/impeccable-teach` references updated to `/impeccable document`
- Reflects current impeccable plugin API (skill renamed upstream)

---


## [1.4.6] - 2026-05-31

### Update FRAMEWORK_GUIDE.md for Path C and Notion template

- Phase 2 Track C row: updated "Before you run" to note Path C requires no prep
- "Bring your data" rule: added exception for pm-market-analysis Path C
- Workspace section: added reference to NOTION_TEMPLATE.md

---


## [1.4.5] - 2026-05-31

### Update README for Notion template and pm-market-analysis Path C

- README: updated pm-market-analysis skill description to mention three input paths (A/B/C)
- README: added Notion setup note in MCP integrations section with link to NOTION_TEMPLATE.md

---


## [1.4.4] - 2026-05-31

### Add Notion template setup guide and onboarding flow

- Added `NOTION_TEMPLATE.md` - setup guide with duplicate link (coming soon), full URL reference table, FAQ
- Updated `/pureinn` init message: after creating pureinn-variables.md, offers Option A (duplicate Notion template) and Option B (use own setup)

---


## [1.4.3] - 2026-05-31

### Add OpenAI Path C to pm-market-analysis with per-project API key via pureinn-variables.md

- pm-market-analysis: added Path C (AI-powered research via OpenAI Responses API with web_search)
- Path C reads OPENAI_API_KEY from pureinn-variables.md; prompts user to add key if blank
- Runs 3 targeted web search queries (market size, competitor analysis, market timing)
- pureinn COMMAND.md: added `AI Research` section to pureinn-variables.md template with OPENAI_API_KEY field

---


## [1.4.2] - 2026-05-31

### Remove Octagon Deep Research MCP integration (paid service)

---


## [1.4.1] - 2026-05-31

### Apply grouped question pattern to pm-reverse-extract Step 1

---


## [1.4.0] - 2026-05-31

### Add scoping question to pm-features-list; add grouped alignment pattern to pm-mvp-scope with preliminary MVP cut after Group 1

---


## [1.3.0] - 2026-05-31

### Apply grouped question pattern to all remaining documentation skills: project-charter, stakeholder-map, team-roster, comms-charter, prd, product-roadmap, privacy-requirements

---


## [1.2.0] - 2026-05-31

### Add grouped questions to decision skills; Path A/B to tech-feasibility and domain-analysis; Path C Octagon MCP to market-analysis

---


## [1.1.0] - 2026-05-31

### Add guided elicitation mode (Path B) to 5 research-dependent skills: pm-personas, jtbd-building, pm-market-analysis, pm-problem-validation, design-thinking

---


## [1.0.7] - 2026-05-31

### Apply grouped question pattern to all Type B skills: reduce options to max 4, restructure pm-pitch-deck into groups with confirmation

---


## [1.0.6] - 2026-05-31

### Separate free-text and option-based questions within groups; document universal question pattern in CLAUDE.md

---


## [1.0.5] - 2026-05-31

### Group intake questions into 3 rounds with confirmation summaries; document grouped question pattern as universal standard

---


## [1.0.4] - 2026-05-31

### Rewrite intake questions in natural A/B/C/D format to trigger AskUserQuestion UI

---


## [1.0.3] - 2026-05-31

### Use AskUserQuestion tool for interactive intake in pureinn

---


## [1.0.2] - 2026-05-31

### Intake questions now asked one at a time in pureinn

---


## [1.0.1] - 2026-05-31

### Test release script

---


## [1.0.0] - 2025-05-29

### Initial release

- 34 skills covering full product lifecycle (Phases 1-7)
- 2 orchestrator commands: `/pureinn`, `/pureinn-resume`
- Three playbooks: Greenfield, Feature Implementation, Rebuild
- MCP integrations: Notion (feature backlog, glossary, domain model), Excalidraw (diagrams), Gamma (pitch deck)
- FDD delivery cycle with Stripe orchestration
- Workspace state management via `pureinn-workspace/[slug]/state.json`
- Notion project configuration via `pureinn-variables.md`
