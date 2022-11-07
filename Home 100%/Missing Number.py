def missing_number(items: list[int]) -> int:
    items.sort()
    for i in range(1,len(items)-1):

        if items[i]-items[i-1]!=items[i+1]-items[i]:
            if items[i]-items[i-1]<items[i+1]-items[i]:
                return items[i]+(items[i]-items[i-1])
            else:
                return items[i]-(items[i+1]-items[i])
            
    return 0