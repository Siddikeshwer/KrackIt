import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

if not API_KEY:
    raise ValueError("OPENROUTER_API_KEY not found in .env")


client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY
)

MODEL = "openai/gpt-oss-20b"


def ask_ai(prompt: str) -> str:

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": """
You are KrackIt, an expert AI career agent.

Your goal is to help candidates maximize their chances
of getting shortlisted and succeeding in interviews.

Be specific, practical and honest.

Never invent:
- Skills
- Experience
- Projects
- Certifications
- Achievements
- Numbers
"""
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content