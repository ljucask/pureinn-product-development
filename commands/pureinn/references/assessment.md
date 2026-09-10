# Pureinn - Assessment reference

> Reference for `commands/pureinn/COMMAND.md`. Assessment output and fast-track detection.

## STEP 3B - Assessment

Combine documents (if any) with intake answers to produce a unified picture of the current state.

If documents exist: for each one, identify content type, phase mapping, and quality signals.

Then synthesize everything - documents + intake answers - into a structured assessment. This is the most important output of the entry point.

---

### Assessment Output Format

**1. Brief context** (2-3 sentences)
What Claude sees, the general picture, what kind of project and stage this appears to be - based on documents and intake answers combined.

**2. Document inventory** (skip section if no documents found)

```
| Document | Content type | Maps to | Quality |
|---|---|---|---|
| [filename or "intake answers"] | [e.g., Interview transcripts] | Phase 2 - Discovery (Track D) | ✅ Good / ⚠️ Partial / ❌ Thin |
```

**3. Phase coverage**

```
| Phase | Coverage | Source | Confidence |
|---|---|---|---|
| Phase 1 - Foundation         | ✅ / ⚠️ / ❌ | [document / intake / none] | High / Med / Low |
| Phase 2 - Discovery          | ✅ / ⚠️ / ❌ | | |
| Phase 3a - Validation        | ✅ / ⚠️ / ❌ | | |
| Phase 3b - Commercial Def.   | ✅ / ⚠️ / ❌ | | |
| Phase 4 - Domain             | ✅ / ⚠️ / ❌ | | |
| Phase 5 - Features           | ✅ / ⚠️ / ❌ | | |
```

**4. What Claude understands about this product**

Synthesize the actual product/market/customer picture. Be specific. Clearly mark the difference between **conclusions** (from documents or explicit user statements) and **assumptions** (inferred by Claude).

```
PROBLEM
  - [Conclusion] [what the problem is, from documents or stated by user]
  - [Assumption] [what Claude is inferring that wasn't explicitly stated]

CUSTOMER
  - [Conclusion] [who the primary customer is]
  - [Assumption] [...]

MARKET
  - [Conclusion] [what market context is established]
  - [Assumption] [...]

BUSINESS MODEL
  - [Conclusion] [revenue logic that's visible]
  - [Assumption] [...]

OPEN QUESTIONS
  - [What is unclear, missing, or contradictory - and why it matters]
```

**5. Confirmation prompt**

```
Review the above. For each section:

  ✅ Confirm - this is correct
  ✗ Reject - this is wrong, here's what's correct: [correction]
  ~ Adjust - partially right, here's the nuance: [adjustment]

You can also add anything I missed.
```

Wait for user confirmation. Update the assessment based on their corrections before proceeding.

After confirmation, save the finalized assessment to:
`pureinn-workspace/[slug]/assessment.md`

---

## STEP 3C - Fast Track Detection

After assessment is confirmed, evaluate whether the user qualifies for a fast track. Check all three conditions independently.

---

### Fast Track 1 - Greenfield Express

**Triggers (all must be true):**
- Playbook = Greenfield
- Current stage (from intake Group 3) = "Validated problem, ready to define strategy" OR "Have a strategy or specs, moving to execution"
- Assessment shows: no significant unknown gaps in problem/customer/market understanding

**If triggered, surface proactively:**

```
Vyzerá to, že discovery a validáciu nepotrebuješ.

Express cesta:
  1. /pm-entity-registry     [lean] → entity list + základné stavy
  2. /pm-business-rules-library [lean] → kľúčové pravidlá, Draft mode
  3. /pm-features-list       → feature inventory + FEAT-IDs
  4. /pm-mvp-scope           → MVP scope + Delivery Stripes
  5. /pm-feature-design [FEAT-ID] → JIT spec, opakuj per feature
  → Build → Test → Release

Preskočíme: Phase 1 (Foundation), Phase 2 (Discovery), Phase 3a/3b (Validation + Commercial).

Use the AskUserQuestion tool:
- Question: "Ktorú cestu zvoliť?"
- Option A: "Express - preskočiť Discovery a Validation (Recommended)" — description: "Lean domain registers → feature list → JIT delivery"
- Option B: "Štandardný flow" — description: "Všetky fázy vrátane Discovery a Validation"
- Option C: "Čiastočný Discovery" — description: "Niektoré Phase 2 tracky chcem prejsť"
```

**Express lean mode rules:**
- `pm-entity-registry` lean: entity list + key states only, no full ERD, no Excalidraw
- `pm-business-rules-library` lean: core rules only, all Draft, finalize JIT per feature
- Skip: pm-domain-model, pm-privacy-requirements (unless regulated industry), pm-product-roadmap

---

### Fast Track 2 - Feature Implementation: First Run

**Triggers (all must be true):**
- Playbook = Feature Implementation
- No `state.json` exists for this project (first time with Pureinn on this product)

**If triggered, surface proactively:**

```
Existujúci produkt, prvý run s Pureinn.

Express cesta:
  1. /common-ground           → tech context z existujúceho kódu → COMMON-GROUND.md
  2. /pm-reverse-extract      → bootstrap z kódu:
                                 - extrahuje entities + business rules do registrov
                                 - generuje feature inventory (FDD formát)
                                 - pushne feature hierarchiu do Notion
                                 → ukáže čo našiel, ty opravíš ak treba
  3. /pm-feature-design [FEAT-ID] → JIT spec pre konkrétnu feature
  → Build → Test → Release (FI delivery pravidlá platia vždy)

Use the AskUserQuestion tool:
- Question: "Ktorú cestu zvoliť?"
- Option A: "Express - pm-reverse-extract bootstrap (Recommended)" — description: "Extrahuje entity, business rules a feature inventory priamo z kódu"
- Option B: "Štandardný Phase 0 onboarding" — description: "Manuálny setup: common-ground + impeccable document + pm-glossary + registre"
```

**Note on pm-reverse-extract bootstrap:** Extrahuje čo môže z kódu. Výsledok ukáže pred pokračovaním - user potvrdí alebo opraví. Štandardný PREREQ pattern.

**FI delivery rules vždy platia bez výnimky:**
- Feature flags (OFF by default), FE + BE
- Additive-only API + DB changes
- Full regression suite
- Performance gate (≤10% latency overhead)
- Gradual rollout: Internal → 5% → 25% → 50% → 100%
- Kill switch ak error rate >5%

---

### Fast Track 3 - Feature Implementation: Returning Session

**Triggers (all must be true):**
- Playbook = Feature Implementation
- `state.json` exists (Pureinn already ran on this project)
- Context files exist: `COMMON-GROUND.md` + domain registers

**If triggered, surface proactively:**

```
Kontext existuje z predošlej session.

Express cesta:
  → /pm-feature-design [FEAT-ID] priamo

Ktorú feature ideme špecifikovať?
(alebo: /pm-stripe pre delivery dashboard ak chceš vidieť stav všetkých stripes)
```

**Note:** Ak FEAT-ID ešte neexistuje (nová feature nie je v `feature_list.md`):
1. Pridaj feature do `feature_list.md` manuálne (FEAT-[DOMAIN]-[NUMBER] formát)
2. Vytvor stub Feature Card v `features/cards/`
3. Potom spusti `/pm-feature-design [FEAT-ID]`

---

After the fast-track choice is made - whichever path the user picks, and also when no fast track applies - read `references/playbooks.md` and continue with **STEP 4 (Playbook Selection)**. A fast track changes which skills get queued, not the need for a playbook, a starting phase and a workspace.
