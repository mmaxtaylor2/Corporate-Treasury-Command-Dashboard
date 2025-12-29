import streamlit as st, pandas as pd
st.title("Revolver Status")
df = pd.read_csv("data/revolver_status.csv")
util = (df["Drawn"].sum() / df["Total"].sum()) * 100
st.metric("Utilization", f"{util:.1f}%")
st.dataframe(df)

