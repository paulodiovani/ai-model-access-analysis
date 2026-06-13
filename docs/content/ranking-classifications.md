# Ranking Classifications & Data Points

This document defines the data points collected for each ranking category and the classification system used to evaluate providers.

## Data Points by Category

### $10 / $20 Subscription Rankings

These pages evaluate subscription-based AI access plans within a fixed monthly budget.

| Data Point | Type | Description |
|:---|:---|:---|
| `monthly_price_usd` | number | Actual monthly subscription cost in USD |
| `computational_value_usd` | number | Total estimated USD value of usage you get per month |
| `value_multiplier` | number | Ratio of computational value to price (e.g., 6.0 = 6x) |
| `limit_type` | enum | Kind of usage limit mechanism |
| `limit_description` | string | Human-readable limit details |
| `limit_vulnerability` | string | Worst-case scenario when limits are hit |
| `models` | array | Which models are included (name, tier, context window) |
| `model_class` | string | General class of models (e.g., "Open Flagships", "Proprietary Flagships") |
| `budget_outcome` | string | Short description of value within the budget |
| `ranking_class` | enum | Qualitative classification (see below) |
| `source_ids` | array | References to verified sources in `data/sources.json` |

### Free Rankings

This page evaluates free tiers from major AI providers.

| Data Point | Type | Description |
|:---|:---|:---|
| `primary_limit` | enum | Type of free limit (rate_limit, message_cap, context_window_limit, web_only, time_limited, model_gating, none) |
| `main_limitation` | string | Biggest practical constraint |
| `api_access` | boolean | Whether programmatic API access is available on the free tier |
| `data_privacy` | enum | How provider uses your data (used_for_training, varies, not_used) |
| `models` | array | What models are available for free (name, tier, context window) |
| `model_class` | string | General class of models |
| `ranking_class` | enum | Qualitative classification (see below) |
| `source_ids` | array | References to verified sources |

### API Pricing

This page compares pay-as-you-go API pricing for production usage.

| Data Point | Type | Description |
|:---|:---|:---|
| `pricing.flagship_input_per_m` | number | Flagship model input price per million tokens (USD) |
| `pricing.flagship_output_per_m` | number | Flagship model output price per million tokens (USD) |
| `pricing.cached_input_discount` | string | Cache hit discount percentage |
| `pricing.cached_input_price_per_m` | number | Cached input price per million tokens (USD) |
| `pricing.batch_discount` | string | Batch API discount (e.g., "50%") |
| `pricing.free_tier` | string | Free tier description |
| `pricing.platform_fee` | string | Platform/aggregator fee (e.g., "5.5%") |
| `pricing.models_detail` | array | Per-model pricing breakdown |
| `models` | array | Models available via API |
| `ranking_class` | enum | Qualitative classification (see below) |
| `source_ids` | array | References to verified sources |

## Classification Definitions

Entries are classified using the `ranking_class` field with a six-tier scale:

| Class | Meaning |
|:---|:---|
| `exceptional_value` | Top tier in category, best ROI, minimal trade-offs |
| `great_value` | Strong offering with minor trade-offs |
| `good_value` | Solid, competitive option |
| `moderate_value` | Average offering with notable limitations |
| `limited_value` | Significant limitations or trade-offs |
| `poor_value` | Bottom tier, major limitations, hard to recommend |

## Limit Types

Subscription rankings use a `limit_type` field to classify usage constraints:

| Limit Type | Description |
|:---|:---|
| `soft_value_cap` | Value-based cap that resets on a rolling schedule (e.g., $12 per 5 hours) |
| `hard_credit_pool` | Fixed credit pool that depletes and resets monthly |
| `message_cap` | Fixed number of messages per time window |
| `rate_limit` | Throttling under sustained load, no hard lockout |
| `compute_allocation` | Rolling compute-based budget that drains with usage |
| `context_window_limit` | Free tier limited primarily by small context window |
| `time_limited` | Free access that is promotional or time-bound |
| `web_only` | Access only through web/app interface, no API |
| `model_gating` | Flagship models locked behind higher subscription tiers |
| `none` | No meaningful usage limit |

## Model Tiers

Models are classified by quality tier:

| Tier | Description |
|:---|:---|
| `flagship` | Top-of-line model from the provider (e.g., GPT-5.5, Claude Opus 4.8, DeepSeek-V4) |
| `mid` | Mid-range model with good capability (e.g., Claude Sonnet, GPT-5.4, Grok Build) |
| `fast` | Optimized for speed/cost over quality (e.g., GPT-5.2 Instant, Flash models) |
| `free` | Free-tier specific model |
| `open` | Open-weights or open-source model |
