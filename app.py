import streamlit as st
import google.generativeai as genai
from prompts import get_intro_prompt, tech_question_prompt
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("AIzaSyBUdJN7j9H9NxNhT8rdfIWQrucBQ-q1pgc")
genai.configure(api_key=api_key)

st.title("🧠 TalentScout - Hiring Assistant")

if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.info = {}

if st.session_state.step == 0:
    st.write(get_intro_prompt())
    if st.button("Start"):
        st.session_state.step = 1

elif st.session_state.step == 1:
    st.session_state.info["name"] = st.text_input("Full Name")
    st.session_state.info["email"] = st.text_input("Email")
    st.session_state.info["phone"] = st.text_input("Phone Number")
    st.session_state.info["experience"] = st.text_input("Years of Experience")
    st.session_state.info["position"] = st.text_input("Desired Position(s)")
    st.session_state.info["location"] = st.text_input("Current Location")
    st.session_state.info["tech_stack"] = st.text_area("Your Tech Stack (e.g., Python, Django, MySQL)")

    if st.button("Submit Info"):
        st.session_state.step = 2

elif st.session_state.step == 2:
    tech_stack = st.session_state.info["tech_stack"]
    prompt = tech_question_prompt(tech_stack)

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        st.subheader("Generated Technical Questions:")
        st.write(response.text)
    except Exception as e:
        st.error(f"Error: {e}")

    st.session_state.step = 3

elif st.session_state.step == 3:
    if st.button("End Chat"):
        st.success("Thanks for using TalentScout!")
        st.session_state.step = 0
