import streamlit as st

# Streamlit UI
st.title("AI-Powered Travel Planner")

source = st.text_input("Enter Source Location")
destination = st.text_input("Enter Destination")

if st.button("Get Travel Recommendations"):
    st.write(f"Fetching travel options from {source} to {destination}...")
