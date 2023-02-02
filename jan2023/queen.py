# ######## N-Queen 남이 푼거 ###########
# Queen = int(input())
# pos = [0] * Queen
# flag_a = [False] * Queen
# flag_b = [False] * ((Queen * 2) - 1)
# flag_c = [False] * ((Queen * 2) - 1)

# chessboard = []
# count = 0


# def make_chessboard():
#     global chessboard
#     chessboard = [["□" for i in range(Queen)] for i in range(Queen)]


# def visualization_chessboard(pos):
#     for pid in range(len(pos)):
#         sample_data = pos[pid]
#         chessboard[sample_data][pid] = "■"

#     for i in range(len(chessboard)):
#         for j in range(len(chessboard[0])):
#             print(chessboard[i][j], end=" ")
#             # fp1.write(str(chessboard[i][j]))
#         print()
#         # fp1.write("\n")

#     make_chessboard()  # Init chessboard
#     print("\n")
#     # fp1.write("\n")


# def print_pos():
#     # fp1.write("pos = "+str(pos)+"\n")
#     for i in range(Queen):
#         print(pos[i], end=" ")
#     print()


# def set(i):
#     global count
#     for j in range(Queen):
#         if (
#             not flag_a[j]
#             and not flag_b[i + j]
#             and not flag_c[i - j + (Queen - 1)]
#         ):
#             pos[i] = j
#             if i == Queen - 1:
#                 count += 1
#                 # print_pos()
#                 visualization_chessboard(pos)
#             else:
#                 flag_a[j] = flag_b[i + j] = flag_c[i - j + (Queen - 1)] = True
#                 set(i + 1)
#                 flag_a[j] = flag_b[i + j] = flag_c[i - j + (Queen - 1)] = False


# make_chessboard()

# set(0)

# print(count)
#########################
###### 스도쿠 2580 ############
import sys

sys.setrecursionlimit(10**9)

# input_data = """0 3 5 4 6 9 2 7 8
# 7 8 2 1 0 5 6 0 9
# 0 6 0 2 7 8 1 3 5
# 3 2 1 0 4 6 8 9 7
# 8 0 4 9 1 3 5 0 6
# 5 9 6 8 2 0 4 1 3
# 9 1 7 6 5 2 0 8 0
# 6 0 3 7 0 1 9 5 2
# 2 5 8 3 9 4 7 6 0"""
input_data1 = """0 4 0 0 0 0 2 0 0
0 6 0 0 0 5 0 0 0
2 0 5 0 8 0 0 0 7
0 0 6 0 0 0 0 0 0
5 0 7 0 0 1 9 0 0
0 0 0 0 4 0 0 1 0
0 0 0 3 0 0 0 0 8
0 2 0 0 0 0 0 0 0
9 0 1 0 0 4 7 0 0"""
input_data = input_data1.split("\n")
# input_data = [i.rstrip() for i in sys.stdin.readlines()]
input_data = [i.split() for i in input_data]
origin = set("123456789")


def zero_not_exist(table):
    for i in table:
        if "0" in i:
            return False
        for j in i:
            if isinstance(j, tuple):
                return False
    return True


def define_part(y, x, table):
    for i in range(9):
        st = i % 3 * 3
        en = i % 3 * 3 + 3
        row = i // 3 * 3
        if st <= x < en and (y // 3 * 3) == row:
            # print("🔥")
            part = set(
                table[row][st:en]
                + table[row + 1][st:en]
                + table[row + 2][st:en]
            )
            col_arr = set([table[i][x] for i in range(9)])
            row_arr = set(table[y])
            part_sub = origin - part
            col_sub = origin - col_arr
            row_sub = origin - row_arr
            total = part_sub & col_sub & row_sub
            if len(part_sub) == 1:
                result = part_sub.pop()
            elif len(col_sub) == 1:
                result = col_sub.pop()
            elif len(row_sub) == 1:
                result = row_sub.pop()
            elif len(total) == 1:
                result = total.pop()
            else:
                if len(total) == 0:
                    result = "0"
                else:
                    result = tuple(total)
            table[y][x] = result
            # print(*table, sep="\n")


def convert_arr(y, x, arr, table):
    new_arr = []
    for i in arr:
        if isinstance(i, tuple) and i != table[y][x]:
            new_arr.extend(list(i))
    if len(new_arr) == 0:
        return arr
    return set(new_arr)


def define_part_tuple(y, x, table):
    for i in range(9):
        st = i % 3 * 3
        en = i % 3 * 3 + 3
        row = i // 3 * 3
        if st <= x < en and (y // 3 * 3) == row:
            # print("🔥")
            part = set(
                table[row][st:en]
                + table[row + 1][st:en]
                + table[row + 2][st:en]
            )
            col_arr = set([table[i][x] for i in range(9)])
            row_arr = set(table[y])
            part = convert_arr(y, x, part, table)
            col_arr = convert_arr(y, x, col_arr, table)
            row_arr = convert_arr(y, x, row_arr, table)
            part_sub = set([*table[y][x]]) - part
            col_sub = set([*table[y][x]]) - col_arr
            row_sub = set([*table[y][x]]) - row_arr
            if len(part_sub) == 1:
                result = part_sub.pop()
            elif len(col_sub) == 1:
                result = col_sub.pop()
            elif len(row_sub) == 1:
                result = row_sub.pop()
            else:
                result = "0"
            table[y][x] = result
            print(*table, sep="\n")
            print("=======================")


pass


def sudoku(table):
    if zero_not_exist(table):
        # print("YES!!")
        return table
    else:
        for y in range(9):
            for x in range(9):
                if table[y][x] == "0":
                    define_part(y, x, table)
                elif isinstance(table[y][x], tuple):
                    define_part_tuple(y, x, table)
        return sudoku(table)


# print("----------")
result = sudoku(input_data)
for i in result:
    print(*i)

# print(origin - set(globals()[f"part{1}"]))
