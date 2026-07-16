# Onboarding Brief - Diego Ramirez
**Role:** Backend Engineer
**Product:** PureHunger
**Date:** 2026-04-06
**Prepared by:** pm-onboarding (Pureinn v5.26.2)

---

## Welcome - what you're joining

PureHunger is a three-sided food delivery marketplace live in Boise, Idaho since late January 2026 - customers, independent restaurants, and couriers. The differentiator is a 12% restaurant commission (vs. the 25-30% major platforms charge) and daily courier payouts (vs. weekly). The core ordering loop shipped and is live; Guest Checkout shipped in March. You're joining as the team's second engineer, right as the courier delivery-assignment and live-tracking feature (FEAT-DEL-002) is queued to start build - this is very likely your first feature.

---

## The product in one page

**Problem we're solving:**
Independent restaurants in mid-size cities are stuck between eroding their margin on 25-30% commission or staying off delivery apps entirely and losing app-first customers. PureHunger's 12% rate and daily courier payouts remove both trade-offs.

**Who we're building for:**
Three personas: Maya Torres (busy professional customer, orders 3-4x/week), Daniel Osei (independent restaurant owner, our first restaurant partner - Jollof Kitchen), and Priya Nair (courier, cares about payout transparency and flexible scheduling). Early adopter profile: Boise-based independent restaurants with 5+ years in business who tried a major platform and dropped it over commission.

**Value we deliver:**
Restaurants keep more of every order; customers get faster discovery of independent (non-chain) restaurants; couriers get transparent per-delivery pay, out daily instead of weekly.

**Current phase:**
Phase 7 (Build) - post-MVP-launch, working through Delivery Stripes. Exit criteria for the current stage: reach the 6-month traction targets (150 Weekly Active Ordering Households, 40 active restaurants, 60 active couriers) to make the second-market Go/No-Go call.

**North Star Metric:**
Weekly Active Ordering Households - a household placing at least one order in a 7-day window.

---

## Settled decisions (do not re-open without new evidence)

These have been decided. They can be changed - but only with new data or a specific argument, not preference.

| Decision | What was decided | Why |
|---|---|---|
| Commission rate | Fixed at 12% for restaurant partners; changes require 30 days written notice (BR-REG-001) | Contractual commitment in the Restaurant Partner Agreement - this rate is the entire differentiator, not a lever to move casually |
| Courier payout cadence | Daily, not weekly ($4 base + $1.25/mile + 100% tips) | Core differentiator vs. competitors' weekly cycles, validated against courier persona evidence (Priya Nair) |
| Payment capture timing | Payment is authorized at order placement but captured in full only when the restaurant accepts (BR-PAY-001); auto-refunded in full if not accepted within 10 minutes (BR-PAY-002) | Protects customers from being charged for orders a restaurant never confirms |
| Card data storage | Never store raw card details - only the payment processor's tokenized reference (BR-GOV-001) | PCI scope minimization and compliance |
| Guest checkout | Ships without full account creation, but requires SMS OTP phone verification before order confirmation; creates a lightweight shadow-Customer record internally (decided 2026-02-10 Product Review, FEAT-ORD-004) | 38% cart abandonment at forced account creation was large enough to act on; OTP balances conversion against fraud/no-show risk |
| Courier suspension threshold | A courier whose rolling average rating over the last 20 deliveries falls below 4.5 is auto-suspended pending manual review (BR-DEL-001) | Quality floor for the marketplace, enforced automatically rather than case-by-case |

---

## Where things live

| Artifact | Location | What it contains |
|---|---|---|
| PRD Master | `/product/PRD_master.md` | Problem, value prop, target customer, scope |
| Product Roadmap | `/artifacts/phase-5-planning/product-roadmap.md` | Phases, deliverables, exit criteria |
| Feature List | `/features/feature_list.md` | All features with KANO/VxC/phase/stripe |
| Feature Cards | `/features/cards/FEAT-[ID].md` | Per-feature spec, ACs, technical design |
| Domain Model | `/domain/entities.md` | Entities, state machines, guard conditions |
| Business Rules | `/domain/business_rules.md` | BR-IDs referenced in Feature Cards |
| Personas | `/artifacts/phase-2-discovery/personas.md` | Customer, restaurant, and courier profiles + pains |
| Notion | Feature Backlog + Meetings DB (URL in `pureinn-variables.md`) | Team collaboration, meeting records |

---

## Current delivery state

**Active stripes:**

| Stripe | Active feature | Status | Next in queue |
|---|---|---|---|
| ordering | FEAT-ORD-004: Guest Checkout | 6_Shipped | - (stripe closed, folded into maintenance) |
| dispatch | FEAT-DEL-002: Courier delivery assignment + live tracking | 3_Ready_to_Build | FEAT-PAY-002 |
| payments | FEAT-PAY-002: Daily courier payout batch automation | 2_Spec_Done | - |

**Features in your immediate queue:**
- **FEAT-DEL-002** - Courier delivery assignment + live tracking. Status `3_Ready_to_Build` - Sections 1-3 of the Feature Card are complete (business rules, guard conditions, sequence diagram, acceptance criteria). This is the natural first feature for you: it's dispatch/backend-heavy (assignment logic, live location updates, state transitions) with limited frontend surface.
- **FEAT-PAY-002** - Daily courier payout batch automation. Status `2_Spec_Done` - JIT design (`pm-feature-design`) hasn't run yet. Queued behind FEAT-DEL-002.

**Features recently shipped (last 2-3):**
- **FEAT-ORD-001** - Browse restaurant, build cart, checkout (the original MVP ordering loop) - `6_Shipped`, live since Boise launch.
- **FEAT-ORD-004** - Guest Checkout - `6_Shipped` in March, following the 2026-02-10 Product Review decision.

---

## Domain you need to understand first

**Key entities and their states:**

| Entity | States | Key guard conditions |
|---|---|---|
| Order | Cart → Placed → Accepted → Preparing → ReadyForPickup → OutForDelivery → Delivered (side branches: Placed → Cancelled by customer, Placed → Refunded auto) | BR-ORD-001 (Restaurant must be Active), BR-ORD-002 (MenuItem must be available), BR-ORD-003 (cancellable only while Placed) |
| Delivery | Assigned → EnRoute-to-Restaurant → PickedUp → EnRoute-to-Customer → Completed | BR-DEL-002 (cannot move to PickedUp until Order is ReadyForPickup) |
| Courier | Applied → Active → Suspended → Deactivated (Active couriers also have an Online/Offline availability toggle) | BR-DEL-001 (auto-suspend below 4.5 rolling average over last 20 deliveries) |
| Payment | Authorized → Captured → Refunded / PartiallyRefunded | BR-PAY-001 (capture only on restaurant acceptance), BR-PAY-002 (auto-refund if not accepted within 10 min), BR-GOV-001 (tokenized reference only, never raw card data) |
| Restaurant | Pending → Active → Paused → Deactivated | BR-ORD-001, BR-REG-001 (commission changes need 30 days notice) |

**Critical business rules (referenced in active Feature Cards):**

| BR-ID | Rule | Enforcement point |
|---|---|---|
| BR-DEL-001 | Courier auto-suspended below 4.5 rolling average over last 20 deliveries | Courier rating aggregation job, checked after every Delivery Completed transition - directly relevant to FEAT-DEL-002 |
| BR-DEL-002 | Delivery cannot move to PickedUp until Order is ReadyForPickup | Delivery state transition guard - directly relevant to FEAT-DEL-002 |
| BR-PAY-001 | Payment authorized at placement, captured only on restaurant acceptance | Order Accepted transition handler |
| BR-PAY-002 | Auto-refund in full if restaurant doesn't accept within 10 minutes | Scheduled job on Order Placed timestamp |
| BR-GOV-001 | Never store raw card details, only the processor's tokenized reference | Payment entity schema / any code path touching card data |
| BR-REG-002 | Courier 1099-NEC must be issued by Jan 31 for any courier paid over $600 in the prior year | Relevant to FEAT-PAY-002 (payout batch automation) - flag if you touch payout record retention |

---

## How we work (delivery conventions)

- **JIT design:** every feature goes through `pm-feature-design` before build. FEAT-DEL-002's Sections 1-3 are already done - read the Feature Card, don't start from `feature_list.md` alone.
- **Atomic commits:** register updates (entities, rules) committed before code. Two commits per feature: `spec(FEAT-DEL-002): registers` then `spec(FEAT-DEL-002): design`.
- **Feature flags:** every feature ships behind a flag (`domain.feature-name`, default OFF). FEAT-DEL-002 will ship behind `delivery.courier-live-tracking`. Non-negotiable.
- **Status transitions:** update the Feature Card frontmatter `status:` at every transition, and keep `feature_list.md`'s status column in sync.
- **Run `/pm-stripe` at the start of every dev session** - it reads current state and tells you exactly what to do next.

---

## Who to ask about what

| Topic | Person | How |
|---|---|---|
| Product decisions / scope | Sam Okonkwo | Slack DM, or raise it at the Founder Weekly Sync |
| Domain model / business rules | Lena Vogt | She owns architecture and the domain model - Slack `#eng` or direct |
| Design / Figma | No dedicated designer yet - Sam handles rough wireframes; a contract UX designer is engaged per Feature Set | Ask Sam who's currently contracted for the active Feature Set |
| Deployment / infra | Lena Vogt | Also owns DevOps until a dedicated hire exists - flagged as a single point of failure in the Skill Gap Assessment, so loop in early on anything infra-related |
| Restaurant / courier operational questions (e.g. what actually happens on the ground during a delivery dispute) | Marcus Field | Slack or in-person - he's often out in the field, so Slack async is more reliable than expecting a quick sync |

---

## Handoff

**Čo si teraz má:** Kompletný day-1 brief - produkt, settled rozhodnutia, kde čo nájsť, aktuálny delivery stav (FEAT-DEL-002 ako tvoja prvá feature), a s kým hovoriť o čom.

**Ďalší krok:** Otvor Feature Card `/features/cards/FEAT-DEL-002.md` a spusti `/pm-stripe` na začiatku prvej dev session - ukáže presne, čo robiť ďalej.
