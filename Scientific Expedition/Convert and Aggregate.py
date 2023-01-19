def conv_aggr(data: list[tuple[str, int]]) -> dict[str, int]:
    dicty = {}
    for i in data:
        if i[0]!="":
            if i[0] not in dicty.keys() and i[1]!= 0 :
                dicty.update({i[0]:i[1]})
            else:
                if dicty!={}:
                    if i[1]+dicty[i[0]] == 0:
                        dicty.pop(i[0])
                    else:
                        dicty.update({i[0]:i[1]+dicty[i[0]]})
    return dicty
conv_aggr([("a", 0), ("b", 0)])