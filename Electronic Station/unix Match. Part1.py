def unix_match(filename: str, pattern: str) -> bool:
    if filename.find(".") != -1:
        filename=[filename[:filename.find(".")],filename[filename.find(".")+1:]]
    else:
        filename=[filename]
    if pattern.find("[.]")!=-1:
        pattern=pattern.replace("[.]",".")
    if pattern.find("[!.]")!=-1:
        pattern=pattern.replace("[!.]","!")
    pattern= pattern.split(".")
    print(filename,pattern)
    if len(filename) == 2:
        if len(pattern) == 2:
            if pattern[1] == "*" or pattern[1].count("!") == len(pattern[1]):
                if filename[1].isalpha():
                    return True
            if pattern[0].find("[")!=-1 and pattern[0].find("]")!= -1:
                repls = pattern[0].replace("]"," ")
                if pattern[0].find("[") == 0:
                    repls= repls.replace("[","")
                else:
                    repls= repls.replace("["," ")
                repls=repls.split(" ")
                print(repls)
                if pattern[0].find("[") == 0:
                    repls.append(filename[0].replace(repls[1],""))
                    x=repls[0]
                    repls[0] = repls[1]
                    repls[1] = x
                else:
                    repls.append(filename[0].replace(repls[0],""))
                print(repls)
                if len(repls[1])!= 0:
                    if repls[1][0] == "!" :
                        if repls[2] not in repls[1]:
                            return True
                    else:
                        if repls[2] in repls[1]:
                            return True
                print(repls)
            if len(filename[0]) == len(pattern[0]):
                if pattern[1] == filename[1] :
                    return True
                elif pattern[1].count("?")==len(filename[1]):
                    return True

        else:
            if pattern[0].count("*") + pattern[0].count("?")== len(pattern[0]):
                return True

    return False
unix_match("name....","name.[!.][!.][!.]")