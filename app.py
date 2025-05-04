import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load env vars
load_dotenv()
genai.configure(api_key=os.getenv("google_gemini_api"))

# Setup
st.set_page_config(page_title="TalentScout - Interview AI", page_icon="🧠")
st.title("🧠 TalentScout - Hiring Assistant")

# Session setup
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.info = {}
    st.session_state.q_index = 0
    st.session_state.questions = []
    st.session_state.answers = []
    st.session_state.chat = None

# Helper: get Gemini model
def get_model():
    return genai.GenerativeModel("gemini-1.5-flash")

# Step 0: Intro
if st.session_state.step == 0:
    st.write("Welcome to TalentScout! Click start to begin your technical interview journey.")
    if st.button("Start"):
        st.session_state.step = 1

# Step 1: Candidate Info
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

# Step 2: Generate Questions
elif st.session_state.step == 2:
    tech_stack = st.session_state.info["tech_stack"]
    model = get_model()
    prompt = f"You are an AI interviewer. The candidate is skilled in: {tech_stack}. Generate 5 concise technical interview questions to assess their skills."
    try:
        response = model.generate_content(prompt)
        questions = [q.strip("- ").strip() for q in response.text.split("\n") if q.strip()]
        st.session_state.questions = questions[:5]

        st.session_state.chat = model.start_chat(history=[
            {
                "role": "user",
                "parts": [f"You are an AI interviewer helping assess a candidate skilled in: {tech_stack}. Ask 5 questions one at a time and evaluate their responses."]
            }
        ])
        st.session_state.step = 3
        st.rerun()
    except Exception as e:
        st.error(f"Error generating questions: {e}")

# Step 3: Interactive Q&A
elif st.session_state.step == 3:
    current_q = st.session_state.questions[st.session_state.q_index]
    st.subheader(f"Question {st.session_state.q_index + 1}")
    st.write(current_q)

    user_answer = st.text_area("Your Answer", key=f"answer_{st.session_state.q_index}")
    if st.button("Submit Answer"):
        st.session_state.answers.append({
            "question": current_q,
            "answer": user_answer
        })

        # Maintain chat context
        st.session_state.chat.send_message(f"Candidate's answer to Q{st.session_state.q_index + 1}: {user_answer}")

        st.session_state.q_index += 1
        if st.session_state.q_index < 5:
            st.rerun()
        else:
            st.session_state.step = 4
            st.rerun()

# Step 4: Evaluation
elif st.session_state.step == 4:
    st.subheader("🧪 Evaluating Your Performance...")

    # Build evaluation prompt
    summary_prompt = "Based on the following questions and candidate responses, give a concise evaluation of the candidate's technical skills:\n\n"
    for qa in st.session_state.answers:
        summary_prompt += f"Q: {qa['question']}\nA: {qa['answer']}\n\n"

    try:
        eval_response = st.session_state.chat.send_message(summary_prompt)
        st.success("✅ Assessment Complete!")
        st.markdown("### 📝 Summary:")
        st.write(eval_response.text)

    except Exception as e:
        st.error(f"Evaluation Error: {e}")

    if st.button("Restart"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
