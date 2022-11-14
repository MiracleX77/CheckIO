def chunking_by(items: list, size: int):
    listy=[]
    count=len(items)//size

    for i in range(0,count):
        listy1=[] 
        for y in range(0,size):
            listy1.append(items[0])
            items.remove(items[0])      
        listy.append(listy1)
    if items!=[]:
        listy.append(items)
    return listy