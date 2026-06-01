# B2B Lead Gen & Outreach Automation 🚀

> **Business Value:** Automatically scrapes decision-makers from B2B directories and executes personalized connection requests, replacing hours of manual prospecting with a highly reliable, Dockerized system.

This project is tailored specifically for **Digital Marketing Agencies** or B2B SaaS companies that rely on high-volume outbound lead generation.

---

## 💼 Core Competencies

1. **Lead Scraper**: Targets B2B directories, navigates via "Load More" pagination, and extracts Decision Maker Names, LinkedIn URLs, and Company IDs.
2. **Sales Outreach Bot**: Logs into the sales account and executes targeted messages with human-like interaction patterns (±20% timing jitter) to bypass strict B2B rate limits.

---

## 🛠 Features

*   **Robust DOM Parsing**: Uses Playwright to handle JavaScript-heavy B2B portals.
*   **Anti-Bot Evading**: Incorporates advanced rate limiting (`requests_per_minute: 15`, `batch_pause: 15m`).
*   **Enterprise Architecture**: Configured via a central `config.json`. Docker-compose ready for VPS deployment.
*   **Audit Trail**: Logs all actions (sent, skipped, failed) to `logs/b2b_outreach_log.csv` using Loguru.

---

## 🚀 Deployment

```bash
# Setup Env Vars
export B2B_USERNAME="sales@agency.com"
export B2B_PASSWORD="secure_pass"

# Run via Docker
docker-compose up -d
```
