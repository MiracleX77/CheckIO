def checkio(num: int) -> str:
    
    if num %3 == 0 and num%5 == 0:
        return "Fizz Buzz"
    elif num %3 == 0:
        return "Fizz"
    elif num %5 == 0:
        return "Buzz"
    return str(num)
checkio(15)