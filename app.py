import streamlit as st
import openai
import os

# Set your OpenAI API key (better to use secrets in production)
openai.api_key = os.getenv("OPENAI_API_KEY")  # or replace with your key directly

st.set_page_config(page_title="AI Resume Builder", page_icon="🧠")

st.title("🤖 AI-Powered Resume Generator")
st.write("Enter your information and let AI generate a professional resume for you!")

# --- User Input ---
name = st.text_input("Full Name")
email = st.text_input("Email Address")
phone = st.text_input("Phone Number")
summary = st.text_area("Professional Summary")
skills = st.text_area("List Your Skills (comma-separated)")
experience = st.text_area("Work Experience")
education = st.text_area("Education Background")

if st.button("Generate Resume"):
    if name and summary and skills:
        prompt = f"""
        Generate a professional resume based on the following details:

        Name: {name}
        Email: {email}
        Phone: {phone}

        Summary:
        {summary}

        Skills:
        {skills}

        Experience:
        {experience}

        Education:
        {education}

        Format the resume in a clean and readable way with sections.
        """
        with st.spinner("Generating your resume..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a resume writing assistant."},
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens=800,
                    temperature=0.7
                )
                generated_resume = response['choices'][0]['message']['content']
                st.success("Resume generated successfully!")
                st.download_button("📄 Download Resume as .txt", generated_resume, file_name=f"{name}_Resume.txt")
                st.text_area("📝 Preview:", generated_resume, height=400)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please fill at least your name, summary, and skills.")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit and OpenAI")
