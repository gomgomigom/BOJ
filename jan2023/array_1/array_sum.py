import sys
from pathlib import Path

base_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(base_dir))
# print(sys.path)

from use_time import use_time

##################################################
import sys

x, y = map(int, input().split())
matrix = [list(map(int, i.strip().split())) for i in sys.stdin.readlines()]
a_matrix, b_matrix = matrix[:x], matrix[x:]


def print_matrix(li):
    for i in li:
        print(*i)


def matrix_sum(x, y, a, b):
    li = []
    for i in range(x):
        in_li = []
        for j in range(y):
            item = a[i][j] + b[i][j]
            in_li.append(item)
        li.append(in_li)
    return li


print_matrix(matrix_sum(x, y, a_matrix, b_matrix))
#############################################
import sys

matrix = [[*map(int, i.strip().split())] for i in sys.stdin.readlines()]


MAX = max(map(max, matrix))
print(MAX)

li = [i for line in matrix for i in line]
location = li.index(MAX)
print(location // 9 + 1, location % 9 + 1)
#####################################
ea = int(input())
a = []
for i in range(ea):
    a.append(list(map(int, input().split())))

paper = [[0 for i in range(100)] for i in range(100)]

for i in a:
    row = i[0]
    col = i[1]
    for x in range(10):
        for y in range(10):
            paper[row + x][col + y] = 1

paper_spread = [item for row in paper for item in row]
print(paper_spread.count(1))
