import streamlit as st
import requests
from datetime import datetime

API_URL= "http://localhost:8000"

def update():
    selected_date = st.date_input("Enter Date", datetime(2024, 8, 3), label_visibility="collapsed")
    response = requests.get(f"{API_URL}/expenses/{selected_date}")

    if response.status_code == 200:
        existing_expenses = response.json()
    else:
        st.error("Failed to retrieve expenses")
        existing_expenses = []

    categories = ["Rent", "Food", "Shopping", "Entertainment", "Other"]
    with st.form(key=f"expense_form_{selected_date}"):
        column1, column2, column3 = st.columns(3)
        with column1:
            st.text("Amount")

        with column2:
            st.text("Category")

        with column3:
            st.text("Notes")

        expenses = []
        for i in range(5):

            if i < len(existing_expenses):
                amount = existing_expenses[i]["amount"]
                category = existing_expenses[i]["category"]
                notes = existing_expenses[i]["notes"]
            else:
                amount = 0.0
                category = "Shopping"
                notes = ""

            column1, column2, column3 = st.columns(3)
            with column1:
                amount_input = st.number_input(label="Amount", min_value=0.0, step=1.0, value=amount,
                                               key=f"amount_{selected_date}_{i}", label_visibility="collapsed")
            with column2:
                category_input = st.selectbox(label="Category", options=categories, index=categories.index(category),
                                              key=f"category_{selected_date}_{i}", label_visibility="collapsed")
            with column3:
                notes_input = st.text_input(label="Note", value=notes, key=f"notes_{selected_date}_{i}",
                                            label_visibility="collapsed")

            expenses.append({
                "amount": amount_input,
                "category": category_input,
                "notes": notes_input
            })

        submit_button = st.form_submit_button()
        if submit_button:
            filtered_expenses = [expense for expense in expenses if expense['amount'] > 0]
            requests.post(f"{API_URL}/expenses/{selected_date}", json=filtered_expenses)
            if response.status_code == 200:
                st.success("Successfully updated expenses")
            else:
                st.error("Failed to update expenses")