def left_join(phrases: tuple) -> str:
    string=",".join(phrases)
    string=string.replace("right","left")
    return string
