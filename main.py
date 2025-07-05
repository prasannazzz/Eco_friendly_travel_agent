# eco_trip_planner/main.py

import asyncio
import streamlit as st
from datetime import date
from dotenv import load_dotenv
from agents.eco_agent import run_agent
from utils.carbon_utils import estimate_co2

# Load environment variables
load_dotenv()

# Configure Streamlit page
st.set_page_config(
    page_title="Eco-Friendly Trip Recommender",
    page_icon="🌱",
    layout="wide"
)

# Sidebar for API Key Setup
with st.sidebar:
    st.header("🔑 API Keys Configuration")

    def init_key(name):
        if name not in st.session_state:
            st.session_state[name] = ""
        st.session_state[name] = st.text_input(name.replace("_", " ").title(), value=st.session_state[name], type="password")

    for key in [
        "google_maps_key", "accuweather_key",
        "google_client_id", "google_client_secret", "google_refresh_token",
        "google_api_key"
    ]:
        init_key(key)

    all_keys_filled = all([st.session_state[k] for k in st.session_state if k.endswith("key") or "client" in k or "token" in k])
    st.success("✅ All API keys configured!" if all_keys_filled else "⚠️ Please fill in all API keys.")

# App Title
st.title("🌱 Eco-Friendly Trip Recommender")
st.markdown("""
Plan sustainable, low-carbon trips using AI:
- 🚆 Eco-friendly transport
- 🏨 Green accommodation
- 🥗 Vegetarian dining
- 🌍 Carbon footprint estimate
""")

# Input: Basic Info
col1, col2 = st.columns(2)

with col1:
    source = st.text_input("Source", placeholder="Enter your departure city")
    destination = st.text_input("Destination", placeholder="Enter your destination city")
    travel_dates = st.date_input("Travel Dates", [date.today(), date.today()], min_value=date.today())

with col2:
    budget = st.number_input("Budget (in USD)", min_value=0, max_value=10000, step=100)
    travel_preferences = st.multiselect("Travel Preferences", [
        "Adventure", "Relaxation", "Sightseeing", "Cultural Experiences", 
        "Beach", "Mountain", "Luxury", "Budget-Friendly", 
        "Food & Dining", "Shopping", "Nightlife", "Family-Friendly"
    ])

# Additional Preferences
st.subheader("Additional Preferences")
col3, col4 = st.columns(2)

with col3:
    accommodation_type = st.selectbox("Preferred Accommodation", ["Any", "Hotel", "Hostel", "Apartment", "Resort"])
    transportation_mode = st.multiselect("Preferred Transportation", ["Train", "Bus", "Flight", "Rental Car"])

with col4:
    dietary_restrictions = st.multiselect("Dietary Restrictions", ["None", "Vegetarian", "Vegan", "Gluten-Free", "Halal", "Kosher"])

# Eco Trip Toggle
eco_friendly = st.checkbox("🌱 Plan an Eco-Friendly Trip", value=False)

# Submit Button
if st.button("Plan My Trip", type="primary", disabled=not all_keys_filled):
    if not source or not destination:
        st.error("Please enter both source and destination cities.")
    elif not travel_preferences:
        st.warning("Consider selecting some travel preferences for better recommendations.")
    else:
        with st.spinner("🤖 Planning your eco-friendly trip..."):
            try:
                data = {
                    "source": source,
                    "destination": destination,
                    "start_date": str(travel_dates[0]),
                    "end_date": str(travel_dates[1]),
                    "budget": budget,
                    "preferences": ", ".join(travel_preferences),
                    "accommodation": accommodation_type,
                    "transport": ", ".join(transportation_mode),
                    "diet": ", ".join(dietary_restrictions),
                    "eco": "Yes" if eco_friendly else "No"
                }

                response = asyncio.run(run_agent(data))
                st.success("✅ Your eco-friendly travel plan is ready!")
                st.markdown(response)

                # Show CO2 footprint
                if eco_friendly:
                    estimate = estimate_co2(source, destination, transportation_mode)
                    st.info(f"🌍 Estimated Carbon Emissions: **{estimate:.2f} kg CO₂**")

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
                st.info("Please try again or contact support.")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>🌱 Built for Sustainable Travel</p>
    <p>Powered by Gemini + LangChain</p>
</div>
""", unsafe_allow_html=True)
