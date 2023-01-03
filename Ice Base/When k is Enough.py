
def remove_after_kth(items, k: int):
    if k == 0:
        return []
    list_result=[]
    for i in items:
        if list_result.count(i) < k:
            list_result.append(i)

    return list_result
remove_after_kth(['tom', 42, 'bob', 'bob', 99, 'bob', 'tom', 'tom', 99], 2)