import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf

from dotenv import load_dotenv

load_dotenv() ##as load all the environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


##Gemini Pro Response
def get_gemini_response(input):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(input)
    return response.text

##Convert PDF to text
def input_pdf_text(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
    # for page in reader(len(reader.pages)):
    for page in reader.pages:
        # page=reader.pages[page] When you use for page in reader.pages, page is already a Page object.You don’t need to use reader.pages[page] since page is already the object you're iterating over.
        text+=str(page.extract_text()) # Extract text from each page
    return text

##Prompt Template
input_prompt= """
Hey ACT like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science,data analyst and big data engineer.
Your task is to evaluate teh resume based on the given job description.You must consider the job market
is very competitive and you should provide best assistance for improving the resumes.Assign the percentage Matching based
on JD and
the missing keywords with high accuracy
resume:{text}
description:{jd}

I want the response in one string having the structure
{{"JD Match":"%","MissingKeywords;[]","Profile Summary":""}}
"""

## streamlit app
st.title("Smart ATS")
st.text("Improve Your Resume ATS")
jd=st.text_area("Paste the Job Description")
uploaded_file=st.file_uploader("Upload Your Resume",type="pdf",help="Please uplaod the pdf")

submit=st.button("Submit")

if submit:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        response=get_gemini_response(input_prompt)
        st.subheader(response)