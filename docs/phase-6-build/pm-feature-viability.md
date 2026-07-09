# pm-feature-viability

> Pre-build decision check: is this feature worth building, what is the smallest valuable scope, and how will you measure success?

**Phase:** 6 - JIT Delivery (optional pre-spec step)  
**Agent mode:** `decision` - drafts, then requires your review  
**Version:** 1.0.0  
**Triggers:** feature viability, worth building, feature scoping, MDP, minimum desirable product

---

## When to use

**Run when:**
- New feature initiated internally (team or product idea, not from a validated roadmap)
- Unclear whether to build now, defer, or not build at all
- Unclear what the smallest valuable scope looks like
- No pre-defined success metric for this feature

**Skip explicitly when:**
- Feature comes from a validated PRD / feature list with KANO already assigned
- Customer commitment (contractual or sales) to deliver this feature
- Hard compliance or infrastructure requirement (no choice)
- Team already has clear scope and knows what "done" looks like

This skill is not a gate. When the decision is already made, skip it and go directly to `pm-feature-design`.

---

## What it produces

Viability Assessment document (saved to `initiatives/[feature-slug]-viability.md` or inline):

- **KANO classification** - Must-be / Performance / Delighter / Indifferent
- **Build/Defer/Cut recommendation** with rationale
- **MDP scope** - Minimum Desirable Product: one complete user action, what's in, what's cut
- **Success metrics** - one observable metric + target + measurement date
- **Failure condition** - what would indicate the feature didn't work

---

## How to invoke

```bash
/pm-feature-viability FEAT-ORD-012        # standard assessment
/pm-feature-viability FEAT-ORD-012 --agent   # autonomous draft, requires review
```

---

## How it works

1. **Skip check** - confirms whether assessment is needed or the decision is already made
2. **Feature context** - what it does, who requested it, what problem it solves today
3. **KANO classification** - how would the primary user feel if this feature did NOT exist?
4. **Build/Defer/Cut decision** - based on KANO + demand signal; logged if Cut
5. **MDP scope** - minimum version that delivers real value; explicitly cuts the "full" version extras
6. **Success metrics** - one observable, measurable metric + target + timeline

**Abbreviated mode (option C - scope unclear but direction is set):** runs Steps 4-5 only (skips KANO).

---

## Outcomes

| Outcome | Next step |
|---|---|
| **Build now** | → `/pm-feature-design [FEAT-ID]` with MDP scope as input |
| **Defer** | → Feature stays in backlog with KANO = Delighter; revisit after defined condition |
| **Cut** | → Feature removed from consideration; logged as explicitly cut |

---

## Related skills

`pm-stripe`, `pm-feature-design`, `pm-features-list`, `pm-mvp-scope`
