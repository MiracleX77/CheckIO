def isometric_strings(a: str, b: str) -> bool:
    dictt={}
    if len(a)==len(b):
        for i in range(len(a)):
            if a[i] not in dictt:
                dictt.update({a[i]:b[i]})
            else:
                if b[i] != dictt[a[i]]:
                    return False
    return True
isometric_strings("adda", "egga")


