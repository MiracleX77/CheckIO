def sum_light(els) -> int:
    total_seconds=0
    for i in range (0,len(els),2):
        delta=els[i]-els[i+1]
        total_seconds+=int(abs(delta.total_seconds()))
    return total_seconds