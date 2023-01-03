def count_chains(circles) -> int:
    group = len(circles)
    list_cir = []
    list_group=[]
    i=0
    for cir in circles:
        x = cir[0] - cir[2]
        y = cir[1] - cir[2]
        list_cir.append([x,y,cir[2]*2])
    print(list_cir)
    #[[0, 0, 2], [3, 1, 2], [3, 2, 2]]
    

    return 0
count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]) 