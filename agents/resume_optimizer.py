from utils.openrouter import ask_ai


def optimize_resume(
    resume_text: str,
    match_analysis: str,
    company: str,
    role: str,
    job_description: str
) -> str:

    prompt = f"""
You are KrackIt's Resume Optimization Agent.

Your task is to improve the candidate's resume specifically
for the target job.

COMPANY:
{company}

ROLE:
{role}

JOB DESCRIPTION:
{job_description}

ORIGINAL RESUME:
{resume_text}

MATCH ANALYSIS:
{match_analysis}

Create a practical resume optimization report.

Use this structure:

# 📄 RESUME OPTIMIZATION

## 1. Overall Resume Assessment
Explain how effective the current resume is for this specific job.

## 2. Critical Changes
List the most important changes that should be made.

For every change use:

### Current
Quote or describe the existing resume content.

### Problem
Explain why it is weak for this job.

### Recommended
Provide an improved version.

### Reason
Explain why the new version is better.

## 3. Professional Summary
Write a tailored professional summary based ONLY on
the candidate's real experience.

## 4. Experience Improvements
Rewrite weak experience bullets where appropriate.

Focus on:
- Relevant technologies
- Responsibilities
- Results
- Impact
- Measurable achievements when they are actually present

Do NOT create fake numbers.

## 5. Project Improvements
Identify projects that should be highlighted for this role.

Rewrite project descriptions where useful.

Do NOT invent project features or technologies.

## 6. Skills Section
Recommend how the skills section should be organized.

Separate:

### Keep
Skills clearly supported by the resume.

### Highlight
Skills that are especially relevant to the job.

### Add Only If True
Skills mentioned in the job description that the candidate
should add ONLY if they genuinely possess them.

## 7. ATS Optimization
Give natural recommendations for improving ATS compatibility.

Do NOT recommend keyword stuffing.

## 8. Remove or Reduce
Identify information that is irrelevant, repetitive,
outdated, or taking unnecessary space.

## 9. Recommended Resume Structure
Give the ideal section order for this candidate.

## 10. Final Checklist
Give a concise checklist the candidate should complete
before submitting the application.

CRITICAL RULES:

- Never fabricate experience.
- Never fabricate achievements.
- Never fabricate numbers.
- Never fabricate certifications.
- Never fabricate skills.
- Never claim the candidate used a technology unless the
  resume supports it.
- If something is missing, say it is missing.
- Preserve the candidate's actual background.
- Optimize for the specific job, not generic ATS scoring.
"""
    
    return ask_ai(prompt)