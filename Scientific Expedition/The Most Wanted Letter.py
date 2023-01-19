
def checkio(text: str) -> str:
    text=text.lower()
    max_char = 0
    list_eques_char=[]
    for i in text:
        if i.isalpha():
            if text.count(i)>max_char:
                list_eques_char.clear()
                max_char=text.count(i)
                list_eques_char.append(i)
                text=text.replace(i," ")
            elif text.count(i)== max_char:
                list_eques_char.append(i)
                text=text.replace(i," ")
    list_eques_char.sort()
    return list_eques_char[0]
        
checkio("Z")