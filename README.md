# Customer Segmentation and Business Analysis (RFM + ETL + Dashboard)

## Overview
This project is an end-to-end data analysis and data engineering solution focused on customer segmentation using RFM (Recency, Frequency, Monetary). It implements a full workflow including data extraction, feature engineering, storage in a SQL database, and an interactive dashboard for visualization.

---

## Business Objective
The goal of this project is to help businesses:
* Identify high-value customers (VIP and Loyal groups).
* Detect at-risk customers who haven't purchased recently.
* Understand revenue distribution across different segments.
* Support data-driven marketing and retention strategies.

---

## Project Architecture
```text
Customer-Segmentation-RFM/
│
├── data/
│   └── SuperStoreOrders.csv
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── main.py
│
├── app.py
├── rfm.db
├── rfm_customer_segmentation.ipynb
└── README.md
```

---

## Tech Stack
* **Python** (Pandas, NumPy, SciPy)
* **SQLite** (Database Storage)
* **Streamlit** (Interactive Dashboard)
* **Matplotlib / Seaborn** (Visualization)

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

## Key Insights
* A small percentage of VIP customers generates a significant portion of total revenue.
* Customer behavior follows a long-tail distribution, requiring different marketing approaches for each segment.
* Automated ETL pipelines ensure that customer segments stay updated as new data arrives.

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
streamlit run app.py
```

---

## Author
**Saba Aslani**
