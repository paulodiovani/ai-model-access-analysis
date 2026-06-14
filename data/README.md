# Data Directory

This directory contains structured data files that serve as the **single source of truth** for all provider rankings, pricing, and analysis displayed on the site.

## Schema

All data files MUST validate against `schema.json`. The schema defines the structure for subscription rankings, free tier rankings, and API pricing entries.

## Files

| File | Description | Budget |
|------|-------------|--------|
| `schema.json` | JSON Schema definition for all data files | — |
| `sources.json` | Centralized registry of data source URLs | — |
| `20-rankings.json` | $20/month subscription ranking data | $20 |
| `10-rankings.json` | $10/month subscription ranking data | $10 |
| `free-rankings.json` | Free tier ranking data | $0 |
| `api-pricing.json` | API pricing comparison data | Production |

## Data Flow

```
sources.json (verification URLs)
       ↓
data/*.json (structured data + page-level text)
       ↓
docs/content/*.md (rendered pages, following page.md.tmpl)
```

## Page-Level Fields

Each data file includes fields that define the page structure:

| Field | Type | Description |
|-------|------|-------------|
| `title` | string | Page title |
| `description` | string | Introduction paragraph |
| `scope_note` | string | Scope callout (what's included/excluded) |
| `ranking_direction` | string | Ranking direction description |
| `conclusion` | string | Strategic takeaway paragraph |
| `summary_columns` | array | Column definitions for the summary table (`{key, label}`) |

## Entry Fields

All entries use unified field names across ALL data files. See `schema.json` for the full definition.

**Core fields:** `rank`, `provider`, `plan`, `category`, `model_class`, `models`, `value_description`, `limit_description`, `limit_vulnerability`, `notes`, `ranking_class`, `source_ids`

**Optional fields (null/empty when not applicable):** `monthly_price_usd`, `value_multiplier`, `computational_value_usd`, `primary_limit`, `main_limitation`, `api_access`, `data_privacy`, `pricing`, `limitations`, `verdict`

## Rules

1. **Every data entry MUST reference at least one `source_id`** that exists in `sources.json`.
2. **Every source MUST have a `last_verified` date** in ISO 8601 format.
3. **Ranks are derived from the data**, not hardcoded. When data changes, ranks may change.
4. **Prices are in USD** unless explicitly noted. CNY prices must be converted or noted.
5. **Never update data without verifying against the source URL first.**
6. **New providers MUST have their source defined in `sources.json` before being added to any data file.**
