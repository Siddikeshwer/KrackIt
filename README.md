# 🚀 KrackIt

**AI-powered job preparation agent that helps you crack your target job.**

KrackIt analyzes your resume against a specific company's job description and generates a personalized preparation strategy.

## ✨ Features

- 🎯 Job Match Score
- 📄 Resume Analysis & Optimization
- 🔍 Skill Gap Detection
- 🤖 ATS Keyword Analysis
- 🎤 Top 20 Role-Specific Interview Questions
- 📝 Personalized Cover Letter
- 📧 Cold Email to HR
- 💬 LinkedIn Recruiter Message
- 📚 Job Preparation Plan

## 🛠️ Tech Stack

- Python
- Streamlit
- OpenRouter API
- PyMuPDF
- python-docx

## ⚙️ Setup

```bash
git clone https://github.com/yourusername/KrackIt.git
cd KrackIt

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

Create a .env file:

OPENROUTER_API_KEY=your_api_key_here

Run:

streamlit run app.py
🔄 How It Works
Resume + Company + Role + Job Description
                    ↓
             KrackIt AI Agent
                    ↓
      ┌─────────────┼─────────────┐
      ↓             ↓             ↓
 Resume Analysis  Job Match   Interview Prep
      ↓             ↓             ↓
 Resume Optimizer  Skill Gaps  Top Questions
                    ↓
             Application Package
                    ↓
       Cover Letter + Cold Email
🔒 Privacy

KrackIt does not use a database or permanently store your resume or job application data.

🚧 Status

V1 — In Development

Built for experimentation and learning with AI agents.
