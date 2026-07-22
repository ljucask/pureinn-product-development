# pm-open-questions

> Open Questions & Decisions Register - Live Register 5 - the single home for unresolved questions, legacy-vs-code divergences, and blockers

**Phase:** Any (cross-phase); initializes on first use, at latest Phase 4
**Agent mode:** `decision` - drafts, then requires your review before closing a question
**Version:** 1.0.0
**Triggers:** open questions, open question register, decisions log, unresolved question, blocker, divergence, OQ-ID, DIV-ID, BLK-ID, decision tracking, Live Register 5

---

## When to use

Any time a skill or the user hits a question that needs a judgment call, a legacy-vs-code divergence that needs a ruling, or a concrete build blocker. There is exactly **one** home for all of these in a Pureinn project: `domain/open_questions.md`. No PRD, Roadmap, Feature Card, or reconcile report carries its own "Open Questions" section anymore - they all route here.

The register is created on first use (by whichever skill hits the first open item), not pre-created empty.

---

## What it produces

**Open Questions & Decisions Register** (`domain/open_questions.md`) - two sections:
- **Open** - current, actionable items
- **Resolved** - audit trail, never deleted, each entry carries its resolution and where the decision now lives

---

## The three record types

| Type | Prefix | Resolves |
|---|---|---|
| **Question** | `OQ-{DOMAIN}-NN` | Real alternatives exist, needs a judgment call |
| **Divergence** | `DIV-{DOMAIN}-NN` | Legacy docs and code disagree, needs a ruling on which is true |
| **Blocker** | `BLK-{DOMAIN}-NN` | Something concrete is missing/broken, no ambiguity about what to do - just execution |

`OQ-BIZ-NN` and `OQ-MVP-NN` are domain-scoped variants of `OQ-` (still Type: Question), not separate types.

---

## How to invoke

```bash
/pm-open-questions            # interactive - add / resolve / migrate / review
/pm-open-questions migrate    # scan the whole project + Notion for scattered open items and consolidate
/pm-open-questions --agent    # autonomous draft of a new entry from context, requires review before closing
```

Most of the time this skill isn't invoked directly - a producing skill (see below) appends an entry as part of its own run, initializing the register first if needed.

---

## Producing skills (who writes here)

`pm-prd`, `pm-product-roadmap`, `pm-reconcile`, `pm-domain-model`, `pm-features-list`, `pm-feature-design`, `pm-business-rules-library`, `pm-market-analysis` - each appends directly to the register when it hits an unresolved item, instead of embedding it in its own artifact.

---

## Migration for an existing project

Run via `/pm-reconcile open-questions` or standalone `/pm-open-questions migrate`:
1. Scan every `.md` artifact + `state.json` for `OQ-*`, `DIV-*`, `BLK-*`, "TBD", "open question" patterns
2. Scan any existing Notion "Open Questions" DB by actual row count, not just schema
3. Cross-check duplicates/conflicts between local and Notion before writing
4. Flag conflicts to the user - never silently decide which is canonical

---

## Lifecycle - never delete

Entries move **Open → Resolved**, they are never deleted. A resolved entry keeps its original context plus the resolution date, the decision itself, and where it now permanently lives (e.g. a BR-ID, a roadmap phase). If a resolved item resurfaces, it's flagged as a possible duplicate for the user to confirm - never silently reopened or silently overwritten.

---

## Dependencies

**No hard dependency** - created standalone or by any producing skill.

**Produces for:**
- Every producing skill listed above (a place to route unresolved items)
- `pm-audit` - flags any open-item content duplicated outside the register

**Related skills:** `pm-reconcile`, `pm-domain-model`, `pm-prd`, `pm-product-roadmap`, `pm-features-list`, `pm-feature-design`, `pm-business-rules-library`, `pm-market-analysis`, `pm-audit`
