from services.slang_service import get_slang
from services.digital_danger_service import get_danger
from services.faq_service import get_faq
from services.symptom_service import get_symptom
from services.media_service import get_media
from services.meme_service import get_meme
from services.trend_service import get_trend
from services.tough_topic_service import get_tough_topic
from services.creator_service import get_creator


def search_knowledge(message):

    services = [
        get_slang,
        get_danger,
        get_faq,
        get_symptom,
        get_media,
        get_meme,
        get_trend,
        get_tough_topic,
        get_creator
    ]

    for service in services:

        result = service(message)

        if result:
            return result

    return None