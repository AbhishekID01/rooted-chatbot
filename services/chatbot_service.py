from services.greeting_service import get_greeting
from services.search_service import search_knowledge
from services.llm_service import generate_response


def get_chatbot_response(message):

    greeting = get_greeting(message)

    if greeting:
        return greeting

    row = search_knowledge(message)
    print("SEARCH RESULT:", row)

    # Found in Excel
    if row:
        return generate_response(
            question=message,
            context=row
        )

    # AI fallback
    return generate_response(
        question=message,
        context="No matching knowledge found."
    )