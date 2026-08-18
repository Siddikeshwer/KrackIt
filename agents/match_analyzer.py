from utils.openrouter import ask_ai


def analyze_match(
    resume_text: str,
    job_analysis: str,
    company: str,
    role: str
) -> str:

    prompt = f"""
You are KrackIt's Job Match Agent.

Analyze how well this candidate matches the target job.

COMPANY:
{company}

ROLE:
{role}

CANDIDATE RESUME:
{resume_text}

JOB ANALYSIS:
{job_analysis}

Create a detailed match report.

Use this structure:

# 🎯 JOB MATCH REPORT

## Overall Match Score
Give a score from 0-100.

Explain why.

## Skill Match
Separate into:

### Strong Matches
Skills clearly demonstrated in the resume.

### Partial Matches
Skills that appear related but are not strongly demonstrated.

### Missing Skills
Important skills from the job that are not demonstrated in the resume.

## Experience Match
Compare the candidate's experience with the role requirements.

## Responsibility Match
Explain which job responsibilities the candidate is prepared for
and which may be difficult.

## ATS Match
Identify important job-description keywords that are:
- Already present
- Missing
- Present but weakly demonstrated

## Education Match
Compare education requirements with the candidate's education.

## Top Strengths
Give the 5 strongest reasons this candidate could be shortlisted.

## Top Weaknesses
Give the 5 biggest weaknesses.

## Rejection Risks
Identify the most likely reasons a recruiter could reject this application.

Rank each risk:
HIGH / MEDIUM / LOW

## Priority Improvements
Give the 5 most important things the candidate should improve
before applying.

IMPORTANT RULES:

1. Never invent skills, experience, projects, certifications,
   achievements, or education.
2. Only consider information actually present in the resume.
3. Do not recommend keyword stuffing.
4. Missing information should be treated as unknown, not assumed.
5. Be honest even if the match score is low.
6. Focus specifically on this job and role.
"""

    return ask_ai(prompt)