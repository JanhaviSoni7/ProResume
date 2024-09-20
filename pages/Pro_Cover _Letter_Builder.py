import streamlit as st
import requests

# Hugging Face API URL and Headers (with your API key)
API_URL = "https://api-inference.huggingface.co/models/gpt2"
HEADERS = {"Authorization": "Bearer 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"}

# Function to get a cover letter from GPT-2 model
def get_cover_letter(prompt):
    payload = {"inputs": prompt, "options": {"wait_for_model": True}}
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    if response.status_code == 200:
        return response.json()[0]['generated_text']
    else:
        return "Error: Could not generate text at this time."

# Streamlit app UI
st.title("Interactive AI-powered Cover Letter Generator")

# User Inputs for Cover Letter
st.subheader("Enter Your Information")

your_name = st.text_input("Your Name", "John Doe")
job_title = st.text_input("Job Title", "Software Engineer")
company_name = st.text_input("Company Name", "ABC Corp")
skills = st.text_area("List Your Skills (comma-separated)", "Python, Machine Learning, Web Development")
experience = st.text_area("Brief Description of Experience", "I have 3 years of experience in software development, specializing in web applications...")
motivation = st.text_area("Motivation for Applying", "I am excited about this opportunity because I am passionate about developing innovative software solutions and I believe my skills and experience align well with the needs of your company.")

# Generate button
if st.button("Generate Cover Letter"):
    # Creating the prompt for the GPT-2 model
    prompt = (
        f"Dear Hiring Manager at {company_name},\n\n"
        f"My name is {your_name}, and I am writing to express my interest in the {job_title} position at your company. "
        f"With my skills in {skills}, I believe I am a strong fit for this role.\n\n"
        f"{experience}\n\n"
        f"{motivation}\n\n"
        "Thank you for considering my application. I look forward to the opportunity to discuss my qualifications further.\n\n"
        "Sincerely,\n"
        f"{your_name}"
    )

    # Fetch cover letter from Hugging Face GPT-2 model
    cover_letter = get_cover_letter(prompt)
    
    # Display the generated cover letter
    st.subheader("Generated Cover Letter")
    st.write(cover_letter)

    # Download the cover letter as a text file
    st.download_button("Download Cover Letter", cover_letter, file_name="cover_letter.txt")