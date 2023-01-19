from datetime import datetime


import datetime
def time_converter(time):
    string=""
    x=datetime.datetime(1970,1,1,int(time[:2]),int((time[3:])))
    if int(x.strftime("%I"))<10:
        string+=x.strftime("%I:%M")[1:]
    else:
        string+=x.strftime("%I:%M")
    a=x.strftime("%p").lower()
    string+=" "+a[0]+"."+a[1]+"."
    return string
time_converter("23.15")