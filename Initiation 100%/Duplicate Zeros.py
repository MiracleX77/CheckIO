def duplicate_zeros(donuts: list) -> list:
    listy=donuts.copy()
    index=0
    for i in range(0,len(donuts)):
        if donuts[i] == 0:
            listy.insert(i+index,0)
            index+=1

    return listy


duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0])