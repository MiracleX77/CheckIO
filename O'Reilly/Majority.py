def is_majority(items: list) -> bool:
    if max(items.count(True),items.count(False))==items.count(True) and items.count(True)!=items.count(False):
        return True
    else:
        return False