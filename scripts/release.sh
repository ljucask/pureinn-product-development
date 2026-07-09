#!/usr/bin/env bash
# Usage: ./scripts/release.sh <patch|minor|major> "Description of changes"

set -e

BUMP=${1:-patch}
MESSAGE=${2:-""}
PLUGIN_JSON=".claude-plugin/plugin.json"
MARKETPLACE_JSON=".claude-plugin/marketplace.json"
CHANGELOG="CHANGELOG.md"

if [[ -z "$MESSAGE" ]]; then
  echo "Error: release message required."
  echo "Usage: ./scripts/release.sh <patch|minor|major> \"Description of changes\""
  exit 1
fi

if [[ "$BUMP" != "patch" && "$BUMP" != "minor" && "$BUMP" != "major" ]]; then
  echo "Error: bump type must be patch, minor, or major"
  exit 1
fi

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
echo "Done. Version updated to $NEW_VERSION."
echo ""
echo "Next steps:"
echo "  1. Review: plugin.json, marketplace.json, CHANGELOG.md, README.md, CLAUDE.md (skill/command count)"
echo "  2. git add ."
echo "  3. git commit -m \"Release v$NEW_VERSION - $MESSAGE\""
echo "  4. git push"
echo "  5. git tag -a v$NEW_VERSION -m \"Release v$NEW_VERSION - $MESSAGE\""
echo "  6. git push origin v$NEW_VERSION"
echo "  7. gh release create v$NEW_VERSION --title \"v$NEW_VERSION\" --notes \"$MESSAGE\""
