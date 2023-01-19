def adjacent_letters(line: str) -> str:
    i = 0
    while i < len(line)-1 and len(line)!=1:
        print("index",i)
        if line[i] == line[i+1]:
            line = line[:i] + line[i+2:]
            i-=1
        else:
            i+=1
        print(line)
        print(len(line))
        
    return line
adjacent_letters("aaa")