# pm-audit

> Workspace health check - scans Pureinn artifacts against framework conventions, fixes drift, surfaces strategic contradictions

**Phase:** Cross-phase  
**Agent mode:** `synthesis` - runs fully autonomously  
**Version:** 1.4.0  
**Triggers:** audit, health check, consistency check, workspace check, framework drift, version migration, fix inconsistencies, sanity check, naming check, anti-pattern, strategic consistency, cross-artifact check, re-check

---

## When to use

- After `pm-reconcile` or `pm-reverse-extract`, as a verification pass
- When a workspace was built with an older Pureinn version
- Before continuing work after a long break, to confirm internal consistency
- After a strategic pivot, to check whether the strategy layer still agrees with itself

---

## What it produces

1. **Audit Report** (`audit/audit_report.md`) - findings by severity (P0-P3), scored
2. **Mechanical fixes applied in place** - with a diff summary
3. **AskUserQuestion round** - for every judgment call that cannot be auto-fixed

---

## How to invoke

```bash
/pm-audit                  # whole workspace (Tier 1 + Tier 2)
/pm-audit domain           # domain/entities.md + domain-model.md only (Tier 1)
/pm-audit rules            # business_rules.md + decision_models.md only (Tier 1)
/pm-audit features         # feature_list.md + features/cards/ only (Tier 1)
/pm-audit open-questions   # domain/open_questions.md only (Tier 1) - ID hygiene, no duplication elsewhere
/pm-audit strategy         # strategic layer only (Tier 2 - read-only)
/pm-audit [artifact-name]  # any specific artifact named by the user
/pm-audit --agent          # autonomous full-workspace audit
```

---

## Two tiers

**Tier 1 - Form (mechanical):**
Naming, IDs, cross-references, lifecycle validity, schema conformance, metadata completeness, framework-version drift. Tier 1 findings are auto-fixed in place. No judgment calls - pure structural integrity.

Checks include:
- BR-ID and TBL-ID format compliance
- Feature Card frontmatter completeness and lifecycle state validity
- Feature Set naming convention (FS-NN format)
- Cross-reference resolution (does every BR-ID reference in a Feature Card resolve in `business_rules.md`?)
- Framework version drift (artifacts missing fields introduced in newer Pureinn versions)
- **Open questions hygiene** - open items have exactly one home, `domain/open_questions.md` (Live Register 5). Flags an "Open Questions" section reappearing in PRD/Roadmap/Feature Cards/reconcile reports, duplicated open-item text, or an `OQ-`/`DIV-`/`BLK-` ID that doesn't resolve to a register entry.

**Tier 2 - Substance (strategic - read-only):**
Does the strategic layer agree with itself and with the research it was built on? PRD target customer vs. personas, value proposition vs. validated pains, roadmap phases vs. feature phases, pricing vs. willingness to pay signal.

Tier 2 is read-only. It surfaces each contradiction as `[CONFLICT]` and routes the fix to the authoring skill (`pm-prd`, `pm-product-roadmap`, `pm-business-model`, ...) in delta mode. The skill never edits strategic content - that is a business decision.

| Area argument | Tiers run |
|---|---|
| (none - default) | Both |
| `domain`, `rules`, `features` | Tier 1 only |
| `strategy` | Tier 2 only |

---

## Severity levels

| Level | Meaning | Action |
|---|---|---|
| P0 | Blocker - artifact cannot be used safely | Auto-fix where possible; flag where not |
| P1 | Structural error - convention violated | Auto-fix |
| P2 | Drift - valid but inconsistent with current standard | Auto-fix with diff |
| P3 | Warning - low impact, judgment call | AskUserQuestion |

---

## Position vs. related skills

| Skill | What it reads | What it does |
|---|---|---|
| `pm-reconcile` | Codebase vs. legacy docs | Reconciled rebuild |
| `pm-reverse-extract` | Codebase | Feature inventory |
| **pm-audit** | Pureinn artifacts vs. Pureinn conventions | Drift / error fix |

`pm-reconcile` and `pm-reverse-extract` hand off to `pm-audit` as their verification step. `pm-audit` does not read the codebase or legacy documents.

---

## Dependencies

**Required:**
- A Pureinn workspace exists: `pureinn-workspace/[project-slug]/` with at least `state.json` and some artifacts

If no workspace is found: tell the user to run `/pureinn` (greenfield) or `/pm-reverse-extract` / `/pm-reconcile` (existing product) first.

**Related skills:** `pm-reconcile`, `pm-reverse-extract`, `pm-feature-card`, `pm-features-list`, `pm-stripe`, `pm-open-questions`
