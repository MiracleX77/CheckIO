def is_acceptable_password(password: str) -> bool:
    if len(password)>9:
        return True
    elif len(password)>6 and password.isdigit()==False:
            for i in  password:
                if i.isdigit():
                    return True
    return False