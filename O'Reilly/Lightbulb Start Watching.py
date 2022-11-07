from datetime import datetime
from typing import Optional

def sum_light(els,start_watching:Optional[datetime]=None,end_watching:Optional[datetime]=None):
    els.append(end_watching)
    result=0
    for start,end in zip(els[::2],els[1::2]):
        print(result)
        result+=(min(end_watching or end,max(start_watching or end,end))-min(end_watching or end,max(start_watching or start ,start))).total_seconds()
    return result
print(sum_light([
datetime(2015, 1, 12, 10, 0, 0),
datetime(2015, 1, 12, 10, 10, 10),
datetime(2015, 1, 12, 11, 0, 0),
datetime(2015, 1, 12, 11, 10, 10)
],
datetime(2015, 1, 12, 10, 30, 0),
datetime(2015, 1, 12, 11, 0, 0)))