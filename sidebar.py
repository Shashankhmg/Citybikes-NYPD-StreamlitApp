import streamlit as st 

def sidebar():
    # Sidebar with Navigation
    st.sidebar.title("🚲 **CitiBike Risk Dashboard**")
    st.sidebar.page_link("main.py", icon="🏠", label= ":blue[*Home*]")
    st.sidebar.page_link("pages/overview.py", icon="▪", label= "**CitiBike Data Analysis**")
    st.sidebar.page_link("pages/risk_prediction.py", icon="▪", label= ":blue[*CitiBike Risk Prediction*]")
    st.sidebar.page_link("pages/demand_prediction.py", icon="▪", label = ":blue[*Demand Prediction*]")
