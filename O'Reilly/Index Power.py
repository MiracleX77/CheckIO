def index_power(array: list, n: int) -> int:
    if n > len(array)-1:
        return -1
    else:
        return array[n]**n