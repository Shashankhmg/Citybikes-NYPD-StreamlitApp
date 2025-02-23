import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
import pandas as pd
# Title & Introduction
st.title("👤 Shashankh Mysore Girish")
# Set Streamlit page layout to wide mode
# Sidebar with Navigation
st.sidebar.title("🚲 **CitiBike Risk Analysis**")

# Define page names (replace with your actual page names)
page_names = ["overview.py", "risk_prediction.py","accident_analysis.py"]

# Create the sidebar and set a title
#st.sidebar.header("🚲 **CitiBike Risk Dashboard**", divider='grey')
st.sidebar.page_link("pages/overview.py", icon="▪", label= ":blue[*CitiBike Data Analysis*]")
st.sidebar.page_link("pages/risk_prediction.py", icon="▪", label= ":blue[*CitiBike Risk Prediction*]")
st.sidebar.page_link("pages/demand_prediction.py", icon="▪", label = ":blue[*Demand Prediction*]")

# Custom CSS for text justification
st.markdown(
    """
    <style>
    .justified-text {
        text-align: justify;
    }
    </style>
    """,
    unsafe_allow_html=True
)


col1, col2 = st.columns([2, 4])  # Adjust column width for better alignment
with col1:
    with st.container():
        st.image("./static/my_photo.jpg", use_container_width=True)

with col2:
    st.subheader("Data Scientist")
    st.markdown(
    """
    <div class="justified-text">
        I am a <b>Data Science enthusiast</b> with a background in <b>engineering and AI</b>, currently pursuing my Master's in <b>Digital Engineering</b> at Otto von Guericke University, Magdeburg. 
        My expertise lies in <b>machine learning, AI-driven automation, and large-scale data processing</b>, with a strong inclination towards <b>innovation and research-driven problem-solving</b>.  
    """,
    unsafe_allow_html=True
)
# Divider
st.markdown("---")

# Set the page title
st.markdown("## 🚲 AXA Case Study: CitiBike Risk Analysis")

# Displaying justified text
st.markdown(
    """
    <div class="justified-text">
        <hr>
        <h4>🌍 About CitiBike</h4>
        CitiBike is New York City's largest bike-sharing system, providing an <b>eco-friendly, flexible, and efficient</b> mode of urban transportation.
        With thousands of daily rides across multiple stations, CitiBike plays a crucial role in <b>reducing congestion and promoting sustainable mobility</b>.
        However, <b>safety remains a key concern</b>, as accident-prone areas can impact rider confidence and service reliability.
        <hr>
        <h4>🏢 About AXA & The Business Opportunity</h4>
        AXA, a global leader in <b>insurance and risk management</b>, specializes in <b>data-driven, personalized insurance solutions</b>.
        With CitiBike’s growing popularity, there is an opportunity to develop <b>customized insurance plans</b> tailored to bikers' risk exposure.
        By <b>analyzing accident trends, risk levels at stations, and rider behaviors</b>, AXA can provide <b>smarter insurance coverage</b> and risk mitigation strategies for CitiBike users.
        <hr>
        <h4>🎯 The Challenge: Data-Driven Risk Insights</h4>
        This case study explores <b>how data and machine learning can optimize CitiBike’s operations while offering innovative insurance solutions</b>.
        Using <b>real-world CitiBike and NYPD accident data</b>, we aim to:
        <ul>
            <li>Identify <b>high-risk stations</b> and accident-prone areas.</li>
            <li>Develop a <b>risk prediction model</b> to enhance rider safety.</li>
            <li>Provide <b>actionable insights</b> for CitiBike and AXA to improve service quality and <b>tailor insurance offerings</b>.</li>
        </ul>
        By bridging <b>mobility data with insurance intelligence</b>, this study seeks to <b>enhance CitiBike's operational efficiency</b> and <b>empower AXA to create better coverage solutions for urban cyclists</b>. 🚴‍♂️🔍
    </div>
    """,
    unsafe_allow_html=True
)

st.success("This study unlocks data-driven opportunities for both CitiBike & AXA, ensuring smarter, safer, and more efficient urban mobility solutions.")
