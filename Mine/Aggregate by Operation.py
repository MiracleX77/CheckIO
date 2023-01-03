def convert_operation(str,num1,num2):
    if str == "+":
        return num1+num2
    elif str == "-":
        return num1-num2
    elif str == "*":
        return num1*num2
    elif str == "/":
        if num1 == 0:
            return 0
        else:
            return num1/num2
    else:
        return num2
def aggr_operation(data: list[tuple[str, int]]) -> dict[str, int]:
    dicty = {}
    for i in data:
        if len(i[0]) != 1:
            if i[0][1:] not in dicty.keys() :
                value = convert_operation(i[0][0],0,i[1])
                dicty.update({i[0][1:]:value})
            else:
                value = convert_operation(i[0][0],dicty[i[0][1:]],i[1])
                dicty.update({i[0][1:]:value})
            if value == 0 :
                dicty.pop(i[0][1:])
    return dicty

aggr_operation([('+a', -5), ('-aa', -20), ('*aa', 5)])