def find_quotes(a):
    list_result = []
    n_round = a.count("\"")
    for i in range(0,n_round,2):
        index_quotes_open = a.find("\"")
        index_quotes_close = a[a.find("\"")+1:].find("\"");
        print(index_quotes_open,index_quotes_open+index_quotes_close+1)
        string = a[index_quotes_open+1:index_quotes_open+index_quotes_close+1];
        list_result.append(string) 
        a= a[index_quotes_open+index_quotes_close+2:]
    return list_result
find_quotes("\"Lorem Ipsum\" is simply dummy text \
    of the printing and typesetting industry. \
    Lorem Ipsum has been the \"industry's standard\
     dummy text ever since the 1500s\", when an \
    unknown printer took a galley of type and scrambled \
    it to make a type specimen book. It has survived \
    not only five centuries, but also the leap into \
    electronic typesetting, remaining essentially \
    unchanged. \"It was popularised in the 1960s\" with the \
    release of Letraset sheets containing Lorem Ipsum passages, \
    and more recently with desktop publishing software like Aldus \
    PageMaker including versions of Lorem Ipsum.")