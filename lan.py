import streamlit as st
import google.generativeai as genai

# Streamlit UI
st.title("AI-Powered Travel Planner")

source = st.text_input("Enter Source Location")
destination = st.text_input("Enter Destination")

# Initialize Google Gemini API
api_key = "Enter ypur API key"  # Your actual API key
genai.configure(api_key=api_key)

# Button to generate travel recommendations
if st.button("Get Travel Recommendations"):
    if source and destination:
        # Create model instance with the correct model name
        model = genai.GenerativeModel("gemini-pro")  # Ensure this is correct

        # Generate content using Gemini model
        response = model.generate_content(f"Suggest travel options from {source} to {destination}, including cost estimates.")
        
        # Display the generated response
        st.write(response.text)
    else:
        st.warning("Please enter both source and destination!")
