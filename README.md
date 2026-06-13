# AI Model Access Analysis

A comparative study of flagship-tier AI model access providers, normalized to $10 and $20 monthly budgets, plus free tiers and production API pricing.

## 🎯 Purpose
Flagship AI is incredibly powerful but can be expensive, creating a barrier for experimentation, education, and occasional use. This analysis provides a guide to the best low-cost alternatives and a calculation of the best price-per-token/period ratios available.

Beyond just the top tier, this project explores frontier alternatives—smaller, more specialized, or open-weights models that provide high utility at a fraction of the cost.

## 📊 Key Metrics
- **Computational Value:** The estimated raw API value delivered for the entry price.
- **Rate Limit Resilience:** How quickly a user hits a "lockout wall" during heavy usage.
- **Agentic Compatibility:** Suitability for autonomous loops that require massive context windows and frequent iterations.
- **API Cost Efficiency:** Per-token pricing, caching discounts, batch incentives, and free tier generosity for production workloads.

## 🗂️ Data-Driven Architecture
All pricing and ranking data lives in structured JSON files under `data/`, validated against a JSON Schema. The markdown pages are derived from this data.

```
data/
├── schema.json          # JSON Schema for validation
├── sources.json         # Centralized source URL registry
├── 20-rankings.json     # $20 budget ranking data
├── 10-rankings.json     # $10 budget ranking data
├── free-rankings.json   # Free tier ranking data
└── api-pricing.json     # API pricing data
```

Charts are generated from the data files using gnuplot and saved to `docs/charts/`.

## 🚀 Live Site
The rendered rankings and budget comparisons are available at:
👉 [https://paulodiovani.github.io/ai-model-access-analysis/](https://paulodiovani.github.io/ai-model-access-analysis/)

## 🛠️ Tech Stack
- **Data:** JSON (structured, schema-validated)
- **Content:** Markdown (generated from data)
- **Charts:** gnuplot
- **Frontend:** HTML5, Tailwind CSS, `marked.js`
- **Hosting:** GitHub Pages
