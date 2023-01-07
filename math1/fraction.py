import time
from functools import wraps
from use_time import use_time


def use_time(func):
    @wraps(func)
    def new_func(*args, **kwargs):
        s = time.time()
        result = func(*args, **kwargs)
        e = time.time()
        print(f"{func.__name__} 소요시간: {e-s:.10f}초")
        return result

    return new_func


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
# t = int(input())


# def person(floor, room):
#     pre_li = [i for i in range(1, 15)]
#     for i in range(floor):
#         sum = 0
#         for index, j in enumerate(pre_li):
#             sum += j
#             pre_li[index] = sum
#     room_index = room - 1
#     print(pre_li[room_index])


# for i in range(t):
#     floor = int(input())
#     room = int(input())

#     if room == 1:
#         print(1)
#     else:
#         person(floor, room)
# #################################
# n = int(input())
# remain = n % 5
# five = n // 5

# if remain == 4 and n >= 9:
#     three = 3
#     five -= 1
# elif remain == 3 and n >= 3:
#     three = 1
# elif remain == 2 and n >= 12:
#     three = 4
#     five -= 2
# elif remain == 1 and n >= 6:
#     three = 2
#     five -= 1
# elif remain == 0:
#     three = 0
# else:
#     three = 0
#     five = -1

# print(five + three)
# #################################
# A, B = map(int, input().split())
# print(A + B)
# ################################
# _ = int(input())
# num_li = list(map(int, input().split()))


# def minority(n):
#     if n == 1:
#         return False
#     result = True
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return result


# count = list(map(minority, num_li)).count(True)
# print(count)
# ##############################################
# import sys


# def minority(n):
#     if n == 1:
#         return 0

#     for i in range(2, n):
#         if n % i == 0:
#             return 0
#     return n


# MIN, MAX = map(int, [i.rstrip() for i in sys.stdin.readlines()])
# li = [i for i in range(MIN, MAX + 1)]
# minority_set = set(list(map(minority, li)))
# minority_set.discard(0)
# minority_sum = len(minority_set) and sum(minority_set)
# minority_min = len(minority_set) and min(minority_set)
# minority_sum or print(-1)
# minority_sum and print(f"{minority_sum}\n{minority_min}")

# MIN, MAX = [60, 60]
# ######################################################
# n = int(input())
# if n == 1:
#     pass
# else:
#     i = 2
#     new = n
#     while i < new:
#         if new % i == 0:
#             new = new // i
#             print(i)
#             i = 2
#         else:
#             i += 1
#             continue
#     print(new)
# #####################################################
# def minority(n):
#     if n == 1:
#         return 0
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return 0
#     return 1


# def prime_number_print(MIN, MAX):
#     for i in range(MIN, MAX + 1):
#         minority(i) and print(i)


# MIN, MAX = map(int, input().split())
# prime_number_print(MIN, MAX)
# ##########################################
# inp = input()

# ascending = "1 2 3 4 5 6 7 8"
# descending = ascending[::-1]
# inp == ascending and print("ascending")
# inp == descending and print("descending")
# inp != ascending and inp != descending and print("mixed")
# ########################################
# import sys


# def minority(n):
#     if n == 1:
#         return 0
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return 0
#     return 1


# # @use_time
# def count_prime(li):
#     li = li[:-1]
#     m = max(li)
#     n = min(li)
#     prime = [False] * (2 * m + 1)
#     for i in range(n, 2 * m + 1):
#         if minority(i):
#             prime[i - 1] = True
#     for i in li:
#         print(prime[i : 2 * i].count(True))


# num_list = list(map(int, [i.strip() for i in sys.stdin.readlines()]))
# count_prime(num_list)
##########################
# import sys

# a, b, c = map(int, [i.strip() for i in sys.stdin.readlines()])
# total = a * b * c
# li = [0 for i in range(10)]
# for i in str(total):
#     li[int(i)] += 1

# for i in li:
#     print(i)
