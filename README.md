# Customer Segmentation and Business Analysis (RFM + ETL + SQl + ML + Dashboard)

## Overview
This project is an end-to-end data analysis and data engineering solution focused on customer segmentation using RFM (Recency, Frequency, Monetary). It implements a full workflow including data extraction, feature engineering, storage in a SQL database, Machine learning for churn prediction and an interactive dashboard for visualization.

---

## Business Objective
The goal of this project is to help businesses:
* Identify high-value customers (VIP and Loyal groups).
* Detect at-risk customers who haven't purchased recently.
* Understand revenue distribution across different segments.
* Support data-driven marketing and retention strategies.

---

## Dashboard preview
<img width="771" height="863" alt="Dashboard preview" src="https://github.com/user-attachments/assets/da736df0-e0fd-4e69-b9de-85dfbbcb6a70" />

## Project Architecture
```text
Customer-Segmentation-RFM/
│
├── SuperStoreOrders.csv
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── main.py
│
├── sql/
│   └── rfm_queries.sql
│
├── churn_prediction.py
├── app.py
├── rfm.db
├── rfm_customer_segmentation.ipynb
├── requirements.txt
└── README.md

```

---

## Tech Stack
* **Python** (Pandas, NumPy, SciPy)
* **SQLite** (Database Storage)
* **Streamlit** (Interactive Dashboard)
* **Matplotlib / Seaborn** (Visualization)
* **Scikit-learn**

---

## ETL Pipeline
The project is structured as a modular ETL pipeline:

1. **Extract**: Loads raw transaction data from CSV files.
2. **Transform**:
    * Cleans data and handles missing values.
    * Converts date columns and formats numerical data.
    * Calculates RFM metrics: **Recency**, **Frequency**, and **Monetary** value.
    * Generates RFM scores and assigns customer segments.
3. **Load**: Stores the final processed data into a SQLite database (`rfm.db`) for persistence.

---

## SQL Analysis
SQL queries were added to analyze the processed RFM data stored in SQLite.

The SQL layer includes:
* Customer count by segment
* Revenue by segment
* Average RFM metrics by segment
* Top customers by spending
* At-risk high-value customers

---

## RFM Segmentation
Customers are segmented based on their purchasing behavior:
* **Champion**: High value, frequent buyers, and very recent.
* **Loyal Customers**: Regular buyers with consistent frequency.
* **Potential Loyalists**: Recently active customers with potential to become loyal.
* **At Risk Customers**: Customers who haven't purchased recently (low recency score).
* **Others**: Customers with average behavior.

---

## Dashboard (Streamlit)
An interactive dashboard was built using Streamlit to visualize the results.

To run the dashboard locally:
```bash
streamlit run app.py
```

---

## Churn Prediction (Machine Learning)
A baseline churn prediction model was built using RFM features.

Approach:
* Churn defined using customer inactivity (Recency)
* To avoid data leakage, Recency was excluded from model features
* Model: Random Forest
* Features: Frequency, Monetary

Results:
* Accuracy: ~0.53
* Indicates realistic performance
* Monetary is the most important feature

Insight:
Customers who spend more and purchase frequently are less likely to churn.

---

## Key Insights
* A small percentage of VIP customers generates a significant portion of total revenue.
* Customer behavior follows a long-tail distribution, requiring different marketing approaches for each segment.
* Automated ETL pipelines ensure that customer segments stay updated as new data arrives.
* SQL enables scalable analysis beyond Python
* Machine learning extends analysis into prediction
---

## Project Highlights
* Built an end-to-end ETL pipeline
* Implemented RFM customer segmentation
* Stored data in SQLite database
* Developed a Streamlit dashboard
* Performed SQL-based analysis
* Built a churn prediction model
* Generated actionable business insights

## How to Run the Project

1. **Clone the repository**:
```bash
git clone <https://github.com/saba-aslani/Customer-Segmentation-RFM>
cd Customer-Segmentation-RFM
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Run the ETL pipeline**:
```bash
python src/main.py
```

4. **Launch the dashboard**:
```bash
streamlit run app.py
```

5. **Run the churn model**:
```bash
python churn_prediction.py
```
---

## Author
**Saba Aslani**
