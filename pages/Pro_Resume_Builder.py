import streamlit as st
from fpdf import FPDF


# Function to create a resume PDF based on selected type
def create_resume_pdf(name, email, phone, job_title, skills, experience, education, objective, declaration, achievements, projects, resume_type):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
   
    # Title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, f"{name}'s Resume", 0, 1, 'C')
   
    # Contact Information
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, f"Email: {email}", 0, 1)
    pdf.cell(0, 10, f"Phone: {phone}", 0, 1)
    pdf.cell(0, 10, "", 0, 1)  # Empty line
   
    # Objective Section
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "Objective", 0, 1)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, objective)
   
    pdf.cell(0, 10, "", 0, 1)  # Empty line


    # Resume Types Formatting
    if resume_type == "Traditional":
        # Education Section
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, "Education", 0, 1)
        pdf.set_font("Arial", '', 12)
        pdf.multi_cell(0, 10, education)


        pdf.cell(0, 10, "", 0, 1)  # Empty line


        # Experience Section
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, "Experience", 0, 1)
        pdf.set_font("Arial", '', 12)
        pdf.multi_cell(0, 10, experience)


    elif resume_type == "Functional":
        # Skills Section
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, "Skills", 0, 1)
        pdf.set_font("Arial", '', 12)
        for skill in skills.split(","):
            pdf.cell(0, 10, f"- {skill.strip()}", 0, 1)


        pdf.cell(0, 10, "", 0, 1)  # Empty line


        # Achievements Section
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, "Achievements", 0, 1)
        pdf.set_font("Arial", '', 12)
        pdf.multi_cell(0, 10, achievements)


    elif resume_type == "Combination":
        # Education Section
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, "Education", 0, 1)
        pdf.set_font("Arial", '', 12)
        pdf.multi_cell(0, 10, education)


        pdf.cell(0, 10, "", 0, 1)  # Empty line


        # Skills Section
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, "Skills", 0, 1)
        pdf.set_font("Arial", '', 12)
        for skill in skills.split(","):
            pdf.cell(0, 10, f"- {skill.strip()}", 0, 1)


        pdf.cell(0, 10, "", 0, 1)  # Empty line


        # Experience Section
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, "Experience", 0, 1)
        pdf.set_font("Arial", '', 12)
        pdf.multi_cell(0, 10, experience)


    # Common Sections
    pdf.cell(0, 10, "", 0, 1)  # Empty line


    # Projects Section
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "Projects", 0, 1)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, projects)


    pdf.cell(0, 10, "", 0, 1)  # Empty line


    # Declaration Section
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "Declaration", 0, 1)
    pdf.set_font("Arial", '', 12)
    pdf.cell(0, 10, declaration, 0, 1)


    # Save the PDF to a file
    pdf_file_path = f"{name}_{resume_type}_resume.pdf"
    pdf.output(pdf_file_path)


    return pdf_file_path


# Streamlit user input for Resume Generator
st.title("Resume Generator")


# Input Fields for Resume
st.header("Enter Your Details")
name = st.text_input("Full Name")
email = st.text_input("Email Address")
phone = st.text_input("Phone Number")
job_title = st.text_input("Job Title You Are Applying For")
user_skills = st.text_area("List Your Skills (comma-separated)", "Python, Machine Learning, Web Development")
experience = st.text_area("Describe Your Experience", "I have worked as a software engineer for 5 years...")
education = st.text_area("Education", "B.Sc. in Computer Science from XYZ University")
objective = st.text_area("Objective (3-4 lines)", "To obtain a challenging position in a reputable organization to expand my learnings, knowledge, and skills.")
achievements = st.text_area("List Your Achievements", "Awarded Employee of the Month...")
projects = st.text_area("List Your Projects", "Developed a machine learning model for...")


# Resume Type Selection
resume_type = st.selectbox("Select Resume Type", ["Traditional", "Functional", "Combination"])


# Generate Resume Button
if st.button("Generate Resume and Download"):
    # Create and provide download link for the PDF
    pdf_file_path = create_resume_pdf(name, email, phone, job_title, user_skills, experience, education, objective, "I hereby declare that the information provided is true and accurate to the best of my knowledge.", achievements, projects, resume_type)
    with open(pdf_file_path, "rb") as f:
        st.download_button("Download PDF Resume", f, file_name=pdf_file_path)