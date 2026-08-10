
import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("ecommerce_revenue_model.pkl")

# Streamlit page configuration
st.set_page_config(
    page_title="E-Commerce Revenue Predictor",
    page_icon="🛒"
)

# App title
st.title("🛒 E-Commerce Revenue Predictor")

# App description
st.write("Enter the order details below to predict the expected revenue.")

# Input: quantity
quantity = st.number_input(
    "Quantity",
    min_value=1,
    max_value=100,
    value=1
)

# Input: unit price
unit_price = st.number_input(
    "Unit Price",
    min_value=0.0,
    value=100.0
)

# Input: discount
discount = st.number_input(
    "Discount",
    min_value=0.0,
    max_value=1.0,
    value=0.10
)

# Input: delivery days
delivery_days = st.number_input(
    "Delivery Days",
    min_value=1,
    max_value=30,
    value=5
)

# Input: customer rating
customer_rating = st.number_input(
    "Customer Rating",
    min_value=1.0,
    max_value=5.0,
    value=3.0
)

# Create a button for prediction
if st.button("Predict Revenue"):

    # Create input data in the same order used during training
    input_data = pd.DataFrame({
        "quantity": [quantity],
        "unit_price": [unit_price],
        "discount": [discount],
        "delivery_days": [delivery_days],
        "customer_rating": [customer_rating]
    })

    # Make the prediction
    prediction = model.predict(input_data)[0]

    # Display the predicted revenue
    st.success(f"Predicted Revenue: ₹{prediction:,.2f}")
