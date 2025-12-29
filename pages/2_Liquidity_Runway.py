import streamlit as st, pandas as pd, plotly.express as px
st.title("Liquidity Runway")
df = pd.read_csv("data/runway_forecast.csv")
avg = abs(df["Net"].mean())
runway = (df["Ending Cash"].iloc[0] / avg) * 4
st.metric("Runway (weeks)", f"{runway:.1f}")
fig = px.line(df, x="Month", y="Ending Cash")
st.plotly_chart(fig, use_container_width=True)
st.dataframe(df)

