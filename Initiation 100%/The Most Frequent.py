def most_frequent(data: list) -> str:
    maxx=0
    for i in data:
        count=data.count(i)
        if count>maxx:
            maxx=count
            result=i
    return result