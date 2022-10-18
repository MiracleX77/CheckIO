
def replace_first(items: list):
    if items==[]:
        return items
    num=items[0]
    items.remove(items[0])
    items.append(num)
   
    return items