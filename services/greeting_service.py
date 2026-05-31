def get_greeting(message):

```
greetings = [
    "hi",
    "hello",
    "hey",
    "heyy",
    "hii",
    "start"
]

if message.lower().strip() not in greetings:
    return None

return """
```

🌱 Welcome to Rooted AI

I'm here to help parents understand their child's digital world.

1️⃣ Apps & Games
📱 Roblox, Discord, TikTok, Snapchat

2️⃣ Creators
🎬 MrBeast, YouTubers, Influencers

3️⃣ Slang & Memes
💬 Rizz, Sigma, Delulu, Gyatt

4️⃣ Online Safety
🚨 Grooming, Scams, Cyberbullying

5️⃣ Parent Concerns
🩺 Screen Addiction, Gaming Rage, Anxiety

Try asking:

• What is rizz?
• Is Roblox safe?
• Who is MrBeast?
• What are signs of grooming?

Type your question below 👇
""".strip()
