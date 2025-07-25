import streamlit as st
import pandas as pd
import joblib
import numpy as np
import os

st.title("🌤 Weather Prediction App")

# Upload the dataset (if required)
if not os.path.exists("Weather_History.csv"):
    st.error("Missing Weather_History.csv file")
else:
    df = pd.read_csv("Weather_History.csv")
    st.write("### Sample Weather Data")
    st.dataframe(df.head())

# Example Inputs
st.write("## 📥 Enter weather details for prediction")

temperature = st.number_input("Temperature (C)", value=20.0)
humidity = st.slider("Humidity (%)", 0, 100, 50)
wind_speed = st.number_input("Wind Speed (km/h)", value=10.0)

# Dummy Prediction (replace with your model)
if st.button("Predict Weather"):
    # Example logic - you will replace with real model.predict
    if humidity > 70:
        prediction = "Rainy"
    elif temperature > 30:
        prediction = "Sunny"
    else:
        prediction = "Cloudy"

    st.success(f"🌤 Predicted Weather: *{prediction}*")