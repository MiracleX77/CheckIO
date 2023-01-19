def not_order(data: list[int]) -> int:
    data_original=data.copy()
    data.sort()
    count=0
    print(data)
    for i in range(len(data_original)):
        if data_original[i] != data[i]:
            count+=1
    return count
not_order([1,3,2,4,3,5,4,6])
