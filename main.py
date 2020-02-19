#!/usr/bin/env python3

board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7],
]


def solve(bo):
    all_find = []
    find = find_empty(bo)
    row, col = find
    all_find.append((row, col))
    while True:
        print(all_find)
        row, col = find
        possibility = find_possibility(find, bo)
        if possibility != 10:
            bo[row][col] = possibility
            print_board(bo)
            find = find_empty(bo)
            if not find_empty(bo):
                return True
            row, col = find
            all_find.append((row, col))
        else:
            bo[row][col] = 0
            print_board(bo)
            all_find.pop()
            find = all_find[len(all_find)-1]
        if not find_empty:
            return True


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
    start_number = bo[row][col] + 1
    for i in range(start_number, 10):
        square = [row - row % 3, col - col % 3]
        for j in range(9):
            if j % 3 == 0 and j != 0:
                square[0] += 1
                square[1] -= 3
           # print(square[0], ", ", square[1], ", j = ", j, ",i = ", i)
            if bo[j][col] == i or bo[row][j] == i or bo[square[0]][square[1]] == i:
            #    print("col=", col, ", row=", row)
                break
            if j == 8:
                return i
            else:
                square[1] += 1
    return 10
