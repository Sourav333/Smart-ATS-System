import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv() 

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Gemini Pro Response
def get_gemini_response(input):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(input)
    return response.text

# Convert PDF to text
def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += str(page.extract_text())  # Extract text from each page
    return text

# Prompt Template
input_prompt = """
Hey ACT like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science,data analyst and big data engineer.
Your task is to evaluate teh resume based on the given job description.You must consider the job market
is very competitive and you should provide best assistance for improving the resumes.Assign the percentage Matching based
on JD and
the missing keywords with high accuracy
resume:{text}
description:{jd}

Please respond with a single string formatted as follows:
{{"JD Match":"%","MissingKeywords":[],"Strengths":[],"Weaknesses":[],"Skill Gap Analysis":[],"Recommendations":"","Overall Feedback":""}}

- "JD Match": Represents the percentage match of the resume against the job description.
- "MissingKeywords": List of essential keywords from the job description that are absent in the resume.
- "Strengths": Key strengths found in the resume that align with the job description.
- "Weaknesses": Notable weaknesses or gaps in the resume.
- "Skill Gap Analysis": Essential skills required for the job that are not present in the resume.
- "Recommendations": Suggestions for improving the resume.
- "Overall Feedback": General assessment of the resume.
"""

gradient_style = """
<style>
.title-gradient {
    background: linear-gradient(45deg, #833AB4, #FD1D1D, #FDC830, #FCAF45); /* Adjust colors as needed */
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 3rem; /* Adjust size as needed */
}
</style>
"""

# Streamlit app

# Display the CSS style
st.markdown(gradient_style, unsafe_allow_html=True)
# Display the title with the gradient effect
st.markdown('<h1 class="title-gradient">Smart ATS ~ Sourav</h1>', unsafe_allow_html=True)
st.title("🚀 Improve Your Resume for ATS Systems")
st.text("Upload your resume and get feedback based on the job description.")

# Job Description input and resume upload
jd = st.text_area("📄 Paste the Job Description")
uploaded_file = st.file_uploader("📁 Upload Your Resume", type="pdf", help="Please upload your resume in PDF format.")

# Submit button
submit = st.button("🔍 Evaluate Resume")

# Process the resume and display response
if submit:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        prompt = input_prompt.format(text=text, jd=jd)
        response = get_gemini_response(prompt)
        
        # Parse the response (assuming response is a valid JSON string)
        try:
            parsed_response = json.loads(response)
            jd_match = parsed_response.get("JD Match", "N/A")
            missing_keywords = parsed_response.get("MissingKeywords", [])
            # profile_summary = parsed_response.get("Profile Summary", "No summary provided.")
            strengths = parsed_response.get("Strengths", [])
            weaknesses = parsed_response.get("Weaknesses", [])
            skill_gaps = parsed_response.get("Skill Gap Analysis", [])
            recommendations = parsed_response.get("Recommendations", "No recommendations provided.")
            overall_feedback = parsed_response.get("Overall Feedback", "No overall feedback provided.")
            
            # Display results in colored boxes with proper layout
            st.markdown("### 📊 **ATS Evaluation Results**")
            st.markdown(f"""
            <div style='border:2px solid #00b4d8; padding: 10px; border-radius: 10px;'>
                <p style='color:#023e8a; font-size:20px;'><b>💼 JD Match:</b> {jd_match}%</p>
                <p style='color:#ff5733; font-size:18px;'><b>🔑 Missing Keywords:</b> {', '.join(missing_keywords) if missing_keywords else 'None'}</p>
                <p style='color:#6a4c93; font-size:18px;'><b>🌟 Strengths:</b> {', '.join(strengths) if strengths else 'None'}</p>
                <p style='color:#e85d04; font-size:18px;'><b>⚠️ Weaknesses:</b> {', '.join(weaknesses) if weaknesses else 'None'}</p>
                <p style='color:#2a9d8f; font-size:18px;'><b>🔍 Skill Gaps:</b> {', '.join(skill_gaps) if skill_gaps else 'None'}</p>
                <p style='color:#3d5a80; font-size:18px;'><b>✅ Recommendations:</b> {recommendations}</p>
                <p style='color:#f3722c; font-size:18px;'><b>📝 Overall Feedback:</b> {overall_feedback}</p>
            </div>
            """, unsafe_allow_html=True)
        
        except json.JSONDecodeError:
            st.error("Error: Unable to parse response. Please try again.")
    else:
        st.error("Please upload a resume.")
