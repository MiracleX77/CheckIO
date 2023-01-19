def is_acceptable_password(password: str) -> bool:
    if len(password)>6:
            for i in  password:
                if i.isdigit():
                    return True
    return False