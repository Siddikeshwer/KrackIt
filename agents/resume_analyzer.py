from utils.openrouter import ask_ai
from utils.prompts import build_job_analysis_prompt


def analyze_resume(
    resume_text: str,
    company: str,
    role: str,
    job_description: str
) -> str:

    prompt = build_job_analysis_prompt(
        resume_text=resume_text,
        company=company,
        role=role,
        job_description=job_description
    )

    return ask_ai(prompt)