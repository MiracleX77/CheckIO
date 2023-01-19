def check_pangram(text):
    text=text.lower()
    latin="abdefghijklmnopqrstuvwxyz"
    for i in latin:
        if i not in text:
            return  False
    return  True
check_pangram("ABCDEFGHIJKLMNOPQRSTUVWXYZ")