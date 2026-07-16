# Stakeholder Map - PureHunger

> **Version:** 1.0 · **Date:** 2025-10-07

---

## Power / Interest Matrix

| | Low interest | High interest |
|---|---|---|
| **High power** | 👁 Keep satisfied | ✅ Manage closely |
| **Low power** | 🔍 Monitor | 📢 Keep informed |

### Manage Closely (High power, High interest)
| Stakeholder | Role | Interest | Engagement strategy |
|---|---|---|---|
| Sam Okonkwo | Internal - CEO/Product | Product success, fundraising, GTM | Core team - daily |
| Lena Vogt | Internal - CTO | Architecture integrity, delivery pace | Core team - daily |
| Marcus Field | Internal - Growth & Partnerships | Restaurant/courier supply growth | Core team - daily |
| Daniel Osei | External - Owner, Jollof Kitchen (first restaurant partner, informal design partner) | Recovering delivery revenue without repeating his prior platform's margin problem; his feedback shapes restaurant-facing tooling | Elevated one power level above a typical single-restaurant partner (see placement heuristic below) - Marcus checks in weekly during Phase 8-9; Sam personally involved in any commercial term changes |

### Keep Satisfied (High power, Low interest)
| Stakeholder | Role | Interest | Engagement strategy |
|---|---|---|---|
| Grace Lindqvist | External - Angel Investor ($180K pre-seed SAFE) | Return on investment, path to a priced round, unit economics proof | Monthly written update from Sam; not currently asking for more, but can influence follow-on funding |
| Payment processor (card network settlement partner) | External - Vendor | Compliance, fraud exposure, settlement risk | Keep integration and compliance documentation current; Lena owns the technical relationship |
| Idaho / federal gig-worker classification regulators | External - Regulatory | Currently near-zero visible interest in PureHunger specifically | **Late-veto risk** - shows no interest today but can reclassify couriers as employees near or after launch. Legal counsel engaged in Phase 1 (not deferred to Phase 7) specifically because of this pattern |

### Keep Informed (Low power, High interest)
| Stakeholder | Role | Interest | Engagement strategy |
|---|---|---|---|
| Mai Nguyen | External - Owner, Two Rivers Ramen (second restaurant partner) | Delivery revenue without commission eating margin; wants to see the marketplace prove itself before recruiting other restaurants on his behalf | Marcus - biweekly check-in during onboarding, monthly after |
| Priya Nair (courier persona, representative of early courier cohort) | External - Courier | Payout transparency, flexible scheduling | Marcus - in-app messaging + periodic courier community calls |

### Monitor (Low power, Low interest)
| Stakeholder | Role | Interest | Engagement strategy |
|---|---|---|---|
| Major delivery platforms (Uber Eats / DoorDash-style incumbents) | External - Competitor | Not yet paying attention to a single mid-size market entrant | No direct engagement; monitor for pricing/incentive response in Boise (see Project Charter R-04) |

---

## Stakeholder Register

| Name / Role | Type | Interests | Concerns / Risks | Preferred communication | Frequency |
|---|---|---|---|---|---|
| Sam Okonkwo | Internal | Product success, runway, GTM | Overrun on scope/timeline hitting fundraising narrative | In person / Slack | Daily |
| Lena Vogt | Internal | Architecture quality, sustainable delivery pace | Being the single point of engineering failure | In person / Slack | Daily |
| Marcus Field | Internal | Restaurant/courier acquisition velocity | Commission pressure from restaurants wanting a discount | In person / Slack | Daily |
| Grace Lindqvist | External - Investor | ROI, unit economics, milestone progress | Cash-flow risk from daily courier payouts (see R-01) | Email | Monthly |
| Daniel Osei | External - Restaurant partner | Margin recovery, being heard on restaurant tooling | Repeating the same commission-erosion experience that made him quit his last platform | Phone / in-person (Marcus) | Weekly during onboarding, then monthly |
| Mai Nguyen | External - Restaurant partner | Delivery revenue at sustainable margin | Wants proof of traction before recommending PureHunger to peers | Phone / in-person (Marcus) | Biweekly during onboarding, then monthly |
| Employment/gig-worker counsel | External - Vendor/Advisor | Compliance fee, correct classification | Courier misclassification exposure | Email | Ad hoc, quarterly review |

---

# RACI Matrix - PureHunger

> **R** = Responsible (does the work) · **A** = Accountable (owns the outcome) · **C** = Consulted (input requested) · **I** = Informed (receives update)
> Each decision has exactly one **A**.

| Decision / Activity | Sam Okonkwo | Lena Vogt | Marcus Field | Grace Lindqvist | Restaurant partners (Daniel, Mai) |
|---|---|---|---|---|---|
| MVP scope definition | A | R | C | I | - |
| Commission rate / pricing model | A | C | R | I | I (informed of final terms per BR-REG-001) |
| Tech stack / architecture decisions | C | A/R | - | - | - |
| Restaurant Partner Agreement terms | A | - | R | - | C (feedback shapes terms before signing) |
| Courier payout policy | A | R | C | - | - |
| Phase 1 Go/No-Go | A | C | C | I | - |
| Phase 3b Go/No-Go (post-validation) | A | C | C | I | - |
| Budget / fundraising | A | C | C | C (as current investor) | - |
| Hiring decisions | A | C (eng roles) | C (growth/ops roles) | - | - |

---

**Warning flags:**
- More than one **A** per decision = conflict, needs resolution. None currently - every row above has exactly one.
- Stakeholder with no **R** anywhere = likely not needed in core team. Grace Lindqvist has no R - correct, she is an informed/consulted investor, not an operator.

---

# Escalation Tree - PureHunger

> Who resolves what when the team cannot agree.

---

## Escalation levels

### Level 1 - Operational decisions (within 24h)
**Decision owner:** Sam Okonkwo (product) / Lena Vogt (technical) / Marcus Field (restaurant/courier field) - whoever owns the workstream
**Types:** Scope details, technical implementation choices, day-to-day restaurant/courier onboarding exceptions

### Level 2 - Strategic decisions (within 72h)
**Decision owner:** Full founder vote (Sam, Lena, Marcus)
**Types:** MVP scope changes, commission/fee structure changes, timeline shifts, resource allocation

### Level 3 - Critical / Escalated (ASAP)
**Decision owner:** Sam Okonkwo (CEO) holds final tie-break; Grace Lindqvist and external legal counsel are looped in before any decision that materially affects investor terms or regulatory/compliance exposure
**Types:** Phase Go/No-Go, budget overruns, legal/compliance blockers (e.g. courier classification), pivot decisions

---

## Conflict resolution protocol

1. Team attempts async resolution (Slack thread, 24h window)
2. If unresolved → sync meeting (max 30 min, Sam facilitates)
3. If still unresolved → escalate to Level 2 (full founder vote)
4. Document the decision (what, why, who decided) → log in Notion

---

## Anticipated conflicts and resolution rules

| Conflict | Parties | Resolution rule / Decider |
|---|---|---|
| Marcus wants to discount commission to close a hesitant restaurant faster; Sam protects the 12% rate as the core differentiator | Marcus Field vs. Sam Okonkwo | No unilateral field discounts. Any commission variance requires Sam's explicit sign-off (Decision Rights Matrix, pricing row) |
| Aggressive GTM timeline pressure (Marcus/Sam want to launch before a competitor notices Boise) vs. Lena's engineering feasibility estimate | Sam/Marcus vs. Lena Vogt | Lena's technical feasibility estimate is final. Per the Project Charter's scope-flex rule, scope narrows before the launch deadline slips |
| Late-stage regulatory veto risk on courier classification | Regulators (external) vs. the business model's payout structure | Legal counsel engaged in Phase 1, not deferred - the escalation tree exists so this surfaces at Level 3 immediately if raised, not discovered at launch |

---

## Handoff

**Čo si teraz má:** Zmapovaných stakeholderov podľa vplyvu a záujmu (+ RACI, eskalačný strom) - vieš koho zapojiť do ktorých rozhodnutí a kadiaľ eskalovať, vrátane externých partnerov a late-veto rizika.

**Ďalší krok:** `/pm-project-charter` — ciele, scope a success kritériá, na ktoré sa stakeholdri viažu.
Alebo `/pureinn` pre Phase 1 gate check.
