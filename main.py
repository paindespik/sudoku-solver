#!/usr/bin/env python3

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


def solve(bo):
    find = find_empty(bo)
    if not find:
        return true
    else:
        bo = find_possibility(find, bo)


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo)):
            if bo[i][j] == 0:
                return (i, j)  # ligne, colonne
    return None


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_possibility(find, bo):
    row, col = find
    square = [row-row % 3, col-col % 3]
    for i in range(1, 10):
        for j in range(9):
            if j % 3 == 0 and j != 0:
                square[1] += 1
                square[0] -= 3

            if bo[col][j] == i or bo[j][row] == i or bo[square[0]][square[1]] == i:
                j = 0
                break
        if(j == 8):
            return i
        else:
            square[0] += 1
    return None
