def beginning_zeros(number: str):
    count=0
    if number.find('0')==0:
        for i in number:
            if i!='0':
                return count
            else:
                count+=1
        return count
    else:
        return 0