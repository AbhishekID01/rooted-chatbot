from services.greeting_service import get_greeting
from services.search_service import search_knowledge
from services.llm_service import generate_response


def get_chatbot_response(message):

    greeting = get_greeting(message)

    if greeting:
        return greeting

    row = search_knowledge(message)

    if not row:
        return (
            "I don't have information about that yet. Try asking about internet slang, social media apps, creators, online safety, or parenting concerns."
        )

    return generate_response(
        question=message,
        context=row
    )