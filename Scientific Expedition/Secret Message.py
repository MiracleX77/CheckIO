def find_message(message: str) -> str:
    result=""
    for i in message:
        if i.isupper():
            result+=i
    return result
        
find_message(('How are you? Eh, ok. Low or Lower? '
 + 'Ohhh.'))