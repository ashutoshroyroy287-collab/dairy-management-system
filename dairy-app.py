import streamlit as st

st.set_page_config(page_title="Dairy Factory Management")

st.title("🥛 Dairy Factory Management System")

st.success("Welcome to Dairy Factory!")

st.subheader("Farmer Registration")
st.text_input("Farmer Name")
st.text_input("Mobile Number")

st.subheader("Milk Collection")
st.number_input("Milk Quantity (Litres)", min_value=0.0)
st.number_input("Rate per Litre (Rs)", min_value=0.0)