---
name: pm-privacy-requirements
description: Generate a PII Inventory, Privacy Requirements document, and GDPR Action Plan for Phase 4. Runs after Domain Model - maps personal data to entities, identifies processing purposes, and produces a concrete compliance action list before build starts.
license: MIT
metadata:
  agent-mode: synthesis
  author: https://github.com/ljucask
  version: "1.0.0"
  domain: product-management
  triggers: privacy, GDPR, PII inventory, data protection, privacy requirements, compliance
  role: specialist
  scope: compliance
  output-format: document
  related-skills: pm-domain-model, pm-domain-analysis, pm-entity-registry, pm-business-rules-library
---

# PM - Privacy Requirements


## Agent mode (`--agent`)

Supports `--agent`: runs autonomously in a subagent, drafts the artifact from existing inputs, and returns a short summary + coverage note.

- **No flag** → interactive (default); if inputs are heavy, offer agent mode.
- **`--agent`** → obey. First check inputs are complete. Anything missing: do NOT invent it - mark `[ASSUMED - what/why]` in the output and summary. Never hallucinate to fill a gap.

---

## What this skill does

Maps the domain model to privacy and data protection obligations. Produces:
1. PII Inventory - which entities contain personal data, what type, and how sensitive
2. Privacy Requirements - what the system must do to comply (consent, retention, rights)
3. GDPR Action Plan - concrete actions with owners and timing before launch

This skill runs after `pm-domain-model` - entities must be defined to inventory PII accurately. Output feeds directly into Phase 6 (`pm-feature-design` references privacy rules in Feature Card Section 1 for features that handle personal data).

This is a PM-level analysis, not a legal opinion. Validate with legal counsel before launch.

---

## Dependencies

**Required before running:**
- `pm-domain-model` - entities and their attributes are the input for PII mapping

**Recommended before running:**
- `pm-domain-analysis` - legal requirements from Phase 2 provide the regulatory baseline

**Produces artifacts used by:**
- `pm-business-rules-library` - privacy rules become RULE-A and RULE-C entries in `business_rules.md`
- `pm-feature-design` - consent flows, data export, deletion - specified JIT in Feature Card Section 1
- Phase 6 build - developers need privacy requirements before implementing user-facing features

---

## Step 0: Current state check

Check for existing artifacts:
- PII Inventory
- Privacy Requirements
- GDPR Action Plan

Also check: does a Domain Model exist? Without it, the PII inventory will be incomplete - flag this. Does a Legal & Regulatory Requirements document exist from Phase 2? Cross-reference regulatory scope stated there.

Look for: PII inventory without sensitivity classification, no legal basis per processing purpose, retention periods missing, user rights (erasure, portability) not addressed, no action plan with owners and dates.

**Re-run behavior (delta mode):** If these artifacts already exist (e.g., Domain Model changed - new entities/attributes added), do not rewrite from scratch. Read the current PII Inventory / Privacy Requirements / GDPR Action Plan first, re-map only the changed entities, update only what the new domain model supports (`[UPDATED - previous: X / new: Y]`), and mark what is unaddressed `[UNCHANGED]`. Show the delta before finalizing.

**Interaction:** Group related questions (2-4 per round) and confirm before moving on. For any A/B/C/D choice, use the AskUserQuestion tool with one option marked **(Recommended)** - never print options as plain text. Keep open-ended questions free-text (don't fake options). If the user is unsure, propose 3-4 concrete options plus "Other". Surface an assumption the moment you make one; never fabricate to fill a gap. (Full standard: CLAUDE.md.)

---

## Step 1: Gather inputs

Ask questions in 2 groups. After each group show a summary and wait for confirmation before continuing.

---

### Group 1 of 2 - Data context

Use AskUserQuestion tool for these two questions:

Which markets / jurisdictions does this product launch in?

  A) EU only (GDPR applies) (Recommended - narrowest compliance surface for a first launch; expand once GDPR compliance is proven, if this hasn't already been fixed by an earlier phase)
  B) EU + US (GDPR + state-level US privacy laws)
  C) Global from launch
  D) Non-EU only (no GDPR obligation)

Who are the primary users whose data the product processes?

  A) Adult consumers (B2C)
  B) Business employees or professionals (B2B)
  C) Mixed - both consumers and businesses
  D) Includes minors (under 16 in EU) - requires additional safeguards

Then ask as plain text:

Paste the Entity Catalogue from the Domain Model (or confirm it's already in context). I need entity names and their attributes to map PII accurately.

What does the product do in one sentence? Does it collect data directly from users, or receive it from third parties?

After answers, confirm: "Is this the correct data context?"

---

### Group 2 of 2 - Data flows and sensitive data

Use AskUserQuestion tool for these two questions - select all that apply for sensitive data:

Does the product handle any sensitive data categories?

  A) Health / medical data or financial data (bank accounts, payment cards)
  B) Location data (real-time or historical) or biometric data
  C) Data about children under 16
  D) None of the above - standard personal data only

Does the product use AI that processes user data?

  A) Yes - sends user content or personal data to an external LLM API (e.g., OpenAI, Anthropic)
  B) Yes - uses AI but only on anonymized or aggregated data
  C) No AI components that process personal data
  D) Unknown - not yet assessed

Then ask as plain text:

Does the product share user data with third parties? List any: analytics (Google Analytics, Mixpanel), payments (Stripe), marketing tools, AI APIs, or other external services.

Have any data retention periods been decided? Is there a cookie and tracking plan? Has a Data Protection Officer been appointed or considered?

After answers, show complete privacy inputs summary. Ask for final confirmation before generating PII Inventory and GDPR Action Plan.

---

## Step 2: Generate artifacts

Generate in English.

---

### ARTIFACT 1: PII Inventory

```markdown
# PII Inventory - [Product Name]

> **Phase:** 4 - Domain Modeling
> **Date:** [date]
> **Based on:** Domain Model v[X]
> **Status:** Draft - requires legal review before acting

---

## PII Classification Legend

| Class | Definition | Examples |
|---|---|---|
| Personal | Identifies or can identify a natural person | Name, email, phone, IP address |
| Sensitive | Special category under GDPR Art. 9 | Health, biometric, political, religious |
| Pseudonymous | Can identify when combined with other data | User ID, hashed email |
| Anonymous | Cannot identify a person even when combined | Aggregated stats, anonymized logs |

---

## Entity PII Map

| Entity | Attribute | PII Class | Legal Basis | Retention | Notes |
|---|---|---|---|---|---|
| [Entity name] | [attribute] | Personal / Sensitive / Pseudo / None | Consent / Contract / Legitimate interest / Legal obligation | [X days / years / until deletion] | [e.g., Required for core function] |
| [Entity] | [attribute] | | | | |

---

## PII by Sensitivity

### High Sensitivity (Sensitive / Special Category)
[List entities and attributes classified as Sensitive]

### Medium Sensitivity (Personal - directly identifying)
[List entities and attributes - name, email, phone, address, IP]

### Low Sensitivity (Pseudonymous)
[List entities and attributes - IDs, hashed values]

### Third-Party Data Flows

| Data type | Sent to | Purpose | Legal basis | Can user opt out? |
|---|---|---|---|---|
| [e.g., User ID + behavior] | [e.g., Analytics provider] | [Product analytics] | [Legitimate interest] | [Yes - cookie banner] |
| [e.g., Message content] | [e.g., OpenAI API] | [AI feature] | [Contract] | [No - core feature] |
```

---

### ARTIFACT 2: Privacy Requirements

```markdown
# Privacy Requirements - [Product Name]

> **Phase:** 4 - Domain Modeling
> **Date:** [date]
> **Regulatory framework:** GDPR (EU), [other applicable frameworks]
> **Status:** Draft - requires legal review

---

## Applicable Regulations

| Regulation | Jurisdiction | Applicability | Key obligations |
|---|---|---|---|
| GDPR | EU / EEA | [High / Med / Low] | Consent, rights, DPA, breach notification |
| ePrivacy Directive | EU | [High if cookies/tracking] | Cookie consent, tracking opt-in |
| EU AI Act | EU | [If AI system deployed to EU users] | Risk classification, transparency |
| [Local law] | [SK / CZ / ...] | | |

---

## Consent Requirements

| Data type / Purpose | Consent required? | Consent type | Implementation |
|---|---|---|---|
| [e.g., Analytics cookies] | Yes | Opt-in (explicit) | Cookie banner with granular controls |
| [e.g., Core product data] | No - contract basis | - | Terms of Service acceptance |
| [e.g., Marketing emails] | Yes | Opt-in | Checkbox at registration (unchecked by default) |
| [e.g., AI processing of content] | [Yes if sensitive] | [Type] | [Where and how] |

**Consent implementation rules:**
- Pre-ticked boxes are prohibited (GDPR)
- Consent must be as easy to withdraw as to give
- Granular consent required - cannot bundle unrelated purposes
- Consent records must be stored (who, when, what they consented to)

---

## Data Retention Policy

| Data type | Retention period | Trigger for deletion | Legal basis for period |
|---|---|---|---|
| [Account data] | [Duration of account + X days after deletion] | [Account deletion request] | [Contract] |
| [Transaction records] | [7 years] | [Transaction date] | [Legal obligation - tax law] |
| [Analytics / logs] | [90 days] | [Rolling - auto-purge] | [Legitimate interest] |
| [Support tickets] | [2 years after resolution] | [Ticket closed] | [Legitimate interest] |

**Automated deletion:** [What mechanism will enforce retention limits - cron job, soft delete + purge, etc.]

---

## User Rights (GDPR Chapter III)

| Right | Applicability | Implementation required | Timeframe |
|---|---|---|---|
| Right of access (Art. 15) | Yes | Data export / account view | 30 days |
| Right to rectification (Art. 16) | Yes | Edit profile / data correction | 30 days |
| Right to erasure / "right to be forgotten" (Art. 17) | Yes | Account deletion + cascade | 30 days |
| Right to data portability (Art. 20) | Yes (if consent or contract basis) | Export in machine-readable format (JSON/CSV) | 30 days |
| Right to restrict processing (Art. 18) | Yes | Freeze account processing without deletion | 30 days |
| Right to object (Art. 21) | Yes (legitimate interest processing) | Opt-out mechanism | Immediately |
| Right not to be subject to automated decisions (Art. 22) | [If using profiling / AI scoring] | [Human review process] | |

**Implementation note:** All rights requests must be logged. Response within 30 days is mandatory. Refusal must be documented and communicated.

---

## Data Minimization

**Principle:** Collect only what is necessary for the stated purpose.

| Processing purpose | Data collected | Is all of it necessary? | What can be removed? |
|---|---|---|---|
| [User registration] | [name, email, password] | [Yes] | [N/A] |
| [Analytics] | [IP address, device] | [Partial] | [IP can be anonymized before storage] |
| [AI feature] | [Full message content] | [Review] | [Can we send only relevant excerpt?] |

---

## Data Processing Agreements (DPA)

A DPA is required with every third-party processor that handles personal data on our behalf.

| Processor | Data shared | DPA status | Notes |
|---|---|---|---|
| [e.g., Stripe] | Payment data | Required | Standard Stripe DPA available |
| [e.g., OpenAI] | User content (if sent to API) | Required | Review OpenAI data processing terms |
| [e.g., Analytics provider] | Behavioral data | Required | |
| [e.g., Cloud hosting (AWS/GCP)] | All data | Required | Standard DPA available |

---

## Privacy by Design Requirements

These must be addressed in architecture and feature specification:

- [ ] Data minimization enforced at collection point (no extra fields "just in case")
- [ ] Personal data encrypted at rest
- [ ] Personal data encrypted in transit (TLS everywhere)
- [ ] PII separated from analytics / logging (no PII in logs)
- [ ] Data access controlled by role (not everyone can see all PII)
- [ ] Audit log for access to sensitive data
- [ ] Deletion cascade: deleting a user removes or anonymizes all their PII across all entities
- [ ] IP anonymization in analytics before storage (if applicable)
- [ ] Data residency: EU data stored on EU infrastructure (if required)
```

---

### ARTIFACT 3: GDPR Action Plan

```markdown
# GDPR Action Plan - [Product Name]

> **Phase:** 4 - Domain Modeling
> **Date:** [date]
> **Target:** Pre-launch compliance

---

## Pre-Launch Mandatory Actions

| Action | Owner | Priority | Target date | Status |
|---|---|---|---|---|
| Draft Privacy Policy | [PM / Legal] | Critical | [Before any user-facing beta] | ☐ |
| Draft Terms of Service | [PM / Legal] | Critical | [Before any user-facing beta] | ☐ |
| Implement cookie consent banner (granular) | [Dev] | Critical | [Before launch] | ☐ |
| Implement account deletion (+ cascade) | [Dev] | Critical | [Before launch] | ☐ |
| Implement data export (portability) | [Dev] | High | [Before launch] | ☐ |
| Sign DPAs with all processors | [Founder / Legal] | Critical | [Before processing user data] | ☐ |
| Consent records logging | [Dev] | Critical | [Before launch] | ☐ |
| Encryption at rest for PII fields | [Dev] | Critical | [Before any user data stored] | ☐ |
| Legal review of Privacy Policy | [Legal] | Critical | [2 weeks before launch] | ☐ |

## Post-Launch Actions

| Action | Owner | Priority | Target date | Status |
|---|---|---|---|---|
| Appoint DPO (if required - >250 employees or systematic processing) | [Founder] | Med | [Q1 post-launch] | ☐ |
| Establish breach notification procedure (72h to supervisory authority) | [PM / Legal] | High | [Before launch] | ☐ |
| Retention policy automation (auto-delete aged data) | [Dev] | High | [Month 2 post-launch] | ☐ |
| Annual privacy audit | [PM / Legal] | Med | [12 months post-launch] | ☐ |

## Open Questions Requiring Legal Input

| Question | Impact | Who to ask |
|---|---|---|
| [e.g., Is our AI processing a "high-risk" activity under EU AI Act?] | [Could require DPIA] | [Legal counsel] |
| [e.g., Do we need a DPO?] | [Affects governance structure] | [Legal counsel] |
| [e.g., What is the correct legal basis for [specific processing]?] | [Affects consent model] | [Legal counsel] |

---

## Disclaimer

This action plan is based on PM and desk research. It does not constitute legal advice.
Validate all items with qualified legal counsel before launch.
```

---

## Step 3: Emit candidate business rules

The Dependencies section promises that privacy rules land in `business_rules.md` - make that real, do not leave it implicit. After the three artifacts are approved, extract every privacy requirement the **product itself must enforce** (not just the team must do) and list them as candidate rules ready for `/pm-business-rules-library`:

```
Candidate business rules from privacy requirements:
- [CANDIDATE-BR] Account deletion cascades to all PII across entities: [list] (Art. 17)
- [CANDIDATE-BR] Marketing consent = opt-in, unchecked by default, withdrawable in one step
- [CANDIDATE-BR] [Data type] auto-purged after [retention period]
- [CANDIDATE-BR] PII never written to logs / analytics events
...
```

Show the list to the user and note: "These go into `/pm-business-rules-library` as governance rules - that is how a privacy obligation becomes an enforceable, testable rule referenced by Feature Cards instead of a forgotten checklist item."

---

## Internal completeness checklist

<!-- Claude reference only - not shown to user.
     Use in Step 0 to identify gaps in existing artifacts.
     Use in Step 2 to verify full coverage before finalizing output. -->

**PII Inventory must cover:**
- [ ] All entities from Domain Model checked for personal data attributes
- [ ] Each PII attribute classified (Personal / Sensitive / Pseudonymous)
- [ ] Legal basis stated per attribute/purpose (Consent / Contract / Legitimate interest / Legal obligation)
- [ ] Retention period stated per data type
- [ ] Third-party data flows mapped (what goes to which processor and why)

**Privacy Requirements must cover:**
- [ ] GDPR applicability confirmed
- [ ] Consent requirements per processing purpose (what needs opt-in, what doesn't)
- [ ] All 7 GDPR user rights addressed with implementation approach
- [ ] Data retention policy with automated enforcement mechanism
- [ ] Data minimization assessment per processing purpose
- [ ] DPA requirements identified per processor
- [ ] Privacy by design checklist

**GDPR Action Plan must cover:**
- [ ] Pre-launch critical actions listed with owners and dates
- [ ] Privacy Policy and Terms of Service drafting scheduled
- [ ] Cookie consent implementation scheduled
- [ ] Account deletion (right to erasure) implementation required before launch
- [ ] Data export (portability) implementation required before launch
- [ ] Legal review scheduled before any user-facing release

**For SaaS/AI products:**
- [ ] AI API data processing assessed - does sending user content to LLM APIs require consent?
- [ ] EU AI Act risk category assessed (transparency obligations, prohibited practices)
- [ ] Multi-tenant data isolation verified - tenant A cannot access tenant B's data
- [ ] Model training on user data: if used, explicit consent and opt-out required
- [ ] Logging of AI outputs: does this constitute personal data processing?
- [ ] Data residency for AI processing: is user data sent to non-EU servers?

## Notion push

**Runs after user approves the privacy artifacts.**

1. Read `pureinn-variables.md` key `"Data Sensitivity Map"` → get DB URL
2. If blank: skip Notion push, output Markdown only
3. Call `mcp__claude_ai_Notion__notion-fetch` → extract `data_source_id`, cache in `state.json notion_ids.data_sensitivity_map`

For each PII field/data class from the PII Inventory, call `mcp__claude_ai_Notion__notion-create-pages` with both `properties` AND `content`. Do NOT use template_id.

```
properties:
  Name: [Field/data class name]
  Attribute (Business Name): [Business-readable attribute name]
  Classification Level: [L2 / L3 / L4]
  Description: [What this data is]
  Implied Sensitivity: [Why it's sensitive]
  Usage Context: [Where it's stored/used]

content:
  ## [Field Name]

  **Classification:** [L2 - Internal / L3 - Confidential / L4 - Restricted]
  **Entity:** [Which entity holds this field]

  ## Sensitivity Rationale

  [Why this data is classified at this level]

  ## Legal Basis (GDPR)

  [Legal basis for processing: consent / contract / legitimate interest / etc]

  ## Retention Period

  [How long this data is kept and why]

  ## Access Controls

  [Who can access this data and how]
```

After push: report counts (created, errors).

## Save to

```
pureinn-workspace/[project-slug]/artifacts/phase-4-domain/pii-inventory.md
pureinn-workspace/[project-slug]/artifacts/phase-4-domain/privacy-requirements.md
pureinn-workspace/[project-slug]/artifacts/phase-4-domain/gdpr-action-plan.md
```

---

## Handoff

**Čo si teraz má:** PII Inventory, Privacy Requirements a GDPR Action Plan - vieš aké osobné údaje spracúvaš a aké povinnosti z toho plynú ešte pred buildom.

**Ďalší krok:** `/pm-features-list` (Phase 5) — feature inventory + KANO/V×C. Privacy pravidlá sa zapíšu ako BR governance pravidlá.

**Môžeš preskočiť ak:** Phase 4 je hotová a chceš rovno plánovať features.
