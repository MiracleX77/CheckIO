def translate(text: str) -> str:
    result=''
    vowels="aeiouy"
    while (text!=""):
        result+=text[0]
        if text[0] in vowels:
            text=text[3:]
        elif text[0]==" ":
            text=text[1:]
        else:
            text=text[2:]
    return result


print("Example:")
print(translate("hieeelalaooo"))