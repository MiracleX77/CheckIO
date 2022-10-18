def backward_string(val: str) -> str:
    string_reve=""
    for i in range(0,len(val)):
        string_reve+=val[len(val)-1-i]
    return string_reve