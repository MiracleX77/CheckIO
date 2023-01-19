


def sum_by_types(items: list[str, int]) -> tuple[str, int] | list[str, int]:
    result=["", 0]
    for i in items:
        if type(i)==type(""):
            result[0]+=i
        else:
            result[1]+=i
    return result
sum_by_types(["1", "2", 3,4])