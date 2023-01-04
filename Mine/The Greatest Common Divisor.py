def greatest_common_divisor(*args: int) -> int:
    args=list(args)
    if len(args) >= 2:
        for i in range(1,len(args)):
            list_gcd =[args[i-1],args[i]]
            list_gcd.sort(reverse=True)
            while list_gcd[1] !=0:
                a = list_gcd[0]
                list_gcd[0] = list_gcd[1]
                list_gcd[1] = a%list_gcd[0]
            args[i] = list_gcd[0]
    return args[-1]
greatest_common_divisor(48,18)