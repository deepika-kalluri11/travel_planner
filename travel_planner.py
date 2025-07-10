import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import google.generativeai as genai
import os

# Set up Google GenAI API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))  # Replace with your Google GenAI API key if needed

# Streamlit UI
st.title("AI-Powered Travel Planner")

source = st.text_input("Enter Source Location")
destination = st.text_input("Enter Destination")

if st.button("Find Travel Options"):
    if source and destination:
        st.write(f"Fetching travel options from {source} to {destination}...")

        # Step 1: LangChain Setup (Conversation flow)
        # Create a prompt template for travel recommendations
        prompt_template = """You are an AI travel assistant. Provide travel options (cab, train, bus, flight) from {source} to {destination} including estimated costs. 
        Return a structured response with each travel option and its cost. 
        For example:
        1. Cab: Estimated cost: $30
        2. Train: Estimated cost: $15
        3. Bus: Estimated cost: $10
        4. Flight: Estimated cost: $120"""

        prompt = PromptTemplate(input_variables=["source", "destination"], template=prompt_template)
        chat_model = ChatOpenAI(model="gpt-3.5-turbo")
        llm_chain = LLMChain(llm=chat_model, prompt=prompt)

        # Step 2: Get Travel Recommendations
        travel_response = llm_chain.run({"source": source, "destination": destination})

        # Step 3: Display Travel Options
        st.write(f"Here are your travel options from {source} to {destination}:")
        st.write(travel_response)

        # Step 4: (Optional) Integrate Google GenAI for additional details or personalized recommendations
        try:
            # Use Google GenAI to give more personalized options or alternatives
            response = genai.generate_text(
                model="google/genai-model", 
                prompt=f"Suggest travel alternatives for {source} to {destination} including a comparison of prices for cab, train, bus, and flight."
            )
            st.write("Google GenAI Suggestions:")
            st.write(response.result)
        except Exception as e:
            st.write(f"Error using Google GenAI: {e}")
    else:
        st.warning("Please enter both source and destination.")
