import streamlit as st
import openai
import os

# Use your API key securely from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="Ask My MBA Tutor", layout="centered")

st.title("🎓 Ask My MBA Tutor")
st.markdown("Ask any question related to MBA subjects like strategy, marketing, finance, and more.")

question = st.text_area("Enter your MBA-related question", height=150)

if st.button("Ask Tutor") and question.strip():
    with st.spinner("Thinking like a B-school professor..."):
        try:
            response = openai.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a helpful MBA professor with expertise in finance, strategy, and marketing."},
                    {"role": "user", "content": question}
                ],
                max_tokens=600,
                temperature=0.7
            )
            st.markdown("### 📘 Tutor's Answer")
            st.write(response.choices[0].message.content)
        except Exception as e:
            st.error(f"Error: {e}")
else:
    st.info("Enter a question and click 'Ask Tutor' to get an expert response.")
