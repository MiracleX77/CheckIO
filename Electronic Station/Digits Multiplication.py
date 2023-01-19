import math 
def checkio(number: int):
    number=str(number)
    number=number.replace("0","")
    
    number=list(number)
    print(number)
    for  i in range (len(number)):
        number[i] = int(number[i])
    print(number)

    return math.prod(number)
checkio(1020)