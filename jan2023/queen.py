Queen = int(input())
pos = [0] * Queen
flag_a = [False] * Queen
flag_b = [False] * ((Queen * 2) - 1)
flag_c = [False] * ((Queen * 2) - 1)

chessboard = []
count = 0


def make_chessboard():
    global chessboard
    chessboard = [["□" for i in range(Queen)] for i in range(Queen)]


def visualization_chessboard(pos):
    for pid in range(len(pos)):
        sample_data = pos[pid]
        chessboard[sample_data][pid] = "■"

    for i in range(len(chessboard)):
        for j in range(len(chessboard[0])):
            print(chessboard[i][j], end=" ")
            # fp1.write(str(chessboard[i][j]))
        print()
        # fp1.write("\n")

    make_chessboard()  # Init chessboard
    print("\n")
    # fp1.write("\n")


def print_pos():
    # fp1.write("pos = "+str(pos)+"\n")
    for i in range(Queen):
        print(pos[i], end=" ")
    print()


def set(i):
    global count
    for j in range(Queen):
        if (
            not flag_a[j]
            and not flag_b[i + j]
            and not flag_c[i - j + (Queen - 1)]
        ):
            pos[i] = j
            if i == Queen - 1:
                count += 1
                # print_pos()
                visualization_chessboard(pos)
            else:
                flag_a[j] = flag_b[i + j] = flag_c[i - j + (Queen - 1)] = True
                set(i + 1)
                flag_a[j] = flag_b[i + j] = flag_c[i - j + (Queen - 1)] = False


make_chessboard()

set(0)

print(count)
