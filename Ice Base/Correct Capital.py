def correct_capital(line: str) -> bool:
    if line.isupper() or line.islower():
        return True
    else:
        if line[0].isupper() and line[1:].islower():
            return True
    return False
correct_capital("ChecKio")