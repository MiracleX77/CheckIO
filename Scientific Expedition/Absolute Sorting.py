def noMinus(ele):
    if ele<0:
        ele=ele*-1
    return ele
def checkio(values: list) -> list:
    values.sort()
    values.sort(key=noMinus)
    return values



checkio([-20, -5, 10, 15])