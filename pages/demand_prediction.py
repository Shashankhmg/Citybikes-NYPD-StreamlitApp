import streamlit as st
# Page Configuration
st.set_page_config(page_title="Demand Prediction", layout="wide")
from sidebar import sidebar
import pandas as pd
from datetime import datetime
import json
import os
import zipfile
import joblib
from huggingface_hub import hf_hub_download, login
sidebar()

HF_TOKEN = st.secrets["HF_TOKEN"]
login(HF_TOKEN)

# Load model from Hugging Face
@st.cache_resource  # Cache the model to avoid reloading it on every run
def load_model():
    model_path = hf_hub_download(repo_id="Shashankhmg/citybike-demnd-prediction", filename="RF.joblib")
    return joblib.load(model_path)

model = load_model()
st.write("Model loaded successfully!")

# Load station data from JSON
with open("./data/station_data_2.json", "r") as file:
    station_data = json.load(file)  # Load full station data
station_names = list(station_data.keys())  # Extract only station names for dropdown

# Title
st.title("🚲 CitiBike Demand Prediction")
st.subheader("Enter Ride Details")

# Create input form
with st.form("demand_form"):
    # Get user inputs
    start_station = st.selectbox("Select Start Station", station_names)
    
    # Get date and time input for ride
    date_input = st.date_input("Select Ride Date", datetime.today())  # Default date is today
    time_input = st.time_input("Select Ride Time", datetime.now().time())  # Default time is now

    # Convert to datetime
    ride_datetime = datetime.combine(date_input, time_input)
    hour_of_day = ride_datetime.hour
    day_of_week = ride_datetime.weekday()  # 0 = Monday, 6 = Sunday
    
    member_type = st.selectbox("User Type", ["member", "casual"])

    # Retrieve corresponding station details (Fixed error)
    station_details = station_data.get(start_station, {})  # Get station details safely

    start_station_id = station_details.get("start_station_id", None)
    start_lat = station_details.get("start_lat", None)
    start_lng = station_details.get("start_lng", None)
    avg_rolling_7days = station_details.get("avg_rolling_7days", None)
    avg_rolling_30days = station_details.get("avg_rolling_30days", None)

    # Display selected details
    st.write(f"**Selected Station:** {start_station}")
    st.write(f"**Ride Date and Time:** {ride_datetime}")

    # Submit button (Fixed issue)
    submit = st.form_submit_button("Predict Demand")  

    if submit:
        # Here you would call your demand prediction model (Placeholder)
        st.write("### Prediction for the demand based on the provided details:")
        st.success(f"Predicted demand for {start_station}: **50 trips** 🚲")
