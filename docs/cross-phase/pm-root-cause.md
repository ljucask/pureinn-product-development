# pm-root-cause

> Diagnostic engine for in-flight anomalies - drills to the real root cause, not the first plausible one

**Phase:** Cross-phase  
**Agent mode:** `never` - value is the live investigative dialogue  
**Version:** 1.0.0  
**Triggers:** root cause, why did this happen, metric dropped, churn spike, conversion drop, funnel drop, retention decline, feature not adopted, DAU drop, diagnose, investigate anomaly, 5 whys, fishbone, something's wrong with the data

---

## When to use

When something live behaves unexpectedly: a metric dropped, churn spiked, a feature isn't adopted, conversion fell, tickets are rising. Cross-phase - run whenever an anomaly needs structured diagnosis, at any point in the product lifecycle.

**Agent mode is not supported.** The value is the live investigative dialogue - hypothesis drill-down requires interactive back-and-forth. Invoking with `--agent` will warn once and proceed interactively.

---

## What it produces

A structured root cause investigation with:

1. **Reality check** - is this a real anomaly or a measurement artifact (data quality, segment definition, seasonality, instrumentation bug)?
2. **Concentration analysis** - where does the anomaly concentrate? Segment / funnel stage / cohort / geography / feature / device?
3. **Change inventory** - what changed (product, marketing, competition, external event) in the relevant time window?
4. **Candidate cause differential** - causes ranked by evidence strength, across categories: product, data/measurement, market, operational, team
5. **5-Whys drill** - structured iterative drill on the highest-confidence candidate
6. **Evidence vs. guess separation** - what is confirmed vs. inferred vs. assumed
7. **Cheapest next test** - the lowest-cost experiment to confirm or reject the root cause hypothesis
8. **Testable hypotheses** - formatted for input into `pm-hypotheses`

---

## Built-in diagnostic methods

- 5-Whys drill
- Fishbone (Ishikawa) categorization
- Anomaly-to-cause differential library
- Measurement trap catalogue (common instrumentation errors)
- Cognitive bias catalogue (availability, confirmation, recency bias checks)

---

## How to invoke

```bash
/pm-root-cause    # interactive only - --agent not supported
```

Describe the symptom: what metric, what change, over what time period, compared to what baseline. The skill takes it from there - you do not need a hypothesis before starting.

---

## Dependencies

**Recommended (provides context):**
- `pm-kpis` - KPI framework helps scope the anomaly and confirm the metric definition
- `pm-personas` - segment breakdown informs where the anomaly concentrates
- `pm-hypotheses` - testable hypotheses from this session feed directly into a new experiment plan

**Produces for:**
- `pm-hypotheses` - root cause hypotheses become entries in the Hypothesis Register for validation
- `pm-prioritize` - confirmed root cause may change feature priority

**Related skills:** `pm-hypotheses`, `pm-problem-validation`, `pm-kpis`, `pm-personas`, `pm-prioritize`
