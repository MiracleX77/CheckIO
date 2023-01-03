def sort_by_ext(files):
    return sorted(files,key=ext)
def ext(file):
    splited = file.split(".")
    if('' == splited[0] and len(splited) == 2):
        splited = [''.join(splited[1:]), '']
    return splited[::-1]

sort_by_ext(['1.cad', '1.bat','.bat', '2.aa'])  