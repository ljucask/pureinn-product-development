# Changelog

## [1.4.8] - 2026-06-01

### pm-reverse-extract: push BRD/FSD/Domain Model to Notion, add FS Overview and Feature Card content

- Step 4c: FS entries now include Feature Set Overview as Notion page body
- Step 4d: Feature entries now include Feature Card content as page body (full for Done/In Progress, stub for Planned)
- Step 4e (new): pushes existing local BRD/FSD/Domain Model files to Notion as pages; links FS entries via BRD/FSD URL properties; updates pureinn-variables.md with created page URLs
- Step 4f (renamed from 4e): updated confirmation summary to include new push counts
- Step 6 migration summary: updated to reflect FS Overview, Feature Card, and doc push results
- Notion section: clarified which pureinn-variables.md keys are used in which steps; removed stale manual reminder

---


## [1.4.7] - 2026-05-31

### Rename impeccable-teach to /impeccable document across all references

- COMMAND.md: all `/impeccable-teach` references updated to `/impeccable document`
- FRAMEWORK_GUIDE.md: all `/impeccable-teach` references updated to `/impeccable document`
- Reflects current impeccable plugin API (skill renamed upstream)

---


## [1.4.6] - 2026-05-31

### Update FRAMEWORK_GUIDE.md for Path C and Notion template

- Phase 2 Track C row: updated "Before you run" to note Path C requires no prep
- "Bring your data" rule: added exception for pm-market-analysis Path C
- Workspace section: added reference to NOTION_TEMPLATE.md

---


## [1.4.5] - 2026-05-31

### Update README for Notion template and pm-market-analysis Path C

- README: updated pm-market-analysis skill description to mention three input paths (A/B/C)
- README: added Notion setup note in MCP integrations section with link to NOTION_TEMPLATE.md

---


## [1.4.4] - 2026-05-31

### Add Notion template setup guide and onboarding flow

- Added `NOTION_TEMPLATE.md` - setup guide with duplicate link (coming soon), full URL reference table, FAQ
- Updated `/pureinn` init message: after creating pureinn-variables.md, offers Option A (duplicate Notion template) and Option B (use own setup)

---


## [1.4.3] - 2026-05-31

### Add OpenAI Path C to pm-market-analysis with per-project API key via pureinn-variables.md

- pm-market-analysis: added Path C (AI-powered research via OpenAI Responses API with web_search)
- Path C reads OPENAI_API_KEY from pureinn-variables.md; prompts user to add key if blank
- Runs 3 targeted web search queries (market size, competitor analysis, market timing)
- pureinn COMMAND.md: added `AI Research` section to pureinn-variables.md template with OPENAI_API_KEY field

---


## [1.4.2] - 2026-05-31

### Remove Octagon Deep Research MCP integration (paid service)

---


## [1.4.1] - 2026-05-31

### Apply grouped question pattern to pm-reverse-extract Step 1

---


## [1.4.0] - 2026-05-31

### Add scoping question to pm-features-list; add grouped alignment pattern to pm-mvp-scope with preliminary MVP cut after Group 1

---


## [1.3.0] - 2026-05-31

### Apply grouped question pattern to all remaining documentation skills: project-charter, stakeholder-map, team-roster, comms-charter, prd, product-roadmap, privacy-requirements

---


## [1.2.0] - 2026-05-31

### Add grouped questions to decision skills; Path A/B to tech-feasibility and domain-analysis; Path C Octagon MCP to market-analysis

---


## [1.1.0] - 2026-05-31

### Add guided elicitation mode (Path B) to 5 research-dependent skills: pm-personas, jtbd-building, pm-market-analysis, pm-problem-validation, design-thinking

---


## [1.0.7] - 2026-05-31

### Apply grouped question pattern to all Type B skills: reduce options to max 4, restructure pm-pitch-deck into groups with confirmation

---


## [1.0.6] - 2026-05-31

### Separate free-text and option-based questions within groups; document universal question pattern in CLAUDE.md

---


## [1.0.5] - 2026-05-31

### Group intake questions into 3 rounds with confirmation summaries; document grouped question pattern as universal standard

---


## [1.0.4] - 2026-05-31

### Rewrite intake questions in natural A/B/C/D format to trigger AskUserQuestion UI

---


## [1.0.3] - 2026-05-31

### Use AskUserQuestion tool for interactive intake in pureinn

---


## [1.0.2] - 2026-05-31

### Intake questions now asked one at a time in pureinn

---


## [1.0.1] - 2026-05-31

### Test release script

---


## [1.0.0] - 2025-05-29

### Initial release

- 34 skills covering full product lifecycle (Phases 1-7)
- 2 orchestrator commands: `/pureinn`, `/pureinn-resume`
- Three playbooks: Greenfield, Feature Implementation, Rebuild
- MCP integrations: Notion (feature backlog, glossary, domain model), Excalidraw (diagrams), Gamma (pitch deck)
- FDD delivery cycle with Stripe orchestration
- Workspace state management via `pureinn-workspace/[slug]/state.json`
- Notion project configuration via `pureinn-variables.md`
