from datetime import date
def days_diff(a, b):
    day_a=0
    a_=date(a[0],a[1],a[2])
    b_=date(b[0],b[1],b[2])
    result=a_-b_
    return abs(result.days)