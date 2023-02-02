import sys
import time

input_data = """0 3 5 4 6 9 2 7 8
7 8 2 1 0 5 6 0 9
0 6 0 2 7 8 1 3 5
3 2 1 0 4 6 8 9 7
8 0 4 9 1 3 5 0 6
5 9 6 8 2 0 4 1 3
9 1 7 6 5 2 0 8 0
6 0 3 7 0 1 9 5 2
2 5 8 3 9 4 7 6 0"""
input_data1 = """0 4 0 0 0 0 2 0 0
0 6 0 0 0 5 0 0 0
2 0 5 0 8 0 0 0 7
0 0 6 0 0 0 0 0 0
5 0 7 0 0 1 9 0 0
0 0 0 0 4 0 0 1 0
0 0 0 3 0 0 0 0 8
0 2 0 0 0 0 0 0 0
9 0 1 0 0 4 7 0 0"""
input_data2 = """0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0"""
input_data3 = """0 0 0 0 4 3 0 0 0
0 0 0 0 0 0 1 0 0
0 0 0 0 5 0 0 0 0
0 8 0 7 0 0 0 2 0
0 6 0 0 0 0 0 0 3
0 0 0 0 0 0 0 4 0
0 0 5 8 0 0 6 0 0
4 0 0 1 0 0 0 0 0
3 0 0 0 0 0 5 0 0"""
input_data = input_data3.split("\n")
# input_data = [i.rstrip() for i in sys.stdin.readlines()]
input_data = [list(map(int, i.split())) for i in input_data]
origin = set([1, 2, 3, 4, 5, 6, 7, 8, 9])


def define_part(y, x, table):
    st = x // 3 * 3
    row = y // 3 * 3
    # part = set(
    #     [
    #         table[row][st],
    #         table[row][st + 1],
    #         table[row][st + 2],
    #         table[row + 1][st],
    #         table[row + 1][st + 1],
    #         table[row + 1][st + 2],
    #         table[row + 2][st],
    #         table[row + 2][st + 1],
    #         table[row + 2][st + 2],
    #     ]
    # )
    # col_arr = set(
    #     [
    #         table[0][x],
    #         table[1][x],
    #         table[2][x],
    #         table[3][x],
    #         table[4][x],
    #         table[5][x],
    #         table[6][x],
    #         table[7][x],
    #         table[8][x],
    #     ]
    # )
    # row_arr = set(table[y])
    total = set(
        [
            table[0][x],
            table[1][x],
            table[2][x],
            table[3][x],
            table[4][x],
            table[5][x],
            table[6][x],
            table[7][x],
            table[8][x],
            table[row][st],
            table[row][st + 1],
            table[row][st + 2],
            table[row + 1][st],
            table[row + 1][st + 1],
            table[row + 1][st + 2],
            table[row + 2][st],
            table[row + 2][st + 1],
            table[row + 2][st + 2],
            *table[y],
        ]
    )
    # possible = origin - (part | col_arr | row_arr)
    possible = origin - total
    return possible


cnt = [0]

s = time.time()


def sudoku(table, zero_arr, index):
    cnt[0] += 1
    if index == len(zero_arr):
        e = time.time()
        print("\033[102m\033[1m", f"e-s: {e-s}", "\033[0m")
        print(cnt[0])
        for i in range(9):
            print(*table[i])
        sys.exit(0)
    else:
        y, x = zero_arr[index]
        possible = define_part(y, x, table)
        if possible:
            for num in range(1, 10):
                if num in possible:
                    table[y][x] = num
                    sudoku(table, zero_arr, index + 1)
                    table[y][x] = 0


def make_zero_loc(table):
    zero_loc_arr = []
    for y in range(9):
        for x in range(9):
            if table[y][x] == 0:
                zero_loc_arr.append((y, x))
    return zero_loc_arr


zero_arr = make_zero_loc(input_data)
sudoku(input_data, zero_arr, 0)
