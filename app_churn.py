import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("churn_model.pkl")

st.title("Customer Churn Predictor")
st.markdown(
    """
    Predict customer churn risk using RFM analytics and Random Forest model.
    """
)

col1, col2 = st.columns(2)

with col1:
    frequency = st.number_input(
        "Purchase Frequency",
        min_value=1,
        value=10
    )

with col2:
    monetary = st.number_input(
        "Monetary Value",
        min_value=0.0,
        value=1000.0
    )

f_score = st.slider(
    "F Score",
    1,
    5,
    3
)

m_score = st.slider(
    "M Score",
    1,
    5,
    3
)

if st.button("Predict Churn Risk"):
    input_data = pd.DataFrame(
        {
            "Frequency":[frequency],
            "Monetary": [monetary],
            "F_score": [f_score],
            "M_score": [m_score]
        }
    )

    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)[0][1]

    st.subheader("Prediction Result")
    st.metric(
    "Churn Probabilty",
     f"{probability:.1%}"
)
    st.progress(float(probability))

    if probability < 0.30:
        risk = "🟢 Low Risk"
    elif probability < 0.70:
        risk = "🟡 Medium Risk"
    else: 
        risk = "🔴 High Risk"

    st.write(f"Risk Level: {risk}")
    st.subheader("Top Churn Driver")
    st.info(
        "Monetary value is the strongest predictor of churn risk based on the trained model."
    )
    st.subheader("Retention Recommendation")

    if probability < 0.30:
        st.success("Customer appears loyal. Maintain engagemnet and continiue regular communcation.")
    elif probability < 0.70:
        st.warning("Monitor this customer and consider targeted promotions or personalized offers.")
    else:
        st.error("High churn risk. Consider a retention campaign, loyalty incentive, or personalized discount.")

