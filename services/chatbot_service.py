from services.greeting_service import get_greeting
from services.search_service import search_knowledge
from services.llm_service import generate_response

from services.formatter_service import (
    format_creator,
    format_slang
)


def get_chatbot_response(message):

    greeting = get_greeting(message)

    if greeting:
        return greeting

    row = search_knowledge(message)

    print("SEARCH RESULT:", row)

    if row:

        # Creator
        if "creator_type" in row:
            return format_creator(row)

        # Slang
        if "slang" in row:
            return format_slang(row)

        # Other categories still use AI
        return generate_response(
            question=message,
            context=row
        )

    # No match found
    return generate_response(
        question=message,
        context="No matching knowledge found."
    )