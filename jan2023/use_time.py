import time
from functools import wraps


def use_time(func):
    @wraps(func)
    def new_func(*args, **kwargs):
        s = time.time()
        s_c = time.process_time()
        for i in range(1):
            result = func(*args, **kwargs)
        e = time.time()
        e_c = time.process_time()
        print(
            f"{func.__name__}{args} 1회 소요시간: {e-s:.10f}초(real), {e_c-s_c:.10f}초(cpu)"
        )
        return result

    return new_func


# import sys


# def prime(n):
#     if n <= 1:
#         return 0
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return 0
#     return 1


# @use_time
# def plus(n, prime_li):
#     half = n // 2
#     if prime_li[half]:
#         return half, half
#     else:
#         for i in range(1, half + 1):
#             if prime_li[half - i] and prime_li[half + i]:
#                 return half - i, half + i


# # n = list(map(int, [i.strip() for i in sys.stdin.readlines()]))[1:]
# n = [8, 10, 16]
# MAX = max(n) + 1
# prime_li = []
# for i in range(MAX):
#     prime_li.append(prime(i))
# for i in n:
#     answer = plus(i, prime_li)
#     print(f"{answer[0]} {answer[1]}")
