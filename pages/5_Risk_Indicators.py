import streamlit as st, pandas as pd
st.title("Risk Indicators")
cash = pd.read_csv("data/bank_balances.csv")["Balance"].sum()
runway = pd.read_csv("data/runway_forecast.csv")
burn = abs(runway["Net"].mean())
weeks = (cash/burn)*4
risk = "LOW" if weeks>=8 else "MEDIUM" if weeks>=4 else "HIGH"
st.metric("Risk Rating", risk)
st.metric("Runway (weeks)", f"{weeks:.1f}")

