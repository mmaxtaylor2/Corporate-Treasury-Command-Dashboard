import streamlit as st, pandas as pd, plotly.express as px
st.title("Investment Ladder")
df = pd.read_csv("data/investments.csv")
fig = px.bar(df, x="Maturity", y="Amount", color="Type")
st.plotly_chart(fig, use_container_width=True)
st.dataframe(df)

