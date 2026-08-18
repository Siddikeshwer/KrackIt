from utils.openrouter import ask_ai


def analyze_job_description(company: str, role: str, job_description: str) -> str:

    prompt = f"""
Analyze this job description for a candidate preparing to apply.

Company:
{company}

Role:
{role}

Job Description:
{job_description}

Identify:

1. Core responsibilities
2. Required technical skills
3. Preferred technical skills
4. Soft skills
5. Required experience
6. Education requirements
7. Important technologies/tools
8. Important keywords
9. Likely interview topics
10. What the hiring manager probably cares about most

Return a concise but useful analysis.

Do not invent requirements that aren't present.
"""

    return ask_ai(prompt)