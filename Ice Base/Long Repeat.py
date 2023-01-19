def long_repeat(line: str) -> int:
    list_repeat =[]
    if len(line) > 1:
        for i in range(len(line)):
            repeat = 1
            for j in range(1,len(line[i:])):
                if line[i] == line[i+j]:
                    repeat +=1
                else:
                    break
            list_repeat.append(repeat)
        return max(list_repeat)
    else:
        return len(line)


long_repeat("sdsffffse")