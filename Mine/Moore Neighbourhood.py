def count_neighbours(grid, row, col):
    chips= 0
    for i in  range (-1,2):
        for j in range (-1,2):
            try: 
                if row+i!= -1 and col+j != -1:
                    if row+i != row or col+j != col:
                        print(grid[row+i][col+j],row+i,col+j)

                        if grid[row+i][col+j] == 1 :
                            chips+=1
            except:
                None
    return chips
count_neighbours([[1,1,1],[1,1,1],[1,1,1]],1,1)