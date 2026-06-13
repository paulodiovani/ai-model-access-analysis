#!/usr/bin/env bash
# update-data.sh — Data update automation for AI Model Access Analysis
#
# Pipeline:
#   1. Validate — check JSON data files against schema
#   2. Check consistency — verify source_ids, rank ordering, page-data alignment
#   3. Report — flag any differences between pages and data files
#
# Usage:
#   bash scripts/update-data.sh              # Run full pipeline
#   bash scripts/update-data.sh --dry-run    # Validate only, no changes
#   bash scripts/update-data.sh --check      # Check page-data consistency

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
DATA_DIR="$PROJECT_ROOT/data"
DOCS_DIR="$PROJECT_ROOT/docs/content"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

DRY_RUN=false
CHECK_ONLY=false

for arg in "$@"; do
  case $arg in
    --dry-run) DRY_RUN=true ;;
    --check)   CHECK_ONLY=true ;;
    --help|-h)
      echo "Usage: $0 [--dry-run] [--check]"
      echo "  --dry-run   Validate only, no changes"
      echo "  --check     Check page-data consistency"
      exit 0
      ;;
  esac
done

errors=0
warnings=0

log_ok()   { echo -e "${GREEN}✓${NC} $1"; }
log_warn() { echo -e "${YELLOW}⚠${NC} $1"; ((warnings++)) || true; }
log_err()  { echo -e "${RED}✗${NC} $1"; ((errors++)) || true; }

# ─── Step 1: Validate JSON ───────────────────────────────────────────────────

echo "═══ Step 1: Validating JSON data files ═══"

if ! command -v jq &>/dev/null; then
  log_err "jq is required but not installed"
  exit 1
fi

for f in "$DATA_DIR"/*.json; do
  fname="$(basename "$f")"
  if jq empty "$f" 2>/dev/null; then
    log_ok "$fname is valid JSON"
  else
    log_err "$fname has invalid JSON"
  fi
done

# ─── Step 2: Validate source_ids ─────────────────────────────────────────────

echo ""
echo "═══ Step 2: Validating source_ids ═══"

valid_ids=$(jq -r '.sources[].id' "$DATA_DIR/sources.json")

for f in "$DATA_DIR"/{20-rankings,10-rankings,free-rankings,api-pricing}.json; do
  fname="$(basename "$f")"
  if [ ! -f "$f" ]; then
    log_warn "$fname not found, skipping"
    continue
  fi

  page_ids=$(jq -r '[.entries[].source_ids[]] | unique | .[]' "$f" 2>/dev/null || true)
  for sid in $page_ids; do
    if echo "$valid_ids" | grep -qx "$sid"; then
      : # valid
    else
      log_err "$fname references unknown source_id: $sid"
    fi
  done
  log_ok "$fname source_ids validated"
done

# ─── Step 3: Validate rank ordering ──────────────────────────────────────────

echo ""
echo "═══ Step 3: Validating rank ordering ═══"

for f in "$DATA_DIR"/{20-rankings,10-rankings,free-rankings,api-pricing}.json; do
  fname="$(basename "$f")"
  if [ ! -f "$f" ]; then continue; fi

  expected=1
  while IFS= read -r rank; do
    if [ "$rank" != "$expected" ]; then
      log_err "$fname: expected rank $expected but found $rank"
      break
    fi
    ((expected++))
  done < <(jq -r '.entries[].rank' "$f")
  log_ok "$fname rank ordering is correct"
done

# ─── Step 4: Check page-data consistency ─────────────────────────────────────

echo ""
echo "═══ Step 4: Checking page-data consistency ═══"

# Check that each data file has a corresponding page
for page_name in 20-rankings 10-rankings free-rankings api-pricing; do
  data_file="$DATA_DIR/${page_name}.json"
  page_file="$DOCS_DIR/${page_name}.md"

  if [ ! -f "$data_file" ]; then
    log_warn "Data file missing: $page_name.json"
    continue
  fi
  if [ ! -f "$page_file" ]; then
    log_warn "Page file missing: $page_name.md"
    continue
  fi

  # Check that each provider in data appears in the page
  while IFS= read -r provider; do
    # Check full name first, then fall back to base name (before parenthetical)
    if grep -qF "$provider" "$page_file"; then
      : # full match
    else
      base_name=$(echo "$provider" | sed 's/ *([^)]*)//')
      if [ -n "$base_name" ] && grep -qF "$base_name" "$page_file"; then
        : # base name match
      else
        log_err "$page_name.md is missing provider: $provider"
      fi
    fi
  done < <(jq -r '.entries[].provider' "$data_file")

  # Check entry count
  data_count=$(jq '.entries | length' "$data_file")
  log_ok "$page_name: $data_count entries in data file"

  log_ok "$page_name page-data consistency checked"
done

# ─── Step 5: Summary ─────────────────────────────────────────────────────────

echo ""
echo "═══ Summary ═══"
if [ "$errors" -gt 0 ]; then
  log_err "$errors error(s), $warnings warning(s)"
  exit 1
elif [ "$warnings" -gt 0 ]; then
  log_warn "$warnings warning(s), 0 errors"
else
  log_ok "All checks passed"
fi
