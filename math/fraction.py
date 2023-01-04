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
import math

up, down, hight = map(int, input().split())

day = math.ceil((hight - up) / (up - down)) + 1
print(day)
