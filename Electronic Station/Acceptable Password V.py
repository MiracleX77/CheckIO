def is_acceptable_password(password: str) -> bool:
    if password.find("password") != -1 or password.find("PASSWORD")!= -1:
        return False
    elif len(password)>9:
        return True
    elif len(password)>6 and password.isdigit()==False:
            for i in  password:
                if i.isdigit():
                    return True
    return False