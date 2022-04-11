
sudoku_grid =  [[0,0,0,6,0,0,0,0,0],\
                [0,4,0,0,3,0,0,7,0],\
                [6,0,1,0,0,0,2,0,9],\
                [1,0,0,0,0,0,7,0,0],\
                [0,9,0,0,5,0,0,4,0],\
                [0,0,7,0,0,0,0,0,3],\
                [2,0,6,0,0,0,5,0,1],\
                [0,8,0,0,7,0,0,9,0],\
                [0,0,0,0,0,2,0,0,0]]
   



def possible(y,x,n):
    for i in range(9):
        if sudoku_grid[y][i] == n:
            return False
        if sudoku_grid[i][x] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if sudoku_grid[y0+i][x0+j] == n:
                return False
    return True

def solve():
    for y in range(9):
        for x in range(9):
            if sudoku_grid[y][x] == 0:
                for n in range(1,10):
                    if possible(y,x,n):
                        sudoku_grid[y][x] = n
                        solve()
                        sudoku_grid[y][x] = 0
                return
    for i in range(9):
        print(sudoku_grid[i], '\n')

for i in range(9):
    print(sudoku_grid[i], '\n')
#Computerfile helped alot
