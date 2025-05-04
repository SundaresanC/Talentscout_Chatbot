# 🧠 TalentScout - AI Hiring Assistant

TalentScout is an intelligent, step-based AI assistant built with **Streamlit** and powered by **Gemini (Google Generative AI)**. It conducts interactive interviews based on the candidate’s tech stack, collects answers, maintains context, and provides a final technical assessment.

---

## 🚀 Features

- 🎯 Step-by-step interactive hiring flow.
- 📄 Collects candidate details (name, email, experience, etc.).
- 🧠 Dynamically generates 5 technical questions from the provided tech stack.
- 💬 Enables user to answer questions one at a time while maintaining conversation context.
- ✅ Final skill evaluation using Gemini based on the full Q&A history.
- 🔄 Option to restart the interview anytime.


## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **LLM:** Gemini-1.5-Flash (Google Generative AI)
- **Language:** Python
- **Environment Management:** python-dotenv

---

## 📦 Installation

1. **Clone the Repository**

```bash
git clone https://github.com/SundaresanC/Talentscout_Chatbot
cd Talentscout_Chatbot
```

2. **Create a Virtual Environment**

```bash
python -m venv venv
```

3. **Activate the Virtual Environment**

**On Windows:**

```bash
venv\Scripts\activate
```

**On macOS/Linux:**

```bash
source venv/bin/activate
```

4. **Install Dependencies**
```bash
pip install -r requirements.txt
```

▶️ **Run the App**

```bash
streamlit run app.py
```
