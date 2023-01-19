import datetime
def vacation(date, days):
    x = datetime.date.fromisoformat(date)
    y=datetime.timedelta(days)
    x=x+y
    ix = x.isocalendar()
    if ix[2] >= 6 :
            y1=datetime.timedelta(8-ix[2])
            x=x+y1
    string = x.isoformat()

    return string
vacation('2018-07-01', 14)