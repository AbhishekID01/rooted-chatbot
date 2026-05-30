def detect_intent(message):

    msg = message.lower()

    if any(word in msg for word in ["sigma", "rizz", "skibidi", "gyatt"]):
        return "slang"

    if any(word in msg for word in ["anxiety", "depression", "stress"]):
        return "symptom"

    if any(word in msg for word in ["sextortion", "grooming", "porn"]):
        return "danger"

    if any(word in msg for word in ["movie", "show", "netflix"]):
        return "media"

    return "faq"