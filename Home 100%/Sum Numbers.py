def sum_numbers(text: str) -> int:
    text=text.split(" ")
    numsum=0
    for i in text:
        if i.isdigit()==True:
            i=int(i)
            numsum+=i
    return numsum