# input = int(input())
# for i in range(1, 10):
#     print(f"{input} * {i} = {input * i}")

import sys

len_num = int(sys.stdin.readline())
num_list = [
    list(map(int, sys.stdin.readline().split())) for i in range(len_num)
]
for i in num_list:
    print(i[0] + i[1])

a = 5
