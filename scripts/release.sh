#!/usr/bin/env bash
# Usage: ./scripts/release.sh <patch|minor|major> "Description of changes" [--yes]
#   --yes  publish without the interactive confirmation prompt

set -e

# Parse args: bump + message in order, --yes / -y anywhere.
AUTO_YES=false
POSITIONAL=()
for arg in "$@"; do
  case "$arg" in
    --yes|-y) AUTO_YES=true ;;
    *) POSITIONAL+=("$arg") ;;
  esac
done
BUMP=${POSITIONAL[0]:-patch}
MESSAGE=${POSITIONAL[1]:-""}
PLUGIN_JSON=".claude-plugin/plugin.json"
MARKETPLACE_JSON=".claude-plugin/marketplace.json"
CHANGELOG="CHANGELOG.md"

# The only paths a release may ever stage. Deliberately NOT `git add .`:
# this repo also hosts local git worktrees, audit scratch files, and other
# non-published material next to the tracked tree, and a blind `git add .`
# would silently sweep whatever untracked thing happens to sit there at
# release time into a public, permanently-tagged GitHub Release. This list
# is the actual tracked top-level content (verified via `git ls-tree`) - add
# a new top-level path here only when it is genuinely part of the published
# framework.
RELEASE_PATHS=(
  ".claude/commands"
  ".claude-plugin"
  ".github"
  ".gitignore"
  "CHANGELOG.md"
  "CLAUDE.md"
  "FRAMEWORK_GUIDE.md"
  "LICENSE"
  "NOTION_TEMPLATE.md"
  "README.md"
  "assets"
  "commands"
  "docs"
  "examples"
  "scripts"
  "skills"
)

if [[ -z "$MESSAGE" ]]; then
  echo "Error: release message required."
  echo "Usage: ./scripts/release.sh <patch|minor|major> \"Description of changes\" [--yes]"
  exit 1
fi

if [[ "$BUMP" != "patch" && "$BUMP" != "minor" && "$BUMP" != "major" ]]; then
  echo "Error: bump type must be patch, minor, or major"
  exit 1
fi

# Structural integrity gate - never ship a release that fails validation.
# Runs before any file is touched, so a broken repo aborts cleanly with no partial state.
echo "Running structural validation..."
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if ! python3 "$SCRIPT_DIR/validate.py"; then
  echo ""
  echo "Error: validation failed. Fix the integrity errors above before releasing."
  exit 1
fi
echo ""

# Read current version from plugin.json
CURRENT=$(python3 -c "import json; print(json.load(open('$PLUGIN_JSON'))['version'])")
MAJOR=$(echo "$CURRENT" | cut -d. -f1)
MINOR=$(echo "$CURRENT" | cut -d. -f2)
PATCH=$(echo "$CURRENT" | cut -d. -f3)

# Bump version
if [[ "$BUMP" == "major" ]]; then
  MAJOR=$((MAJOR + 1)); MINOR=0; PATCH=0
elif [[ "$BUMP" == "minor" ]]; then
  MINOR=$((MINOR + 1)); PATCH=0
else
  PATCH=$((PATCH + 1))
fi

NEW_VERSION="$MAJOR.$MINOR.$PATCH"
TODAY=$(date +%Y-%m-%d)

echo "Bumping $CURRENT -> $NEW_VERSION ($BUMP)"

# Update plugin.json
python3 - <<EOF
import json

with open('$PLUGIN_JSON', 'r') as f:
    data = json.load(f)
data['version'] = '$NEW_VERSION'
with open('$PLUGIN_JSON', 'w') as f:
    json.dump(data, f, indent=2)
    f.write('\n')
EOF

# Update marketplace.json
python3 - <<EOF
import json

with open('$MARKETPLACE_JSON', 'r') as f:
    data = json.load(f)
data['metadata']['version'] = '$NEW_VERSION'
data['plugins'][0]['version'] = '$NEW_VERSION'
with open('$MARKETPLACE_JSON', 'w') as f:
    json.dump(data, f, indent=2)
    f.write('\n')
EOF

# Sync skill/command counts everywhere they're hardcoded (plugin.json,
# marketplace.json, README.md, CLAUDE.md) so a release never ships a stale count.
ACTUAL_SKILLS=$(find skills -mindepth 1 -maxdepth 1 -type d | wc -l | tr -d ' ')
ACTUAL_COMMANDS=$(find commands -mindepth 1 -maxdepth 1 -type d | wc -l | tr -d ' ')

python3 - <<EOF
import re

files = ["$PLUGIN_JSON", "$MARKETPLACE_JSON", "README.md", "CLAUDE.md"]
changed = []

for path in files:
    with open(path, "r") as f:
        content = f.read()
    new_content = re.sub(r"\d+(?= active skills)", "$ACTUAL_SKILLS", content)
    new_content = re.sub(r"\d+(?= commands)", "$ACTUAL_COMMANDS", new_content)
    if new_content != content:
        with open(path, "w") as f:
            f.write(new_content)
        changed.append(path)

if changed:
    print(f"Synced skill/command counts ({$ACTUAL_SKILLS} skills, {$ACTUAL_COMMANDS} commands) in: " + ", ".join(changed))
else:
    print(f"Skill/command counts already correct ({$ACTUAL_SKILLS} skills, {$ACTUAL_COMMANDS} commands).")
EOF

# Prepend to CHANGELOG.md
CHANGELOG_ENTRY="## [$NEW_VERSION] - $TODAY

### $MESSAGE
"

if [[ "$BUMP" == "major" ]]; then
  CHANGELOG_ENTRY="## [$NEW_VERSION] - $TODAY

### Breaking Changes

### $MESSAGE
"
fi

EXISTING=$(cat "$CHANGELOG")
echo -e "# Changelog\n\n$CHANGELOG_ENTRY\n---\n" > "$CHANGELOG"
# Append existing content minus the first line (old "# Changelog" header)
echo "$EXISTING" | tail -n +2 >> "$CHANGELOG"

echo ""
echo "Version prepared: $CURRENT -> $NEW_VERSION"
echo ""

# Stage only the allowlisted framework paths - never a blind `git add .`.
EXISTING_RELEASE_PATHS=()
for p in "${RELEASE_PATHS[@]}"; do
  [[ -e "$p" ]] && EXISTING_RELEASE_PATHS+=("$p")
done
git add -- "${EXISTING_RELEASE_PATHS[@]}"

echo "Staged for release:"
git --no-pager diff --cached --stat
echo ""

# Visibility only (never staged): anything changed/untracked outside the
# allowlist. Catches the exact class of thing `git add .` would have swept in.
OUTSIDE=""
while IFS= read -r line; do
  file="${line:3}"
  in_allowlist=false
  for p in "${RELEASE_PATHS[@]}"; do
    if [[ "$file" == "$p" || "$file" == "$p"/* ]]; then
      in_allowlist=true
      break
    fi
  done
  if [[ "$in_allowlist" == false ]]; then
    OUTSIDE="$OUTSIDE  $line"$'\n'
  fi
done < <(git status --porcelain --untracked-files=all)

if [[ -n "$OUTSIDE" ]]; then
  echo "Outside the release allowlist (excluded, not staged):"
  echo -n "$OUTSIDE"
  echo ""
fi

# Confirm before publishing, unless --yes was passed.
if [[ "$AUTO_YES" != true ]]; then
  read -r -p "Publish v$NEW_VERSION? (commit + push + tag + GitHub Release) [y/N] " REPLY
  if [[ ! "$REPLY" =~ ^[Yy]$ ]]; then
    echo "Aborted. Version files are updated and staged, but nothing was committed."
    echo "Review the changes, then re-run with --yes, or commit manually."
    exit 0
  fi
fi

# Publish: commit (already staged above), push, tag, push tag, create GitHub Release.
git commit -m "Release v$NEW_VERSION - $MESSAGE"
git push
git tag -a "v$NEW_VERSION" -m "Release v$NEW_VERSION - $MESSAGE"
git push origin "v$NEW_VERSION"
gh release create "v$NEW_VERSION" --title "v$NEW_VERSION" --notes "$MESSAGE"

echo ""
echo "Released v$NEW_VERSION. The website will rebuild automatically (deploy-web Action)."
