ROMAN = {
    1000:"M",
    900:"CM",
    500:"D",
    400:"CD",
    100:"C",
    90:"XC",
    50:"L",
    40:"XL",
    10:"X",
    9:"IX",
    5:"V",
    4:"IV",
    1:"I"
}
def checkio(data):
    Roman_string =""
    while data != 0 :
        for i in ROMAN.keys():
            if data>=i:
                data = data - i
                Roman_string+=ROMAN[i]
    return Roman_string
checkio(9)        
