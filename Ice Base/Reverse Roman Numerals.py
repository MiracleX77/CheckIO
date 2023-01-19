ROMAN = {
    "M":1000,
    "D":500,
    "C":100,
    "L":50,
    "X":10,
    "V":5,
    "I":1
}
def reverse_roman(roman_string):
    result = 0
    i=0
    while True:
        print(roman_string[i])
        if i < len(roman_string)-1:
            if ROMAN[roman_string[i]] < ROMAN[roman_string[i+1]]:
                result+=ROMAN[roman_string[i+1]] - ROMAN[roman_string[i]]
                i+=1
                if i == len(roman_string)-1:
                    break
            else:
                result+=ROMAN[roman_string[i]]
        else:
            result+=ROMAN[roman_string[i]]
            break
        i+=1
    return result
reverse_roman("MMMCMXCIX")