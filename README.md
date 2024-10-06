# 🚀 AI-Powered Resume Evaluator Using ATS Logic

This project is an AI-driven tool that helps job seekers optimize their resumes for Applicant Tracking Systems (ATS). The evaluator compares resumes against job descriptions in fields like tech, software engineering, data science, and big data, identifying missing keywords, and providing detailed feedback on strengths, weaknesses, and skill gaps.

## 📋 Project Overview

In today’s competitive job market, making your resume stand out is more important than ever. Many companies use ATS to filter candidates, which is why it's crucial to optimize your resume accordingly. This AI-powered solution helps users achieve that by offering:

- **ATS Compatibility**: Evaluates how well a resume matches a job description based on ATS filters.
- **PDF Resume Parsing**: Converts resume PDFs into text for analysis.
- **AI-Driven Analysis**: Uses Google’s Gemini AI to provide a detailed analysis.
- **Keyword Matching**: Identifies missing keywords and gaps in the resume.
- **Strengths and Weaknesses**: Offers a breakdown of the resume’s strengths and weaknesses.
- **Skill Gap Analysis**: Highlights skill gaps in the resume.
- **Recommendations**: Suggests improvements for better ATS matching.

## 🛠️ Technologies Used

- **Python**: Backend logic and PDF parsing.
- **Streamlit**: Front-end for interactive UI.
- **Google Gemini AI**: AI for analyzing and comparing resumes with job descriptions.
- **PyPDF2**: For extracting text from PDF files.
- **Natural Language Processing (NLP)**: To understand and process text data.
- **JSON**: Parsing and handling the AI model’s responses.

## 🚀 Features

- **PDF Resume Parsing**: Upload your resume in PDF format.
- **Job Description Matching**: Paste the job description and get feedback.
- **AI-Generated Recommendations**: Get personalized advice based on missing keywords, skill gaps, and more.

## 📂 Project Structure

```
├── app.py                    # Main application file
├── app_updated.py            # Main updated applciation file
├── README.md                 # Project documentation
├── requirements.txt          # Required Python libraries
├── .env                      # Environment variables for API keys
├── venv/                     # Virtual environment
└── ats_evaluator/
    ├── __init__.py           # Init file for module
    ├── utils.py              # Utility functions (PDF parsing, etc.)
    ├── gemini_integration.py # Gemini AI integration and response handling
```

## ⚙️ Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/ATS_resume_evaluator.git
   cd ATS_resume_evaluator
   ```

2. **Create and Activate Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

3. **Install the Required Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   - Create a `.env` file in the root directory.
   - Add your **Google API key** in the following format:
     ```bash
     GOOGLE_API_KEY=your-google-api-key
     ```

5. **Run the Application**:
   ```bash
   streamlit run app.py  (for basic code)
   or,
   streamlit run app_updated.py (for more updated code)
   ```

## 📝 Usage

1. **Upload Resume**: Upload your resume in PDF format.
2. **Enter Job Description**: Paste the job description into the provided text area.
3. **Evaluate Resume**: Click the **Evaluate Resume** button to receive feedback, including:
   - ATS match percentage
   - Missing keywords
   - Strengths and weaknesses
   - Skill gaps
   - Recommendations for improvement

## 📊 Sample ATS Evaluation Results
  <img width="883" alt="image" src="https://github.com/user-attachments/assets/81a49509-dfab-4628-836e-65b4edf7b838">



## 🧑‍💻 Contributing

Feel free to contribute by creating issues, submitting pull requests, or suggesting new features. Any contribution you make is greatly appreciated!

---

**Author**: [Sourav Nandi]

**License**: This project is licensed under the MIT License.

---

This README provides clear instructions on setup, usage, and highlights the functionality of the tool, making it easy for others to understand your project!
