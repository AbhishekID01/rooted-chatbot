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

    try:

        print(f"\nUsing model: {model}")

        context_text = str(context)

        print(
            "CONTEXT LENGTH:",
            len(context_text)
        )

        response = client.chat.completions.create(
            model=model,
            max_tokens=500,
            temperature=0.5,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are Rooted AI, a warm and practical "
                        "parenting companion. "
                        "Give complete, natural answers. "
                        "Keep answers short, clear, and friendly. "
                        "Use 1-2 sentences maximum. "
                    )
                },
                {
                    "role": "user",
                    "content": f"""
Question:
{question}

Knowledge:
{context_text}
"""
                }
            ]
        )

        answer = response.choices[0].message.content

        print(
            "FINISH REASON:",
            response.choices[0].finish_reason
        )

        print(
            "ANSWER LENGTH:",
            len(answer)
        )

        print(
            "USAGE:",
            response.usage
        )

        print("\n===== ANSWER =====")
        print(answer)
        print("==================\n")

        return answer

    except Exception as e:

        error_message = str(e)

        print("\n===== OPENROUTER ERROR =====")
        print(error_message)
        print("============================\n")

        return (
            "Sorry, I'm temporarily unavailable right now. "
            "Please try again in a few minutes."
        )