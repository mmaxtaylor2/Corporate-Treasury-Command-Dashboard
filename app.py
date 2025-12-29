import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Corporate Treasury Command Dashboard", layout="wide")
st.title("Corporate Treasury Command Dashboard")

# Load data
cash = pd.read_csv("data/bank_balances.csv")
runway = pd.read_csv("data/runway_forecast.csv")
revolver = pd.read_csv("data/revolver_status.csv")
ladder = pd.read_csv("data/investments.csv")

# KPI Calculations
total_cash = cash["Balance"].sum()
avg_burn = abs(runway["Net"].mean())
runway_weeks = round((total_cash / avg_burn) * 4, 1)
revolver_util = (revolver["Drawn"].sum() / revolver["Total"].sum()) * 100

risk = "LOW"
if runway_weeks < 8 or revolver_util > 60: risk = "MEDIUM"
if runway_weeks < 4 or revolver_util > 80: risk = "HIGH"

# KPIs
c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Total Cash", f"${total_cash:,.0f}")
c2.metric("Runway (Weeks)", runway_weeks)
c3.metric("Revolver Utilization", f"{revolver_util:.1f}%")
c4.metric("Average Burn", f"${avg_burn:,.0f}")
c5.metric("Risk Level", risk)

# Chart
fig = px.bar(cash, x="Bank", y="Balance", color="Currency", title="Cash by Bank")
st.plotly_chart(fig, use_container_width=True)

