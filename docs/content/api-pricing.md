## **API Pricing Guide for Production AI Applications**

This guide compares pay-as-you-go API pricing across AI model providers, focused on **production usage** — applications, services, and pipelines that call AI models programmatically at scale. What matters here is not just per-token cost, but **value incentives** — discounts, free credits, caching bonuses, and savings levers that reduce your effective spend.

> **Scope:** Prices are per million tokens unless noted. All prices sourced from official provider pages. Prices may change — always verify against the provider's current pricing page.

Here is the ranking from **most savings incentives (Best) to fewest savings levers (Worst)**.

### **🥇 1. DeepSeek (N/A)**

* **The Model Class:**  (*DeepSeek-V4-Pro, DeepSeek-V4-Flash*)
* **What you get:** 
* **Limits:** 
* **Limit Vulnerability:** 
* **Why it's #1:** DeepSeek publishes V4-Pro at $0.435/M cache-miss input, $0.003625/M cache-hit input, and $0.87/M output; V4-Flash is $0.14/$0.0028/$0.28. The page also notes a future 2x peak-hour pricing policy.

### **🥈 2. Z.ai / Zhipu AI (GLM) (N/A)**

* **The Model Class:**  (*GLM-5.1, GLM-5, GLM-4.7, GLM-4.7-Flash*)
* **What you get:** 
* **Limits:** 
* **Limit Vulnerability:** 
* **Why it's #2:** Triple incentive — 80% caching discount, 50% batch discount, AND a free unlimited model. The free tier alone (GLM-4.7-Flash) can handle serious workloads.

### **🥉 3. Google AI (Gemini) (N/A)**

* **The Model Class:**  (*Gemini 3.6 Flash, Gemini 3.5 Flash, Gemini 3 Flash*)
* **What you get:** 
* **Limits:** 
* **Limit Vulnerability:** 
* **Why it's #3:** Google currently highlights Gemini 3.6 Flash ($1.50/M input, $7.50/M output, $0.15/M cached input) with 50% Batch API pricing. Free-tier input and output remain available for supported models with data used to improve products.

### **4. Anthropic (Claude) (N/A)**

* **The Model Class:**  (*Claude Opus 4.7, Claude Sonnet 4.6*)
* **What you get:** 
* **Limits:** 
* **Limit Vulnerability:** 
* **Why it's #4:** Anthropic lists Sonnet 4.6 and Opus 4.7 with 90% prompt-cache read discounts and 50% batch processing savings.

### **5. OpenAI (N/A)**

* **The Model Class:**  (*GPT-5.6 Sol, GPT-5.6 Terra, GPT-5.6 Luna, GPT-5.5, GPT-5.4*)
* **What you get:** 
* **Limits:** 
* **Limit Vulnerability:** 
* **Why it's #5:** OpenAI added the GPT-5.6 family. Sol carries the same $5/$30 short-context flagship pricing as GPT-5.5 but adds cache-write and long-context tiers; Terra and Luna provide cheaper tiers. Cached input remains a 90% discount.

### **6. MiniMax (N/A)**

* **The Model Class:**  (*MiniMax-M3, MiniMax-M2.7*)
* **What you get:** 
* **Limits:** 
* **Limit Vulnerability:** 
* **Why it's #6:** 85% caching discount plus 50% promo pricing on M3. 1M context window. Native multimodal (text, image, video, audio).

### **7. xAI (Grok) (N/A)**

* **The Model Class:**  (*Grok 4.5, Grok 4.3, Grok Build 0.1*)
* **What you get:** 
* **Limits:** 
* **Limit Vulnerability:** 
* **Why it's #7:** xAI now lists Grok 4.5 as the latest text model, with 500K context and $2.00/M input, $0.30/M cached input, and $6.00/M output before long-context pricing.

### **8. Qwen / Alibaba Cloud (N/A)**

* **The Model Class:**  (*Qwen 3.7 Max, Qwen 3.7 Plus, Qwen 3.6 Flash, Qwen 3.5 Flash, Turbo*)
* **What you get:** 
* **Limits:** 
* **Limit Vulnerability:** 
* **Why it's #8:** Massive model family with tiered pricing for every use case. 50% batch discount. Also hosts third-party models through Alibaba Cloud Bailian.

### **9. OpenCode Zen (N/A)**

* **The Model Class:**  (*~49 models across all major providers*)
* **What you get:** 
* **Limits:** 
* **Limit Vulnerability:** 
* **Why it's #9:** Zero markup means you get provider-level pricing without the middleman. Volume discounts available. 4 free models with no limits. Single API key for every major provider.

### **10. Fireworks AI (N/A)**

* **The Model Class:**  (*100+ open and proprietary models*)
* **What you get:** 
* **Limits:** 
* **Limit Vulnerability:** 
* **Why it's #10:** ~90% caching discount plus 50% batch discount by default. Two-tier serving (Standard and Priority) lets you trade latency for cost.

### **11. Amazon Bedrock (N/A)**

* **The Model Class:**  (*18+ vendors (OpenAI, Anthropic, Mistral, DeepSeek, Meta, Cohere, etc.)*)
* **What you get:** 
* **Limits:** 
* **Limit Vulnerability:** 
* **Why it's #11:** Multiple pricing tiers that stack — Standard/Flex/Batch/Reserved. 50% batch discount. Enterprise features (Guardrails, Knowledge Bases, prompt routing).

### **12. OpenRouter (N/A)**

* **The Model Class:**  (*400+ models across 60+ providers*)
* **What you get:** 
* **Limits:** 
* **Limit Vulnerability:** 
* **Why it's #12:** 25+ free models and BYOK eliminates the platform fee entirely. Auto-routing picks the cheapest/fastest provider. No minimum spend.

### **13. Xiaomi MiMo (N/A)**

* **The Model Class:**  (*MiMo-V2.5 Pro, MiMo-V2.5*)
* **What you get:** 
* **Limits:** 
* **Limit Vulnerability:** 
* **Why it's #13:** Frontier-class model at extremely competitive prices. MiMo-V2.5 at ~$0.28/M blended rivals models costing 10x more. Available through Alibaba Cloud Bailian.

### **14. Together AI (N/A)**

* **The Model Class:**  (*100+ open-source models*)
* **What you get:** 
* **Limits:** 
* **Limit Vulnerability:** 
* **Why it's #14:** Best platform for open-source model hosting with fine-tuning (LoRA and full). GPU cluster rental (H100 at $4.99/hr). Dedicated endpoints for production.

### **15. Mistral (N/A)**

* **The Model Class:**  (*Medium 3.5, Large 3, Small 4, Magistral, Devstral*)
* **What you get:** 
* **Limits:** 
* **Limit Vulnerability:** 
* **Why it's #15:** Every model is open-weight — self-host for zero marginal cost. Small 4 at $0.10/$0.30 is excellent for high-volume tasks. Fine-tuning and classifier APIs included.

---

## **Summary Comparison Table**

| Rank | Provider | Best Discount | Free Credits/Tier | Batch |
| :---| :---| :---| :---| :--- |
| **\#1** | DeepSeek | 99% | Free chat at chat.deepseek.com (no API f |  |
| **\#2** | Z.ai / Zhipu AI (GLM) | 75-80% | GLM-4.7-Flash is completely free and unl | 50% |
| **\#3** | Google AI (Gemini) | 90% | Rate-limited free access on most Gemini  | 50% |
| **\#4** | Anthropic (Claude) | 90% | None for API | 50% |
| **\#5** | OpenAI | 90% | None for API | available |
| **\#6** | MiniMax | 85% | None for API. Token Plan subscription at |  |
| **\#7** | xAI (Grok) | 85% | $25/mo free credits for team orgs | 20-50% |
| **\#8** | Qwen / Alibaba Cloud | varies | 1M tokens per model for 90 days (China m | 50% |
| **\#9** | OpenCode Zen | passes through | 4 free models (MiMo-V2.5 Free, North Min |  |
| **\#10** | Fireworks AI | 90% | $1 in free credits on signup | 50% |
| **\#11** | Amazon Bedrock | select models | Free tier for select models during initi | 50% |
| **\#12** | OpenRouter | passes through | 25+ free models (50 requests/day) |  |
| **\#13** | Xiaomi MiMo | not documented | 1M tokens for 90 days via Alibaba Cloud  |  |
| **\#14** | Together AI | select models | Not clearly defined (signup credits may  | available |
| **\#15** | Mistral | none | Leanstral (Lean 4 coding) is free. No ge |  |

💡 **The Strategic Takeaway:** Most production apps should **cache aggressively** — a 90% cache discount on Claude or GPT can be cheaper than a budget model without caching. Batch eligible workloads for 50% off. Use free tiers for experimentation. Route simple tasks to cheap models and escalate complex reasoning to frontier models only when needed. The best provider is the one whose incentives match your usage pattern.

---

*Sources: All data sourced from official provider pages as of 2026-08-01. Prices may change — always verify against the provider's current pricing page.*
