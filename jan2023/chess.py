# ############ 230114 분해합 #############
# n = input()


# def constructor_finder(n):
#     constructor = []
#     n_len = len(n)
#     n = int(n)
#     if n < 20:
#         for num in range(1, n):
#             num_str = str(num)
#             num_sum = 0
#             for i in num_str:
#                 num_sum += int(i)
#             if num + num_sum == n:
#                 constructor.append(num)
#     else:
#         for num in range(n - n_len * 9, n):
#             num_str = str(num)
#             num_sum = 0
#             for i in num_str:
#                 num_sum += int(i)
#             if num + num_sum == n:
#                 constructor.append(num)
#     return constructor


# constructor = constructor_finder(n)
# constructor and print(min(constructor))
# constructor or print(0)
# ######### 덩치 ##########
# import sys

# n = int(input())
# member_li = [list(map(int, (i.strip().split()))) for i in sys.stdin.readlines()]
# member_len = len(member_li)
# rank_li = []


# for i in range(member_len):
#     rank = 1
#     for j in range(member_len):
#         if (member_li[i][0] < member_li[j][0]) and (
#             member_li[i][1] < member_li[j][1]
#         ):
#             rank += 1
#     rank_li.append(rank)

# print(*rank_li)
# ########## 영화감독 숌 ############
# n = int(input())


# def count_six(s):
#     count = 0
#     for i in s:
#         if i == "6":
#             count += 1
#         else:
#             count = 0
#     return count


# def create_end_num(n):
#     end_num = "666"
#     count = 1
#     for i in range(n):
#         if i % 10 == 6:
#             six_count = count_six(str(i))
#             for j in range(10**six_count):
#                 n_end_num = (
#                     str(i)[:-six_count] + end_num + str(f"{j:0{six_count}}")
#                 )
#                 if count == n:
#                     return int(n_end_num)
#                 count += 1
#         else:
#             n_end_num = str(i) + end_num
#             if count == n:
#                 return int(n_end_num)
#             count += 1


# print(create_end_num(n))
########### 230115 숫자 카드 ###########
# import sys

# N = int(input())
# n_li = list(map(int, sys.stdin.readline().split()))
# n_li.sort()
# M = int(input())
# m_li = list(map(int, sys.stdin.readline().split()))
# result_list = []


# def check_num(li, target):
#     start = 0
#     end = len(li) - 1
#     while start <= end:
#         mid = (start + end) // 2
#         if li[mid] == target:
#             return 1
#         elif li[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return 0


# for m in m_li:
#     result_list.append(check_num(n_li, m))
# print(*result_list)
######### 230116 문자열 집합 #############
# import sys

# input_li = [i.strip() for i in sys.stdin.readlines()]
# n, m = map(int, (input_li[0].split()))
# check_li = input_li[1 : n + 1]
# origin_li = input_li[n + 1 :]
# cnt = 0
# for i in origin_li:
#     if i in check_li:
#         cnt += 1
# print(cnt)
# ############ 포켓몬 마스터 ############
# import sys

# n, m = map(int, input().split())
# num_d = dict()
# name_d = dict()

# pocket_li = [
#     (i[0], i[1].strip()) for i in enumerate(sys.stdin.readlines(), start=1)
# ]
# for num, item in pocket_li[:n]:
#     num_d[str(num)] = item
#     name_d[item] = str(num)

# for _, target in pocket_li[n:]:
#     num_d.get(target) and print(num_d.get(target))
#     num_d.get(target) or print(name_d.get(target))
# ########### 큐 ############
# from collections import deque
# import sys

# n = int(input())
# command = [i.rstrip().split() for i in sys.stdin.readlines()]
# q = deque()
# for i in command:
#     if i[0] == "push":
#         q.append(int(i[1]))
#     elif i[0] == "front":
#         try:
#             f = q.popleft()
#             print(f)
#             q.appendleft(f)
#         except Exception:
#             print(-1)
#     elif i[0] == "back":
#         try:
#             b = q.pop()
#             print(b)
#             q.append(b)
#         except Exception:
#             print(-1)
#     elif i[0] == "pop":
#         try:
#             print(q.popleft())
#         except Exception:
#             print(-1)
#     elif i[0] == "size":
#         print(len(q))
#     elif i[0] == "empty":
#         q_len = len(q)
#         if q_len:
#             print(0)
#         else:
#             print(1)
# ############### 숫자 카드 2 ########
# N = int(input())
# n_li = list(map(int, input().split()))
# M = int(input())
# m_li = list(map(int, input().split()))
# n_d = dict()
# for n in n_li:
#     if n_d.get(n):
#         n_d[n] = n_d.get(n) + 1
#     else:
#         n_d[n] = 1
# for m in m_li:
#     target = n_d.get(m)
#     if target:
#         print(target, end=" ")
#     else:
#         print(0, end=" ")
######## 230117 듣보잡 #########
# import sys

# N, M = map(int, input().split())

# li = [i.strip() for i in sys.stdin.readlines()]
# n_set = set(li[:N])
# m_li = li[N:]
# m_li.sort()
# m_set = set(m_li)
# print(len(m_set.intersection(n_set)))

# for m in m_li:
#     if m in n_set:
#         print(m)
# ########## 대칭 차집합 #############
# A_len, B_len = map(int, input().split())
# A_set = set(map(int, input().split()))
# B_set = set(map(int, input().split()))
# A_B = len(A_set - B_set)
# B_A = len(B_set - A_set)
# print(A_B + B_A)
# ##### 서로 다른 부분 문자열의 개수 #######
# s = input()
# s_len = len(s)
# s_set = set()
# count = 0
# for i in range(s_len):
#     for j in range(i + 1, s_len + 1):
#         item = s[i:j]
#         item in s_set or s_set.add(item)
# print(len(s_set))
# ########## 네 번째 점 ############
# import sys

# coor1, coor2, coor3 = [
#     [*map(int, i.rstrip().split())] for i in sys.stdin.readlines()
# ]
# coor_zip = list(zip(coor1, coor2, coor3))
# for i in coor_zip:
#     for j in i:
#         if i.count(j) == 1:
#             print(j, end=" ")
# ######## 직각삼각형 #############
# while True:
#     test_li = list(map(int, input().split()))
#     test_li.sort()
#     a = test_li[0]
#     b = test_li[1]
#     c = test_li[2]
#     if sum(test_li) == 0:
#         break
#     if a**2 + b**2 == c**2:
#         print("right")
#     else:
#         print("wrong")
# ########## 참외밭 ################
# # 동:1, 서:2, 남:3, 북:4
# # (┏, ┗, ┛,ㄱ)
# from collections import deque

# melon_per_sqmt = int(input())
# m_li = deque()
# for _ in range(6):
#     direction, m = map(int, input().split())
#     m_li.append(m)
# MAX = 0
# for _ in range(6):
#     MAX = max(MAX, m_li[0] + m_li[1])
#     m_li.rotate()
# while (m_li[0] + m_li[1]) != MAX:
#     m_li.rotate()
# print(melon_per_sqmt * (m_li[0] * m_li[1] - (m_li[3] * m_li[4])))
############### 230118 택시 기하학 ################
# from math import pi

# n = int(input())

# print(f"{n**2 * pi:6f}")
# print(f"{((n**2 * 2) ** 0.5) ** 2:6f}")
# ######## 터렛 #########
# import sys

# n = int(input())
# turret_li = [list(map(int, i.rstrip().split())) for i in sys.stdin.readlines()]
# for turret in turret_li:
#     x1, y1, r1 = turret[0], turret[1], turret[2]
#     x2, y2, r2 = turret[3], turret[4], turret[5]

#     distance = (abs(x2 - x1) ** 2 + abs(y2 - y1) ** 2) ** 0.5
#     distance = round(distance, 10)
#     # print(distance)
#     MIN = min(r1, r2)
#     MAX = max(r1, r2)
#     delta_r = MAX - MIN
#     sum_r = r2 + r1
#     if distance == 0 and r1 == r2:
#         print(-1)
#     elif distance == delta_r:
#         print(1)
#     elif distance == sum_r:
#         print(1)
#     elif delta_r < distance < sum_r:
#         print(2)
#     else:
#         print(0)
# ########## 어린 왕자 #############
# t = int(input())


# def calculate_distance(x1, y1, x2, y2):
#     return round((abs(x2 - x1) ** 2 + abs(y2 - y1) ** 2) ** 0.5, 10)


# for _ in range(t):
#     x1, y1, x2, y2 = map(int, input().split())
#     count = 0
#     n = int(input())
#     for _ in range(n):
#         cx, cy, r = map(int, input().split())
#         star_start_dist = calculate_distance(x1, y1, cx, cy)
#         star_end_dist = calculate_distance(x2, y2, cx, cy)
#         if star_start_dist < r and star_end_dist < r:
#             continue
#         elif star_start_dist < r:
#             count += 1
#         elif star_end_dist < r:
#             count += 1
#         else:
#             continue
#     print(count)
# ###### 배수와 약수 ######
# import sys

# case_li = [list(map(int, i.rstrip().split())) for i in sys.stdin.readlines()][
#     :-1
# ]
# for case in case_li:
#     a, b = case[0], case[1]
#     if b % a == 0:
#         print("factor")
#     elif a % b == 0:
#         print("multiple")
#     else:
#         print("neither")
# ##### 3n + 1 수열 ##########
# N = int(input())


# def C(n, count=0):
#     count += 1
#     if n == 1:
#         return count
#     if n % 2 == 0:
#         return C(n / 2, count)
#     else:
#         return C(n * 3 + 1, count)


# print(C(N))
# ######### 약수 ###########
# n = int(input())
# num_li = list(map(int, input().split()))

# if n == 1:
#     print(num_li[0] ** 2)
# else:
#     print(min(num_li) * max(num_li))
# ###### 최대공약수와 최소공배수 ########
# b, a = sorted(list(map(int, input().split())))


# def gcd(a, b):
#     r = a % b
#     if r == 0:
#         return b
#     else:
#         return gcd(b, r)


# def lcm(a, b, GCD):
#     return (a * b) // GCD


# GCD = gcd(a, b)
# LCM = lcm(a, b, GCD)
# print(GCD)
# print(LCM)
########## 230119 수열과 커리 38 (18917) ##########
# import sys

# n = int(input())
# query_li = [list(map(int, i.rstrip().split())) for i in sys.stdin.readlines()]
# A = [0]
# A_sum = 0
# A_xor_sum = 0
# for query in query_li:
#     if query[0] == 1:
#         # A.append(query[1])
#         A_xor_sum ^= query[1]
#         A_sum += query[1]
#     elif query[0] == 2:
#         # A.remove(query[1])
#         A_sum -= query[1]
#         A_xor_sum ^= query[1]
#     elif query[0] == 3:
#         print(A_sum)
#     else:
#         print(A_xor_sum)
######### 최소공배수 ########
# T = int(input())


# def gcd(a, b):
#     if a % b == 0:
#         return b
#     else:
#         return gcd(b, a % b)


# for _ in range(T):
#     a, b = sorted(list(map(int, input().split())), reverse=True)
#     print(a * b // (gcd(a, b)))
########## 검문 (2981) ########
import sys
from functools import reduce

N = int(input())
li = sorted([int(i.rstrip()) for i in sys.stdin.readlines()])


def gcd(a, b):
    if b > a:
        a, b = b, a
    if a % b == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcd(b, a % b)


def li_gcd(li: list):
    new_li = li[:]
    for i in range(len(new_li) - 1):
        new_li[i + 1] = gcd(new_li[i], new_li[i + 1])
    return new_li[-1]


def new_li_maker(li):
    length = len(li)
    new_li = []
    for i in range(length):
        if i + 1 == length:
            new_li.append(li[i] - li[0])
        else:
            new_li.append(li[i + 1] - li[i])
    return sorted(new_li)


def factorization(num, num_li=[0]):
    if num < max(num_li):
        # print("🔥", num_li, num)
        num_li.remove(0)
        new_li = []
        for i in range(len(num_li)):
            for j in range(i + 1, len(num_li) + 1):
                new_li.append(reduce(lambda x, y: x * y, num_li[i:j]))
        # print("✨", new_li)
        return sorted(set(new_li))
    else:
        for i in range(2, num + 1):
            if num % i == 0:
                # print("🔥", "i:", i, "num:", num, "num_li:", num_li)
                num_li.append(i)
                return factorization(num // i, num_li)


li = new_li_maker(li)
GCD = li_gcd(li)
result = factorization(GCD)
print(*result, sep=" ")

# result_set = set()
# while li[0] > 1:
#     GCD = li_gcd(li)
#     if GCD != 1:
#         print(GCD)
#         result_set.add(GCD)
#     li = list(map(lambda x: x - 1, li))

# print(*sorted(result_set), sep=" ")


def get_submultiple_li(num):
    num_li = []
    for i in range(2, num + 1):
        if num % i == 0:
            print(num)
            num = num // i

            num_li.append(i)

    return sorted(num_li)
