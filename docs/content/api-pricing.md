## **API Pricing Guide for Production AI Applications**

This guide compares pay-as-you-go API pricing across AI model providers, focused on **production usage** — applications, services, and pipelines that call AI models programmatically at scale. What matters here is not just per-token cost, but **value incentives** — discounts, free credits, caching bonuses, and savings levers that reduce your effective spend.

> **Scope:** Prices are per million tokens unless noted. All prices sourced from official provider pages as of June 2026. Prices may change — always verify against the provider's current pricing page.

Here is the ranking from **most savings incentives (Best)** to **fewest savings levers (Worst)**.

### **🥇 1\. DeepSeek**

* **Models:** DeepSeek-V4-Flash, DeepSeek-V4-Pro (1M context, 384K output)
* **Flagship Pricing (per M tokens):** V4-Pro: $0.435 input / $0.87 output · V4-Flash: $0.14 input / $0.28 output
* **Cached Input:** $0.003625/M (V4-Pro) · $0.0028/M (V4-Flash) — **up to 99% off**
* **Free Tier:** Free chat at chat.deepseek.com (no API free tier)
* **Why it's \#1:** The most extreme caching discount in the industry — 99% off cached input makes repeated prompts nearly free. V4-Pro competes with GPT-5.4 and Claude Sonnet on reasoning benchmarks. Cache hits at $0.003/M are unmatched.
* **Limitations:** Only two models. No built-in tooling, guardrails, or enterprise features. Based in China — data sovereignty may be a concern. API only (no managed platform).
* **Source:** https://api-docs.deepseek.com/quick_start/pricing

### **🥈 2\. Z.ai / Zhipu AI (GLM)**

* **Models:** GLM-5.1, GLM-5, GLM-4.7, GLM-4.7-Flash (128K–1M context)
* **Flagship Pricing (per M tokens):** GLM-5.1: $0.83 input / $3.33 output · GLM-5: $0.56 input / $2.50 output · GLM-4.7-Flash: **Free**
* **Cached Input:** Available — cache hits at **75–80% off**. Cache storage free during promo.
* **Batch API:** **50% off** on supported models
* **Free Tier:** GLM-4.7-Flash is **completely free and unlimited**. New user credits on signup.
* **Why it's \#2:** Triple incentive — 80% caching discount, 50% batch discount, AND a free unlimited model. The free tier alone (GLM-4.7-Flash) can handle serious workloads. Cache storage is currently free during their promo.
* **Limitations:** Prices in CNY. Platform primarily Chinese-language. GLM-5.1 pricing doubles above 32K context. Limited international ecosystem support.
* **Source:** https://open.bigmodel.cn/pricing

### **🥉 3\. Google AI (Gemini)**

* **Models:** Gemini 3.1 Pro, 3.5 Flash, 3 Flash, 2.5 Pro (1M+ context) · Gemma 4 (open-source, free) · Imagen 4 (image gen) · Veo 3.1 (video gen) · Lyria 3 (music gen) · Gemini Embedding
* **Flagship Pricing (per M tokens):** 3.1 Pro: $2.00 input / $12.00 output · 3.5 Flash: $1.50 input / $9.00 output · 3 Flash: $0.50 input / $3.00 output · Gemma 4: Free
* **Cached Input:** **Up to 90% off** on Flash models
* **Batch API:** **50% off**
* **Free Tier:** Rate-limited free access on most Gemini models. Gemma 4 (open-source) is free.
* **Why it's \#3:** Stacked incentives — 90% caching discount on Flash, 50% batch discount, generous free tier, and open-source Gemma 4. Multiple discount levers that compound. Media generation models (Imagen, Veo, Lyria) included.
* **Limitations:** Free-tier data used for model improvement. Prices double above 200K context on Pro models. API behavior can change between preview versions.
* **Source:** https://ai.google.dev/gemini-api/docs/pricing

### **4\. Anthropic (Claude)**

* **Models:** Claude Fable 5, Opus 4.8, Sonnet 5 (200K context)
* **Flagship Pricing (per M tokens):** Fable 5: $10.00 input / $50.00 output · Opus 4.8: $5.00 input / $25.00 output · Sonnet 5: $2.00 input / $10.00 output (intro pricing through Aug 2026, then $3/$15)
* **Cached Input:** Read: **90% off**. Write: 25% premium for persistent cache.
* **Batch API:** **50% off**
* **Free Tier:** None for API
* **Why it's \#4:** 90% cached read discount is among the best. Unique persistent cache (write-cache) pays for itself in high-context recurring workloads — cache once, reuse across requests. Best-in-class for coding and structured reasoning.
* **Limitations:** Most expensive output pricing (Opus at $25/M). 200K context limit. No free API tier. Cache write adds cost if context changes frequently.
* **Source:** https://www.anthropic.com/pricing

### **5\. OpenAI**

* **Models:** GPT-5.5, GPT-5.5-pro, GPT-5.4, GPT-5.4-mini (128K context)
* **Flagship Pricing (per M tokens):** GPT-5.5: $5.00 input / $30.00 output · GPT-5.5-pro: $30.00 input / $180.00 output · GPT-5.4: $2.50 input / $15.00 output · GPT-5.4-mini: $0.75 input / $4.50 output
* **Cached Input:** **90% off**
* **Batch API:** Available for non-urgent workloads
* **Free Tier:** None for API
* **Why it's \#5:** 90% cached input discount brings GPT-5.4 to $0.25/M input — competitive with cheap models for repeated prompts. The most polished API ecosystem with best tool calling and structured output.
* **Limitations:** Most expensive per-token pricing. GPT-5.5 at $30/M output is prohibitive for high-volume use. No free API tier.
* **Source:** https://developers.openai.com/api/docs/pricing

### **6\. MiniMax**

* **Models:** MiniMax-M3, M2.7 (1M context, multimodal)
* **Flagship Pricing (per M tokens):** M3: $0.29 input / $1.17 output (promo 50% off) · M2.7: $0.29 input / $1.17 output
* **Cached Input:** M3 cache read: $0.06/M — **up to 85% off**
* **Batch API:** Not documented
* **Free Tier:** None for API. Token Plan subscription available ($14.99/mo).
* **Why it's \#6:** 85% caching discount plus 50% promo pricing on M3. 1M context window. Native multimodal (text, image, video, audio). Token Plan subscription at $14.99/mo for unlimited-style access.
* **Limitations:** Prices in CNY — international billing may vary. M3 promo pricing may not be permanent. Limited international ecosystem.
* **Source:** https://platform.minimaxi.com/docs/guides/pricing-billing

### **7\. xAI (Grok)**

* **Models:** Grok 4.3, Grok Build 0.1, Grok 4.20 variants (1M context)
* **Flagship Pricing (per M tokens):** Grok 4.3: $1.25 input / $2.50 output · Grok Build 0.1 (coding): $1.00 input / $2.00 output
* **Cached Input:** $0.20/M — **84% off**
* **Batch API:** **20–50% off**
* **Free Tier:** **$25/mo free credits** for team orgs
* **Why it's \#7:** $25/mo free credits is the strongest recurring free credit among Western providers. 84% caching discount and batch savings stack on top. Built-in tools via API: web search, X/Twitter search, code execution.
* **Limitations:** Smaller ecosystem. Tool calls cost extra ($5/1K calls). Newer API with less third-party integration support.
* **Source:** https://docs.x.ai/developers/pricing

### **8\. Qwen / Alibaba Cloud**

* **Models:** Qwen 3.7 Max, 3.7 Plus, 3.6 Flash, 3.5 Flash, Turbo (1M context on flagship)
* **Flagship Pricing (per M tokens):** 3.7 Max: $1.67 input / $5.00 output · 3.7 Plus: $0.28 input / $1.11 output · 3.5 Flash: $0.028 input / $0.28 output · Turbo: $0.042 input / $0.083 output
* **Cached Input:** Available on most models (discount varies)
* **Batch API:** **50% off** on supported models
* **Free Tier:** 1M tokens per model for 90 days (China mainland)
* **Why it's \#8:** Massive model family with tiered pricing for every use case. 50% batch discount across the board. Also hosts third-party models (DeepSeek, Kimi, GLM, MiniMax, MiMo) through Alibaba Cloud Bailian.
* **Limitations:** Prices in CNY — international billing may vary. Free tier limited to China mainland. Some models have context-length tiered pricing that doubles above 256K.
* **Source:** https://help.aliyun.com/zh/model-studio/models

### **9\. OpenCode Zen**

* **Models:** ~49 models across all major providers — GPT 5.5/5.5-pro/5.4/5.4-mini (17 OpenAI models), Claude Fable 5/Opus 4.8/Sonnet 5/Haiku (11 Anthropic models), Gemini 3.5 Flash/3.1 Pro (3 Google models), Qwen 3.7 Max/Plus, DeepSeek V4 Pro/Flash, GLM 5.1, MiniMax M2.7, Kimi K2.6, Grok Build 0.1, plus free models (MiMo-V2.5 Free, DeepSeek V4 Flash Free, Nemotron 3 Ultra Free)
* **Flagship Pricing (per M tokens):** **Zero-markup pass-through** — DeepSeek V4-Flash/MiMo-V2.5: $0.28 · DeepSeek V4-Pro: $0.87 · Qwen 3.7 Plus: $3.00 · Kimi K2.6: $4.00 · Qwen 3.7 Max: $7.50 · GPT-5.4: $2.50/$15.00 · Claude Sonnet 5: $2.00/$10.00 (intro)
* **Cached Input:** Passes through provider caching
* **Batch API:** Not available
* **Free Tier:** **4 free models** (MiMo-V2.5 Free, North Mini Code Free, Nemotron 3 Ultra Free, DeepSeek V4 Flash Free). $20 minimum deposit for paid models.
* **Why it's \#9:** Zero markup means you get provider-level pricing without the middleman. **Volume discounts** available. 4 free models with no limits. Single API key for every major provider — Western, Chinese, and open-source.
* **Limitations:** $20 minimum top-up. Not a model provider — passes through underlying pricing. No batch API.
* **Source:** https://opencode.ai/zen

### **10\. Fireworks AI**

* **Models:** 100+ open and proprietary models (DeepSeek, Qwen, Kimi, GLM, MiniMax, etc.)
* **Flagship Pricing (per M tokens):** DeepSeek V4 Pro: $1.74 input / $3.48 output · DeepSeek V4 Flash: $0.14 input / $0.28 output · Qwen 3.6 Plus: $0.50 input / $3.00 output
* **Cached Input:** **50% off** by default on all text/vision models
* **Batch API:** **50% off** serverless pricing
* **Free Tier:** **$1 in free credits** on signup
* **Why it's \#10:** 50% off both caching AND batch by default. Two-tier serving (Standard and Priority) lets you trade latency for cost. Strong open-source model support. On-demand GPU deployments.
* **Limitations:** Markup over direct provider pricing (e.g., DeepSeek V4 Pro at $1.74 vs $0.435 direct). Standard tier has variable latency.
* **Source:** https://fireworks.ai/pricing

### **11\. Amazon Bedrock**

* **Models:** 18+ vendors (OpenAI, Anthropic, Mistral, DeepSeek, Meta, Cohere, etc.)
* **Flagship Pricing (per M tokens):** DeepSeek v3.2: $0.62 input / $1.85 output · Mistral Large 3: $0.50 input / $1.50 output · GPT-5.4: $2.75 input / $16.50 output
* **Cached Input:** Available on select models
* **Batch API:** **50% off** on-demand for select models
* **Flex Tier:** ~**20% cheaper** than Standard (non-urgent workloads)
* **Free Tier:** Free tier available for select models during initial period
* **Why it's \#11:** Multiple pricing tiers that stack — Standard/Flex/Batch/Reserved. 50% batch discount. Enterprise features (Guardrails, Knowledge Bases, prompt routing). Deepest AWS integration.
* **Limitations:** Highest markup of any infrastructure provider. Complex pricing structure. Provisioned Throughput requires commitment.
* **Source:** https://aws.amazon.com/bedrock/pricing/

### **12\. OpenRouter**

* **Models:** 400+ models across 60+ providers (OpenAI, Anthropic, Google, DeepSeek, Mistral, etc.)
* **Flagship Pricing:** Provider pricing + **5.5% platform fee**. BYOK (bring your own keys) eliminates the fee — 1M free requests/month.
* **Cached Input:** Passes through provider caching
* **Batch API:** Not available
* **Free Tier:** **25+ free models** (50 requests/day)
* **Why it's \#12:** 25+ free models and BYOK eliminates the platform fee entirely. Auto-routing picks the cheapest/fastest provider. No minimum spend. Single API for every model on the market.
* **Limitations:** 5.5% fee adds up at scale (eliminated with BYOK). Free models have low rate limits. Routing can introduce latency variability.
* **Source:** https://openrouter.ai/pricing

### **13\. Xiaomi MiMo**

* **Models:** MiMo-V2.5 Pro, MiMo-V2.5 (1M context, 42B active params)
* **Flagship Pricing (per M tokens):** V2.5 Pro: ~$0.87 · V2.5: ~$0.28 (blended via Alibaba Cloud Bailian)
* **Cached Input:** Not separately documented
* **Batch API:** Not documented
* **Free Tier:** 1M tokens for 90 days via Alibaba Cloud for new users
* **Why it's \#13:** Frontier-class model at extremely competitive prices. MiMo-V2.5 at ~$0.28/M blended rivals models costing 10x more. Available through Alibaba Cloud Bailian.
* **Limitations:** No caching or batch incentives documented. No direct API — available only through Alibaba Cloud or third-party routers. Newer platform with smaller ecosystem.
* **Source:** https://mimo.xiaomi.com (via Alibaba Cloud Bailian)

### **14\. Together AI**

* **Models:** 100+ open-source models (DeepSeek, Qwen, Kimi, GLM, MiniMax, Llama, etc.)
* **Flagship Pricing (per M tokens):** DeepSeek V4 Pro: $2.10 input / $4.40 output · Qwen 3.6 Plus: $0.50 input / $3.00 output · LFM2 24B: $0.03 input / $0.12 output
* **Cached Input:** Available on select models (e.g., DeepSeek V4 Pro cached: $0.20/M)
* **Batch API:** Available at lower rates
* **Free Tier:** Not clearly defined (signup credits may apply)
* **Why it's \#14:** Best platform for open-source model hosting with fine-tuning (LoRA and full). GPU cluster rental (H100 at $4.99/hr). Dedicated endpoints for production workloads.
* **Limitations:** Markup over direct provider pricing. Limited caching/batch incentives compared to competitors.
* **Source:** https://www.together.ai/pricing

### **15\. Mistral**

* **Models:** Medium 3.5, Small 4 (all open-weight — MIT/Apache 2.0)
* **Flagship Pricing (per M tokens):** Medium 3.5: $2.00 input / $6.00 output · Small 4: $2.00 input / $6.00 output
* **Cached Input:** Not available
* **Batch API:** Not available
* **Free Tier:** Leanstral (Lean 4 coding) is free. No general free API tier.
* **Why it's \#15:** Every model is open-weight — self-host for zero marginal cost. Small 4 at $0.10/$0.30 is excellent for high-volume tasks. Fine-tuning and classifier APIs included.
* **Limitations:** No caching or batch discounts. Fewest savings levers of any provider on this list. Self-hosting requires significant GPU resources.
* **Source:** https://mistral.ai/pricing

---

## **Summary: Value Incentives Comparison**

| Rank | Provider | Best Discount | Free Credits/Tier | Batch |
| :--- | :--- | :--- | :--- | :--- |
| **\#1** | **DeepSeek** | 99% cache | Free chat | — |
| **\#2** | **Z.ai** | 80% cache | Unlimited free model | 50% |
| **\#3** | **Google** | 90% cache | Free tier + Gemma 4 | 50% |
| **\#4** | **Anthropic** | 90% cache | — | 50% |
| **\#5** | **OpenAI** | 90% cache | — | Yes |
| **\#6** | **MiniMax** | 85% cache | — | — |
| **\#7** | **xAI** | 84% cache | $25/mo credits | 50% |
| **\#8** | **Qwen** | Varies | 1M tokens/90d | 50% |
| **\#9** | **OpenCode Zen** | 0% markup | 4 free models | — |
| **\#10** | **Fireworks** | 50% cache | $1 credits | 50% |
| **\#11** | **Bedrock** | 20% Flex | Free initial | 50% |
| **\#12** | **OpenRouter** | BYOK fee waiver | 25+ free models | — |
| **\#13** | **MiMo** | Low base price | 1M tokens/90d | — |
| **\#14** | **Together** | Select caching | Signup credits | Yes |
| **\#15** | **Mistral** | Open-weight | Leanstral free | — |

> **Key insight:** The cheapest per-token price doesn't always mean the best value. Providers like Anthropic and OpenAI offer 90% caching discounts that make repeated prompts nearly as cheap as budget providers — with superior model quality. Always factor in your caching hit rate and batch eligibility when comparing.

---

💡 **The Strategic Approach:** Most production apps should **cache aggressively** — a 90% cache discount on Claude or GPT can be cheaper than a budget model without caching. Batch eligible workloads for 50% off. Use free tiers for experimentation. Route simple tasks to cheap models and escalate complex reasoning to frontier models only when needed. The best provider is the one whose incentives match your usage pattern.

---

*Sources: All pricing data sourced from official provider pages in June 2026.*
