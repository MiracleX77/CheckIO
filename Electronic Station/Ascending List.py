def is_ascending(items: list[int]) -> bool:
    for i in range(1,len(items)):
        if items[i]<=items[i-1]:
            return False
    return True
is_ascending([1, 1, 1, 1])