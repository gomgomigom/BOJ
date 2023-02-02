# ############ 230128 ###########
# ###### 피보나치 수1 24416 #######
# N = int(input())


# def fibonacci(n):
#     if n <= 2:
#         return 1
#     pre, cur = 1, 1
#     count = 0
#     for i in range(n - 2):
#         count += 1
#         cur, pre = pre + cur, cur
#     return cur, count


# print(*fibonacci(N))
############ 230129 #########
###### 신나는 함수 실행 9184 #######
# import sys


# def fun(a, b, c):
#     if (a, b, c) in check:
#         return check[(a, b, c)]
#     else:
#         if a <= 0 or b <= 0 or c <= 0:
#             check[(a, b, c)] = 1
#             return 1
#         elif a > 20 or b > 20 or c > 20:
#             check[(a, b, c)] = fun(20, 20, 20)
#             return fun(20, 20, 20)
#         elif a < b and b < c:
#             check[(a, b, c)] = (
#                 fun(a, b, c - 1) + fun(a, b - 1, c - 1) - fun(a, b - 1, c)
#             )
#             return fun(a, b, c - 1) + fun(a, b - 1, c - 1) - fun(a, b - 1, c)
#         else:
#             check[(a, b, c)] = (
#                 fun(a - 1, b, c)
#                 + fun(a - 1, b - 1, c)
#                 + fun(a - 1, b, c - 1)
#                 - fun(a - 1, b - 1, c - 1)
#             )
#             return (
#                 fun(a - 1, b, c)
#                 + fun(a - 1, b - 1, c)
#                 + fun(a - 1, b, c - 1)
#                 - fun(a - 1, b - 1, c - 1)
#             )


# check = dict()
# input_li = [i.rstrip().split() for i in sys.stdin.readlines()][:-1]
# for i in input_li:
#     result = fun(int(i[0]), int(i[1]), int(i[2]))
#     print(f"w({i[0]}, {i[1]}, {i[2]}) = {result}")
# ############### 230130 ################
######### 수 정렬하기 5 15688 ##########
# import sys

# n = int(input())
# n_li = [int(i.rstrip()) for i in sys.stdin.readlines()]
# # n = 5
# # n_li = [1, 2, 1, 2, 1]
# n_li.sort()
# print(*n_li, sep="\n")
############# 230131 ##########
############ 구간 합 구하기4 11659 ###########
# import sys

# N, M = map(int, input().split())
# n_arr = list(map(int, input().split()))
# terms = [[*map(int, i.rstrip().split())] for i in sys.stdin.readlines()]

# sum_arr = [0]
# total = 0
# for i in n_arr:
#     total += i
#     sum_arr.append(total)

# for term in terms:
#     start = term[0] - 1
#     end = term[1]
#     print(sum_arr[end] - sum_arr[start])
########## 230201 ############
# =============== 230201 ===============
import sys

input_data = [i.rstrip() for i in sys.stdin.readlines()][:-1]

for i in input_data:
    if i == i[::-1]:
        print("yes")
    else:
        print("no")
