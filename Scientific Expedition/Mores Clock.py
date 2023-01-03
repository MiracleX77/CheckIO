def checkio(time_string: str) -> str:
    time=time_string.split(":")
    count=2
    for i in range (len(time)):
        if len(time[i]) == 1:
            time[i]="0"+time[i]
        bin_for_digit=""
        for y in range(len(time[i])):
            binny=bin(int(time[i][y]))
            binny=binny[2:]
            if len(binny)!=count:
                while len(binny)!=count:
                    binny="0"+binny
            bin_for_digit+=binny+" "
            if y == 0  :
                count=4
            else:
                count=3
        time[i]=bin_for_digit
    result=": ".join(time)
    result=result.replace("1","-")
    result=result.replace("0",".")
    return result[:29]
checkio("10:37:0")