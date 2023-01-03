
def yaml(a):

    data={}
    a=a.split("\n")
    for i in a :
        if i.find(":")!= -1:
            if i.find(":") == len(i)-1:
                print("asd")
                i=i+"  "
            i=i.split(": ")
            print(i)
            key=i[0]
            print(i[1])
            if i[1].isdigit():
                i[1]=int(i[1])
            elif i[1] == "false" or i[1] == "true":
                if i[1] == "false":
                    i[1] = False
                else:
                    i[1]= True
            elif i[1]==" " or i[1]=="null":
                i[1]=None
            else:
                print(i[1])
                if i[1][0]=="\"":
                    i[1]=i[1][1:len(i[1])-1]
                    if i[1][len(i[1])-1] =="\"":
                        i[1]=i[1][:len(i[1])-1]
                for char in "\\":
                    i[1]=i[1].replace(char,"")
            value=i[1]
            data.update({key:value})
    return dict(sorted(data.items()))
yaml("name: \"Bob Dylan\"\nchildren: 6\ncoding: \"null\" ")