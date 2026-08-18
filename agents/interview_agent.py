from utils.openrouter import ask_ai


def generate_interview_questions(
    resume_text: str,
    company: str,
    role: str,
    job_description: str
) -> str:

    prompt = f"""
You are preparing a candidate for an interview.

Company:
{company}

Role:
{role}

Job Description:
{job_description}

Candidate Resume:
{resume_text}

Generate the TOP 20 questions the candidate should prepare for.

Divide them into:

## Technical Questions
Questions specific to the technical skills and responsibilities
mentioned in the job description.

## Resume-Based Questions
Questions the interviewer may ask based on the candidate's actual resume.

## Behavioral Questions
Questions related to teamwork, leadership, conflict, failure,
problem solving, communication, etc.

## Company/Role Questions
Questions related specifically to the role and company context
provided.

For each question provide:

### Question
### Why They May Ask
### What a Strong Answer Should Cover

Do not invent company facts that are not provided.

Do not write fake candidate experience.

Make the questions realistic and challenging.
"""

    return ask_ai(prompt)