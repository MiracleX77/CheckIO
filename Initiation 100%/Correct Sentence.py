def correct_sentence(text: str) -> str:
    text=text[0].upper()+text[1:]
    if text[len(text)-1]!=".":
        text=text+"."
    return text