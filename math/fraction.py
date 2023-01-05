# select_num = int(input())


# def find_row(n):
#     acc = 0
#     for row in range(1, n + 1):
#         acc += row
#         if acc >= n:
#             return row


# def pre_total(row):
#     acc = 0
#     for i in range(1, row):
#         acc += i
#     return acc


# def make_list(n):
#     result_li = []
#     for i in range(1, n + 1):
#         result_li.append(i)
#     return result_li


# row = find_row(select_num)
# pre = pre_total(row)
# li = make_list(row)
# move = select_num - pre
# index = row - 1

# if row % 2 == 0:
#     numerator = move
#     denominator = li[index] - (numerator - 1)
# else:
#     denominator = move
#     numerator = li[index] - (denominator - 1)
# print(f"{numerator}/{denominator}")
# ###############################################
# import math

# up, down, hight = map(int, input().split())

# day = math.ceil((hight - up) / (up - down)) + 1
# print(day)
# # ###############################################
# import sys

# case = int(input())
# li = [[*map(int, i.split())] for i in sys.stdin.readlines()]

# for i in li:
#     H, W, N = i
#     y = N % H
#     x = (N // H) + 1
#     if y == 0:
#         y = H
#         x = N // H
#     print(f"{y}{x:0>2}")
# ####################################
t = int(input())


def person(floor, room):
    pre_li = [i for i in range(1, 15)]
    for i in range(floor):
        sum = 0
        for index, j in enumerate(pre_li):
            sum += j
            pre_li[index] = sum
    room_index = room - 1
    print(pre_li[room_index])


for i in range(t):
    floor = int(input())
    room = int(input())

    if room == 1:
        print(1)
    else:
        person(floor, room)
