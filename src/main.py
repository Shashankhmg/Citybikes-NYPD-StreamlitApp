import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
import pandas as pd
from pages import overview
from pages import accident_analysis
from pages import risk_prediction

# Title & Introduction
st.title("🚴‍♂️ CitiBike Usage Insights")
# Load local configuration
st.set_option('client.showSidebarNavigation', False)
# Sidebar with Navigation
st.sidebar.title("🚲 **CitiBike Risk Dashboard**")



# Define page names (replace with your actual page names)
page_names = ["overview.py", "risk_prediction.py","accident_analysis.py"]

# Create the sidebar and set a title
#st.sidebar.header("🚲 **CitiBike Risk Dashboard**", divider='grey')
st.sidebar.page_link("pages/overview.py", icon="▪", label= "**Overview**")
st.sidebar.page_link("pages/risk_prediction.py", icon="▪", label= ":blue[*Risk Prediction*]")




st.markdown("""
CitiBike is New York City's bike-sharing system, providing a **convenient, eco-friendly** mode of transportation.
Understanding its usage patterns and accident risks can help optimize operations and improve rider safety.  
""")

# About AXA Section
st.markdown("---")
st.header("🏢 About AXA & Potential Collaboration")
st.markdown("""
AXA, a leading insurance provider, can collaborate with CitiBike by offering **data-driven insurance plans**.
Analyzing accident risk at different stations allows AXA to create **customized policies** while CitiBike can **enhance safety measures**.
""")


