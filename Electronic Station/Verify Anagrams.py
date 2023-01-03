def verify_anagrams(a: str, b: str) -> bool:
    a=a.lower()
    a=a.replace(" ","")
    b=b.lower()
    b=b.replace(" ","")
    if len(a)!=len(b):
        return False
    for i in a:
        if b.find(i) !=-1:
            b=b[:b.find(i)]+b[b.find(i)+1:]

    if b =="":
        return True
    return False