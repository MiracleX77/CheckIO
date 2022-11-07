import math
def split_list(items: list) -> list:
    listy1=[]
    listy2=[]
    for i in range(0,len(items)):
        if i<=math.floor((len(items)-1)/2):
            listy1.append(items[i])
        else:
            listy2.append(items[i])
    items.clear()
    items.append(listy1)
    items.append(listy2)


    return items