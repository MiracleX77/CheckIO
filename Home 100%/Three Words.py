def checkio(words: str) -> bool:
    words=words.split(" ")
    count=0
    for i in words:
        if i.isdigit()==False:
            count+=1
            if count==3:
                return True
        else:
            count=0
    return False