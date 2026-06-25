import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

st.title("📊 RFM Customer Dashboard")

# Load data
conn = sqlite3.connect("src/rfm.db")
rfm = pd.read_sql("SELECT * FROM rfm_table", conn)

# Show data table
st.subheader("RFM Table")
st.dataframe(rfm.head())

def plot_histogram(data, title, xlabel):
    fig, ax = plt.subplots()
    ax.hist(data, bins=20, color='skyblue', edgecolor='black')
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel("Number of Customers")
    return fig

# Frequency Distribution
st.subheader("Customer Frequency Distribution")
st.pyplot(plot_histogram(rfm["Frequency"], "Frequency Distribution", "Frequency"))

# Monetary Distribution
st.subheader("Revenue Distribution")
st.pyplot(plot_histogram(rfm["Monetary"], "Monetary Distribution", "Revenue"))