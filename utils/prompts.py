def build_job_analysis_prompt(
    resume_text: str,
    company: str,
    role: str,
    job_description: str
) -> str:

    return f"""
Analyze this candidate for the following job.

COMPANY:
{company}

ROLE:
{role}

JOB DESCRIPTION:
{job_description}

CANDIDATE RESUME:
{resume_text}

Perform a detailed job-fit analysis.

Return the response using this structure:

# KRACKIT JOB ANALYSIS

## 1. Overall Match Score
Give a score out of 100.

Explain the score briefly.

## 2. Strengths
List the candidate's strongest points for this specific job.

## 3. Matching Skills
Identify skills from the resume that directly match the job description.

## 4. Missing Skills
Identify important skills mentioned in the job description that are missing
or not clearly demonstrated in the resume.

## 5. Experience Match
Explain how well the candidate's experience matches the role.

## 6. Resume Problems
Identify weaknesses in the current resume that could reduce the chance
of getting shortlisted.

## 7. Resume Changes
Give specific changes that should be made.

For every important change explain:
- Current problem
- Recommended change
- Why it matters for this job

## 8. ATS Keywords
List the most important keywords from the job description that should
naturally appear in the resume.

Do NOT recommend keyword stuffing.

## 9. Biggest Risks
List the top 5 things that could cause rejection.

## 10. Action Plan
Give the candidate the 5 most important things they should do before applying.

IMPORTANT:
- Do not invent experience.
- Do not claim the candidate has skills that are absent from the resume.
- Base the analysis specifically on this company's job description.
- Be direct and practical.
"""