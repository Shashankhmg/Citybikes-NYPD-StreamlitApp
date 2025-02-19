import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
import pandas as pd
# Set page configuration
st.set_page_config(page_title="Overview - CitiBike Risk Analysis", layout="wide")

# Title & Introduction
st.title("🚴‍♂️ CitiBike Usage Insights")

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


# Load images
image_files = {
    "CitiBike Usage by Weekday vs. Weekend": "../static/citybikes_usage_weekday_weekend.png",
    "Rides per Hour": "../static/Rides per Hour.png",
    "CitiBike Users: Subscribers vs. Casual Riders": "../static/CitiBike Users- Subscribers vs. Casual Riders.png",
    "Trip Duration Distribution": "../static/Trip Duration Distribution.png",
    "Top 10 Most Popular Start Stations": "../static/Top 10 Most Popular Start Stations.png",
    "CitiBike Start Locations (Filtered for NYC)": "../static/CitiBike Start Locations (Filtered for NYC).png",
    "CitiBike Start vs. End Locations (NYC)": "../static/CitiBike Start vs. End Locations (NYC).png",
}

# Display visualizations with better UI
st.markdown("---")
for title, file_name in image_files.items():
    st.subheader(title)
    
    col1, col2 = st.columns([2, 4])  # Adjust column width for better alignment
    
    
    img = Image.open(file_name)
    st.image(img, caption=title, use_container_width=True)
    # Explanation for each visualization
    if title == "CitiBike Usage by Weekday vs. Weekend":
        with st.container(border=True):
            
            # Center the graph using st.columns()
            col1, col2, col3 = st.columns([1, 4, 1])  # Adjust column proportions
            with col2:  # Center the graph in the middle column
                st.write(f"**{title}**")
                st.image(img, caption=title, use_container_width=True)

            col1, col2, col3 = st.columns([2, 2, 2])  # Adjust column proportions
            with col1:
                st.write("#### Insights from the Chart")
                st.write("""
                - CitiBike usage is significantly higher on weekdays, especially Wednesday to Friday.
                - Lower usage on weekends suggests different riding behaviors among casual vs. daily commuters.
                """)
            with col2:
                st.write("#### How CitiBike Can Improve")
                st.write("""
                - Introduce weekend promotions to increase usage.
                - Adjust bike availability dynamically to match demand trends.
                """)
            with col3:
                st.write("#### How AXA Can Help")
                st.write("""
                - Offer weekday vs. weekend insurance plans based on accident risk.
                - Provide different coverage plans for commuters and casual riders.
                """)

    elif title == "Rides per Hour":
        st.write("### 🔍 Insights from the Chart")
        st.write("""
        - Peak riding hours occur during **morning (7-9 AM)** and **evening (4-7 PM)** rush hours.
        - Off-peak hours see significantly lower usage.
        """)

        st.write("### 🚲 How CitiBike Can Improve")
        st.write("""
        - Allocate more bikes to high-demand areas during peak hours.
        - Offer incentives for off-peak riding to balance demand.
        """)

        st.write("### 💡 How AXA Can Help")
        st.write("""
        - Provide **time-based insurance pricing**, offering higher coverage during peak accident hours.
        - Promote accident prevention campaigns during rush hours.
        """)

    elif title == "CitiBike Users: Subscribers vs. Casual Riders":
        st.write("### 🔍 Insights from the Chart")
        st.write("""
        - **Subscribers dominate CitiBike usage**, making up the majority of rides.
        - Casual riders make up a smaller portion of total trips.
        """)

        st.write("### 🚲 How CitiBike Can Improve")
        st.write("""
        - Encourage casual riders to become subscribers through discounts.
        - Offer more flexible plans for occasional riders.
        """)

        st.write("### 💡 How AXA Can Help")
        st.write("""
        - Provide different insurance coverage for **subscribers vs. casual riders**.
        - Offer bundle deals for long-term CitiBike users.
        """)

    elif title == "Trip Duration Distribution":
        st.write("### 🔍 Insights from the Chart")
        st.write("""
        - Most CitiBike trips are short, averaging **5-15 minutes**.
        - Few rides exceed 30 minutes.
        """)

        st.write("### 🚲 How CitiBike Can Improve")
        st.write("""
        - Offer pricing incentives for longer trips.
        - Increase bike availability for short-duration rides.
        """)

        st.write("### 💡 How AXA Can Help")
        st.write("""
        - Provide micro-duration accident coverage for short trips.
        - Offer protection plans for longer rides with increased accident exposure.
        """)

    elif title == "Top 10 Most Popular Start Stations":
        st.write("### 🔍 Insights from the Chart")
        st.write("""
        - Stations in high-traffic areas (e.g., W 21 St & 6 Ave) see the most rides.
        - Certain neighborhoods have a **higher CitiBike dependency**.
        """)

        st.write("### 🚲 How CitiBike Can Improve")
        st.write("""
        - Expand high-traffic stations with more docking spaces.
        - Improve infrastructure around **busiest stations** to reduce congestion.
        """)

        st.write("### 💡 How AXA Can Help")
        st.write("""
        - Focus insurance plans around high-traffic stations.
        - Provide **risk-based pricing for frequently used start locations**.
        """)

    elif title == "CitiBike Start Locations (Filtered for NYC)":
        st.write("### 🔍 Insights from the Chart")
        st.write("""
        - CitiBike stations are densely clustered around **Manhattan** and some Brooklyn areas.
        - Sparse presence in outer boroughs.
        """)

        st.write("### 🚲 How CitiBike Can Improve")
        st.write("""
        - Expand CitiBike network to underserved areas.
        - Identify high-demand zones outside the current coverage.
        """)

        st.write("### 💡 How AXA Can Help")
        st.write("""
        - Work with CitiBike to **assess risk factors** in expansion areas.
        - Offer coverage for new locations based on accident history.
        """)

    elif title == "CitiBike Start vs. End Locations (NYC)":
        st.write("### 🔍 Insights from the Chart")
        st.write("""
        - Most start locations also serve as **end locations**, meaning round trips are common.
        - Some routes have imbalanced bike drop-offs, leading to station shortages.
        """)

        st.write("### 🚲 How CitiBike Can Improve")
        st.write("""
        - Use dynamic bike rebalancing to **prevent shortages** at busy stations.
        - Offer incentives for riders to return bikes to high-demand areas.
        """)

        st.write("### 💡 How AXA Can Help")
        st.write("""
        - Provide **route-specific insurance pricing** for high-traffic areas.
        - Identify risky routes based on trip start and end patterns.
        """)

# Final insights
st.header("🚀 Key Takeaways")
st.write("""
By analyzing CitiBike's data, we can:
1. Identify high-risk areas for **better safety measures**.
2. Improve CitiBike's operations with **demand-based strategies**.
3. Create **customized insurance** offerings with AXA, benefiting both riders and CitiBike.

This case study offers actionable insights for CitiBike & AXA to optimize their collaboration. 🚴‍♂️💡
""")

st.success("This analysis provides actionable insights for both CitiBike and AXA to enhance safety and business collaboration.")
