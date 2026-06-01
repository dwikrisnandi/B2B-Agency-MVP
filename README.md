# B2B Lead Gen & Outreach Architecture 🏢

> **Enterprise Value:** Automates the tedious process of B2B lead generation. This pipeline extracts decision-maker data and executes personalized initial outreach sequences, saving sales teams countless hours.

This implementation is specifically designed for **B2B Digital Agencies** and Sales teams that require structured, verifiable lead data.

## 🛠 Technical Highlights

*   **Strict Data Contracts (Pydantic):** B2B data is notoriously messy. This architecture utilizes `pydantic` to enforce strict validation rules on incoming data (e.g., mandatory URL formats, required company identifiers), ensuring no garbage data pollutes your CRM.
*   **Flat-File Data Sink (CSV):** Outputs verified leads directly into clean CSV files, which is the universal standard for easy import into tools like Salesforce, HubSpot, or Lemlist.
*   **Robust DOM Orchestration:** Powered by Playwright with advanced waiting strategies to handle dynamically loaded single-page applications (SPAs) common in modern business directories.
*   **Jitter-Based Rate Limiting:** Automates outreach with randomized micro-delays to perfectly simulate human typing and clicking behaviors, protecting sender reputation.

## 🚀 Deployment

```bash
# Install strict requirements
pip install -r requirements.txt

# Execute
python run_scraper.py --config config.json
```
