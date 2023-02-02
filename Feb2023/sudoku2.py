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

y_check = [[0] * 10 for _ in range(9)]
x_check = [[0] * 10 for _ in range(9)]
part_check = [[0] * 10 for _ in range(9)]
zero_arr = []
for y in range(9):
    for x in range(9):
        num = input_data[y][x]
        if num == 0:
            zero_arr.append((y, x))
        else:
            y_check[y][num] = 1
            x_check[x][num] = 1
            part_check[(y // 3) * 3 + x // 3][num] = 1

cnt = [0]

s = time.time()


def sudoku(table, zero_arr, y_check, x_check, part_check, index):
    cnt[0] += 1
    if index == len(zero_arr):
        e = time.time()
        print("\033[102m\033[1m", cnt[0], "\033[0m")
        print("\033[102m\033[1m", f"{e-s}", "\033[0m")
        for i in table:
            print(*i, end="\n")
        sys.exit(0)
    else:
        y, x = zero_arr[index]
        part = (y // 3) * 3 + x // 3
        for i in range(1, 10):
            if not (y_check[y][i] or x_check[x][i] or part_check[part][i]):
                y_check[y][i], x_check[x][i], part_check[part][i] = 1, 1, 1
                table[y][x] = i
                sudoku(table, zero_arr, y_check, x_check, part_check, index + 1)
                y_check[y][i], x_check[x][i], part_check[part][i] = 0, 0, 0
                table[y][x] = 0


sudoku(input_data, zero_arr, y_check, x_check, part_check, 0)
