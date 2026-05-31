import os
import requests
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv(
"WHATSAPP_ACCESS_TOKEN"
)

PHONE_NUMBER_ID = os.getenv(
"WHATSAPP_PHONE_NUMBER_ID"
)

def send_whatsapp_message(to, message):

```
url = (
    f"https://graph.facebook.com/v25.0/"
    f"{PHONE_NUMBER_ID}/messages"
)

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

payload = {
    "messaging_product": "whatsapp",
    "to": to,
    "type": "text",
    "text": {
        "body": message
    }
}

response = requests.post(
    url,
    headers=headers,
    json=payload
)

return response.json()
```

def send_welcome_menu(to):

```
url = (
    f"https://graph.facebook.com/v25.0/"
    f"{PHONE_NUMBER_ID}/messages"
)

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

payload = {
    "messaging_product": "whatsapp",
    "to": to,
    "type": "interactive",
    "interactive": {
        "type": "button",
        "body": {
            "text": "🌱 Welcome to Rooted AI\n\nChoose a topic:"
        },
        "action": {
            "buttons": [
                {
                    "type": "reply",
                    "reply": {
                        "id": "apps",
                        "title": "📱 Apps"
                    }
                },
                {
                    "type": "reply",
                    "reply": {
                        "id": "creators",
                        "title": "🎬 Creators"
                    }
                },
                {
                    "type": "reply",
                    "reply": {
                        "id": "slang",
                        "title": "💬 Slang"
                    }
                }
            ]
        }
    }
}

response = requests.post(
    url,
    headers=headers,
    json=payload
)

return response.json()
```
