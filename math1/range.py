# import sys

# numbers = [int(i.strip()) for i in sys.stdin.readlines()]
# numbers.sort()
# print(int(sum(numbers) / 5))
# print(numbers[2])
# #################################
# N, k = map(int, input().split())
# score_li = list(map(int, input().split()))
# score_li.sort(reverse=True)
# print(score_li[k - 1])
# ##############################
# import sys

# line = int(sys.stdin.readline())
# counting = [0] * 10000
# for _ in range(line):
#     number = int(sys.stdin.readline())
#     counting[number - 1] += 1

# for index, i in enumerate(counting, start=1):
#     if i:
#         for _ in range(i):
#             print(index)
############230109###############
# import sys


# numbers = int(input())
# num_li = [int(i.strip()) for i in sys.stdin.readlines()]
# num_li.sort()
# counting = [0] * 8001
# print(int(round((sum(num_li) / numbers), 0)))
# print(num_li[numbers // 2])
# for i in num_li:
#     counting[4000 + i] += 1
# new_counting = counting[:]
# max_index = counting.index(max(counting))
# max_value = counting[max_index]
# new_counting[max_index] = 0
# new_max_index = new_counting.index(max(new_counting))
# new_max_value = new_counting[new_max_index]
# if max_value == new_max_value:
#     print(new_max_index - 4000)
# else:
#     print(max_index - 4000)
# print(abs(num_li[-1] - num_li[0]))
######################################
# num = input()
# num_li = [int(i) for i in num]
# num_li.sort(reverse=True)
# print(*num_li, sep="")
############################
import sys

number = int(input())

xy_li = [list(map(int, i.strip().split())) for i in sys.stdin.readlines()]

# x_li = [x[0] for x in xy_li]
# y_li = [y[1] for y in xy_li]

xy_li.sort(key=lambda x: (x[0], x[1]))
for i in xy_li:
    print(i[0], i[1])
