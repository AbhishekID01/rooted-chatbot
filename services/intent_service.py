def detect_intent(message):

    msg = message.lower()

    # Slang / Meme
    if any(word in msg for word in [
        "sigma", "rizz", "skibidi", "gyatt"
    ]):
        return "slang"

    # Symptoms
    if any(word in msg for word in [
        "anxiety", "depression", "stress",
        "hides phone", "hide phone"
    ]):
        return "symptom"

    # Digital Dangers
    if any(word in msg for word in [
        "sextortion", "grooming", "porn"
    ]):
        return "danger"

    # Media
    if any(word in msg for word in [
        "movie", "show", "netflix",
        "tiktok", "youtube", "discord", "roblox"
    ]):
        return "media"

    # Creator
    if any(word in msg for word in [
        "mrbeast"
    ]):
        return "creator"

    return "faq"