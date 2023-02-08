# =============== 230203 ===============
# =============== 요세푸스 문제0 11866 ===============
# from collections import deque

# N, K = map(int, input().split())
# N_arr = deque([i for i in range(1, N + 1)])
# yo = []
# while N_arr:
#     N_arr.rotate(-K)
#     yo.append(N_arr.pop())
# print("<", end="")
# print(*yo, sep=", ", end="")
# print(">")
# =============== 230204 ===============
# =============== 아니메 컵 1쿨 A번 ===============
# emoji = input()
# score = len(emoji)
# for i in emoji:
#     if i == ":":
#         score += 1
#     elif i == "_":
#         score += 5

# print(score)
# =============== 아니메 컵 1쿨 B번 ===============
# import sys


# T = int(input())
# for _ in range(T):
#     R, C = map(int, input().split())
#     latte_art = [input() for _ in range(R)]
#     print(latte_art)

#     start_arr = []
#     for row in latte_art:

#         index = -1
#         for c in range(C):
#             if row[c] == "#":
#                 index += 1
#                 start_arr.append(index)
#             else:
#                 start_arr.append(index)
#     print(start_arr)
# =============== 230207 ===============
# =============== 스택 10828 ===============
import sys

N = int(input())
stack = []
input_arr = [i.rstrip().split() for i in sys.stdin.readlines()]
for order in input_arr:
    if order[0] == "push":
        stack.append(order[1])
    elif order[0] == "pop":
        try:
            print(stack.pop())
        except Exception:
            print(-1)
    elif order[0] == "size":
        print(len(stack))
    elif order[0] == "empty":
        if len(stack) >= 1:
            print(0)
        else:
            print(1)
    else:
        try:
            print(stack[-1])
        except Exception:
            print(-1)
