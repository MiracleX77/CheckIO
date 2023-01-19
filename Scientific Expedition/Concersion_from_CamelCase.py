def from_camel_case(name: str) -> str:
    for i in name:
        if i.isupper():
            name=name.replace(i,f"_{i}")
    name=name.lower()
    return name[1::]

from_camel_case("ANm")