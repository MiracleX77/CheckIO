def first_word(text: str) -> str:
   
    for i in range(0,len(text)):
        if text[i] ==" ":
            text=text[0:i]
            break
    return text