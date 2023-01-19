def to_decrypt(cryptotext, delta):
    result = ""
    for i in range (len(cryptotext)):
        if cryptotext[i].isalpha():
            if ord(cryptotext[i])+delta > 122:
                result += chr(ord(cryptotext[i])+delta -26)
            elif ord(cryptotext[i])+delta < 97:
                result += chr(ord(cryptotext[i])+delta +26)
            else:
                result += chr(ord(cryptotext[i])+delta)
        elif  cryptotext[i].isspace():
            result+=" "
    return result 
to_decrypt("ax^$# y&*( (z):-)",-25)