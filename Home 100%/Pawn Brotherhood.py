def safe_pawns(pawns: set):
    board=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
    count_safe=0
    for i in pawns:
        board[7-(int(i[1])-1)][(ord(i[0])-96)-1] = 1

    for i in pawns:
        index_colum=(ord(i[0])-96)-1
        index_row=7-(int(i[1])-1)
        if index_row != 7  :
            try:
                if board[index_row+1][index_colum-1] == 1 or board[index_row+1][index_colum+1] == 1:
                    print("1=",index_row, index_colum)
                    if index_colum!=0 or board[index_row+1][index_colum-1] != 1:
                        count_safe+=1
            except:
                try:
                    if board[index_row+1][index_colum-1] == 1 :
                        print("2=",index_row, index_colum)
                        count_safe+=1
                except:
                    if board[index_row+1][index_colum+1] == 1:
                        print("3=",index_row, index_colum)
                        count_safe+=1

    return count_safe