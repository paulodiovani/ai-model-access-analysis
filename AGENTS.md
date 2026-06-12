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

## 📁 Project Structure

- `docs/content/20-rankings.md` — $20 budget analysis
- `docs/content/free-rankings.md` — Free tier analysis
- `docs/content/about.md` — About the project
- `docs/index.html` — SPA entry point
- `.github/ISSUE_TEMPLATE/` — Issue templates
- `.github/pull_request_template.md` — PR template
- `CONTRIBUTING.md` — Contribution guidelines

## 🚀 Deployment

This project is hosted on GitHub Pages from the `docs/` folder on the `main` branch. Any changes merged to `main` are automatically deployed.
