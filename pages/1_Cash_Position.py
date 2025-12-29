import streamlit as st, pandas as pd, plotly.express as px
st.title("Cash Position")
df = pd.read_csv("data/bank_balances.csv")
st.metric("Total Cash", f"${df['Balance'].sum():,.0f}")
fig = px.bar(df, x="Bank", y="Balance", color="Currency")
st.plotly_chart(fig, use_container_width=True)
st.dataframe(df)

