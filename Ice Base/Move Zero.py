def move_zeros(items: list[int]) -> list[int]:
    for i in range(items.count(0)):
        items.remove(0)
        items.append(0)
    return items
move_zeros([0, 1, 0, 3, 12])