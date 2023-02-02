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
input_data = input_data.split("\n")
# input_data = [i.rstrip() for i in sys.stdin.readlines()]
input_data = [list(map(int, i.split())) for i in input_data]


spaces = []
rowcheck = [[0] * 10 for _ in range(9)]
colcheck = [[0] * 10 for _ in range(9)]
gridcheck = [[0] * 10 for _ in range(9)]
for r in range(9):
    for c in range(9):
        num = input_data[r][c]
        if num == 0:
            spaces.append((r, c))
        else:
            rowcheck[r][num] = 1
            colcheck[c][num] = 1
            gridcheck[(r // 3) * 3 + c // 3][num] = 1


def dfs(board, rowcheck, colcheck, gridcheck, spaces, idx):
    if idx == len(spaces):
        print(
            "\033[102m\033[1m",
            "\n".join([" ".join(map(str, line)) for line in board]),
            "\033[0m",
        )
        sys.exit(0)
    r, c = spaces[idx]
    g = (r // 3) * 3 + c // 3
    for num in range(1, 10):
        if not (rowcheck[r][num] or colcheck[c][num] or gridcheck[g][num]):
            rowcheck[r][num] = 1
            colcheck[c][num] = 1
            gridcheck[g][num] = 1
            board[r][c] = num
            dfs(board, rowcheck, colcheck, gridcheck, spaces, idx + 1)
            rowcheck[r][num] = 0
            colcheck[c][num] = 0
            gridcheck[g][num] = 0
            board[r][c] = 0


if __name__ == "__main__":
    dfs(input_data, rowcheck, colcheck, gridcheck, spaces, 0)
