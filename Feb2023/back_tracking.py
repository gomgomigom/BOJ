# =============== 230202 ===============
# =============== 부분수열의 합 1182 ===============

# N, S = 5, 0
# n_arr = [-7, -3, -2, 5, 8]
# N, S = map(int, input().split())
# n_arr = list(map(int, input().split()))
# visited = [0] * N
# sub_arr = [[]]
# temp_arr = []


# def part(cnt=0):
#     if len(temp_arr) == cnt and cnt != 0:
#         sub_arr.append(temp_arr)
#     else:
#         for i in range(N):
#             if visited[i]:
#                 continue
#             else:
#                 visited[i] = 1
#                 temp_arr.append(n_arr[i])
#                 part(i + 1)
#                 temp_arr.pop()
#                 visited[i] = 0


# part(0)
# count = 0
# for i in sub_arr:
#     if sum(i) == S:
#         count += 1
# print(count)
# =============== 230205 ===============
# N, S = 5, 0
# n_arr = [-7, -3, -2, 5, 8]
# N, S = map(int, input().split())
# n_arr = list(map(int, input().split()))

# cnt = [0]


# def part(cnt, index, total):
#     if index >= N:
#         return
#     total += n_arr[index]
#     if total == S:
#         cnt[0] += 1
#         return
#     else:
#         part(cnt, index + 1, total)
#         part(cnt, index + 1, total - n_arr[index])


# part(cnt, 0, 0)
# print(cnt[0])
# =============== 230205 ===============
# =============== 부분수열의 합 1182 ===============
# N, S = 5, 0
# n_arr = [-7, -3, -2, 5, 8]
# n_arr = [0, 0, 0, 0, 0]
# N, S = map(int, input().split())
# n_arr = list(map(int, input().split()))
# cnt = [0]
# temp_arr = []


# def part(index):
#     if len(temp_arr) > 0 and sum(temp_arr) == S:
#         cnt[0] += 1

#     for i in range(index, N):
#         temp_arr.append(n_arr[i])
#         part(i + 1)
#         temp_arr.pop()


# part(0)
# print(cnt[0])
# =============== 230206 ===============
# =============== 연산자 끼워넣기 14888 ===============
# import sys

# N = int(input())
# N_arr = list(map(int, sys.stdin.readline().strip().split()))
# add, sub, mul, div = map(int, input().split())
# result_arr = []


# def cal(index, pre, add, sub, mul, div):
#     if index == N:
#         result_arr.append(pre)
#         return
#     else:
#         if add > 0:
#             cal(index + 1, pre + N_arr[index], add - 1, sub, mul, div)
#         if sub > 0:
#             cal(index + 1, pre - N_arr[index], add, sub - 1, mul, div)
#         if mul > 0:
#             cal(index + 1, pre * N_arr[index], add, sub, mul - 1, div)
#         if div > 0:
#             if pre < 0:
#                 cal(
#                     index + 1,
#                     -(abs(pre) // N_arr[index]),
#                     add,
#                     sub,
#                     mul,
#                     div - 1,
#                 )
#             else:
#                 cal(
#                     index + 1,
#                     pre // N_arr[index],
#                     add,
#                     sub,
#                     mul,
#                     div - 1,
#                 )


# cal(1, N_arr[0], add, sub, mul, div)
# # print(result_arr)
# print(max(result_arr))
# print(min(result_arr))
# =============== 230207 ===============
# =============== 스타트와 링크 14889 ===============
# import sys
# from itertools import permutations

# N = int(input())
# Sij = [[*map(int, i.rstrip().split())] for i in sys.stdin.readlines()]
# start_arr = []
# link_arr = []
# origin_set = set([i for i in range(1, N + 1)])
# visited = [0] * (N + 1)


# def start_link(result):
#     if len(result) == N // 2:
#         # start_arr.append(result[:])
#         link_arr.append(list(origin_set - set(result)))
#         return

#     for i in range(1, N + 1):
#         if visited[i]:
#             continue
#         else:
#             result.append(i)
#             visited[i] = 1
#             start_link(result)
#             visited[i] = 0
#             result.pop()


# def score(arr):
#     total = 0
#     for item in arr:
#         i, j = item[0] - 1, item[1] - 1
#         total += Sij[i][j]
#     return total


# start_link([])

# min_num = 1e10


# for i in range(len(link_arr) // 2 + 1):
#     start_coor = list(permutations(list(origin_set - set(link_arr[i])), 2))
#     start_total = score(start_coor)
#     link_coor = list(permutations(link_arr[i], 2))
#     link_total = score(link_coor)
#     min_num = min(min_num, abs(start_total - link_total))

# print(min_num)
# =============== 230208 ===============
import time
import sys
from itertools import permutations

N = int(input())
Sij = [[*map(int, i.rstrip().split())] for i in sys.stdin.readlines()]
origin_set = set([i for i in range(1, N + 1)])
visited = [0] * (N + 1)
min_num = 1e10


def score(arr):
    total_start = 0
    total_link = 0
    for item in arr:
        link_item = list(origin_set - set(item))
        i, j = item[0] - 1, item[1] - 1
        i2, j2 = link_item[0] - 1, link_item[1] - 1
        total_start += Sij[i][j]
        total_link += Sij[i2][j2]
    total = abs(total_start - total_link)
    return total


def start_link(result):
    global min_num
    if len(result) == N // 2:
        start_arr = result
        # link_arr = list(origin_set - set(result))
        start_coor = list(permutations(start_arr, 2))
        min_num = min(min_num, score(start_coor))
        # link_coor = list(permutations(link_arr, 2))
        # link_total = score(link_coor)
        # min_num = min(min_num, abs(start_total - link_total))
        return

    for i in range(1, N + 1):
        if visited[i]:
            continue
        else:
            result.append(i)
            visited[i] = 1
            start_link(result)
            visited[i] = 0
            result.pop()


s = time.time()
start_link([])
e = time.time()
# print("\033[102m\033[1m", e - s, "\033[0m")
print(min_num)
