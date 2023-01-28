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

input_data = """0 3 5 4 6 9 2 7 8
7 8 2 1 0 5 6 0 9
0 6 0 2 7 8 1 3 5
3 2 1 0 4 6 8 9 7
8 0 4 9 1 3 5 0 6
5 9 6 8 2 0 4 1 3
9 1 7 6 5 2 0 8 0
6 0 3 7 0 1 9 5 2
2 5 8 3 9 4 7 6 0"""
input_data = input_data.split("\n")

input_data = [i.split() for i in input_data]
origin = set("123456789")
print(*input_data, sep="\n")


def zero_not_exist(table):
    s = set("0")
    for i in table:
        s = s & set(i)
    return not s


result = origin - set(input_data[0])
if len(result) == 1:
    result = result.pop()
    print(result)


def create_set(table, x, y):
    pass


part1 = input_data[0][0:3] + input_data[1][0:3] + input_data[2][0:3]
part2 = input_data[0][3:6] + input_data[1][3:6] + input_data[2][3:6]
part3 = input_data[0][6:9] + input_data[1][6:9] + input_data[2][6:9]
part4 = input_data[3][0:3] + input_data[4][0:3] + input_data[5][0:3]
part5 = input_data[3][3:6] + input_data[4][3:6] + input_data[5][3:6]
part6 = input_data[3][6:9] + input_data[4][6:9] + input_data[5][6:9]
part7 = input_data[6][0:3] + input_data[7][0:3] + input_data[8][0:3]
part8 = input_data[6][3:6] + input_data[7][3:6] + input_data[8][3:6]
part9 = input_data[6][6:9] + input_data[7][6:9] + input_data[8][6:9]
print(part1, part2)


def part_maker(table, x, y):
    for i in range(9):
        for j in range(9):
            pass


def sudoku(table, origin):
    if zero_not_exist(table):
        return
    else:
        for i in range(9):

            pass
