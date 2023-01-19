def checkio(data) :
    data.sort()
    if len(data)%2==0:
   
        return ((data[int((len(data)/2)-1)])+(data[int((len(data)/2))]))/2
    else:
        return data[len(data)//2]