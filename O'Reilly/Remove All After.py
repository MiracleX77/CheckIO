def remove_all_after(items: list, border: int):
    try:
        return items[:items.index(border)+1]
    except:
        return items