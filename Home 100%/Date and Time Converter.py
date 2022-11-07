import datetime
def date_time(time):
    xtime=datetime.datetime(int(time[6:10]),int(time[3:5]),int(time[:2]))
    if int(time[11:13])==1:
        hourstr=str(int(time[11:13]))+" hour "
    else:
        hourstr=str(int(time[11:13]))+" hours "
    if int(time[14:16])==1:
        minstr=str(int(time[14:16]))+" minute"
    else:
        minstr=str(int(time[14:16]))+" minutes"
    return str(int(time[:2]))+xtime.strftime(" %B %Y year ")+hourstr+minstr