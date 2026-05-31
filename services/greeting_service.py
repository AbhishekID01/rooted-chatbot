def get_greeting(message):

    greetings = [
        "hi",
        "hello",
        "hey",
        "good morning",
        "good evening"
    ]

    if message.lower().strip() in greetings:
        return (
            "Hello! 👋 I'm Rooted AI. "
            "Ask me about internet slang, TikTok, YouTubers, online safety, or parenting concerns."
        )

    return None