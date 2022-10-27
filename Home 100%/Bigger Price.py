def bigger_price(limit: int, data: list) -> list:
    list_1=[]
    listy=[]
    for i in data:
        listy.append(i["price"])
    listy.sort(reverse=True)
    for y in range(0,limit):
        for k in data:
            if listy[y]==k["price"]:
                list_1.append(k)
    return list_1
