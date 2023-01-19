def count_words(text: str, words: set) -> int:
    text= text.lower()
    count = 0
    for i in words:
        if i in text:
            count+=1
    return count
count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"})