from utils.openrouter import ask_ai


def generate_application_package(
    resume_text: str,
    company: str,
    role: str,
    job_description: str
) -> str:

    prompt = f"""
Create an application package for this candidate.

Company:
{company}

Role:
{role}

Job Description:
{job_description}

Candidate Resume:
{resume_text}

Generate:

# COVER LETTER

Write a professional, personalized cover letter for this exact role.

Do not invent experience, achievements, projects, or skills.

---

# COLD EMAIL TO HR

Create a concise cold email to a recruiter or HR person.

Include:
- Strong subject line
- Short introduction
- Why the candidate is relevant
- Specific role
- Clear call to action

Keep it concise.

---

# LINKEDIN MESSAGE

Create a short recruiter connection/message suitable for LinkedIn.

Keep it natural and under 100 words.

---

# FOLLOW-UP EMAIL

Create a professional follow-up email that can be sent
after applying if there is no response.

Do not use fake claims or statistics.
"""

    return ask_ai(prompt)