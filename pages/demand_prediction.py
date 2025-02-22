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
sidebar()

# Local paths
MODEL_ZIP_PATH = "/Users/shashankhmg/Documents/AXA-Casestudy/Citybikes-NYPD-StreamlitApp/models/RF.joblib.zip"
MODEL_EXTRACT_PATH = "models"
MODEL_FILE_PATH = os.path.join(MODEL_EXTRACT_PATH, "RF.joblib")

# Function to extract model if not already extracted
def extract_model():
    if not os.path.exists(MODEL_FILE_PATH):  # Only extract if not already done
        st.write("Extracting model...")
        with zipfile.ZipFile(MODEL_ZIP_PATH, "r") as zip_ref:
            zip_ref.extractall(MODEL_EXTRACT_PATH)
        st.write("Model extracted!")

# Extract and load model
extract_model()
model = joblib.load(MODEL_FILE_PATH)
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
