import streamlit as st
from analytics_ui import analytics
from update_data import update

st.title("Expense Management System")

tab1, tab2 = st.tabs(["Add/Update","Analytics"])

with tab1:
    update()
with tab2:
    analytics()