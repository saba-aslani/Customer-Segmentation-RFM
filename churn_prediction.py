import sqlite3
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


# 1. Load RFM data from SQLite database
conn = sqlite3.connect("rfm.db")
rfm = pd.read_sql("SELECT * FROM rfm_table", conn)
conn.close()


# 2. Create churn label
# Customers with high Recency are considered more likely to churn
churn_threshold = rfm["Recency"].median()
rfm["Churn"] = (rfm["Recency"] > churn_threshold).astype(int)


# 3. Select features and target
X = rfm[["Frequency", "Monetary"]]
y = rfm["Churn"]


# 4. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# 5. Train Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)


# 6. Make predictions
y_pred = model.predict(X_test)


# 7. Evaluate model performance
accuracy = accuracy_score(y_test, y_pred)

print("Churn Prediction Model Results")
print("--------------------------------")
print(f"Accuracy: {accuracy:.2f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# 8. Feature importance
feature_importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
}).sort_values(by="Importance", ascending=False)

print("\nFeature Importance:")
print(feature_importance)