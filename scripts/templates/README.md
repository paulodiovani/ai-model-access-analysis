# Page Templates

This directory contains template specifications for the markdown content pages.

Each page in `docs/content/` is **data-driven** — the structured JSON files in `data/` are the source of truth. These templates define the markdown structure for each page type.

---

## Subscription Rankings Template ($10 / $20)

Applies to: `docs/content/20-rankings.md`, `docs/content/10-rankings.md`

```markdown
## **Comparative Analysis of AI Model Access Providers (Normalized to a $XX Budget)**

[introduction paragraph — scope, what the analysis covers, budget threshold]

> **Scope:** Only providers with recurring monthly subscriptions are included. Pay-as-you-go API providers are not listed here — see the [Free Rankings](#free-rankings.md) for those.

[ranking introduction sentence]

### **🥇 1. Provider (Plan)**
* **The Model Class:** [model class] (*[model names]*)
* **What your $XX gets you:** [budget outcome]
* **Why it's #1:** [analysis paragraph]

### **🥈 2. Provider (Plan)**
[same structure]

... repeat for all entries ...

## **Summary Comparison Table**

| Rank | Provider / Plan | Model Tier | $XX Budget Outcome | Limit Vulnerability |
|------|----------------|-----------|-------------------|-------------------|
| #1   | Provider       | Tier      | Outcome            | Vulnerability      |
| ...  | ...            | ...       | ...                | ...                |

💡 **The Strategic Takeaway:** [closing analysis]
```

### Key Points
- Medals for top 3: 🥇 🥈 🥉
- Rank 4+ uses `### **N. Provider (Plan)**`
- Each entry has exactly 3 bullet points
- Summary table matches the data in `data/XX-rankings.json`

---

## Free Rankings Template

Applies to: `docs/content/free-rankings.md`

```markdown
## **Free AI Model Access: A Developer's Guide**

[introduction paragraph]

### **Free Tier Rankings (Best to Worst for Small Projects)**

#### **🥇 1. Provider (Model)**
* **The Deal:** [one-line description]
* **What you get:** [capabilities]
* **Things to Consider:** **[Limit Type].** [detail]
* **Why it's #1:** [analysis]
* **Verdict:** [practical recommendation]

... repeat for all entries ...

---

## **Summary Table: Free Tier Overview**

| Rank | Provider | Top Free Model | Primary Limit | Main Limitation | Data Privacy |
|------|---------|---------------|--------------|----------------|-------------|
| #1   | Provider | Model         | Limit Type   | Description     | Privacy     |
| ...  | ...     | ...           | ...          | ...             | ...         |

💡 **The Bottom Line:** [closing analysis]
```

### Key Points
- Uses `####` (h4) for entries (one level deeper than paid rankings)
- Each entry has 5 bullet points including "Verdict"
- Summary table matches the data in `data/free-rankings.json`

---

## API Pricing Template

Applies to: `docs/content/api-pricing.md`

```markdown
## **API Pricing Guide for Production AI Applications**

[introduction paragraph — focus on production usage, value incentives]

> **Scope:** Prices are per million tokens unless noted. All prices sourced from official provider pages as of [date].

[ranking introduction sentence]

### **🥇 1. Provider**
* **Models:** [model list]
* **Flagship Pricing (per M tokens):** [pricing details]
* **Cached Input:** [cache discount details]
* **Batch API:** [batch discount if any]
* **Free Tier:** [free tier description]
* **Why it's #1:** [analysis]
* **Limitations:** [list of limitations]
* **Source:** [URL]

... repeat for all entries ...

---

## **Summary: Value Incentives Comparison**

| Rank | Provider | Best Discount | Free Credits/Tier | Batch |
|------|---------|--------------|-------------------|-------|
| #1   | Provider | Discount     | Free tier          | %    |
| ...  | ...     | ...          | ...                | ...  |

> **Key insight:** [insight about caching and value]

---

💡 **The Strategic Approach:** [closing analysis]

---

*Sources: All pricing data sourced from official provider pages in [month/year].*
```

### Key Points
- Uses `### **N. Provider**` format (no plan suffix for API providers)
- Each entry has 8 bullet points
- Summary table focuses on value incentives
- Source URLs included per entry

---
