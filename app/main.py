from fastapi import FastAPI
from pydantic import BaseModel

from services.slang_service import get_slang
from services.digital_danger_service import get_danger
from services.faq_service import get_faq
from services.symptom_service import get_symptom
from services.media_service import get_media
from services.meme_service import get_meme
from services.trend_service import get_trend
from services.tough_topic_service import get_tough_topic
from services.creator_service import get_creator

from services.llm_service import generate_response

app = FastAPI()


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {
        "status": "running"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    row = None

    # 1. Slang
    row = get_slang(request.message)

    # 2. Digital Danger
    if not row:
        row = get_danger(request.message)

    # 3. FAQ
    if not row:
        row = get_faq(request.message)

    # 4. Symptom
    if not row:
        row = get_symptom(request.message)

    # 5. Media
    if not row:
        row = get_media(request.message)

    # 6. Meme
    if not row:
        row = get_meme(request.message)

    # 7. Trend
    if not row:
        row = get_trend(request.message)

    # 8. Tough Topic
    if not row:
        row = get_tough_topic(request.message)

    # 9. Creator
    if not row:
        row = get_creator(request.message)

    if not row:
        return {
            "response": "I couldn't find information about that topic yet."
        }

    response = generate_response(
        question=request.message,
        context=row
    )

    return {
        "response": response
    }