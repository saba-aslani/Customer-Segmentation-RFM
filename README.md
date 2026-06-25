# Customer Segmentation & Business Analytics Platform
### RFM Analysis · ETL Pipeline · SQL · Statistical Testing · Streamlit Dashboard

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-red)](https://customer-segmentation-rfm-earfpdvjqosyqkkacpjnpu.streamlit.app/)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey)
![Streamlit](https://img.shields.io/badge/Dashboard-Streamlit-FF4B4B)

---

## Overview

End-to-end customer analytics project on the Global Superstore dataset (795 customers · 25,035 orders · $7.8M revenue). The pipeline segments customers into actionable RFM groups, validates results with statistical testing, and serves insights through a live Streamlit dashboard.

---

## Key Results

| Metric | Value |
|---|---|
| Total Revenue | $7,835,128 |
| Total Profit | $1,469,035 |
| Profit Margin | 18.75% |
| Avg Order Value | $312.96 |
| Total Customers Segmented | 795 |
| ANOVA F-Statistic (Category Profit) | 166.03 (p < 0.0001) |

**Segment Distribution:**

| Segment | Customers | Action |
|---|---|---|
| At Risk | 209 | Win-back campaigns |
| Loyal Customers | 199 | Loyalty rewards |
| Potential Loyalists | 169 | Onboarding sequences |
| Champions | 119 | VIP programs |
| Others | 99 | General nurturing |

---

## Project Architecture

```
Customer-Segmentation-RFM/
│
├── src/                        # ETL pipeline modules
│   ├── extract.py              # Load raw CSV data
│   ├── transform.py            # Clean data + compute RFM metrics
│   ├── load.py                 # Write results to SQLite
│   └── main.py                 # Pipeline entry point
│
├── sql/
│   └── rfm_queries.sql         # Segment analysis queries
│
├── rfm_customer_segmentation.ipynb   # Full analysis notebook
├── app_churn.py                      # Streamlit dashboard
├── rfm.db                      # SQLite database (ETL output)
├── SuperStoreOrders.csv        # Source dataset
└── requirements.txt
```

---

## Tech Stack

- **Python** — Pandas, NumPy, SciPy, Scikit-learn, Matplotlib, Seaborn
- **SQLite** — persistent RFM storage, queryable via SQL
- **Streamlit** — interactive live dashboard
- **Jupyter Notebook** — full exploratory analysis

---

## ETL Pipeline

A modular 3-stage pipeline processes raw transactions into segmented customer data:

1. **Extract** — loads raw transaction CSV
2. **Transform** — cleans data, engineers RFM metrics (Recency, Frequency, Monetary), assigns quintile scores and segment labels
3. **Load** — writes final `rfm_table` to SQLite (`rfm.db`) for downstream SQL analysis

---

## RFM Segmentation Logic

Customers are scored 1–5 per dimension (R: lower days = better; F/M: higher = better), then assigned to segments:

```python
if R >= 4 and F >= 4 and M >= 4  →  Champions
elif F >= 4                       →  Loyal Customers
elif R >= 4                       →  Potential Loyalists
elif R <= 2                       →  At Risk
else                              →  Others
```

---

## SQL Analysis

SQL queries run directly on the SQLite database to validate and extend the Python analysis:

- Customer count by segment
- Revenue and average spend per segment
- Top customers by lifetime value
- At-risk high-value customers

---

## Statistical Validation

**ANOVA — Profit by Category**

Tested whether profit differences across Technology, Office Supplies, and Furniture are statistically significant.

- **F-Statistic:** 166.03
- **p-Value:** < 0.0001 → significant at 99.9% confidence

**Finding:** Technology is statistically more profitable. Furniture shows high variance with frequent negative-profit orders.

**Discount Break-Even Analysis**

Profit turns negative at discounts above 20%. Recommendation: cap standard discounts at 15–20% and require approval for anything higher.

---

## Key Business Insights

- **Revenue concentration:** A small group of Champions and Loyal Customers drives a disproportionate share of revenue — prioritize retention over acquisition.
- **At-Risk opportunity:** 209 customers (the largest segment) have lapsed — a targeted win-back campaign represents the highest near-term revenue recovery opportunity.
- **Seasonality:** Q4 consistently spikes; Q1 is slow — inventory and staffing should align to this pattern.
- **Shipping efficiency:** Standard Class handles 30,755 orders at avg $19.97. Same Day is 115% more expensive and used in <7% of orders — review premium shipping eligibility.
- **Category strategy:** Technology generates the highest margin; Furniture shows structural profitability issues driven by deep discounting.

---

## Dashboard

Live dashboard allows users to explore customer segments, KPIs, and revenue trends interactively.

**[→ Open Live Demo](https://customer-segmentation-rfm-earfpdvjqosyqkkacpjnpu.streamlit.app/)**

To run locally:

```bash
git clone https://github.com/saba-aslani/Customer-Segmentation-RFM
cd Customer-Segmentation-RFM
pip install -r requirements.txt
python src/main.py        # Run ETL pipeline
streamlit run app.py      # Launch dashboard
```

---

## Author

**Saba Aslani** — Data Analyst · Data Engineer  
[GitHub](https://github.com/saba-aslani) · [LinkedIn](https://www.linkedin.com/in/saba-aslani/)
