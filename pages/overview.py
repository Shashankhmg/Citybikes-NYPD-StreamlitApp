import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image

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
st.header("📊 CitiBike Usage Insights")

for title, file_name in image_files.items():
    st.subheader(f"📌 {title}")  # Add bullet icon
    
    # Create two equal columns for better alignment
    col1, col2 = st.columns([1, 2])  

    with col1:
        img = Image.open(file_name)
        st.image(img, caption=title, use_container_width=True)

    with col2:
        # Explanation for each visualization
        if title == "CitiBike Usage by Weekday vs. Weekend":
            st.markdown("### 🔍 Insights from the Chart")
            st.write("""
            - 🚴 CitiBike usage is significantly higher on **weekdays**, especially Wednesday to Friday.
            - 📉 Lower usage on weekends suggests different behaviors among casual vs. daily commuters.
            """)

            st.markdown("### 🚲 How CitiBike Can Improve")
            st.write("""
            - 📢 **Introduce weekend promotions** to increase usage.
            - 🚲 **Adjust bike availability dynamically** to match demand trends.
            """)

            st.markdown("### 💡 How AXA Can Help")
            st.write("""
            - 📅 **Offer weekday vs. weekend insurance plans** based on accident risk.
            - 🛡 **Provide tailored insurance for commuters vs. casual riders.**
            """)

        elif title == "Rides per Hour":
            st.markdown("### 🔍 Insights from the Chart")
            st.write("""
            - 🚦 **Peak riding hours:** Morning (7-9 AM) & Evening (4-7 PM).
            - 🏙 **Off-peak hours** see lower usage, indicating commuting patterns.
            """)

            st.markdown("### 🚲 How CitiBike Can Improve")
            st.write("""
            - 🚲 Allocate **more bikes during peak hours**.
            - 🎁 Offer **discounts for off-peak riding** to balance demand.
            """)

            st.markdown("### 💡 How AXA Can Help")
            st.write("""
            - 🛡 Provide **time-based insurance pricing** with extra coverage for peak hours.
            - 📢 **Promote accident prevention campaigns** during rush hours.
            """)

        elif title == "CitiBike Users: Subscribers vs. Casual Riders":
            st.markdown("### 🔍 Insights from the Chart")
            st.write("""
            - 📊 **Subscribers dominate CitiBike usage**, making up the majority of rides.
            - 🚴 Casual riders contribute a smaller portion.
            """)

            st.markdown("### 🚲 How CitiBike Can Improve")
            st.write("""
            - 🎟 Encourage casual riders to become **subscribers through discounts**.
            - 📅 Offer **more flexible plans** for occasional users.
            """)

            st.markdown("### 💡 How AXA Can Help")
            st.write("""
            - 🛡 Provide **different insurance tiers** for subscribers vs. casual riders.
            - 🎯 Offer **bundle deals for long-term CitiBike users**.
            """)

        elif title == "Trip Duration Distribution":
            st.markdown("### 🔍 Insights from the Chart")
            st.write("""
            - ⏳ Most CitiBike trips last **5-15 minutes**.
            - 🚲 Longer rides (above 30 min) are rare.
            """)

            st.markdown("### 🚲 How CitiBike Can Improve")
            st.write("""
            - 🎟 Introduce **longer ride incentives**.
            - 🚴 Increase bike availability for **shorter-duration rides**.
            """)

            st.markdown("### 💡 How AXA Can Help")
            st.write("""
            - 🛡 Provide **micro-duration accident coverage**.
            - 📈 Increase **insurance options for longer rides** with higher accident risks.
            """)

        elif title == "Top 10 Most Popular Start Stations":
            st.markdown("### 🔍 Insights from the Chart")
            st.write("""
            - 📍 **High-traffic stations** (e.g., W 21 St & 6 Ave) see the most rides.
            - 🏙 Some neighborhoods rely **heavily on CitiBike for transport**.
            """)

            st.markdown("### 🚲 How CitiBike Can Improve")
            st.write("""
            - 🚴 Expand **docking spaces at high-traffic stations**.
            - 🏙 Improve **infrastructure to manage congestion**.
            """)

            st.markdown("### 💡 How AXA Can Help")
            st.write("""
            - 🛡 Provide **higher coverage for high-risk stations**.
            - 📉 Offer **discounts in low-risk areas**.
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


# Add final insights
st.markdown("---")
st.header("🚀 Key Takeaways")
st.write("""
✅ CitiBike can optimize its operations by **analyzing demand trends** and adjusting availability.  
✅ AXA can create **custom insurance plans** based on accident risk insights.  
✅ Together, they can enhance rider **safety & experience** while ensuring business growth.  
""")

st.success("This case study highlights key areas where CitiBike & AXA can collaborate for a smarter, safer biking experience! 🚴‍♂️💡")
