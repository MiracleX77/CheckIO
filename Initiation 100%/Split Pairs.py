def split_pairs(a):
    listy=[]
    for i in range(0,len(a)-1,2):
        listy.append(a[i:i+2])
    if len(a)%2==1:
        listy.append(a[len(a)-1]+"_")
    return listy