import time
from functools import wraps
from use_time import use_time


# def use_time(func):
#     @wraps(func)
#     def new_func(*args, **kwargs):
#         s = time.time()
#         for i in range(1000):
#             result = func(*args, **kwargs)
#         e = time.time()
#         print(f"{func.__name__} 소요시간: {e-s:.10f}초")
#         return result

#     return new_func


#########################################
# # 골드바흐의 추측
import sys


def prime(n):
    if n <= 1:
        return 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return 0
    return 1


@use_time
def plus(n, prime_li):
    half = n // 2
    if prime_li[half]:
        return half, half
    else:
        for i in range(1, half + 1):
            if prime_li[half - i] and prime_li[half + i]:
                return half - i, half + i


# n = list(map(int, [i.strip() for i in sys.stdin.readlines()]))[1:]
n = [8, 10, 16, 1000, 1002, 1004, 1100]
MAX = max(n) + 1
prime_li = []
for i in range(MAX):
    prime_li.append(prime(i))
for i in n:
    answer = plus(i, prime_li)
    print(f"{answer[0]} {answer[1]}")
###########################################
# #######직사각형에서의 탈출############
# x, y, w, h = map(int, input().split())

# x_axis = [w - x, x]
# y_axis = [h - y, y]
# print(min(x_axis + y_axis))
# ################################
# import sys

# numbers = list(map(int, [i.strip() for i in sys.stdin.readlines()]))
# numbers = sorted(numbers[1:])
# for i in numbers:
#     print(i)
