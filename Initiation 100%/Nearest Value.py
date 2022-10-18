def nearest_value(values: set, one: int) -> int:
    listy=[]
    for i in values:
        listy.append(i)
    listy.sort()
    for y in range(0,len(listy)):
        if one==0:
            minn=listy[0]
            maxx=listy[0]
        elif one>=listy[y]:
            if one>=listy[len(listy)-1]:
                minn=listy[len(listy)-1]
                maxx=listy[len(listy)-1]
            else:
                minn=listy[y]
                maxx=listy[y+1]
    if maxx-one<one-minn:
        return maxx
    else:
        return minn