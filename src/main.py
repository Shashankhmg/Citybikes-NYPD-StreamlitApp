import streamlit as st

# Set page config
st.set_page_config(page_title="CitiBike Risk Analysis", layout="wide")

# Sidebar Navigation
st.sidebar.title("🚲 CitiBike Risk Dashboard")
page = st.sidebar.radio("Go to", ["Overview", "Accident Analysis", "Risk Prediction"])

# Load the selected page
if page == "Overview":
    from pages import overview
    overview.show()
elif page == "Accident Analysis":
    from pages import accident_analysis
    accident_analysis.show()
elif page == "Risk Prediction":
    from pages import risk_prediction
    risk_prediction.show()
