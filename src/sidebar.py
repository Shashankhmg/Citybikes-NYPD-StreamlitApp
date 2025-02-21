import streamlit as st 

def sidebar():
    # Sidebar with Navigation
    st.sidebar.title("🚲 **CitiBike Risk Dashboard**")
    st.sidebar.page_link("pages/overview.py", icon="▪", label= "**Overview**")
    st.sidebar.page_link("pages/risk_prediction.py", icon="▪", label= ":blue[*Risk Prediction*]")
