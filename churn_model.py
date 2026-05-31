import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import joblib

from sklearn.model_selection import train_test_split
from sklearn. metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier

# Connect to SQLite database
conn = sqlite3.connect("rfm.db")

# Load RFM table into a dataframe
df = pd. read_sql_query("SELECT * FROM rfm_table", conn)

# Create target variable for churn predction
# Churn = 1 (customer inactive for more than 90 days)
# Active = 0 (customer purchased within the last 90 days)
df["Churn"] = df["Recency"].apply(
    lambda x: 1 if x > 90 else 0
)

# Feature selection
X = df[
    [
        "Frequency",
        "Monetary",
        "F_score",
        "M_score"
    ]
]

# Target variable
y = df["Churn"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
model.fit(X_train, y_train)

# Make prediction
y_pred = model.predict(X_test)

# Predict churn probability
y_prob = model.predict_proba(X_test)
print("\nFirst 10 Churn Probalities:")
print(y_prob[:10])

# Evaluate model
print("Accuracy:", accuracy_score(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Create risk categories
risk_scores = y_prob[:, 1]
risk_level = []

for score in risk_scores:
    if score < 0.30:
        risk_level.append("Low Risk")
    elif score < 0.70:
        risk_level.append("Medium Risk")
    else:
        risk_level.append("High Risk")

print("\nSample Risk Levels:")
print(risk_level[:10])



# Display feature importance
feature_importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

feature_importance = feature_importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nFeature Importance:")
print(feature_importance)

# Create feature importance chart
plt.figure(figsize=(8,5))

plt.bar(
    feature_importance["Feature"],
    feature_importance["Importance"]
)
plt.title("Feature Importance for Customer Churn Prediction")
plt.xlabel("Features")
plt.ylabel("Importance Score")

plt.tight_layout()
plt.show()

# Save trained model
joblib.dump(model, "churn_model.pkl")
print("Model saved successfully")

# Close database connection
conn.close()

