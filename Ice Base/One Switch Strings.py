def switch_strings(line: str, result: str) -> bool:
    if len(line) != len(result):
        return False
    if line == result:
        return True
    else:
        for i in range(len(line)):
            if line[i] != result[i]:
                for j in range(line.count(result[i])):
                    if j == 0:
                        index = line.find(result[i])
                    else:
                        index = line.find(result[i],index+1)
                    new_line =  line[:i]+result[i]+line[i+1:index]+line[i]+line[index+1:]
                    if new_line==result:
                        return True
                break
    return False
switch_strings("knerse","keern")
