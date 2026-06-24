---
name: pm-glossary
description: Generate and maintain a project glossary - terms, abbreviations, entities, artifacts, and concepts used across the product lifecycle. Runs progressively throughout the project. Can be called at any time to add terms, review existing entries, or export the full glossary.
license: MIT
metadata:
  author: https://github.com/ljucask
  version: "1.0.0"
  domain: product-management
  triggers: glossary, domain glossary, terminology, definitions, ubiquitous language, terms
  role: specialist
  scope: documentation
  output-format: document
  related-skills: pm-domain-model, pm-entity-registry, pm-business-rules-library, pm-feature-design
---

# PM - Project Glossary

## What this skill does

Builds and maintains a living glossary of terms used across the product development lifecycle - from discovery through launch. Captures business terms, domain entities, product artifacts, process concepts, rules, and abbreviations in a structured table.

This skill is continuous - it runs throughout the project, not in a single phase. It can be triggered:
- Manually by the user at any time (`/pm-glossary`)
- After completing a phase, to capture new terminology introduced
- When a term needs to be clarified or defined precisely

The glossary is additive: each run merges new entries with existing ones. Existing definitions are updated only if explicitly requested.

---

## Dependencies

**No hard dependencies.** Can run at any point in the project.

**Best used after:**
- `pm-project-charter` - captures initial product and business terminology
- `pm-domain-model` - generates the richest set of domain entities and relationships
- `pm-business-rules-library`, `pm-feature-design` - introduces business rules and functional terms
- Any phase completion - new terms surface naturally as phases complete

---

## Step 0: Current state check

Check for an existing glossary artifact in `pureinn-workspace/[project-slug]/artifacts/glossary.md`.

Show state table:

| Artifact | Status | Detail |
|---|---|---|
| Glossary | ✅ / ❌ | [X terms / not yet created] |

If glossary exists: show a summary - how many terms, which domains are covered, when it was last updated.

Apply the standard skill interaction pattern (CLAUDE.md).

Use AskUserQuestion tool with:
- Question: "What do you want to do in this session?"
- Option A: "Add new terms - paste or describe what to capture (Recommended)"
- Option B: "Extract terms from an existing artifact - paste the artifact text"
- Option C: "Review and update existing entries"
- Option D: "Export full glossary as a clean table or something specific"

If user provides explicit intent with the command (e.g., `/pm-glossary add "Feature Set, Delivery Stripe, Stripe"`), skip the question and proceed directly.

---

## Step 1: Gather inputs

### If adding terms manually (Option A)

```
Provide the terms you want to add to the glossary.

For each term, share what you know:
  - Name (the term, abbreviation, or entity name)
  - What it means in this project context
  - Which domain it belongs to (Business / Technical / UX / Operations / Legal / Finance / Other)
  - Where it is used (which phases, documents, or conversations)
  - Any related terms or connected entities

You can provide a raw list and I will structure the entries.
```

### If extracting from an artifact (Option B)

```
Paste the artifact text below.
I will identify terms that should be in the glossary:
  - Domain entities and data objects
  - Process steps and methodologies
  - Artifacts and document names
  - Business rules and constraints
  - Abbreviations and acronyms
  - Roles and stakeholders
  - Metrics and KPIs

[paste artifact text]
```

---

## Step 2: Generate or update glossary

Generate in English.

Apply glossary name types consistently:

| Type | Definition | Examples |
|---|---|---|
| Artifact | A document or structured output produced during the process | PRD, BRD, FSD, Feature Card, Lean Canvas |
| Concept | An abstract idea or principle that shapes how the product is built or defined | PMF, JTBD, MDP, Value Proposition |
| Entity | A domain object: a real-world thing the system tracks or acts on | User, Booking, Feature Set, Stripe, Invoice |
| Metric | A measurement, KPI, or success indicator | NPS, LTV, CAC, AARRR, North Star Metric |
| Process | A methodology, workflow, or repeatable activity | FDD, Design Thinking, KANO Analysis, Sprint |
| Role | A stakeholder, team member, or system actor | PM, Tech Lead, Early Adopter, External API |
| Rule | A business rule, constraint, or governance requirement | Spec Gate, Feature Flag, Backward Compatibility |
| Abbreviation | A short form used throughout documents | B2B, SaaS, POV, HMW, V×C |

---

### ARTIFACT: Project Glossary

```markdown
# Project Glossary - [Product Name]

> **Phase:** Cross-phase (continuous)
> **Last updated:** [date]
> **Total terms:** [X]

---

## Glossary

| Name | Definition | Domain | Usage Context | Type | Connected Entities | Note |
|---|---|---|---|---|---|---|
| [Term] | [Clear, precise definition in project context] | [Business / Technical / UX / Operations / Legal / Finance] | [Which phases, documents, or conversations use this term] | [Artifact / Concept / Entity / Metric / Process / Role / Rule / Abbreviation] | [Related terms, linked entities, parent/child relationships] | [Disambiguation, edge cases, what this is NOT] |
```

**Ordering:** Alphabetical within each domain group.

**Domain groups (in order):**
1. Business
2. Technical
3. UX
4. Operations
5. Legal / Compliance
6. Finance

---

## Internal completeness checklist

<!-- Claude reference only - not shown to user.
     Use in Step 0 to identify gaps in existing glossary.
     Use in Step 2 to verify output quality before finalizing. -->

**Each entry must cover:**
- [ ] Name: the exact term as used in project documents (match casing and spelling)
- [ ] Definition: precise, not circular (does not use the term in its own definition)
- [ ] Domain: one of the 6 standard domains, or "Other" with explanation
- [ ] Usage Context: specific enough to tell someone where to look (e.g., "Used in Feature Card Section 1 and business_rules.md - defines the guard conditions for this entity state transition")
- [ ] Type: one of the 8 standard types
- [ ] Connected Entities: at least one link where relevant; empty only for standalone abbreviations
- [ ] Note: filled when term has a common misuse, overlaps with another term, or is context-specific

**Common issues to catch:**
- [ ] Abbreviations without expansion (e.g., "FDD" without "Feature Driven Development")
- [ ] Entities without their parent/child relationships noted (e.g., "Feature" without "Feature Set")
- [ ] Process terms without phase assignment in Usage Context
- [ ] Rules without the constraint they enforce noted

## Notion push

**Runs after user approves the glossary artifact.**

Read `pureinn-variables.md` key "Glossary" → get DB URL.
If blank: ask user, save URL to pureinn-variables.md.
Check `state.json notion_ids.glossary` for cached ID. If not cached: call `mcp__claude_ai_Notion__notion-fetch`, extract data source ID, save to `state.json notion_ids.glossary`.

For each term in the glossary, call `mcp__claude_ai_Notion__notion-create-pages` with both `properties` AND `content`. Do NOT use template_id - provide content directly.

```
properties:
  Name: [Term]
  Definícia (2–4 vety): [Definition text]
  Doména: [Domain]
  Typ pojmu: [Type - Entity/Status/Rule/Event/etc]
  Kontext použitia: [Usage context]
  Prepojené entity/procesy: [Related entities]

content:
  ## [Term]

  [Full definition - 2-4 sentences]

  **Domain:** [Domain]
  **Type:** [Type]
  **Used in:** [Where this term appears in the product]
  **Related:** [Related terms or entities]
```

Update if entry with matching Name already exists (use `mcp__claude_ai_Notion__notion-update-page`).

After push: report counts (created, updated, errors).

## Save to

```
pureinn-workspace/[project-slug]/glossary.md
```

---

## Handoff

**Čo si teraz má:** Aktualizovaný glossary - zdieľaný slovník termínov, entít a skratiek, ktorý drží jazyk projektu konzistentný.

**Ďalší krok:** Pokračuj v aktuálnej fáze - glossary je cross-phase utilita, spúšťaj ho kedykoľvek pribudne nová terminológia. `/pureinn` ti ukáže ďalší krok podľa fázy.
