import numpy as np


def possible(y,x, n):  # y and x is positiona dn n is number
    for i in range(0, 9):  # check if num is there in column
        if puzzle[y][i] == n:
            return False
    for i in range(0, 9):  # check if num is there in row
        if puzzle[i][x] == n:
            return False
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3

    for i in range(0, 3):  # check if num there in box
        for j in range(0, 3):
            if puzzle[y0 + i][x0 + j] == n:
                return False
    return True


# print(possible(1,1,5))

def solve():
    for y in range(9):
        for x in range(9):
            if puzzle[y][x] == 0:  # for all of the possibility in row and col
                for n in range(1, 10):  # check all possiblility ofn um 1-9
                    if possible(y, x, n):
                        puzzle[y][x] = n
                        solve()
                        puzzle[y][x] = 0
                return
    print (' * *' * 9)
    print_board()
    input('More?')



def print_board():

    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" *27)
        for j in range(9):
            if j % 3 == 0:
                print(" | ", end="")

            if j == 8:
                print(puzzle[i][j], end="\n")
            else:
                print(str(puzzle[i][j]) + " ", end="")




if __name__ == '__main__':
    puzzle = [[0, 4, 0, 8, 0, 0, 0, 0, 6],
              [0, 0, 1, 0, 0, 6, 0, 0, 3],
              [0, 0, 6, 3, 0, 9, 8, 0, 0],
              [2, 5, 0, 6, 0, 3, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 8, 7, 0, 0, 0, 0, 4, 0],
              [0, 0, 0, 0, 9, 0, 7, 0, 0],
              [0, 0, 0, 0, 0, 4, 0, 1, 0],
              [0, 0, 0, 0, 0, 2, 0, 0, 5]]

    print_board()
    solve()



