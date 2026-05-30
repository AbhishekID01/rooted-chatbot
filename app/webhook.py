from fastapi import APIRouter, Request
from fastapi.responses import PlainTextResponse
from dotenv import load_dotenv

from services.chatbot_service import get_chatbot_response
from services.whatsapp_service import send_whatsapp_message

import os

load_dotenv()

router = APIRouter()

VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")


@router.get("/webhook")
async def verify(request: Request):

    mode = request.query_params.get("hub.mode")
    token = request.query_params.get("hub.verify_token")
    challenge = request.query_params.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return PlainTextResponse(content=challenge)

    return PlainTextResponse(
        content="verification failed",
        status_code=403
    )


@router.post("/webhook")
async def receive(request: Request):

    data = await request.json()

    print("\n===== WHATSAPP WEBHOOK =====")
    print(data)
    print("============================\n")

    try:

        value = data["entry"][0]["changes"][0]["value"]

        # Ignore status updates
        if "messages" not in value:
            print("Status webhook received")
            return {"status": "ok"}

        message = value["messages"][0]["text"]["body"]
        sender = value["messages"][0]["from"]

        print("MESSAGE:", message)
        print("SENDER:", sender)

        reply = get_chatbot_response(message)

        print("REPLY:", reply)

        send_whatsapp_message(
            sender,
            reply
        )

    except Exception as e:
        print("ERROR:", str(e))

    return {"status": "ok"}