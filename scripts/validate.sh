#!/usr/bin/env bash
# Structural integrity check for the Pureinn framework.
# Thin wrapper around scripts/validate.py so there is a stable, bash-style CLI
# consistent with release.sh. Runs from anywhere - resolves the repo root itself.
#
# Usage:
#   ./scripts/validate.sh            # check; exit 1 on integrity errors
#   ./scripts/validate.sh --strict   # also exit 1 on warnings
#
# release.sh calls this automatically before every version bump.

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec python3 "$SCRIPT_DIR/validate.py" "$@"
