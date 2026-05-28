---
name: pm-privacy-requirements
description: Generate a PII Inventory, Privacy Requirements document, and GDPR Action Plan for Phase 4. Runs after Domain Model - maps personal data to entities, identifies processing purposes, and produces a concrete compliance action list before build starts.
license: MIT
metadata:
  author: https://github.com/ljucask
  version: "1.0.0"
  domain: product-management
  triggers: privacy, GDPR, PII inventory, data protection, privacy requirements, compliance
  role: specialist
  scope: compliance
  output-format: document
  related-skills: pm-domain-model, pm-domain-analysis, pm-brd
---

# PM - Privacy Requirements

## What this skill does

Maps the domain model to privacy and data protection obligations. Produces:
1. PII Inventory - which entities contain personal data, what type, and how sensitive
2. Privacy Requirements - what the system must do to comply (consent, retention, rights)
3. GDPR Action Plan - concrete actions with owners and timing before launch

This skill runs after `pm-domain-model` - entities must be defined to inventory PII accurately. Output feeds directly into Phase 6 (BRD and FSD reference privacy rules when specifying features that handle personal data).

This is a PM-level analysis, not a legal opinion. Validate with legal counsel before launch.

---

## Dependencies

**Required before running:**
- `pm-domain-model` - entities and their attributes are the input for PII mapping

**Recommended before running:**
- `pm-domain-analysis` - legal requirements from Phase 2 provide the regulatory baseline

**Produces artifacts used by:**
- `pm-brd` - privacy rules become RULE-A and RULE-C entries in the BRD
- `pm-fsd` - consent flows, data export, deletion - all specified at feature level in FSD
- Phase 6 build - developers need privacy requirements before implementing user-facing features

---

## Step 0: Current state check

Check for existing artifacts:
- PII Inventory
- Privacy Requirements
- GDPR Action Plan

Also check: does a Domain Model exist? Without it, the PII inventory will be incomplete - flag this. Does a Legal & Regulatory Requirements document exist from Phase 2? Cross-reference regulatory scope stated there.

Look for: PII inventory without sensitivity classification, no legal basis per processing purpose, retention periods missing, user rights (erasure, portability) not addressed, no action plan with owners and dates.

Apply the standard skill interaction pattern (CLAUDE.md).

---

## Step 1: Gather inputs

```
I need inputs for the Privacy Requirements analysis.

1. DOMAIN MODEL
   Paste the Entity Catalogue from the Domain Model (or confirm it's in context).
   I need the entity names and their attributes to map PII accurately.
   [paste Entity Catalogue or "in context"]

2. PRODUCT AND MARKET CONTEXT
   What does the product do in one sentence?
   Who are the users? (consumers, businesses, employees, children?)
   What markets / jurisdictions? (EU, US, global...)

3. KEY DATA FLOWS
   Does the product collect data directly from users, or receive it from third parties?
   Does the product share user data with third parties? (analytics, payment, marketing, AI APIs...)
   Does the product use AI that processes user data? (e.g., sends user content to an LLM API)

4. SENSITIVE DATA
   Does the product handle any of the following?
   - Health or medical data
   - Financial data (bank accounts, payment cards)
   - Location data (real-time or historical)
   - Biometric data (face recognition, fingerprints)
   - Data about children (under 16 in EU)
   - Political, religious, or union membership data

5. EXISTING DECISIONS
   Have any data retention periods been decided?
   Is there a cookie / tracking plan?
   Has a Data Protection Officer (DPO) been appointed or considered?
```

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

Read `pureinn-variables.md` key "Data Sensitivity Map" → get DB URL.
If blank: skip Notion push, output Markdown only.
Check `state.json notion_ids.data_sensitivity_map` for cached ID. Fetch and cache if missing.

Push one entry per PII field/data class from the PII Inventory to the Data Sensitivity Map DB.
Use actual schema from notion-fetch to map: field name → title, entity → related entity field, sensitivity level (Public / Internal / Confidential / Restricted) → classification property, legal basis → notes, retention period → retention field if available.

After push: report counts (created, errors).

## Save to

```
pureinn-workspace/[project-slug]/artifacts/phase-4/pii-inventory.md
pureinn-workspace/[project-slug]/artifacts/phase-4/privacy-requirements.md
pureinn-workspace/[project-slug]/artifacts/phase-4/gdpr-action-plan.md
```
