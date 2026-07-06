---
name: pm-root-cause
description: Diagnostic engine for in-flight anomalies. When something live behaves unexpectedly - a metric dropped, churn spiked, a feature isn't adopted, conversion fell, tickets are rising - you describe the symptom and the skill drills to the real root cause, not the first plausible one. Runs a structured investigation: is it real or a measurement artifact, where does it concentrate (segment/funnel), what changed, candidate causes across categories, 5-Whys drill, evidence-vs-guess separation, and the cheapest test to confirm. Baked-in diagnostic methods, an anomaly-to-cause differential library, measurement traps, and a bias catalogue. Ends with testable hypotheses that feed pm-hypotheses. Cross-phase.
license: MIT
metadata:
  agent-mode: never
  author: https://github.com/ljucask
  version: "1.0.0"
  domain: product-management
  triggers: root cause, why did this happen, metric dropped, churn spike, conversion drop, funnel drop, retention decline, feature not adopted, DAU drop, diagnose, investigate anomaly, 5 whys, fishbone, something's wrong with the data
  role: specialist
  scope: validation
  output-format: document
  related-skills: pm-hypotheses, pm-problem-validation, pm-kpis, pm-personas, pm-prioritize
---

# PM - Root Cause (diagnose an in-flight anomaly)


## Agent mode (`--agent`)

Hodnota tohto skillu je živý dialóg - `--agent` nie je podporený. Pri `--agent` raz varuj ("tento skill potrebuje interakciu, agent režim ho vyprázdni") a pokračuj interaktívne.

---

## What this skill does

Something live is behaving unexpectedly - a metric moved, users act strangely, churn spiked, a feature flopped. You describe the **symptom**; the skill runs a structured investigation and drills to the **real root cause**, then hands you testable hypotheses and the cheapest way to confirm.

**This is in-flight diagnosis, not foundational validation.** It differs from the neighbours:
- `pm-problem-validation` - is the core problem real (at project start)?
- `pm-stress-test` - poke holes in my plan (adversarial, before a room)?
- **`pm-root-cause`** - why is THIS happening now (diagnostic, on a live thing)?

**Two modes:**

| Mode | When | What it does |
|---|---|---|
| **Guided investigation** (default) | You want to find the cause | Interactive Socratic drill through the steps: real vs artifact → localize → what changed → candidate causes → 5 Whys → evidence-vs-guess → confirm test |
| **Quick differential** | You just want the candidate-cause map | One pass: for the stated anomaly, the likely causes, their data signature, and exactly what data to pull to confirm/rule out - no long back-and-forth |

**Data-optional (graceful).** If you have analytics, the skill uses it. If not, it still structures the investigation and tells you exactly **which data to pull** and how to read it.

---

## Hard rule: don't stop at the first plausible cause

The single most common failure of root-cause work is premature closure - grabbing the first believable answer and stopping. This skill actively resists it:

- **Correlation is not causation.** Two things moving together is a lead, not a cause. Demand the mechanism ("how exactly did A produce B?").
- **Symptom is not root.** "Engineer ran the wrong command" / "a bug" is a symptom - ask what *allowed* it.
- **Rarely one cause.** Complex systems usually need several contributing factors. Ask: if we removed this one factor, would the anomaly still happen?
- **Separate what you KNOW (evidence) from what you GUESS (hypothesis).** Never present a guess as a finding. Mark every candidate `[EVIDENCE]` or `[HYPOTHESIS - untested]`.
- Before accepting any root cause, run the **validation checklist** (end of skill).

A confirmed testable hypothesis beats a confident unverified conclusion.

---

## Step 0: Detect mode + capture the symptom

Guided (default) or quick differential. Then capture the symptom **precisely** - a vague symptom produces a vague investigation:

- **What** metric/behavior moved, and in which direction?
- **By how much** (magnitude), vs. what was expected/normal?
- **When** was it first noticed, and when did it actually start (often earlier)?
- **Where** noticed - which surface, segment, geography if already known?

Apply the standard skill interaction pattern (CLAUDE.md). If the user is vague, help them sharpen the symptom before investigating - do not start drilling a fuzzy target.

---

## Step 1: Is it real, or a measurement artifact?

**Before hunting causes, rule out that the data is lying.** A huge share of "anomalies" are instrumentation, not reality.

Checks:
- **Cross-check against ground truth:** does an independent KPI move too? (e.g. sign-ups jumped but revenue/orders flat → suspicious). If the metric moved but the money didn't, suspect measurement.
- **Is the recent window complete?** Many systems backfill 1-2 days - comparing against today/yesterday creates false spikes/drops. Compare fully-recorded periods.
- **Level shift vs. gradual trend?** A clean step-change right after a deploy points to a change event; a slow slope points to erosion or seasonality.

### Measurement traps (baked-in - check these first)

| Trap | Tell | Quick check |
|---|---|---|
| Tracking change | Metric moved with no backend change; only one platform/version affected | Compare event counts + unique users 14 days before/after a release, by platform; check for null params (user_id, currency), duplicate fires |
| Attribution change | Attributed conversions jump but raw backend conversions flat | Changed lookback window / model? Compare raw vs attributed |
| Funnel redefinition | Conversion rate jumps with no behavior change | Definition of the entry step / denominator changed? Look at absolute counts before/after |
| Data-pipeline issue | Spike on a day with heavy backfill; de-dupe/timezone/currency changes | Inspect pipeline changes, backfill, de-dupe keys |
| Bots / spam | Sudden traffic inflation, very high bounce, zero conversion, unknown referrers / (not set) | Filter by user-agent / mark bots; inspect referrers |
| Sampling (GA4 etc.) | Big move in an exploration report over huge datasets | Check sampling indicator; verify on raw data (BigQuery) |
| Simpson's paradox | Aggregate says one thing, segments say the opposite | Split by key dimension and re-check |

If it's a measurement artifact → that IS the root cause. Fix the tracking; stop.

---

## Step 2: Localize - where does the anomaly concentrate?

**Narrow the search before generating causes.** An anomaly concentrated in one segment points straight at its cause. Slice by the standard dimensions and find where the movement lives:

- **New vs. returning users**
- **Platform / OS** (desktop / iOS / Android)
- **App / SDK version** (concentration in one version → likely a release/implementation bug)
- **Geography / region**
- **Acquisition channel / source** (ads, SEO, social, email)
- **Plan / tier** (free vs. paid)
- **Cohort by signup date / tenure**
- **Funnel step** (which step drops)

Ask: is the drop **broad** (everywhere → external/seasonality/measurement) or **narrow** (one segment → that segment's specific change)? Watch for Simpson's paradox - an aggregate can hide or invert a segment trend.

---

## Step 3: What changed?

The prime suspect for a sudden movement is a change right before it. **Inventory everything that changed** in the window before the anomaly - internal and external, even things that seem irrelevant:

- Code deploys / releases; feature flags flipped
- Pricing / packaging / plan changes
- Marketing campaigns started or ended; channel mix shift
- Tracking / attribution / pipeline changes (also Step 1)
- External events: seasonality, competitor launch/promo, PR, market shift, outage

Then map each change to the anomaly's timing and location (Step 2). A change that lines up with *when* and *where* the anomaly appears is your leading candidate. A change that doesn't align in time or segment is probably noise.

---

## Step 4: Generate candidate causes across categories

**Don't stop at the first candidate.** Spread across categories (fishbone) so you don't tunnel on one:

**Product/UX · Tech/Performance · Pricing/Packaging · Measurement/Tracking · Acquisition/Mix · Seasonality/External · Competitor · Market · Operations/Support**

Use the differential library below for the specific anomaly to seed candidates fast. For each candidate, note its expected **data signature** (where it would concentrate, what would co-move) and check whether Step 2-3 findings match it.

### Anomaly → candidate-cause differential library (baked-in)

For the stated anomaly, these are the usual suspects: cause (category) — data signature — fastest test [frequency].

**DAU/WAU/MAU drop**
- Release bug (Tech) — sharp drop in one segment after release — reproduce on device, crash logs [occasional]
- Tracking error (Measurement) — drop with no backend change, sources disagree — compare analytics sources, SDK logs [occasional]
- Acquisition mix shift (Acquisition) — fewer new users, specific channels — traffic/campaign analysis by cohort [occasional]
- Seasonality/external (External) — aligns with holiday/weekend, similar YoY — compare prior periods, event calendar [common]
- Pricing change (Pricing) — DAU/ARPU drop after price/trial-end — review pricing, simulate purchase [occasional]
- Confusing UX change (Product) — drop-off up in key flows, negative feedback — A/B rollback, user interviews [occasional]

**Activation / onboarding drop**
- Onboarding flow change (Product) — activation drops with a deploy, complaints — A/B vs previous flow [occasional]
- Signup/API errors (Tech) — errors/timeouts at signup, incomplete records — test signup path, server logs [occasional]
- Acquisition mix (Acquisition) — more low-converting sources — compare cohorts by channel [occasional]
- Tracking bug (Measurement) — completions vanish from reports, backend correct — verify events vs raw DB [occasional]

**Conversion funnel drop**
- Hidden costs/friction (Pricing) — sharp drop at final steps when fees appear — simulate purchase with all fees [common]
- Confusing nav/UI (Product) — consistent drop at one step, session replays show confusion — usability test that step [common]
- Technical error (Tech) — error spike, drop at failing element — reproduce, error monitoring [occasional]
- Mobile-specific (Tech) — much higher drop on mobile at same step — segment funnel by device [common]

**Free-to-paid drop**
- Hard paywall / unclear value (Product) — high drop at paywall — review paywall, test messaging [common]
- Pricing/plan change (Pricing) — revenue/conversion drop after change — pricing history, simulate signup [occasional]
- Payment gateway failure (Tech) — spike in declines — payment logs, manual transaction [occasional]
- Low trial-lead quality (Acquisition) — trials don't convert for some channels — segment trials by source [occasional]

**Churn / retention spike**
- Weak usage habit (Product) — falling session depth, users drop below engagement threshold — DAU/MAU by cohort, value survey [common]
- Poor onboarding / value misalignment (Product) — high early churn, few reach "aha" — cohort retention, interviews [common]
- Missing/complex features (Product) — feature-request spike, usage decline — tickets/feedback analysis [occasional]
- Competitor shift (Competitor) — churn clusters with competitor promo — track competitors, exit survey [occasional]
- Price increase (Pricing) — churn spike after hike/perk removal — churn vs price timeline [occasional]
- Major bug/outage (Tech) — immediate retention drop after incident — correlate with outage logs [rare]

**Revenue / ARPU drop**
- Cancellations/downgrades (Churn/Pricing) — subscription-change spike, lower expansion — analyze changes, interview leavers [common]
- Lower usage by payers (Product) — usage decline among paid — usage dashboards, cohort retention [common]
- Pricing/packaging change (Pricing) — ARPU drop after change — pricing history, simulate flows [occasional]
- Billing/analytics error (Measurement) — expected vs recorded revenue mismatch — reconcile with finance/billing [rare]
- Market/competitor (Market) — industry-wide, competitor promos — market trend analysis [occasional]

**Feature non-adoption**
- Built for wrong reason (Product/Market) — very low usage, no "aha", only power users — usefulness survey, reassess strategy [common]
- Poor discovery (Product) — few users exposed, low aware→use — in-app announcements, track exposure [common]
- Confusing UI/friction (Product) — drop exposed→activated, usability tickets — session replay, simplify [occasional]
- Competing alternative (Competitor) — users stay on competitor for the task — interviews on alternatives [occasional]

**Engagement decline**
- Eroded habit (Product) — slow DAU/MAU + session decline — engagement cohorts, at-risk survey [common]
- Reduced re-engagement (Product/External) — drop when email/push pauses — check campaigns, run re-engagement test [occasional]
- Stale product/UI (Product) — long-term downtrend, "outdated" feedback — cohort compare, satisfaction survey [occasional]
- Performance degradation (Tech) — gradual error/latency rise with usage drop — perf metrics, old vs new build [occasional]

**NPS / CSAT drop**
- Outages/bugs (Tech) — NPS drop at incident times, reliability comments — correlate with incidents, read detractors [common]
- Support overload (Operations) — ticket spike, longer response times — ticket queues, support interview [common]
- Unpopular UI/feature change (Product) — NPS decline after release, "prefer old" — segment NPS by cohort [occasional]
- Pricing/policy change (Pricing/External) — NPS drop after change — before/after compare, feedback topics [occasional]

**Support-ticket spike**
- Major bug/regression (Tech) — surge of same-error tickets after deploy — find common error, reproduce/rollback [common]
- New feature confusion (Product) — spike about one new feature — release notes, better in-app help [occasional]
- Outage/degradation (Tech) — ticket jump during downtime — cross-check uptime logs [common]
- Billing/account issues (Operations) — unexpected-charge/login tickets — verify billing, simulate account flow [occasional]

**Sign-up drop**
- Marketing/acquisition issue (Acquisition) — fewer visits/submissions, channels underperform — check campaigns/SEO, referral traffic [common]
- Signup form bug (Tech) — errors/timeouts, no new accounts — test signup on devices, logs [common]
- Landing UX friction (Product) — high bounce pre-signup, long form — A/B form design, heatmaps [occasional]
- Pricing confusion (Pricing) — abandon when pricing unclear — clarify pricing, simplify [occasional]

**Cart / checkout abandonment**
- Unexpected costs (Pricing) — abandonment when hidden fees show — show full price earlier, A/B checkout [common]
- Complex checkout form (Product) — drop while filling long form — simplify fields, user test [common]
- Payment errors (Tech) — payment-failure spike, abrupt drop — manual transaction test, gateway logs [occasional]
- Missing trust signals (Product) — exit at payment over security — add SSL/trust badges [occasional]

---

## Step 5: 5-Whys drill on the leading candidate(s)

Take the 1-2 candidates that best match the timing + location and drill: ask "why?" repeatedly until you reach an **actionable** cause. Rules that keep it honest:

- Five is a convention, not a target. **Stop when the cause is actionable** (in your power to fix, and you can measure that the fix worked) - not before (too generic: "insufficient training"), not after (too far: "market forces").
- At each "why", prefer the systemic answer over the personal one: not "the engineer forgot" but "what allowed that to happen" (no safeguard, no test, no validation).
- If two contributing factors are both necessary, drill both - don't force a single chain.

For complex or high-stakes anomalies, escalate to a structured method (below) instead of scattered questions.

### Method selection (baked-in)

| Method | Surfaces | Use when |
|---|---|---|
| **5 Whys** | Direct sequential cause | Quick incident, cause near the symptom |
| **Ishikawa / fishbone** | Categorized causes across areas | Many possible factors, need breadth |
| **Issue tree / MECE** | Structural decomposition of a KPI | Metric = f(components); split volume vs rate |
| **Change analysis** | The change event that triggered it | Sudden movement with a known date/version |
| **Funnel analysis** | Local drop-off in the journey | Conversion/step problem |
| **Cohort / segmentation** | Group- or time-specific cause | Anomaly may live in one segment |
| **Correlation vs causation / Simpson** | False leads, hidden confounders | Any new relationship, aggregate vs segment |
| **Pareto (80/20)** | The vital few causes by volume | Many small causes, need to prioritize |
| **Fault tree** | Combinations of failures (AND/OR) | Well-defined mechanical/system failure |
| **DMAIC** | Process/operational root cause | Recurring process defect, long-term fix |
| **Kepner-Tregoe** | "is vs is-not" precise problem spec | Complex, unclear, formal audit needed |

---

## Step 6: Separate evidence from guess, and rank

List every surviving candidate cause and label it:
- `[EVIDENCE]` - data confirms it (segment concentration, timing match, reproduced, mechanism shown)
- `[HYPOTHESIS - untested]` - plausible but not yet proven

Rank by **likelihood × strength of evidence**. Never let a `[HYPOTHESIS]` masquerade as the answer. If the leading candidate is still a hypothesis, the deliverable is a test, not a conclusion.

---

## Step 7: Confirm - cheapest test + action

For the top cause(s): state the **cheapest test** that would confirm or rule it out (from the differential library's "fastest test"), and the recommended action once confirmed. Prefer a test that can falsify the hypothesis, not just confirm it.

Before finalizing, run the validation checklist.

### Validation checklist (baked-in - run before accepting any root cause)

- [ ] **Alternatives considered?** Not just the first plausible one (premature closure).
- [ ] **Multiple factors?** Looked for several contributing causes, not a single one.
- [ ] **Causation, not correlation?** A clear mechanism, not just timing coincidence.
- [ ] **Tried to disprove it?** Actively looked for data that would refute the cause, not only confirm.
- [ ] **Root, not symptom?** Asked what *allowed* the symptom, didn't stop at the surface step.
- [ ] **System, not person?** Framed in process/system terms, not "someone messed up".
- [ ] **Ignored no data?** Checked less-visible logs / history (not just what's at hand).
- [ ] **Not survivorship?** Didn't dismiss a risk just because "it never happened before".
- [ ] **Not politically convenient?** Not chosen because it's the comfortable answer.
- [ ] **Actionable?** In our power to fix, and verifiable by measurement.

Any "no" or "unsure" → re-open the investigation.

---

## Step 8: Output - Root Cause Analysis

```markdown
# Root Cause Analysis - [Symptom]

**Date:** [YYYY-MM-DD]
**Symptom:** [what moved, direction, magnitude, vs expected]
**First started / noticed:** [dates]

## Is it real?
[Confirmed real, or measurement artifact - and which trap if so.]

## Where it concentrates
[Segment(s) / funnel step / platform where the anomaly lives - or "broad".]

## What changed
[The change(s) that align with the anomaly's timing and location.]

## Candidate causes
| Cause | Category | Evidence status | Data signature match | Fastest test |
|---|---|---|---|---|
| [cause] | [category] | [EVIDENCE / HYPOTHESIS] | [does it fit?] | [test] |

## Leading root cause
[The best-supported cause. If still a hypothesis, say so plainly.]
- Status: [EVIDENCE / HYPOTHESIS - untested]
- Mechanism: [how it produces the symptom]

## Confirm test + action
- Test: [cheapest confirm/rule-out]
- If confirmed → action: [fix]

## Testable hypotheses (for pm-hypotheses)
- [HYP]: [statement] - test: [how] - would refute if: [signal]

## Validation checklist: [passed / re-opened because ...]
```

---

## Internal completeness checklist

<!-- Claude reference only -->

- [ ] Symptom captured precisely (what/how much/when/where) before investigating
- [ ] Real-vs-measurement ruled on before hunting causes
- [ ] Localized by segment/funnel before generating causes
- [ ] "What changed" inventoried and time/segment-aligned
- [ ] Candidates spread across categories (not tunnel on one)
- [ ] Every candidate labeled [EVIDENCE] or [HYPOTHESIS]
- [ ] 5-Whys stopped at an actionable, systemic cause
- [ ] Validation checklist run before accepting a root cause
- [ ] Output includes cheapest confirm test + testable hypotheses

---

## Save to

```
pureinn-workspace/[project-slug]/root-cause/[YYYY-MM-DD]-[symptom-slug].md
```

`root-cause/` is a cross-cutting operational folder (like `meetings/`, `stress-tests/`) - created on demand, not part of the phase artifact flow. Save if the anomaly is significant or recurring; a quick check can stay in-chat.

---

## Handoff

**Čo si teraz má:** Vieš, či je anomália reálna, kde sa koncentruje, čo ju najpravdepodobnejšie spôsobilo - a najlacnejší test na potvrdenie. Namiesto hádania alebo opravovania symptómu máš testovateľnú príčinu.

**Ďalší krok:**
- Ak je leading príčina ešte hypotéza → `/pm-hypotheses` (zaraď a validuj testom, kým nekonáš).
- Ak potvrdená a je to feature/spec problém → oprav Feature Card / `/pm-feature-design`.
- Ak odhalí hlbší problém s produktom/segmentom → `/pm-personas` alebo `/pm-problem-validation` (re-check).

**Môžeš preskočiť ak:** Pohyb metriky je v normálnom šume (v očakávanom pásme, sezónny, víkendový) - vtedy nie je čo diagnostikovať, len sleduj ďalej.
