import streamlit as st
import pandas as pd
import json
import requests
from datetime import datetime
from sidebar import sidebar

# Page Configuration
st.set_page_config(page_title="Demand Prediction", layout="wide")

# Sidebar
sidebar()

# Define your API endpoint
API_URL = "https://fastapi-example-production-fdcd.up.railway.app/predict"

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
    start_station = st.selectbox("**Select Start Station**", station_names)
    
    # Get date and time input for ride
    date_input = st.date_input("**Select Ride Date**", datetime.today())  # Default date is today
    time_input = st.time_input("**Select Ride Time**", datetime.now().time())  # Default time is now

    # Convert to datetime
    ride_datetime = datetime.combine(date_input, time_input)
    hour_of_day = ride_datetime.hour
    day_of_week = ride_datetime.weekday()  # 0 = Monday, 6 = Sunday
    
    #member_type = st.selectbox("User Type", ["member", "casual"])

    # Retrieve corresponding station details
    station_details = station_data.get(start_station, {})

    start_station_id = station_details.get("start_station_id", None)
    start_lat = station_details.get("start_lat", None)
    start_lng = station_details.get("start_lng", None)
    avg_rolling_7days = station_details.get("avg_rolling_7days", None)
    avg_rolling_30days = station_details.get("avg_rolling_30days", None)

    # Determine if it's a weekend (0 = No, 1 = Yes)
    weekend = 1 if day_of_week in [5, 6] else 0

    # Define rush hour (Example: 7-9 AM & 4-7 PM)
    rush_hour = 1 if (7 <= hour_of_day <= 9) or (16 <= hour_of_day <= 19) else 0

    # Submit button
    submit = st.form_submit_button("Predict Demand")  

    if submit:
        if None in (start_station_id, start_lat, start_lng, avg_rolling_7days, avg_rolling_30days):
            st.error(" Missing station data! Please select another station.")
        else:
            # Prepare request payload
            params = {
                "start_station_id": start_station_id,
                "hour_of_day": hour_of_day,
                "day_of_week": day_of_week,
                "weekend": weekend,
                "month": ride_datetime.month,
                "rush_hour": rush_hour,
                "avg_rolling_7days": avg_rolling_7days,
                "avg_rolling_30days": avg_rolling_30days,
                "start_lat": start_lat,
                "start_lng": start_lng
            }

            # Make request to FastAPI
            try:
                #st.write(params)
                response = requests.get(API_URL, params=params)
                #st.write(response)
                response_data = response.json()
                #st.write(response_data)

                if "predicted_demand" in response_data:
                    predicted_demand = response_data["predicted_demand"][0]
                    #st.success(f" Predicted demand for **{start_station}** on **{date_input}** at **{time_input}** : **{predicted_demand} trips** 🚲")
                    # Display the result with a metric component
                    #st.metric(label=f"Predicted demand for **{start_station}** on **{date_input}** at **{time_input}** ", value=f"{predicted_demand} trips", delta=None)
                    # Use markdown for better styling
                    st.markdown(
                            f"""

                                <h3 style="color:#2d862d; margin-bottom:5px;">📊 Predicted Demand</h3>
                                <p style="font-size:16px; margin:5px 0;">
                                    <b>🚲 Station:</b> {start_station} <br>
                                    <b>🕒 Date & Time:</b> {ride_datetime.strftime('%Y-%m-%d %H:%M')}<br>
                                    <b>📈 Predicted Demand:</b> <span style="font-size:22px;color:#007bff;font-weight:bold;">{predicted_demand} trips</span>
                                </p>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )


                else:
                    st.error(" API did not return expected output!")

            except Exception as e:
                st.error(f" API Request Failed! Error: {e}")
