---
name: pm-business-rule-governance
description: JIT helper - add a single Compliance or Policy rule to domain/business_rules.md. For GDPR, regulatory obligations, admin constraints, data handling policies, and UX behavioral rules. Use when pm-privacy-requirements or pm-domain-analysis surfaces a regulatory requirement that needs a BR-ID for referencing in Feature Cards.
license: MIT
metadata:
  agent-mode: decision
  author: https://github.com/ljucask
  version: "2.0.0"
  domain: product-management
  triggers: governance rules, compliance rules, GDPR rules, policy rules, regulatory, data handling, admin constraints
  role: specialist
  scope: specification
  output-format: document
  related-skills: pm-business-rules-library, pm-privacy-requirements, pm-domain-analysis, pm-feature-design
---

# PM - Business Rule: Compliance / Policy Rule (JIT Helper)


## Agent mode (`--agent`)

Podporuje `--agent`: beží autonómne v subagentovi, nadraftuje artefakt z existujúcich vstupov, vráti krátky súhrn + coverage note.

- **Bez flagu** → interaktívne (default); pri ťažkých vstupoch ponúkni agent režim.
- **`--agent`** → poslúchni. Najprv over úplnosť vstupov. Čo chýba: NEVYMÝŠĽAJ - označ `[ASSUMED - čo/prečo]` vo výstupe aj v súhrne. Nikdy nehalucinuj medzeru.
- **Review povinný:** artefakt obsahuje záväzky - po drafte vynúť review používateľa pred finalizáciou; nezavieraj rozhodnutia autonómne.

---

## What this skill does

Adds a single **Compliance or Policy rule** to `domain/business_rules.md` under the Regulatory/Compliance or User/Authorization section.

A rule belongs here when:
- It stems from a regulatory or legal requirement (GDPR, PSD2, ePrivacy, local tax law)
- It governs admin or ops behavior (what support agents can and cannot do)
- It defines a data handling policy (retention, deletion, logging, consent)
- It enforces a UX behavioral standard required by law or company policy
- It may have regional or partner-specific variations

If the rule has no exceptions and violation causes financial/legal harm → use `pm-business-rule-critical`.
If it is standard operational logic → use `pm-business-rule-core`.

**When to run:** When `pm-privacy-requirements` or `pm-domain-analysis` surfaces a regulatory requirement that needs a formal BR-ID. Or during `pm-feature-design` when a compliance constraint is discovered that must be documented before the feature is built.

---

## Dependencies

**Required before running:**
- `pm-business-rules-library` - `domain/business_rules.md` must exist (initialized in Phase 4)

**Recommended before running:**
- `pm-privacy-requirements` - GDPR and compliance requirements become REG-category rules
- `pm-domain-analysis` - regulatory requirements from Phase 2 may generate REG entries

**Produces artifacts used by:**
- `pm-feature-design` - JIT design reads BR-IDs when defining Feature Card Section 1 (Biznis Mantinely)
- Build phase - admin and compliance features implement REG-category logic

---

## Step 0: Current state check

Read `domain/business_rules.md` - specifically the Regulatory/Compliance and User/Authorization sections.

List existing compliance rules. Identify the next available BR-REG-NNN (or BR-USR-NNN for user/auth rules).

Check: does a similar compliance rule already exist? Check if this is actually a Critical invariant (use pm-business-rule-critical) or an operational rule (use pm-business-rule-core).

Use AskUserQuestion to confirm rule category (REG / USR / policy) before proceeding.

Apply the standard skill interaction pattern (CLAUDE.md).

---

## Step 1: Gather inputs

Use AskUserQuestion for structured choices. Gather via text prompt:

```
I need inputs to define a Compliance / Policy Rule for business_rules.md.

1. WHAT IS THE RULE?
   Describe the policy or requirement in plain language.
   (e.g., "Personal data must not be included in system logs",
    "Users must be shown a clear opt-out option for marketing emails in every email sent",
    "Admin actions on user accounts must be logged with the acting admin's ID and reason",
    "User data must be fully deleted within 30 days of an erasure request",
    "All payment transactions must be logged for 7 years for tax compliance")

2. RULE CATEGORY
   a) REG - Regulatory/Legal (GDPR, PSD2, tax law, local regulation)
   b) USR - User rights / Authorization (consent, data access, admin constraints)
   c) POL - Internal policy (company standard, operational guideline)

3. REGULATION / SOURCE
   Which specific regulation or policy does this stem from?
   (e.g., GDPR Article 17 / PSD2 SCA / ePrivacy Directive / local tax law / company policy)

4. SCOPE
   Which entity, data type, or user action does this apply to?
   Does it apply globally or only in specific markets/regions?

5. DATA RETENTION OR ACTION REQUIRED
   What must be stored, deleted, logged, or reported - and by when?
   (e.g., "deleted within 30 days", "retained for 7 years", "logged with timestamp and actor ID")

6. EXCEPTIONS OR REGIONAL VARIATIONS
   Are there known exceptions or market-specific variations?
```

---

## Step 2: Generate rule entry

Generate the appropriate BR-ID:
- REG category → `BR-REG-NNN`
- USR/auth category → `BR-USR-NNN`
- Policy category → `BR-POL-NNN` (or fold into nearest fitting existing category)

Generate in English.

---

### OUTPUT: business_rules.md entry

```markdown
### BR-REG-[NNN]: [Rule Name]
**Category:** Compliance
**Regulation:** [GDPR Article X / PSD2 / ePrivacy / local tax law / company policy]
**Affected entity:** [Entity name or data type]
**Priority:** Critical / High
**Status:** Draft / Final

**Rule:**
[Compliance requirement in business language. Precise enough to implement.]
Example: "All personal data associated with a deleted account must be purged from primary storage, backups, and logs within 30 days of the erasure request being confirmed."

**Data retention / action required:**
[What must be stored, deleted, reported, or logged - and within what timeframe]
Example: "Primary DB: delete within 24h of confirmed request. Backups: purge in next scheduled backup cycle (max 30 days). Logs: anonymize actor references within 30 days."

**Enforcement point:** [When and where this must be enforced in the system]
**Exceptions:** [Regional variations or known exceptions, or "None"]
**Applies to features:** [TBD - filled JIT by pm-feature-design]
**Source:** [Regulation name + article / policy document reference]
```

---

## Save to

Append the new rule under the correct section in:
```
pureinn-workspace/[project-slug]/domain/business_rules.md
```

Use `## Regulatory / Compliance Rules` section for REG-category rules.
Use `## User / Authorization Rules` section for USR-category rules.

If the section does not yet exist, create it.

Update the Rule Coverage Map. Update the Changelog.

---

## Handoff

**Čo si teraz má:** Jedno Compliance/Policy pravidlo (REG/USR kategória) pridané do `business_rules.md`.

**Ďalší krok:** Späť do JIT cyklu - `/pm-feature-design [FEAT-ID]` alebo `/pm-stripe`. Pre širšie PII súvislosti pozri `/pm-privacy-requirements`.

**Môžeš preskočiť ak:** Pravidlo už v registri je.
