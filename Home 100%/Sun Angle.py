def sun_angle(time: str):
    hour=int(time[0:2])
    minint=(hour-6)*60+int(time[3:5])
    if hour<6 or hour>17 and int(time[3:5])>0:
        string="I don't see the sun!"
        return string
    degee=(minint)/4
    return degee