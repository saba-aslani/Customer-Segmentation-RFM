# Customer Segmentation, Churn Prediction & Business Analytics Platform (RFM + ETL + SQl + ML + Dashboard)

[![Live App](https://img.shields.io/badge/Live%20Demo-Streamlit-red)](https://customer-segmentation-rfm-earfpdvjqosyqkkacpjnpu.streamlit.app/)

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
<img width="770" height="850" alt="churn_app" src="https://github.com/user-attachments/assets/040a80fd-8f9b-4efc-87a5-2e375dd27abf" />

---

## Churn Prediction app
https://customer-segmentation-rfm-earfpdvjqosyqkkacpjnpu.streamlit.app/

---

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
├── churn_model.py
├── churn_model.pkl
├── app_churn.py
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
Dashboard (Streamlit)

An interactive Streamlit dashboard was developed to transform analytical results into actionable business insights.

Users can:
- Explore customer behavior metrics
- Predict churn probability in real time
- Classify customers into risk categories
- View retention recommendations
- Understand the main drivers behind churn predictions

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
Accuracy: ~0.77

Feature Importance:
1. Monetary Value
2. Purchase Frequency
3. M Score
4. F Score

Key Finding:
Monetary Value was identified as the strongest predictor of customer churn within the dataset.

Insight:
Customers who spend more and purchase frequently are less likely to churn.

---

## Interactive Churn Prediction App

The project includes a production-style prediction interface built with Streamlit.

Features:
- Real-time churn prediction
- Churn probability scoring
- Risk classification
- Retention recommendations
- Business-friendly outputs

Example Output:
Churn Probability: 43%
Risk Level: Medium Risk

Recommendation:
Monitor this customer and consider targeted promotions or personalized offers.

---

## Key Insights
* A small percentage of VIP customers generates a significant portion of total revenue.
* Customer behavior follows a long-tail distribution, requiring different marketing approaches for each segment.
* Automated ETL pipelines ensure that customer segments stay updated as new data arrives.
* SQL enables scalable analysis beyond Python
* Machine learning extends analysis into prediction
---

## Project Highlights
- Built an end-to-end ETL pipeline
- Developed RFM customer segmentation
- Designed and queried a SQLite database
- Created an interactive Streamlit dashboard
- Performed advanced SQL analysis
- Built a Random Forest churn prediction model
- Generated churn probabilities
- Implemented customer risk classification
- Created retention recommendation logic
- Visualized feature importance
- Delivered business-focused insights

---

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
streamlit run app_churn.py
```

5. **Run the churn model**:
```bash
python churn_model.py
```
---

## Author
**Saba Aslani**
