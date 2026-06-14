# Agents Guide

Rules for autonomous agents contributing to this project.

## 📋 Workflow Rules

### Always Fetch Before Working
Before making any changes, always fetch the latest state from origin and ensure your branch is up to date:
```
git fetch origin
git checkout main
git pull origin main
```
Then create or update your branch from the latest `main`.

### Keep Branches in Sync
When working on a feature or fix branch, regularly sync with `main` to avoid merge conflicts:
```
git fetch origin
git rebase origin/main
```
Resolve any conflicts before pushing.

### Update Documentation When Applicable
If your change adds, removes, or renames files, update:
- **`README.md`** — keep the project structure and tech stack accurate
- **`AGENTS.md`** — keep the project structure and workflow rules current

If your change affects the live site behavior or deployment, update the relevant docs.

### One Branch Per Change
Create a new branch for each logical change. Never commit directly to `main`.

## 🔍 Verification Rules

### ALWAYS Verify Pricing and Limits
**This is the most important rule.** Never write or update pricing, token limits, or rate limits from memory or training data. Always:

1. **Fetch the provider's official documentation** or pricing page from the live website
2. **Cross-reference** the specific price, limit, or feature against the source
3. **Include the source URL** in your commit message or PR description

This project's value depends on factual accuracy. Stale or incorrect information is worse than no information at all.

When updating a provider entry, find their official pricing or documentation page first. Every entry in `rankings.md` and `free-rankings.md` should have a verifiable source behind it.

### Ranking Scope — Subscriptions Only
The **$10 and $20 ranking pages are for subscription-based plans only.** Before adding a provider, verify it has a recurring monthly subscription (not just pay-as-you-go API credits). Pay-as-you-go providers (like DeepSeek API or OpenCode Zen) belong in the **free rankings** only if they offer a free tier.

**Quick checklist before adding to a paid ranking:**
- Does the provider have a monthly subscription plan?
- Does the plan fit within the budget threshold ($10 or $20)?
- If it's API-only / pay-per-token → do NOT add to paid rankings. Add to free rankings only if there's a free tier.

### API Pricing Page — Production Focus
The `api-pricing.md` page is for **production API usage** — applications and services calling AI models at scale. When adding or updating providers:
- Focus on per-token cost, optimization features (caching, batching, routing), and production reliability
- Include both direct providers and infrastructure/aggregator platforms
- Always verify prices from official pricing pages
- Note: prices are standardized per model across providers — what differentiates providers are edge cases (free credits, cache discounts, batch tiers, routing, model variety)

## 📊 Data-Driven Rules

### Data Files Are the Source of Truth
All pricing, rankings, and analysis data lives in structured JSON files under `data/`. The markdown pages in `docs/content/` are **derived from** the data files — never the other way around.

**When updating information:**
1. Update the data file (`data/*.json`) FIRST
2. Then regenerate the markdown pages
3. Never edit pricing or ranking data directly in markdown

### Schema Compliance
Every data file MUST validate against `data/schema.json`. Before committing:
- Check that all required fields are present
- Check that enum values match the schema
- Check that `source_ids` reference valid entries in `data/sources.json`

### Source Registry (`data/sources.json`)
Every provider MUST have its data sources registered in `data/sources.json` before it can be added to any ranking or pricing file.

**To add a new provider:**
1. First add the provider's source URL(s) to `data/sources.json` with:
   - `id`: a unique slug (e.g., `newprovider-pricing`)
   - `url`: the official pricing/documentation page
   - `type`: one of `pricing_page`, `subscription_page`, `product_page`, `documentation`
   - `last_verified`: today's ISO date
   - `reliability`: `primary` (official source) or `secondary` (third-party)
2. Then add the provider entry to the appropriate `data/*.json` file, referencing the source IDs
3. Update the corresponding `docs/content/*.md` page

### Data Update Procedure
When updating existing provider data:
1. Fetch the source URL listed in `data/sources.json`
2. Compare current data against the live page
3. Update the data file with any changes
4. Update `last_verified` dates in both `data/sources.json` and the entry
5. If prices changed, re-evaluate rankings (ranks may shift)
6. Regenerate pages

### Unified Entry Fields
All entries across ALL data files use the same field names. When a field doesn't apply to a page type, use an empty string (`""`) or `null`. Never omit fields.

**Core fields (all entries):** `rank`, `provider`, `plan`, `category`, `model_class`, `models`, `value_description`, `limit_description`, `limit_vulnerability`, `notes`, `ranking_class`, `source_ids`

**Derived fields (auto-generated):** `rank_display`, `provider_plan`, `value_description_short` — these are computed from core fields for the summary table.

**Optional fields (use null/empty when not applicable):** `monthly_price_usd`, `value_multiplier`, `computational_value_usd`, `primary_limit`, `main_limitation`, `api_access`, `data_privacy`, `pricing`, `limitations`, `verdict`

### Single Template Rule
ALL pages follow `scripts/templates/page.md.tmpl`. Never create per-page templates. The template has no conditional sections — every page uses the same structure.

### Ranking Classifications
Entries are classified using the `ranking_class` field.

**Classification tiers:**
- `exceptional_value` — Best in category, strong ROI
- `great_value` — Strong with minor trade-offs
- `good_value` — Solid, competitive
- `moderate_value` — Average, notable limitations
- `limited_value` — Significant limitations
- `poor_value` — Bottom tier, major limitations

## 📁 Project Structure

```
├── AGENTS.md                    # This file
├── CONTRIBUTING.md              # Contribution guidelines
├── README.md                    # Project overview
├── data/
│   ├── schema.json              # JSON Schema for validation
│   ├── sources.json             # Source URL registry
│   ├── 20-rankings.json         # $20 budget ranking data
│   ├── 10-rankings.json         # $10 budget ranking data
│   ├── free-rankings.json       # Free tier ranking data
│   ├── api-pricing.json         # API pricing data
│   └── README.md                # Data directory docs
├── docs/
│   ├── index.html               # SPA entry point
│   ├── content/
│   │   ├── 20-rankings.md       # $20 budget analysis
│   │   ├── 10-rankings.md       # $10 budget analysis
│   │   ├── free-rankings.md     # Free tier analysis
│   │   ├── api-pricing.md       # API pricing guide
│   │   └── about.md             # About the project
├── scripts/
│   ├── update-data.sh           # Data update automation
│   └── templates/               # Page templates
│       ├── README.md            # Template documentation
│       └── page.md.tmpl         # Single canonical template for all pages
└── .github/
    ├── ISSUE_TEMPLATE/
    └── pull_request_template.md
```

## 🚀 Deployment

This project is hosted on GitHub Pages from the `docs/` folder on the `main` branch. Any changes merged to `main` are automatically deployed.
