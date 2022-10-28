def between_markers(text: str, begin: str, end: str) -> str:
    index_b=text.find(begin)
    index_e=text.find(end)
    if index_b==-1 and index_e==-1:
        return text
    elif index_b==-1:
        index_b=0
        return text[index_b:index_e]
    elif index_e==-1:
        index_e=len(text)
    elif index_e<index_b:
        return ""
    return text[index_b+len(begin):index_e]