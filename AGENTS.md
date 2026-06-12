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

### One Branch Per Change
Create a new branch for each logical change. Never commit directly to `main`.

## 🔍 Verification Rules

### ALWAYS Verify Pricing and Limits
**This is the most important rule.** Never write or update pricing, token limits, or rate limits from memory or training data. Always:

1. **Fetch the provider's official documentation** or pricing page from the live website
2. **Cross-reference** the specific price, limit, or feature against the source
3. **Include the source URL** in your commit message or PR description

This project's value depends on factual accuracy. Stale or incorrect information is worse than no information at all.

### Providers to Verify Against
- OpenAI: https://openai.com/pricing
- Anthropic: https://www.anthropic.com/pricing
- Google: https://ai.google.dev/pricing
- OpenRouter: https://openrouter.ai/models
- Hugging Face: https://huggingface.co/pricing
- Check each provider's official docs page for the most current limits

## 📁 Project Structure

- `docs/content/rankings.md` — $20 budget analysis
- `docs/content/free-rankings.md` — Free tier analysis
- `docs/content/about.md` — About the project
- `docs/index.html` — SPA entry point
- `.github/ISSUE_TEMPLATE/` — Issue templates
- `.github/pull_request_template.md` — PR template
- `CONTRIBUTING.md` — Contribution guidelines

## 🚀 Deployment

This project is hosted on GitHub Pages from the `docs/` folder on the `main` branch. Any changes merged to `main` are automatically deployed.
