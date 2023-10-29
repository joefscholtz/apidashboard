import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout="wide")
st.header("Test")

#read
df = pd.read_csv("sales.csv",sep=";",decimal=",",index_col=1)

df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values(["Date"]).reset_index()
df["year-month"] = df["Date"].dt.strftime("%Y-%m")


month_selector = st.sidebar.selectbox("year-month",df["year-month"].unique())

df_displayed = df[df["year-month"] == month_selector].reset_index().copy()

col1,col2 = st.columns(2)

fig_date = px.bar(df_displayed,x="Date",y="Total",title="Faturamento por dia")
col1.plotly_chart(fig_date)

df_displayed

