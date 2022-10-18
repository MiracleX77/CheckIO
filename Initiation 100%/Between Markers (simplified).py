def between_markers(text: str, begin: str, end: str) -> str:
    text=text[text.find(begin)+1:text.find(end)]
    return text