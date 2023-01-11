# 0으로 채워진 19 * 19 바둑판 생성
ROW = 19
COLUMN = 19

board = []
for i in range(ROW):
    board.append([])
    for j in range(COLUMN):
        board[i].append(0)

# 정수 1, 0의 입력을 받는다.
# 뒤집을 횟수 입력 받기
num = int(input())

# 뒤집을 좌표 입력 받기
for i in range(num):
    x, y = input().split()
    x = int(x) - 1
    y = int(y) - 1
    for j in range(19):
        if board[j][y] == 0:
            board[j][y] = 1
        else:
            board[j][y] = 0
        if board[x][j] == 0:
            board[x][j] = 1
        else:
            board[x][j] = 0


for i in range(19):
    for j in range(19):
        print(board[i][j], end=" ")
    print()
