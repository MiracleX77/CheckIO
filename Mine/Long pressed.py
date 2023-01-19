def long_pressed(text: str, typed: str) -> bool:
    if text != typed:
        for i in range (len(text)):
            if text[i] != typed[i]:
                print(typed[i],typed[i-1])
                while typed[i] == typed[i-1]:
                    print(typed)
                    typed = typed[:i] + typed[i+1:]
                if text[i] != typed[i]:
                    return False

        if typed == text:
            return True
    return False
long_pressed('hello from usaaaa', 'hello from japannnn')