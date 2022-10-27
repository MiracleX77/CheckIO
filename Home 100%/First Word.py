
def first_word(text: str) -> str:
    index_f=0
    count=0
    check=0
    for i in text:
        if i.isalpha()==True and check==0:
            check=1
            index_f=count
        elif i=="." and check!=0:
            break
        elif i=="," and check!=0:
            break
        elif i==" " and check!=0:
            break
        count+=1
    return text[index_f:count]