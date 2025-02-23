import streamlit as st
import pandas as pd
import joblib
import numpy as np
import json
from sidebar import sidebar
from datetime import datetime

sidebar()

# Load model & station risk data
model = joblib.load("./models/DT.joblib")
# Load preprocessed station data from JSON 
with open("./data/station_data.json", "r") as f:
    station_map = json.load(f)

# Title
st.title("CitiBike Risk Prediction")
st.markdown("*Predicts the risk involved at a Citybike Station at a particular time (Present day)*")

# Define example cases for different risk levels
example_cases = pd.DataFrame({
    "Start Station": ["W 36 St & 7 Ave", "W 31 St & 7 Ave", "W 41 St & 8 Ave", "11 Ave & W 41 St"],
    "End Station": ["W 24 St & 7 Ave", "E 27 St & 1 Ave", "Mercer St & Bleecker St", "Lexington Ave & E 26 St"],
    "Ride Start Time": ["22:19", "18:37", "10:29", "18:05"],
    "Day of Week": ["Tuesday", "Monday", "Wednesday", "Friday"],
    "Accident Count": [694, 703, 1280, 1596],
    "Normalized Risk Score": [0.129, 0.480, 0.664, 1.000],
    "Predicted Risk Level": ["🟢 Low Risk", "🟡 Moderate Risk", "🔴 High Risk", "🔴🔴 Very High Risk"]
})

with st.container(border=True):
    # Display the example cases in Streamlit
    st.markdown("##### 📊 **Example Cases of Risk Prediction**")
    st.dataframe(example_cases, hide_index=True)

with st.container(border=True):
    st.markdown("### Enter ride details to predict the accident risk level for your trip.")

    # User Inputs
    col1, col2 = st.columns(2)

    with col1:
        start_station = st.selectbox("🚲 **Select Start Station**", list(station_map.keys()))
        end_station = st.selectbox("🏁 **Select End Station**", list(station_map.keys()))

    with col2:
        user_type = st.radio("👤 **Rider Type**", ["Member", "Casual"])
        #hour_of_day = st.slider("⏰ Time of Ride", 0, 23, 12)
        time_input = st.time_input("**Time of the Planned Ride**", datetime.now().time())  # Default time is now
        hour_of_day = time_input.hour  # Extract hour in 24-hour format


# Fetch station details from JSON
start_info = station_map[start_station]
end_info = station_map[end_station]

# Infer Other Features
day_of_week = pd.Timestamp.now().dayofweek  # Assume prediction for today
weekend = 1 if day_of_week >= 5 else 0
rush_hour = 1 if (7 <= hour_of_day <= 9) or (16 <= hour_of_day <= 19) else 0
trip_distance = np.sqrt((start_info["start_lat"] - end_info["start_lat"])**2 + (start_info["start_lng"] - end_info["start_lng"])**2)
trip_duration = np.random.randint(5, 20)  # Placeholder

# Prepare Input for Model
input_data = pd.DataFrame({
    "start_station_id": [start_info["start_station_id"]],
    "end_station_id": [end_info["start_station_id"]],
    "start_lat": [start_info["start_lat"]],
    "start_lng": [start_info["start_lng"]],
    "end_lat": [end_info["start_lat"]],
    "end_lng": [end_info["start_lng"]],
    "member_casual": [1 if user_type == "Member" else 0],
    "normalized_risk_score": [start_info["normalized_risk_score"]],
    "hour_of_day": [hour_of_day],
    "day_of_week": [day_of_week],
    "weekend": [weekend],
    "rush_hour": [rush_hour],
    "trip_duration": [trip_duration],
    "trip_distance": [trip_distance]
})

#st.write(input_data)
if st.button('Predict'):
    #Predict
    with st.container(border=True):
        col1,col2,col3 = st.columns([1, 4, 0.5])
        with col2:
            risk_prediction = model.predict(input_data)[0]
            risk_levels = {1: "🟢 Low Risk", 2: "🟡 Medium Risk", 3: "🔴 High Risk", 4: "🔴 🔴 Very High Risk" }
            st.markdown(f"#### 🔍 Predicted Risk Level -  {risk_levels[risk_prediction]}")

        st.warning("This prediction is based on historical accident data, station risk levels, and ride details.")

st.subheader("CitiBike Stations & Accident Hotspots: Insights from NYPD Data")
st.warning("⚠️ **Warning:** Some CitiBike stations are located in high-accident zones. Ride safely and stay alert! 🚲")

# Load the HTML file
heatmap_path = "./data/optimized_citibike_accident_heatmap.html"


### **Key Takeaway:**  
# Read and display the heatmap in Streamlit
with open(heatmap_path, "r", encoding="utf-8") as f:
    heatmap_html = f.read()

st.components.v1.html(heatmap_html, height=600, scrolling=True)
st.subheader("**Insights from the Machine Learning Risk Prediction Analysis**")
with st.container(border=True):
    
    col1, col2, col3 = st.columns([2, 2, 2])  # Adjust column proportions
    with col1:
        st.write("#### **For CitiBike Users:** ")
        st.write("""
            - Users can identify **high-risk stations** before starting their trip, allowing them to **plan safer routes**.  
            - By understanding the accident risk associated with different stations and times of the day, users can take **precautions, such as wearing helmets or choosing alternative paths**.  
            - Casual riders and daily commuters can **opt for additional safety measures** in high-risk zones.  
        """)
    with col2:
        st.write("#### How CitiBike Can Improve")
        st.write("""
        - CitiBike can **optimize station placement and bike allocation** based on accident risks.  
        - It can introduce **dynamic pricing models** to encourage safer riding times and routes.  
        - Safety measures like **enhanced road infrastructure, warning alerts, or collaboration with city officials** can be implemented to reduce risk.  
        - CitiBike can use **AI-powered data insights** to **plan expansion areas** while ensuring user safety.  

        """)
    with col3:
        st.write("#### How AXA Can Help")
        st.write("""
        - **Risk-based insurance policies**: AXA can offer **customized insurance coverage** based on station risk levels.  
        - **Dynamic premiums**: Riders using CitiBike in high-risk areas could be eligible for **on-demand, micro-insurance plans** for extra protection.  
        - **Safety incentives**: AXA and CitiBike can collaborate to **offer discounts on insurance plans** for safe riding habits, such as using designated routes.  
        - **Predictive accident prevention**: By leveraging **ML models**, AXA can **proactively identify accident-prone areas** and **work with CitiBike and city officials** to improve infrastructure.  
        """)