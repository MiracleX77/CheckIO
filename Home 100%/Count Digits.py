def count_digits(text: str) -> int:
    count=0
    for i in text:
        if i.isdigit()==True:
            count+=1
    return  count
