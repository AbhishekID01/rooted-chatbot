import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(dotenv_path=Path(".env"))

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


def generate_response(question, context):

    model = os.getenv("MODEL")

    prompt = f"""
You are Rooted AI.

You are a warm parenting companion.

Rules:
- Sound human
- Sound warm
- Never sound robotic
- Never say "As an AI"
- Keep answers under 120 words

Question:
{question}

Knowledge:
{context}
"""

    try:

        print(f"\nUsing model: {model}")

        response = client.chat.completions.create(
            model=model,
            max_tokens=1500,
            temperature=0.7,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        answer = response.choices[0].message.content

        print("\n===== ANSWER =====")
        print(answer)
        print("==================\n")

        return answer

    except Exception as e:

        error_message = str(e)

        print("\n===== OPENROUTER ERROR =====")
        print(error_message)
        print("============================\n")

        return f"ERROR: {error_message}"