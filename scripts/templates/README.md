# Templates

This directory contains the canonical page template for generating `docs/content/*.md` pages from `data/*.json` data files.

## Template File

**`page.md.tmpl`** — The single template that ALL ranking and pricing pages follow.

This template defines the standardized structure:
1. **Title** — from `title` field
2. **Description** — from `description` field
3. **Scope** — from `scope_note` field
4. **Ranking direction** — from `ranking_direction` field
5. **Entries** — ranked list with unified fields per entry
6. **Summary table** — columns defined by `summary_columns` in the data file
7. **Conclusion** — from `conclusion` field

## Data Files

| Data File | Page Type |
|:---|:---|
| `data/20-rankings.json` | $20 budget subscription rankings |
| `data/10-rankings.json` | $10 budget subscription rankings |
| `data/free-rankings.json` | Free tier rankings |
| `data/api-pricing.json` | API pricing comparison |

## Workflow

1. **Update data first** — edit `data/*.json` files (the single source of truth)
2. **Reference the template** — ensure the page follows `page.md.tmpl` structure
3. **Update the page** — regenerate or manually update `docs/content/*.md` to match data
4. **Validate** — run `scripts/update-data.sh --check` to check consistency

## Template Syntax

Templates use a Handlebars-inspired `{{placeholder}}` syntax:

- `{{title}}` — page title from data
- `{{description}}` — page introduction
- `{{scope_note}}` — scope callout
- `{{ranking_direction}}` — ranking direction text
- `{{#each entries}}` — iterates over all entries
- `{{summary_columns}}` — defines table columns from data
- `{{conclusion}}` — strategic takeaway

These are **documentation-first templates** — they define the expected format. Actual page generation is done manually or via the `update-data.sh` script.

## Rules

- **One template for all pages** — never create per-page templates
- Data files (`data/*.json`) are the **single source of truth**
- Pages must match data files exactly (ranks, prices, models, limits)
- All entries use the same field names (empty string where not applicable)
- Summary table columns are defined per-page via `summary_columns`
- Never edit pricing data directly in markdown — update the data file first
