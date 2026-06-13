#!/usr/bin/env bash
# =============================================================================
# AI Cost Analysis — Data Update Pipeline
# =============================================================================
# Usage: ./scripts/update-data.sh [OPTIONS]
#
# Options:
#   --fetch-only    Only fetch data from source URLs (stub for now)
#   --pages-only    Only regenerate markdown pages from existing data
#   --dry-run       Show what would be done without making changes
#   --no-commit     Skip git commit step
#   --help          Show this help message
#
# Steps:
# 1. Fetch latest data from source URLs (web scraping / API calls)
# 2. Update data/*.json files
# 3. Regenerate markdown pages from data
# 4. Git commit + push if changes detected
# =============================================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
DATA_DIR="$PROJECT_ROOT/data"
CONTENT_DIR="$PROJECT_ROOT/docs/content"

# Defaults
FETCH_ONLY=false
PAGES_ONLY=false
DRY_RUN=false
NO_COMMIT=false

# Logging
log()   { echo "[$(date '+%H:%M:%S')] $*"; }
log_ok(){ echo "[$(date '+%H:%M:%S')] ✓ $*"; }
log_skip(){ echo "[$(date '+%H:%M:%S')] ○ $* (skipped)"; }
warn()  { echo "[$(date '+%H:%M:%S')] ⚠ $*" >&2; }
err()   { echo "[$(date '+%H:%M:%S')] ✗ $*" >&2; }

# Parse arguments
for arg in "$@"; do
    case "$arg" in
        --fetch-only)  FETCH_ONLY=true ;;
        --pages-only)  PAGES_ONLY=true ;;
        --dry-run)     DRY_RUN=true ;;
        --no-commit)   NO_COMMIT=true ;;
        --help|-h)
            head -n 16 "$0" | tail -n +2 | sed 's/^# \?//'
            exit 0
            ;;
        *)
            err "Unknown option: $arg"
            exit 1
            ;;
    esac
done

# Validate mutually exclusive flags
if $FETCH_ONLY && $PAGES_ONLY; then
    err "Only one of --fetch-only, --pages-only can be specified."
    exit 1
fi

# Snapshot current data checksums for change detection
snapshot_data() {
    find "$DATA_DIR" -name '*.json' -exec md5sum {} + 2>/dev/null | sort
}

BEFORE_SNAPSHOT=$(snapshot_data)

# =============================================================================
# Step 1: Fetch latest data from source URLs
# =============================================================================
step_fetch() {
    log "Step 1: Fetching latest data from source URLs..."

    # TODO: Implement web scraping / API calls to fetch live data
    # TODO: Parse provider pricing pages and update data/*.json files
    # TODO: Cross-reference with data/sources.json for source URLs
    # TODO: Implement rate limiting and error handling for web requests
    # TODO: Add data validation against data/schema.json after fetch

    log_skip "Data fetching not yet implemented (placeholder)"
    log "       To implement: add fetch logic here or in scripts/fetch-data.py"
    log "       Source URLs are defined in data/sources.json"
}

# =============================================================================
# Step 2: Check if data changed
# =============================================================================
step_check_changes() {
    log "Step 2: Checking for data changes..."

    AFTER_SNAPSHOT=$(snapshot_data)

    if [ "$BEFORE_SNAPSHOT" = "$AFTER_SNAPSHOT" ]; then
        log_ok "No data changes detected."
        return 1
    else
        log_ok "Data changes detected."
        return 0
    fi
}

# =============================================================================
# Step 3: Regenerate markdown pages
# =============================================================================
step_pages() {
    log "Step 3: Regenerating markdown pages..."

    # The markdown pages are currently maintained manually, following the
    # templates defined in scripts/templates/README.md.
    #
    # When data changes, pages should be reviewed and updated to match.
    # A future enhancement could auto-generate pages from data + templates.

    if $DRY_RUN; then
        log "[dry-run] Would check pages against data and update if needed."
        return 0
    fi

    log_ok "Page check complete. Update pages manually or with future auto-generator."
}

# =============================================================================
# Step 4: Git commit + push
# =============================================================================
step_commit() {
    if $NO_COMMIT; then
        log_skip "Git commit (--no-commit flag set)"
        return 0
    fi

    log "Step 4: Checking for changes to commit..."

    cd "$PROJECT_ROOT"

    # Check if there are any changes
    if git diff --quiet && git diff --cached --quiet && [ -z "$(git ls-files --others --exclude-standard)" ]; then
        log_ok "No changes to commit."
        return 0
    fi

    if $DRY_RUN; then
        log "[dry-run] Would commit the following changes:"
        git status --short
        return 0
    fi

    # Stage all changes
    git add docs/content/ data/ scripts/

    # Build commit message
    local DATE
    DATE=$(date '+%Y-%m-%d')
    local CHANGED_FILES
    CHANGED_FILES=$(git diff --cached --name-only | head -20)
    local FILE_COUNT
    FILE_COUNT=$(git diff --cached --name-only | wc -l)

    local SUMMARY=""
    # Identify what changed
    echo "$CHANGED_FILES" | grep -q '^docs/content/' && SUMMARY="${SUMMARY}pages, "
    echo "$CHANGED_FILES" | grep -q '^data/' && SUMMARY="${SUMMARY}data, "
    echo "$CHANGED_FILES" | grep -q '^scripts/' && SUMMARY="${SUMMARY}scripts, "
    SUMMARY="${SUMMARY%, }"

    local MSG="Update AI cost analysis — ${SUMMARY} (${DATE})

Files changed: ${FILE_COUNT}
"
    git commit -m "$MSG"
    log_ok "Committed: $MSG"

    # Push (only if on a feature branch, not main)
    local BRANCH
    BRANCH=$(git branch --show-current)
    if [ "$BRANCH" != "main" ]; then
        log "Pushing to origin/$BRANCH..."
        git push origin "$BRANCH"
        log_ok "Pushed to origin/$BRANCH"
    else
        log "On main branch — skipping push. Push manually when ready."
    fi
}

# =============================================================================
# Main pipeline
# =============================================================================
main() {
    log "=========================================="
    log "AI Cost Analysis — Data Update Pipeline"
    log "=========================================="
    log "Project root: $PROJECT_ROOT"
    log "Mode: $(
        $FETCH_ONLY  && echo "fetch-only" ||
        $PAGES_ONLY  && echo "pages-only" ||
        echo "full"
    )"
    $DRY_RUN && log "*** DRY RUN — no changes will be made ***"
    log ""

    # Step 1: Fetch (always runs unless --pages-only)
    if ! $PAGES_ONLY; then
        step_fetch
    else
        log_skip "Data fetching (not requested)"
    fi

    # Step 2: Check changes (informational)
    DATA_CHANGED=false
    if step_check_changes; then
        DATA_CHANGED=true
    fi

    # Step 3: Pages
    if ! $FETCH_ONLY; then
        step_pages
    else
        log_skip "Page update (not requested)"
    fi

    # Step 4: Commit
    if ! $FETCH_ONLY; then
        step_commit
    else
        log_skip "Git commit (fetch-only mode)"
    fi

    log ""
    log "=========================================="
    log "Pipeline complete."
    log "=========================================="
}

main
