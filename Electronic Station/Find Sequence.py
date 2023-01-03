def checkio(matrix) -> bool:
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if len(matrix[i]) - j >=4:
                if matrix[i][j:j+4].count(matrix[i][j]) == 4:
                    return True
            if len(matrix)-i >=4:
                column=[]
                for row in range(0,4):
                    column.append(matrix[i+row][j])
                if column.count(matrix[i][j]) == 4:
                    return True
            if len(matrix)-i >=4 and len(matrix[i]) - j >=4:
                ne_sw_check=[]
                for row in range(0,4):
                    ne_sw_check.append(matrix[i+row][j+row])
                if ne_sw_check.count(matrix[i][j]) == 4:
                    return True
            if len(matrix)-i >=4 and j >=3:
                nw_se_check=[]
                for row in range(0,4):
                    print(i,j)
                    nw_se_check.append(matrix[i+row][j-row])
                if nw_se_check.count(matrix[i][j]) == 4:
                    return True
    return False
checkio([
        [1, 1, 2, 1,1],
        [1, 1, 4, 1,2],
        [2, 2, 1, 6,3],
        [1, 1, 3, 2,4],
        [1, 7, 2, 1,4]
    ])