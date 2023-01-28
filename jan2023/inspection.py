import time

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
######## 이항 계수 1 (11050) ##########
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

# ########### 230120 ###############
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
# ############## 패션왕 신해빈 (9375) ##################
# def factorial(n):
#     if n <= 1:
#         return 1
#     else:
#         return n * factorial(n - 1)


# T = int(input())
# for _ in range(T):
#     n = int(input())
#     d = dict()
#     for _ in range(n):
#         a, b = input().split()
#         d.get(b) or d.update({b: 0})
#         d[b] += 1
#     total = 1
#     for i in d.values():
#         total *= i + 1
#     print(total - 1)
# ######## 팩토리얼 0의 개수 (1676) #########
# n = int(input())


# def factorial_new(n):
#     last = int(str(n)[-1])
#     if n <= 1:
#         return 1

#     elif (last % 2) == 0 or (last % 5) == 0:
#         return n * factorial_new(n - 1)

#     else:
#         return factorial_new(n - 1)


# result = str(factorial_new(n))
# length = len(result)
# cnt = 0
# for i in range(1, length + 1):
#     if result[-i] == "0":
#         cnt += 1
#     else:
#         break
# print(cnt)
# ######### 조합 0의 개수 (2004) ############
# import math

# n, m = map(int, input().split())
# five = 0
# while n // 5**five > 1:
#     five += 1
# two = 0
# while n // 2**two > 1:
#     two += 1

# five_li = [5**i for i in range(1, five + 1)]
# two_li = [2**i for i in range(1, two + 1)]


# def right_zero(n):
#     five_cnt = 0
#     two_cnt = 0
#     for i in five_li:
#         five_cnt += n // i
#     for i in two_li:
#         two_cnt += n // i
#     return [two_cnt, five_cnt]


# result2 = right_zero(n)[0] - right_zero(m)[0] - right_zero(n - m)[0]
# result5 = right_zero(n)[1] - right_zero(m)[1] - right_zero(n - m)[1]
# print(min(result2, result5))
# ############ 노 땡스! 27159 ##########
# N = int(input())
# n_li = list(map(int, input().split()))
# n_li.append(0)


# def determine_score(li, N):
#     score = []
#     start = 50
#     for i in range(N):
#         if abs(li[i] - li[i + 1]) == 1:
#             start = min(i, start)
#         else:
#             if start != 50:
#                 score.append(li[start])
#                 start = 50
#             else:
#                 score.append(li[i])
#                 start = 50

#     return score


# print(sum(determine_score(n_li, N), 0))
############ 230121 ##############
########### N과M(1) 15649 #########
# N,M = map(int, input().split())
# N, M = [4, 3]

# n_li = [i for i in range(1, N + 1)]
# new = []


# def select_num(n_li, m, count, s):
#     if m == 0:
#         m += count
#         return
#     else:
#         for i in n_li:
#             new.append(i)
#         return select_num()
#  make list
########### 230122 ###########
######### 수 찾기 1920 ##########
# N = int(input())
# N_set = set(map(int, input().split()))
# M = int(input())
# M_li = list(map(int, input().split()))

# for i in M_li:
#     if i in N_set:
#         print(1, end=" ")
#     else:
#         print(0, end=" ")
######### 230123 #########
########## N과M (1) 15649 #######
# N, M = map(int, input().split())
# N, M = 4, 3
# s = []
# visited = [False] * N


# def n2m(n, m, s, visited):
#     if len(s) == m:
#         print(*s)
#         return
#     else:
#         for i in range(N):
#             if visited[i]:
#                 continue
#             else:
#                 visited[i] = True
#                 s.append(i + 1)
#                 n2m(n, m, s, visited)
#                 s.pop()
#                 visited[i] = False


# n2m(N, M, s, visited)
########### 230124 ###########
########## N과M (2) 15650 #######
# # N, M = map(int, input().split())
# N, M = 8, 4
# s = []
# visited = [False] * N


# def n2m2(n, m, visited, s):
#     if len(s) == m:
#         print(*s)
#         return
#     else:
#         for i in range(n):
#             if visited[i]:
#                 continue
#             else:
#                 if len(s) == 0:
#                     visited[i] = True
#                     s.append(i + 1)
#                     n2m2(n, m, visited, s)
#                     s.pop()
#                     visited[i] = False

#                 else:
#                     if max(s) < i + 1:
#                         visited[i] = True
#                         s.append(i + 1)
#                         n2m2(n, m, visited, s)
#                         s.pop()
#                         visited[i] = False


# n2m2(N, M, visited, s)
########## 230125 ###########
######### N과M (3) 15651 #######
# N, M = map(int, input().split())
# N, M = 3, 3
# s = []


# def nm3(n, m, s):
#     if len(s) == m:
#         print(*s)
#         return
#     else:
#         for i in range(1, n + 1):
#             s.append(i)
#             nm3(n, m, s)
#             s.pop()


# nm3(N, M, s)
# ############# N과M(4) 15652 #############
# N, M = map(int, input().split())
# N, M = 3, 3
# temp_li = []


# def nm4(n, m, temp_li, start):
#     if len(temp_li) == m:
#         print(*temp_li)
#         return
#     else:
#         for i in range(start, n + 1):
#             temp_li.append(i)
#             nm4(n, m, temp_li, i)
#             temp_li.pop()


# nm4(N, M, temp_li, 1)
############# 230126 ############
########## N-Queen 9663 ########

N = 10
# N = int(input())
n_li = [i for i in range(1, N + 1)]
temp_li = []


def n_queen(n, li, temp_li, count: int):
    if len(temp_li) == n:
        count += 1
        # print(temp_li)
        return count
    else:
        length = len(temp_li)
        for i in li:
            if i in temp_li:
                continue
            if length != 0:
                isExist = False
                for index, temp in enumerate(temp_li):
                    delta = length - index
                    if abs(temp - i) == delta:
                        isExist = True
                        break
                if isExist:
                    continue

            temp_li.append(i)
            count = n_queen(n, li, temp_li, count)
            temp_li.pop()
    return count


start = time.time()
print(n_queen(N, n_li, temp_li, 0))
end = time.time()
print("\033[33m" + f"{end - start}" + "\033[0m")
