def end_zeros(num: int) -> int:
    count=0
    if num==0:
        return 1
    while True:
        if num%(10**(1+count))==0:
            count+=1
        else:
            return count