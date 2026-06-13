# Templates

This directory contains page templates for generating the `docs/content/*.md` pages from `data/*.json` data files.

## Template Files

| Template | Data Source | Output Page |
|:---|:---|:---|
| `20-rankings.md.tmpl` | `data/20-rankings.json` | `docs/content/20-rankings.md` |
| `10-rankings.md.tmpl` | `data/10-rankings.json` | `docs/content/10-rankings.md` |
| `free-rankings.md.tmpl` | `data/free-rankings.json` | `docs/content/free-rankings.md` |
| `api-pricing.md.tmpl` | `data/api-pricing.json` | `docs/content/api-pricing.md` |

## Purpose

Templates define the **structure and format** of each page. They serve as the canonical reference for how data should be rendered into markdown. Currently, templates are documentation-first — pages are updated manually to match the data files, using these templates as the style guide.

## Workflow

1. **Update data first** — edit `data/*.json` files (the single source of truth)
2. **Reference the template** — ensure the page follows the template structure
3. **Update the page** — regenerate or manually update `docs/content/*.md` to match data
4. **Validate** — run `scripts/update-data.sh --dry-run` to check consistency

## Template Syntax

Templates use a Handlebars-inspired `{{placeholder}}` syntax for documentation purposes:

- `{{provider}}` — provider name from data
- `{{plan}}` — plan name from data  
- `{{rank}}` — ranking position
- `{{model_names}}` — comma-separated model names
- `{{#each entries}}` — iterates over all entries in the data file

These are **not executable templates** — they document the expected format. Actual page generation is done manually or via the `update-data.sh` script.

## Rules

- Data files (`data/*.json`) are the **single source of truth**
- Pages must match data files exactly (ranks, prices, models, limits)
- Templates define the canonical page structure
- Never edit pricing data directly in markdown — update the data file first
