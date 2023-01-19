def goes_after(word: str, first: str, second: str) -> bool:
    if len(word)!= 0 and word.find(first) != len(word)-1:
        if word[word.find(first)+1] == second  :
            return True
    return False
goes_after("word","d","o")