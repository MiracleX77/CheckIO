
import math
def checkio(radius):
    count = 0
    partial = 0
    if radius >0:
        for i in range(1,round(radius+1)):
            for j in range(1,round(radius+1)):
                if (i**2 + j**2)**0.5<radius:
                    count+=1
    print(count*4)

    return [count*4,(math.ceil(radius)*2-1)*4]
checkio(2)