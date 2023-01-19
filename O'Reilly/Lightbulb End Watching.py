from datetime import datetime
from typing import Optional

def sum_light(els,start_watching:Optional[datetime]=None,end_watching:Optional[datetime]=None):
    els.append(end_watching)
    result=0
    for start,end in zip(els[::2],els[1::2]):
        print(result)
        result+=(min(end_watching or end,max(start_watching or end,end))-min(end_watching or end,max(start_watching or start ,start))).total_seconds()
    return result