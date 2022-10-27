
def changing_direction(element):
    count=0
    check = 0
    for i in range (1,len(element)-1):
        if element[i]>element[i-1]:
            check = 1
        if element[i]>element[i+1] and element[i] >= element[i-1] and check == 1:
            count+=1
            print("1",i)
        elif element[i]<element[i-1] and element[i] <element[i+1]:
            count+=1
            print("2",i)
    return count