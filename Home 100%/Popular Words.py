def popular_words(text: str, words: list) -> dict:
    text=text.lower()
    text=text.split()
    dicty={}
    for i in words:
        dicty.update({i:text.count(i)})