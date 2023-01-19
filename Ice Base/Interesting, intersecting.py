def squares_intersect(s1: tuple[int, int, int], s2: tuple[int, int, int]) -> bool:
    if s2[0] >s1[0]+s1[2] or s2[0] < s1[0]:
        if s2[1] > s1[1]+s1[2] or s2[1]<s1[1]:
            return False
    return True
squares_intersect((3,6,1),(8,3,5))