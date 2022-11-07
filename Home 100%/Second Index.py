def second_index(text: str, symbol: str):

    indexfirst=text.find(symbol)
    indextwo=text.find(symbol,indexfirst+1)
    if indextwo==-1:
        return None
    return indextwo