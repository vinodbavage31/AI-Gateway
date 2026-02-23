async def moderate(text: str):
    banned_words = ["hack", "attack"]

    for word in banned_words:
        if word in text.lower():
            return False

    return True