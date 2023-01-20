# ########## 검문 (2981) ##########
# import sys
# from functools import reduce

# N = int(input())
# li = sorted([int(i.rstrip()) for i in sys.stdin.readlines()])


# def gcd(a, b):
#     if b > a:
#         a, b = b, a
#     if a % b == 0:
#         return b
#     else:
#         return gcd(b, a % b)


# def li_gcd(li: list):
#     new_li = li[:]
#     for i in range(len(new_li) - 1):
#         new_li[i + 1] = gcd(new_li[i], new_li[i + 1])
#     return new_li[-1]


# def new_li_maker(li):
#     length = len(li)
#     new_li = []
#     for i in range(length):
#         if i + 1 == length:
#             new_li.append(li[i] - li[0])
#         else:
#             new_li.append(li[i + 1] - li[i])
#     return sorted(new_li)


# # def factorization(num, num_li=[0]):
# #     if num < max(num_li):
# #         # print("🔥", num_li, num)
# #         num_li.remove(0)
# #         new_li = []
# #         for i in range(len(num_li)):
# #             for j in range(i + 1, len(num_li) + 1):
# #                 new_li.append(reduce(lambda x, y: x * y, num_li[i:j]))
# #         print("✨", new_li)
# #         return sorted(set(new_li))
# #     else:
# #         print("❌else")
# #         for i in range(2, num + 1):
# #             if num % i == 0:
# #                 print("🔥", "i:", i, "num:", num, "num_li:", num_li)
# #                 num_li.append(i)
# #                 return factorization(num // i, num_li)


# def factorization2(num):
#     divisor = set([num])
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             divisor.add(num // i)
#             divisor.add(i)
#     return sorted(divisor)


# li = new_li_maker(li)
# GCD = li_gcd(li)
# result = factorization2(GCD)
# print(*result)
# ###### 링 (3036) #########
# N = int(input())
# n_li = list(map(int, input().split()))


# def gcd(a, b):
#     if b > a:
#         a, b = b, a
#     if a % b == 0:
#         return b
#     else:
#         return gcd(b, a % b)


# def fractional_expression(de, nu):
#     GCD = gcd(de, nu)
#     return f"{de//GCD}/{nu//GCD}"


# answer = []
# for i in range(1, N):
#     denominator = n_li[0]
#     numerator = n_li[i]
#     answer.append(fractional_expression(denominator, numerator))
# print(*answer, sep="\n")
# ######## 이항 계수 1 (11050) ##########
# N, K = map(int, input().split())
# denominator = 1
# for i in range(1, N + 1):
#     denominator *= i
# numerator = 1
# for i in range(1, K + 1):
#     numerator *= i
# for i in range(1, N - K + 1):
#     numerator *= i
# print(f"{((denominator // numerator) % 10007):.0f}")
# ######### 다리 놓기 (1010) ########
# import sys

# T = int(input())
# site_li = [list(map(int, i.strip().split())) for i in sys.stdin.readlines()]


# def factorial(n):
#     if n <= 1:
#         return 1
#     else:
#         return n * factorial(n - 1)


# def number_of_case(a, b):
#     return factorial(b) // (factorial(a) * factorial(b - a))


# for site in site_li:
#     print(f"{site[0]} {site[1]} result : {number_of_case(site[0],site[1])}")
############### 패션왕 신해빈 (9375) ##################
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


T = int(input())
for _ in range(T):
    n = int(input())
    d = dict()
    for _ in range(n):
        a, b = input().split()
        d.get(b) or d.update({b: 0})
        d[b] += 1
    total = 1
    for i in d.values():
        total *= i + 1
    print(total - 1)
