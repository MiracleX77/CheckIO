def sum_digits(num: int) -> int:
    ans=0
    while True:
        num=str(num)
        for i in num:
            ans+=int(i)
        if ans>9:
            num=ans
            ans=0
        else:
            break
    return ans