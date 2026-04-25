from extract import extract
from transform import transform
from load import load

# Path to the dataset
file_path = "SuperStoreOrders.csv"

# Run ETL pipeline
df = extract(file_path)
rfm = transform(df)
load(rfm)

print("ETL pipeline executed successfully.")
