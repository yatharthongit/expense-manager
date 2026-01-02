import streamlit as st
import requests
import pandas as pd
from datetime import datetime

API_URL= "http://localhost:8000"

def analytics():
    col1,col2=st.columns(2)
    with col1:
        start_date=st.date_input("Enter Start Date", datetime.today())
    with col2:
        end_date=st.date_input("Enter End Date", datetime.today())

    if st.button("Get Analytics"):
        payload={
            "start_date" : start_date.strftime("%Y-%m-%d"),
            "end_date" : end_date.strftime("%Y-%m-%d")
        }
        response = requests.post(f"{API_URL}/analytics",json=payload)
        response=response.json()
        df = pd.DataFrame({
            "Category":list(response.keys()),
            "Total":[response[category]["total"] for category in response],
            "Percentage":[response[category]["percentage"] for category in response]
        })

        df_sorted=df.sort_values("Total",ascending=False)
        st.title("Expense Breakdown By Category")
        st.bar_chart(data=df_sorted.set_index("Category")["Percentage"])

        df_sorted["Total"] = df_sorted["Total"].map("{:,.2f}".format)
        df_sorted["Percentage"] = df_sorted["Percentage"].map("{:,.2f}".format)
        st.table(df_sorted)