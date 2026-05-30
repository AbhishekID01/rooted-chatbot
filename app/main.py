from fastapi import FastAPI
from pydantic import BaseModel

from services.search_service import search_knowledge
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

    row = search_knowledge(
        request.message
    )

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