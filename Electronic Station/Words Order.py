def words_order(text: str, words: list) -> bool:
    text=text.split()
    if len(words) == 1 and text.count(words) >=1:
        return True
    for i in range (len(words)):
        if words.count(words[i]) >= 2 or text.count(words[i])==0:
            return False
        words[i]=text.index(words[i])
    list_check = words.copy()
    words.sort()
    print(list_check)
    print(words)
    if list_check == words:
        return True
    else:
        return False
words_order("hi world im here", ["worl", "here","here"])
