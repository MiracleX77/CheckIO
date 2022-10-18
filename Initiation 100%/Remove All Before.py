def remove_all_before(items: list, border: int):
    for i in items:
        if i == border:
            return items[items.index(i):]
    return items