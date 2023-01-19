def caps_lock(text: str) -> str:
    # your code here
    control = 0
    text=text.split("a")
    for i in range(len(text)):
        if control%2==1:
            text[i]=text[i].upper()
        control+=1
    return "".join(text)
caps_lock("Why are you asking me that?")