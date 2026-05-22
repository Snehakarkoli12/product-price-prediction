import streamlit as st
import pandas as pd
import pickle

# Load model
with open("xgboost_price_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load subcategory mapping
with open("subcategory_map.pkl", "rb") as f:
    subcategory_map = pickle.load(f)

st.set_page_config(
    page_title="Price Prediction App",
    page_icon="💰",
    layout="centered"
)

st.title("💰 Product Price Predictor")

st.write("Enter product details to predict its price.")

# User Inputs
subcategory_name = st.selectbox(
    "Select Subcategory",
    list(subcategory_map.keys())
)

discount = st.slider(
    "Discount (%)",
    min_value=0.0,
    max_value=90.0,
    value=10.0,
    step=0.5
)

rating = st.slider(
    "Rating",
    min_value=1.0,
    max_value=5.0,
    value=4.0,
    step=0.1
)

review_count = st.number_input(
    "Review Count",
    min_value=0,
    value=100
)

# Predict
if st.button("Predict Price"):

    subcategory_encoded = subcategory_map[subcategory_name]

    input_data = pd.DataFrame({
        "subcategory": [subcategory_encoded],
        "discount": [discount],
        "rating": [rating],
        "review_count": [review_count]
    })

    prediction = model.predict(input_data)[0]

    st.success(f"Predicted Price: ₹{prediction:,.2f}")

    st.subheader("Input Details")

    st.dataframe(input_data)