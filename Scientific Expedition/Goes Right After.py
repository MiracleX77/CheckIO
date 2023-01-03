def goes_after(word,first,second):
    if word.find(first) != -1 and word.find(first) != len(word):
        print(word.find(first))
        if word[word.find(first)+1] == second:
            return True
    return False

goes_after("world","d","w")