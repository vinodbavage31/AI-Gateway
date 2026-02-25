async def moderate(text: str):
    banned_words = ["hack", "attack"]

    for word in banned_words:
        if word in text.lower():        #check case-insensitive
            return False            #Meaning unsafe

    return True