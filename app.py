import streamlit as st
import openai
import os

# OpenAI API key (add your key here or use dotenv)
openai.api_key = os.getenv("OPENAI_API_KEY")

# Streamlit Web App
st.set_page_config(page_title="AI Resume Generator", layout="centered")
st.title("🧠 AI Resume Summary Generator")

# Input fields
name = st.text_input("Your Full Name")
role = st.text_input("Target Job Role", placeholder="e.g. Data Scientist, Software Engineer")
skills = st.text_area("Your Top Skills", placeholder="e.g. Python, Machine Learning, SQL")
experience = st.text_area("Brief Work Experience", placeholder="e.g. 3 years in data analytics at ABC Corp.")
education = st.text_area("Educational Background", placeholder="e.g. BS in Computer Science from XYZ University")

# Generate Resume Summary
if st.button("Generate Summary"):
    if not (name and role and skills and experience and education):
        st.warning("Please fill in all fields.")
    else:
        with st.spinner("Generating your resume summary..."):
            prompt = f"""
You are an expert resume writer. Write a short, professional, and impactful resume summary for the following person:

Name: {name}
Target Role: {role}
Skills: {skills}
Experience: {experience}
Education: {education}

The summary should be suitable for the top section of a resume and within 80–120 words.
"""

            try:
                response = openai.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7,
                    max_tokens=200
                )
                summary = response.choices[0].message.content.strip()
                st.subheader("📄 Generated Resume Summary")
                st.success(summary)
            except Exception as e:
                st.error(f"Error: {e}")
