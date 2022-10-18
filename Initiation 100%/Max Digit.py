def max_digit(number: int) -> int:
    max_list=[]
    for i in str(number):
        max_list.append(int(i))
    return max(max_list)