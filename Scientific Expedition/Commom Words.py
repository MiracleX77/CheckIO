
def checkio(line1: str, line2: str) -> str:
    result=[]
    line1=line1.split(",")
    line2=line2.split(",")
    for i in line1:
        for y in line2:
            if i == y :
                result.append(i)
    result.sort()
    result=",".join(result)
    return result
checkio("one,two,three", "four,five,one,two,six,three")