# Team Roster - PureHunger

> **Version:** 1.0 · **Date:** 2025-10-13

---

## Core Team

| Name | Role | Type | Availability | Responsibility |
|---|---|---|---|---|
| Sam Okonkwo | CEO / Product | Co-founder | 100% | Product vision and scope, restaurant/customer/courier commercial strategy, fundraising, GTM decisions, phase gate approvals |
| Lena Vogt | CTO | Co-founder | 100% | Architecture and domain model ownership, ordering/dispatch system, engineering delivery, tech stack decisions, DevOps/infra (until a dedicated hire exists) |
| Marcus Field | Head of Growth & Restaurant Partnerships | Co-founder | 100% | Restaurant recruitment and onboarding, courier recruitment, local Boise marketing, partnership terms execution |

---

## Extended Team / Advisors

| Name / Role | Type | Involvement | When |
|---|---|---|---|
| Grace Lindqvist, Angel Investor ($180K pre-seed SAFE) | External | Monthly async update; ad-hoc strategic input | Phase 1 onward |
| Employment/gig-worker counsel | External | Ad-hoc | Phase 1 (courier agreement, classification review), then quarterly |
| Contract UX designer (TBD) | External | Per Feature Set, project basis | Phase 4-6 (customer ordering flow, restaurant onboarding flow) |
| Contract QA (TBD) | External | Pre-launch regression pass | Phase 8-9 (Beta, Launch) |

---

## Team Capacity

**Total capacity (as stated):** 3.0 FTE (Sam 100%, Lena 100%, Marcus 100%)

**Effective FTE (discounted for hats worn, not summed at face value):**

| Person | Stated | Discount applied | Effective |
|---|---|---|---|
| Sam Okonkwo | 100% | Splits across product, fundraising, and GTM - only ~70% lands on core product execution | 0.7 FTE (product) |
| Lena Vogt | 100% | Sole engineer, no context-switch discount needed - but this is also the entire engineering org | 1.0 FTE (engineering) |
| Marcus Field | 100% | Fully allocated to growth/partnerships, none of it engineering or product execution capacity | 1.0 FTE (growth, non-engineering) |

**Total effective:** ~2.7 FTE across the business, but only **1.0 effective engineering FTE**.

**Peak capacity (Phase 6-7 Build):** 1.0 FTE engineering.

🔴 **Flag:** 1.0 effective engineering FTE is below the ~1.5 FTE floor this framework treats as a rough minimum for an MVP build of this scope (customer app + restaurant tooling + courier app + dispatch + payments). Carried into the Skill Gap Assessment below as a Critical gap - not deferred to Phase 6, where discovering it costs months.

**Critical dependency:** Lena Vogt is the entire engineering function. If she is unavailable, all technical delivery and infrastructure stop - there is no backup owner for architecture, the codebase, or deployment until a backend hire is in place.

---

# Decision Rights Matrix - PureHunger

> Each decision has one **owner** (Final Say). Others may consult.

---

| Decision area | Final Say | Consulted | Notes |
|---|---|---|---|
| **Product** | | | |
| MVP scope definition | Sam Okonkwo | Lena Vogt, Marcus Field | |
| Feature prioritization | Sam Okonkwo | Lena Vogt | |
| Scope change during build | Sam Okonkwo + Lena Vogt | Marcus Field | Changes affecting launch date by more than 1 week escalate to full founder vote |
| Phase Go/No-Go | Sam Okonkwo | Lena Vogt, Marcus Field | |
| **Technology** | | | |
| Tech stack selection | Lena Vogt | Sam Okonkwo | |
| Architecture decisions | Lena Vogt | Sam Okonkwo | |
| Tech debt prioritization | Lena Vogt | Sam Okonkwo | |
| **Design** | | | |
| UX direction and flow | Sam Okonkwo (until a dedicated designer is hired) | Lena Vogt, contract UX designer | Gap - see Skill Gap Assessment |
| Design system | Lena Vogt | Sam Okonkwo | Gap - see Skill Gap Assessment |
| **Business** | | | |
| Budget approval | Sam Okonkwo | Lena Vogt, Marcus Field | |
| Hiring decisions | Sam Okonkwo | Lena Vogt (engineering hires), Marcus Field (growth/ops hires) | |
| Investor communication | Sam Okonkwo | - | |
| Pricing / commission / payout model | Sam Okonkwo + Marcus Field | Lena Vogt (feasibility) | Any commission discount to a specific restaurant requires Sam's sign-off - Marcus cannot unilaterally discount in the field |

---

# Skill Gap Assessment - PureHunger

> **Goal:** Identify what the team is missing and have a plan before Phase 4+ (Build phases).

---

## Gap Analysis

| Skill / Role | Current state | Gap | Criticality | Mitigation | Timeline |
|---|---|---|---|---|---|
| Backend / dispatch engineering | Lena Vogt solo (1.0 FTE) | Cannot cover payments, dispatch, and courier tracking engineering simultaneously with ongoing feature build pace at Phase 6-7 | 🔴 Critical | Hire a dedicated backend engineer | By start of Phase 6 (Build) |
| UX/UI design | Nobody dedicated - Sam does rough wireframes | No professional design craft for customer, restaurant, or courier surfaces | 🟡 Medium | Contract UX designer per Feature Set (customer ordering flow first, then restaurant onboarding) | Before Phase 6 for customer- and restaurant-facing surfaces |
| QA / Testing | Nobody dedicated | No formal regression coverage before public launch | 🟡 Medium | Lena + incoming backend hire own automated tests; contract QA for a pre-launch regression pass | Before Boise public launch (Phase 8-9) |
| Data Analytics | Nobody | No dedicated reporting/analytics function | 🟢 Low | Sam handles basic reporting via Notion/Sheets until volume justifies a hire | Phase 9 Beta |
| Legal / Compliance (gig-worker classification, partner agreements) | No in-house counsel | Courier and restaurant partner agreements need legal review before signing partners | 🟡 Medium | Retain external gig-economy employment counsel ad-hoc | Phase 1, before first courier/restaurant agreements are signed |

**Criticality:**
- 🔴 Critical - without this we cannot start Phase 6 (Build)
- 🟡 Medium - slows us down, but we have a workaround
- 🟢 Low - needed later, we have time

---

## Mitigation Plan

### Immediate actions (by end of Phase 1)
- [ ] Lena to draft backend engineer job description; Sam to open the search
- [ ] Retain gig-economy employment counsel before drafting courier agreement

### Short-term (by Phase 4)
- [ ] Contract a UX designer for the customer ordering flow and restaurant onboarding flow

### Long-term (Phase 6+)
- [ ] Hire the backend engineer and onboard onto the dispatch/tracking Feature Set
- [ ] Contract QA for pre-launch regression pass
- [ ] Revisit dedicated analytics hire at Phase 9 Beta

---

**Team risk assessment:**
The team is sufficient for Phase 1-5 (strategy, discovery, planning) - all three founders cover product, tech, and go-to-market decisions directly. The biggest risk is Phase 6 Build: 1.0 effective engineering FTE cannot deliver the full MVP scope (ordering, dispatch, payments, courier app) at pace, and Lena is a single point of failure with no backup. The backend engineer hire is not optional - it is the gate that determines whether Phase 6 can start on schedule.

---

## Handoff

**Čo si teraz má:** Roly, zodpovednosti a decision rights v tíme - jasné kto čo vlastní a kde sú skill gapy, vrátane kritického gapu v backend engineeringu pred Phase 6.

**Ďalší krok:** `/pm-comms-charter` — komunikačná kadencia a meeting rhythm pre tento 3-člennný founder tím.
Alebo `/pureinn` pre Phase 1 gate check.
