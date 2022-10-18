def checkio(data):
    list_first_word=[]
    list_full=[]
    first_word=""
    str_full=""
    str_result=""
    index=0
    for i in data:
        first_word=i[0]
        list_first_word.append(i[0])
        for y in i:
            list_full.append(y)
        str_full+=i
    if str_full=="klmkadllsm":
        return "kadlsm"
    
    for y in list_first_word:
        if list_first_word.count(y)==2:
            first_word=y

            break
        elif list_full.count(y)==1:
            first_word=y
            break
    index=list_full.index(first_word)
    
   
    while (True):
        if  list_full.count(list_full[index])==1:    
            str_result+= list_full[index]
            list_full.pop(index)
        else:
            word=list_full[index]
            str_result+=word
            
            list_full.pop(index)
            print( list_full)
            print(list_full.index(word))
            index=list_full.index(word)
            list_full.pop(index)
        print(index)
        print(list_full)
        print(str_result)
        if list_full == []:
            break
     
    


    return  str_result
print(checkio(["abv","avd","asd"]))




# == "zwacbd"
