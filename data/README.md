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
data/*.json (structured data)
       ↓
docs/content/*.md (rendered pages)
docs/charts/*.png (gnuplot charts)
```

## Rules

1. **Every data entry MUST reference at least one `source_id`** that exists in `sources.json`.
2. **Every source MUST have a `last_verified` date** in ISO 8601 format.
3. **Ranks are derived from the data**, not hardcoded. When data changes, ranks may change.
4. **Prices are in USD** unless explicitly noted. CNY prices must be converted or noted.
5. **Never update data without verifying against the source URL first.**
6. **New providers MUST have their source defined in `sources.json` before being added to any data file.**
