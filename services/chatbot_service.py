from services.greeting_service import get_greeting
from services.search_service import search_knowledge
from services.llm_service import generate_response

from services.formatter_service import (
    format_creator,
    format_slang,
    format_danger,
    format_media,
    format_symptom,
    format_trend,
    format_tough_topic,
    format_faq
)


def get_chatbot_response(message):

    greeting = get_greeting(message)

    if greeting:
        return greeting

    if "apps" in message:
        return (
            "Apps & Platforms\n\n"
            "• Roblox\n"
            "• Discord\n"
            "• TikTok\n"
            "• Character AI\n\n"
            "Type any app name to learn more."
        )

    if "creators" in message:
        return (
            "Creators & Influencers\n\n"
            "• MrBeast\n"
            "• IShowSpeed\n"
            "• Bluey\n\n"
            "Type any creator name to learn more."
        )

    if "slang" in message:
        return (
            "Slang Dictionary\n\n"
            "• Rizz\n"
            "• Gyat\n"
            "• Skibidi\n\n"
            "Type any slang word to learn more."
        )

    if message == "dangers":
        return (
            "Online Dangers\n\n"
            "• Grooming\n"
            "• Sextortion\n"
            "• Gaming Rage\n"
            "• Online Scams\n\n"
            "Type any danger name to learn more."
        )

    if message == "faq":
        return (
            "Parent FAQs\n\n"
            "• How much screen time is okay?\n"
            "• Is Roblox safe?\n"
            "• Is TikTok safe?\n\n"
            "Ask your question directly."
        )

    row = search_knowledge(message)

    print("SEARCH RESULT:", row)

    if row:

        if "creator_type" in row:
            return format_creator(row)

        if "slang" in row:
            return format_slang(row)

        if "danger_type" in row:
            return format_danger(row)

        if "media_type" in row:
            return format_media(row)

        if "symptom" in row:
            return format_symptom(row)

        if "platform" in row:
            return format_trend(row)

        if "parent_emotion" in row:
            return format_tough_topic(row)

        if "question" in row and "answer" in row:
            return format_faq(row)

        return generate_response(
            question=message,
            context=row
        )

    print("UNKNOWN QUESTION:", message)

    return generate_response(
        question=message,
        context="No matching knowledge found."
    )