!pip install streamlit

import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("property_data.csv")

# Title
st.title("🏡 Property Deal Analyzer")

# User input
postcode = st.selectbox("Select a postcode", df["postcode"].unique())
price = st.number_input("Purchase price (£)", value=250000, step=1000)
monthly_rent = st.number_input("Monthly rent (£)", value=1200, step=50)

# Fetch area averages
area_data = df[df["postcode"] == postcode].iloc[0]
avg_price = area_data["avg_price"]
avg_rent = area_data["avg_rent"]

# Metrics
annual_rent = monthly_rent * 12
gross_yield = round((annual_rent / price) * 100, 2)
monthly_cashflow = monthly_rent - (0.05 * price / 12)  # Assume 5% annual costs
roi = round((monthly_cashflow * 12) / (0.25 * price) * 100, 2)  # 25% deposit

# Display
st.subheader("📊 Deal Metrics")
st.write(f"**Gross Yield:** {gross_yield}%")
st.write(f"**Monthly Cashflow:** £{monthly_cashflow:.2f}")
st.write(f"**ROI (est. on deposit):** {roi}%")

# Area comparison
st.subheader("📍 Area Averages")
st.write(f"**Avg Price in {postcode}:** £{avg_price}")
st.write(f"**Avg Rent in {postcode}:** £{avg_rent}")