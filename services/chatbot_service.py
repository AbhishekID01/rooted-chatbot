from services.search_service import search_knowledge
from services.llm_service import generate_response


def get_chatbot_response(message):

    row = search_knowledge(message)

    if not row:
        return "Sorry, I couldn't find information about that topic."

    return generate_response(
        question=message,
        context=row
    )