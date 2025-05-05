import streamlit as st
import pandas as pd

df = pd.read_csv('data/retail_sales_features.csv')
st.title("Retail Sales Dashboard")
st.line_chart(df.groupby('Date')['Revenue'].sum())
