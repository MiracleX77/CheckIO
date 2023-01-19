def checkio(text, word):
    text=text.replace(" ","")
    text=text.split("\n")
    list_result=[0,0,0,0]
    print(text)
    for i in range (0,len(text)):
        print(list_result)
        for j in range(0,len(text[i])):
            if text[i][j] == word[0]:
                
                for x in range (1,len(word)):
                    
                    if j+x <len(text[i]):
                        if text[i][j+x] != word[x]:
                            break
                        if x == len(word)-1:
                            list_result[0]=i+1
                            list_result[1]=j+1
                            list_result[2]=i+1
                            list_result[3]=j+x+1
                            return list_result
                for y in range (1,len(word)):
                    print(i)
                    if len(word)+i-1 < len(text):

                        if text[i+y][j] != word[y]:
                                break
                        if y == len(word)-1:
                                list_result[0]=i+1
                                list_result[1]=j+1
                                list_result[2]=i+y+1
                                list_result[3]=j+1
                                return list_result
                    
        if list_result[3] != 0:
            return list_result
    return list_result
checkio("Twas brillig, and the slithy toves\nDid gyre and gimble in the wabe;\nAll mimsy were the borogoves,\nAnd the mome raths outgrabe.","stog")