# **🚲 AXA Data Science Challenge - Interactive Streamlit Application**  

This repository contains an interactive **Streamlit web application** built as part of the **AXA Data Science Challenge**. Instead of a traditional presentation, I developed this application to provide a hands-on, dynamic experience of my analysis and predictive models.

## Overview 
The application consists of the following sections:

### 1. Introduction Page**  
This page provides:
- An overview of **my background** and experience.
- A brief **introduction to the challenge** and its objectives.
- Insights into how **AXA and CitiBike** can collaborate for data-driven decision-making.
- Analysis of **CitiBike usage patterns along with NYPD accident data** to assess risks.

### 2. CitiBike & NYPD Data Analysis**  
This section presents the **Exploratory Data Analysis (EDA)** results of the **CitiBike dataset** (January 2025) along with **NYPD accident data** to evaluate accident risk at different locations.  

📂 [Download the dataset here](https://s3.amazonaws.com/tripdata/index.html) 

#### Key insights include:
- Peak hours and popular stations.  
- Subscriber vs. casual rider usage patterns.  
- Distribution of trip durations and distance.  
- Heatmap analysis of CitiBike stations **overlaid with NYPD accident hotspots** to assess risk.

### 3. Risk Prediction
This module predicts the **risk level for a user** based on specific input features.  

#### Input Features Used:  
| Feature                | Description |
|------------------------|-------------|
| `start_station_id`     | Start station identifier |
| `end_station_id`       | End station identifier |
| `start_lat` / `start_lng` | Latitude & longitude of start station |
| `end_lat` / `end_lng`  | Latitude & longitude of end station |
| `member_casual`        | Rider type (Member/Casual) |
| `normalized_risk_score` | Risk score for starting station |
| `hour_of_day`          | Hour of the day (0-23) |
| `day_of_week`          | Day of the week (0=Monday, 6=Sunday) |
| `weekend`              | Binary (1 = Weekend, 0 = Weekday) |
| `rush_hour`            | Binary (1 = Peak Hours, 0 = Off-Peak) |
| `trip_duration`        | Estimated trip duration |
| `trip_distance`        | Estimated trip distance |

- The user provides **minimal inputs**, while additional station-specific details are fetched dynamically from a **pre-processed JSON file** in the backend.

### 4. Demand Prediction
This module predicts the **expected demand (number of trips) at a CitiBike station** at a given date & time.  

#### Input Features for Demand Model:
| Feature                | Description |
|------------------------|-------------|
| `start_station_id`     | Start station identifier |
| `hour_of_day`          | Hour of the day (0-23) |
| `day_of_week`          | Day of the week (0=Monday, 6=Sunday) |
| `weekend`              | Binary (1 = Weekend, 0 = Weekday) |
| `month`               | Month of the ride |
| `rush_hour`            | Binary (1 = Peak Hours, 0 = Off-Peak) |
| `avg_rolling_7days`    | 7-day rolling average of trips for the station |
| `avg_rolling_30days`   | 30-day rolling average of trips for the station |
| `start_lat`            | Latitude of start station |
| `start_lng`            | Longitude of start station |

How It Works?  
- The user selects a **station** and provides a **future date & time**.
- The **regression model** predicts the **average number of trips expected** at that station.
- The model is trained using **historical CitiBike data** with features like **time of day, rush hour, rolling averages, and station popularity**.
- The **trained model is too large (2.5GB)** to store locally, so it's **uploaded to GitHub Models & served via a FastAPI endpoint on Railway**.

🔗 **GitHub Repository for the Model API**: [Link Here](#) *([Add actual repo link](https://github.com/Shashankhmg/Fastapi-Citybike-Demand-Forecase))*  

---

## 🛠️ Tech Stack & Deployment
- **Frontend:** Streamlit  
- **Backend:** FastAPI (Railway)  
- **Data Processing:** Pandas, NumPy  
- **Machine Learning:** Scikit-Learn  
- **Hosting:** Streamlit Cloud, Railway  
- **Model Storage:** Hugging Face Hub

---

## How to Run the App Locally?

### **1. Clone the Repository**  
```bash
git clone https://github.com/your-username/citybike-axa-app.git
cd citybike-axa-app
```

### **2. Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **3. Run the Streamlit App**  
```bash
streamlit run main.py

