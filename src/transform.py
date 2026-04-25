import pandas as pd
import datetime as dt

def transform(df):
    """
    Clean the dataset and create RFM customer segmentation.
    """

    # Standardize column names for consistency
    df.columns = df.columns.str.strip().str.lower()

    # Convert date columns to datetime format
    df["order_date"] = pd.to_datetime(df["order_date"], dayfirst=True, errors="coerce")

    # Convert sales to numeric
    df["sales"] = pd.to_numeric(df["sales"], errors="coerce")
    
    # Remove rows with missing critical values
    df = df.dropna(subset=["order_id", "order_date", "customer_name", "sales"])

    # Keep only positive sales
    df = df[df["sales"] > 0]

    # Set reference date as one day after the latest order date
    current_date = df["order_date"].max() + dt.timedelta(days=1)

    # Calculate customer-level RFM metrics
    rfm = df.groupby("customer_name").agg({
        "order_date": lambda x: (current_date - x.max()).days,
        "order_id": "count",
        "sales": "sum"
    })

    # Rename columns
    rfm.columns = ["Recency", "Frequency", "Monetary"]

    # Create RFM scores
    rfm["R_score"] = pd.qcut(
        rfm["Recency"],
        5,
        labels=[5, 4, 3, 2, 1]
    )

    rfm["F_score"] = pd.qcut(
        rfm["Frequency"].rank(method="first"),
        5,
        labels=[1, 2, 3, 4, 5]
    )

    rfm["M_score"] = pd.qcut(
        rfm["Monetary"],
        5,
        labels=[1, 2, 3, 4, 5]
    )

    # Combine individual scores into one RFM score
    rfm["RFM_score"] = (
        rfm["R_score"].astype(str)
        + rfm["F_score"].astype(str)
        + rfm["M_score"].astype(str)
    )

    # Define customer segmentation logic
    def segment_customer(row):
        if row["R_score"] == 4 and row["F_score"] >= 4 and row["M_score"] >= 4:
            return "Champions"
        elif row["F_score"] >= 4:
            return "Loyal Customers"
        elif row["R_score"] >= 4:
            return "Potential Loyalists"
        elif row["R_score"] <= 2:
            return "At Risk"
        else:
            return "others"

    # Apply segmentation
    rfm["Segment"] = rfm.apply(segment_customer, axis=1)

    return rfm
