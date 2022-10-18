
def replace_last(line: list):
    if line==[]:
        return line
    else:
        line.insert(0,line.pop(len(line)-1))
    return line