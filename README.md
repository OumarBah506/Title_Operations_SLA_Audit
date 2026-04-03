# Title_Operations_SLA_Audit
An operational audit using Python, SQL, and Power BI to quantify mortgage funding SLA breaches and evaluate interest differential penalties.

# FCT Operational Audit: Reducing Financial Leakage in Mortgage Funding

## 📌 Project Overview
This project simulates a real-world operational audit of title insurance and mortgage funding files. As a Bilingual Title Officer, I identified internal bottlenecks that cause files to exceed a 21-day Service Level Agreement (SLA). When FCT misses this deadline due to internal backlogs, the company is often contractually responsible for covering the interest differential if the refinancing rate is lower than the actual rate; from the 22nd day until the funding date. In most cases, when a mortgage reaches its maturity and the mortgagee(s) decide 

This repository tracks the operational and financial impact of these processing delays across Canada, specifically benchmarking external refinancing and Quebec's notary workflow against top-tier lenders.

---

## 💼 Business Impact & ROI
* **Quantifying Financial Leakage:** Analyzed a transactional volume of 50,000 files to isolate specific instances where FCT absorbs penalty costs due to processing backlogs.
* **Benchmarking Operational Excellence:** Discovered that Fairstone’s pre-scheduled notary appointment model reduces turnaround to 2-3 days, serving as a zero-penalty model for the company.
* **Bilingual Resource Optimization:** Isolated high-frequency delay points in Quebec caused by missing lender instruction packages, providing data to justify automated early-triage routing.

---

## 🛠️ Technical Stack
* **Python:** Used for advanced synthetic data generation, applying complex real-world logic weighted to specific lenders, provincial rules, and operational workflow steps.
* **SQL:** Conducted localized querying to highlight extreme edge cases where missing lender files overlap with external payout delays. 
* **Power BI & DAX:** Built dynamic visualizations on highly raw source data. I intentionally kept the Python output raw so I could calculate the true `NETWORKDAYS` (excluding weekends) and execute conditional `SUMX` iterator formulas directly in Power BI to track continuous penalty leakage.

---

## 📊 Key Measures & Formulas (DAX)

### 1. Processing Business Days (Ignores Weekends)
```dax
Processing Business Days = 
NETWORKDAYS(
    'FCT_Operations_Data'[Date_Received], 
    'FCT_Operations_Data'[Date_Funded], 
    1
)
