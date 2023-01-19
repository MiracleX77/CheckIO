def to_camel_case(name: str) -> str:
    name = name[:1].upper() + name[1::]
    for i in range(0,len(name)):
        if name[i]=="_":
            name=name[:i+1]+name[i+1].upper()+name[i+2:]
    name=name.replace("_","")
    return name
to_camel_case("my_function_name")