class Data:
    def __init__(self,value,index,count=0) -> None:
        self.value=value
        self.index=index
        self.count=count
        pass

def frequency_sort(items):
    count={}
    for i in range(len(items)):
        count.setdefault(items[i],Data(items[i],i)).count+=1
    values=[*count.values()]
    values.sort(key=lambda x: (-x.count, x.index))
    k = 0
    for data in values:
        for j in range(data.count):
            items[k] = data.value
            k += 1
    
    return items
