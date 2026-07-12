---
description: Cut a Pureinn framework release - inspect changes, propose version bump + message, confirm, then publish (bump, commit, push, tag, GitHub Release). The website rebuilds automatically.
---

The user wants to publish a release of the framework (this repo). Run this flow. Triggers: `/release`, or natural phrases like "urob release", "aktualizuj git", "vydaj novú verziu".

1. **Inspect what changed** since the last release: run `git status` and `git --no-pager diff` (and `git log <lastTag>..HEAD --oneline` if useful). Understand what actually changed - do not guess.

2. **Decide the version bump** per the repo's rules in CLAUDE.md:
   - **patch**: bug fix, text correction, clarification
   - **minor**: new skill, significant skill update, new integration
   - **major**: renamed/removed skill, breaking workflow/structure change
   Note: the release history is deliberately kept to major+minor only (patches are treated as noise). Prefer minor for real content changes; use patch only for genuine fixes.

3. **Draft a one-line release message** describing the change, in the style of existing releases (see `git tag` / CHANGELOG.md).

4. **Confirm with the user** before publishing. Show: the bump type, the resulting version number, and the message. Ask if it is correct or should be adjusted. Do NOT publish until the user confirms. If the user wants changes, update and re-confirm.

5. **Publish** once confirmed: run
   ```
   ./scripts/release.sh <bump> "<message>" --yes
   ```
   The script bumps the version, syncs skill/command counts across plugin.json/marketplace.json/README/CLAUDE.md, updates the CHANGELOG, then commits, pushes, tags, and creates the GitHub Release. `--yes` is correct here because you already confirmed with the user in step 4.

6. **Report the result**: the new version, and that the website (pureinn-web) will rebuild automatically via the `deploy-web` GitHub Action pinging the Vercel deploy hook. No further action is needed for the web.

If there are no uncommitted changes and no unreleased commits since the last tag, tell the user there is nothing to release rather than cutting an empty version.
