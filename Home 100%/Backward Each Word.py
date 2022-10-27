def backward_string_by_word(text: str) -> str:
    listy=[]
    string=""
    for i in text:
        if i==" ":
            listy.reverse()
            listy.append(i)
            string+="".join(listy)
            listy.clear()
        else:
            listy.append(i)
    listy.reverse()
    string+="".join(listy)
    return string 
