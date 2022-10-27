
def checkio(data: list) -> list:
    listyy=[]
    for i in data:
        check=0
        for k in data:
            if i==k:
                check+=1
                if check==2:
                    listyy.append(i)
    return listyy