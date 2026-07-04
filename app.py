import streamlit as st
import pandas as pd
import pickle

# Load Model
model = pickle.load(open("house_price_model.pkl", "rb"))

# Load Feature Columns
columns = pickle.load(open("labelen.pkl", "rb"))

st.set_page_config(
    page_title="Bengaluru House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 Bengaluru House Price Prediction")

st.write("Enter the house details below.")

# --------------------------
# User Inputs
# --------------------------

total_sqft = st.number_input(
    "Total Square Feet",
    min_value=300.0,
    max_value=20000.0,
    value=1200.0
)

bath = st.number_input(
    "Bathrooms",
    min_value=1,
    max_value=10,
    value=2
)

balcony = st.number_input(
    "Balconies",
    min_value=0,
    max_value=5,
    value=1
)

bhk = st.number_input(
    "BHK",
    min_value=1,
    max_value=10,
    value=2
)

area_type = st.selectbox(
    "Area Type",
    [
        "Super built-up Area",
        "Built-up Area",
        "Plot Area",
        "Carpet Area"
    ]
)

availability = st.selectbox(
    "Availability",
    [
        "Ready To Move",
        "Immediate Possession"
    ]
)

location = st.text_input(
    "Location",
    "Whitefield"
)

# --------------------------
# Prediction
# --------------------------

if st.button("Predict Price"):

    input_data = pd.DataFrame(
        [[0]*len(columns)],
        columns=columns
    )

    # Numerical features
    input_data["total_sqft"] = total_sqft
    input_data["bath"] = bath
    input_data["balcony"] = balcony
    input_data["bhk"] = bhk

    # One-hot encoded columns
    area_col = "area_type_" + area_type
    availability_col = "availability_" + availability
    location_col = "location_" + location

    if area_col in input_data.columns:
        input_data[area_col] = 1

    if availability_col in input_data.columns:
        input_data[availability_col] = 1

    if location_col in input_data.columns:
        input_data[location_col] = 1

    prediction = model.predict(input_data)

    st.success(f"Estimated Price : ₹ {prediction[0]:.2f} Lakhs")