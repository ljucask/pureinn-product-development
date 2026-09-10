# Pureinn - Entry reference

> Reference for `commands/pureinn/COMMAND.md`. The document scan and the `explore` mode conversation - both belong to **STEP 0 (Intent Gate)** and run before any path-specific step.

## STEP 0a - Document Scan

Runs on **every** path, not only on new-project intake. A user who drops new research into the directory and then runs `/pureinn` to resume must never have it silently ignored.

Scan the working directory recursively for existing documents (.md, .txt, .pdf, .docx, .csv, notes, research files - anything that could be product or research material). Exclude code files, system files, dependency/build directories (`node_modules/`, `.git/`, `dist/`, `build/`), and this framework's own operational files (`.claude/`, `pureinn-workspace/`).

Depth of the scan depends on the mode classified in STEP 0:

| Mode | Scan |
|---|---|
| `new`, `explore` | **Full** - the whole tree, nothing is known yet |
| `resume`, `stage` | **Delta** - list the tree, then report only what is *not* already recorded in `state.json` (`documents_found`) or `assessment.md`. Do not re-read what has already been ingested |
| `map` | none - skip the scan entirely |

Apply the **Deep source ingestion** standard to whatever you do read: traverse subfolders, follow references, never treat an index or summary table as the content itself.

**Full scan - documents found:**

Read them. Then inform the user:

```
I found the following files that may be relevant:

  [list of files with paths]

I'll include these in the analysis. If you have additional documents
not yet in the directory, add them now and let me know - otherwise
we'll proceed with what's here.
```

**Full scan - no documents found:**

```
I don't see any existing documents in the directory.

If you have research notes, specs, interview transcripts, or anything
else relevant - add them anywhere in this directory and let me know.

If you're starting from scratch, say "nothing" and we'll go from there.
```

Wait for confirmation. If user adds files, read them. If "nothing", continue with no documents.

**Delta scan - new material found:**

```
Since the last session I found [N] new file(s):

  [list of files with paths]

Read them into this project now?
```

Use **AskUserQuestion**: read them now and note which artifacts may need a re-run *(Recommended)* · ignore for this session · ignore permanently (record in `state.json`).

If the user reads them in, record the files in `state.json` → `documents_found`, and name the artifacts whose conclusions the new material could change (the cascade rule from the Adaptive execution standard - e.g. new interview notes → `pm-personas`, `jtbd-building`, `pm-problem-validation`). Do not silently rewrite those artifacts here; surface them so the user decides.

**Delta scan - nothing new:** say nothing. Continue to the path's own step. Silence is the correct output when there is nothing to report.

---

## STEP 0b - Explore mode

Reached when STEP 0 classified the input as `explore`: the user described a situation, a brief, or a problem out loud, but has not asked to start a project. This is the shape of input that used to fall through the router and produce nothing at all.

**Two failure modes to avoid, in both directions:**
- Doing nothing useful - answering conversationally and never connecting the input to the framework
- Doing too much - scaffolding a workspace, running an intake, or generating an artifact the user never asked for

The mode's job is to *understand and route*, not to produce. **No workspace is created and no artifact is written in this mode.**

**a) Ingest whatever they pointed at.** The brief itself, plus anything the STEP 0a scan found. Full depth.

**b) Read back what you understood.** Keep it short - this is a mirror, not a report:

```
CO SOM POCHOPIL
  - [situation - what they are actually facing]
  - [what has to be produced, and for whom]
  - [hard constraints: deadline, budget, access, team]

CO CHYBA / NA CO JE TO CITLIVE
  - [the 1-3 gaps that would most change the answer]
```

Assumptions go inline, in the format from the Skill question pattern: `Assumption: [what and why]. If this is wrong, tell me - it affects [what].` Never silently fill a gap in a brief you were handed.

**c) Offer three routes.** Use **AskUserQuestion**, one question, with a recommendation reasoned from *their* stated goal and constraints - not from what is easiest:

| Route | When it is the right call | What happens |
|---|---|---|
| Whole project | They are actually starting something and will keep working on it | Continue as mode `new`: STEP 1A, then `references/intake.md` |
| One stage | The upstream work exists already (their own research, a client mandate) and one part of the framework is what's missing | Continue as mode `stage`: STEP 1C |
| One skill, no workspace | Short-horizon work - a take-home, a pitch, a teardown, a single decision to make today | Run that one skill directly. No workspace, no `state.json` |

For the third route, name the specific skill and why it fits - `/pm-scope-brief` for a commissioned definition, `/pm-stress-test` to pressure-test a position before a meeting, `/pm-prototype` when something visual has to exist, `/pm-root-cause` for an in-flight anomaly. Do not list the catalogue; recommend one and say what it produces.

Always include a fourth way out: *"Neither - I just wanted to think it through"*. Explore mode is allowed to end without routing anywhere, and must not nag.

**d) Time-boxed briefs.** If the input states a hard limit (a take-home, "we present tomorrow"), say plainly what fits inside it and what does not, before they choose. A three-hour brief does not fit a full Greenfield run, and the engine should say so rather than starting one.
