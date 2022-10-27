
def checkio(array: list) -> int:
    numsum=0
    if array==[]:
        return 0
    for i in range(0,len(array),2):
        numsum+=array[i]
    return numsum*array[len(array)-1]