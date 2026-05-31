# CLAUDE.md

This file provides guidance to Claude Code when working in this repository.

## What this repository is

The Pureinn product development framework published as a Claude Code plugin. Contains 34 skills and 2 commands covering the full product lifecycle.

**Plugin repo is the master copy.** The `AI Workflow/.claude/commands/` folder in the personal framework repo is secondary. Always edit here first.

---

## Repository structure

```
.claude-plugin/
  plugin.json       - Package metadata (name, version, author, paths)
  marketplace.json  - Marketplace registration metadata
commands/
  pureinn/          - Main orchestrator (entry point, routing, exit gates)
  pureinn-resume/   - Resume paused project
skills/
  [skill-name]/
    SKILL.md        - Skill content + frontmatter (name, description, triggers, metadata)
scripts/
  release.sh        - Versioning + CHANGELOG automation (run before every release)
assets/
  pureinn-banner.png
README.md           - Public-facing documentation
FRAMEWORK_GUIDE.md  - Detailed playbook and skill reference
CHANGELOG.md        - Version history
```

---

## Update and versioning process

### Where to edit

Edit skill files directly in this repo (`skills/[name]/SKILL.md` or `commands/[name]/COMMAND.md`). This is the master copy.

### Versioning rules (semantic versioning)

| Change type | Version bump | Examples |
|---|---|---|
| Bug fix, text correction, clarification | **patch** `1.0.x` | Fixed logic error in pm-brd, corrected description |
| New skill, significant skill update, new MCP integration | **minor** `1.x.0` | Added pm-competitive-analysis, updated pm-hypotheses flow |
| Renamed/removed skill, broken workflow change, structural change | **major** `x.0.0` | pm-business-model renamed, skill removed, phase restructure |

### Release process

Every release - in this order:

```bash
# 1. Make your edits to skill/command files

# 2. Run release script (handles version bump + CHANGELOG entry)
./scripts/release.sh patch "Fixed X in pm-brd"
./scripts/release.sh minor "Added pm-competitive-analysis skill"
./scripts/release.sh major "Renamed pm-business-model to pm-revenue-model"

# 3. Review the changes the script made (plugin.json, marketplace.json, CHANGELOG.md)

# 4. Commit and push
git add .
git commit -m "Release vX.Y.Z - [summary]"
git push
```

Never push a release without bumping the version. Users will not receive updates unless the version changes.

### Adding a new skill

1. Create `skills/[skill-name]/SKILL.md` with proper frontmatter:
```yaml
---
name: skill-name
description: Use when...
license: MIT
metadata:
  author: https://github.com/ljucask
  version: "1.0.0"
  domain: product-management
  triggers: keyword1, keyword2, keyword3
  role: specialist
  scope: [analysis|specification|planning|research|validation|documentation]
  output-format: document
  related-skills: skill-a, skill-b
---
```
2. Reference the skill in `FRAMEWORK_GUIDE.md` under the correct phase
3. Add it to the skill map in `README.md`
4. Run `./scripts/release.sh minor "Added [skill-name]"`

### Updating an existing skill

1. Edit `skills/[skill-name]/SKILL.md`
2. If logic/flow changed significantly: bump `version` in the skill's own frontmatter metadata too
3. Run `./scripts/release.sh patch "Updated [skill-name]: [what changed]"` (or minor if substantial)

### Renaming or removing a skill

This is a major version change - existing users may have workflows referencing the old name.

1. Rename/remove the file
2. Update all references in `FRAMEWORK_GUIDE.md` and `README.md`
3. Add a migration note in `CHANGELOG.md` under Breaking Changes
4. Run `./scripts/release.sh major "[Old-skill] renamed to [new-skill]"`

---

## Installation

```bash
/plugin marketplace add ljucask/pureinn-product-development
/plugin install pureinn-product-development@pureinn-product-development
```

Select **user scope** for global availability across all projects.

## Updating (for end users)

```bash
/plugin update pureinn-product-development@pureinn-product-development
```
