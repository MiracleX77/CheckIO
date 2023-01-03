
def is_number(val: str) -> bool:
    try:
        float(val)
        str(val)
        for i in val:
            if i.isalpha() == True:
                return False
    except:
        return False
    return True
is_number("+34.0") 