# import sys

# numbers = [int(i.strip()) for i in sys.stdin.readlines()]
# numbers.sort()
# print(int(sum(numbers) / 5))
# print(numbers[2])
# #################################
# N, k = map(int, input().split())
# score_li = list(map(int, input().split()))
# score_li.sort(reverse=True)
# print(score_li[k - 1])
# ##############################
# import sys

# line = int(sys.stdin.readline())
# counting = [0] * 10000
# for _ in range(line):
#     number = int(sys.stdin.readline())
#     counting[number - 1] += 1

# for index, i in enumerate(counting, start=1):
#     if i:
#         for _ in range(i):
#             print(index)
# ###########230109###############
# import sys


# numbers = int(input())
# num_li = [int(i.strip()) for i in sys.stdin.readlines()]
# num_li.sort()
# counting = [0] * 8001
# print(int(round((sum(num_li) / numbers), 0)))
# print(num_li[numbers // 2])
# for i in num_li:
#     counting[4000 + i] += 1
# new_counting = counting[:]
# max_index = counting.index(max(counting))
# max_value = counting[max_index]
# new_counting[max_index] = 0
# new_max_index = new_counting.index(max(new_counting))
# new_max_value = new_counting[new_max_index]
# if max_value == new_max_value:
#     print(new_max_index - 4000)
# else:
#     print(max_index - 4000)
# print(abs(num_li[-1] - num_li[0]))
# #####################################
# num = input()
# num_li = [int(i) for i in num]
# num_li.sort(reverse=True)
# print(*num_li, sep="")
# ###########################
# import sys

# number = int(input())

# xy_li = [list(map(int, i.strip().split())) for i in sys.stdin.readlines()]


# xy_li.sort(key=lambda x: (x[0], x[1]))
# for i in xy_li:
#     print(i[0], i[1])
# ##############################
# import sys

# num = int(input())

# s_li = list(set([i.strip() for i in sys.stdin.readlines()]))
# s_li = list(map(lambda x: [len(x), x], s_li))
# s_li.sort(key=lambda x: x[0])
# counting = [[] for i in range(51)]
# for length, s in s_li:
#     counting[length].append(s)

# for li in counting:
#     if len(li) >= 2:
#         li.sort()

# for i in counting:
#     len(i) and print(*i, sep="\n")
# ################################
# import sys

# num = int(input())
# member = []
# for _ in range(num):
#     age, name = sys.stdin.readline().split()
#     member.append([int(age), name])
# member.sort(key=lambda x: x[0])
# for i in member:
#     print(*i)
#########230109#########################
# import sys

# num = int(sys.stdin.readline())
# x = list(map(int, sys.stdin.readline().split()))

# not_dup_x = list(set(x))
# not_dup_x.sort()

# dict_x = {not_dup_x[i]: i for i in range(len(not_dup_x))}

# for i in x:
#     print(dict_x[i], end=" ")
##############factorial########################
# num = int(input())


# def fac(n):
#     if n <= 1:
#         return 1
#     else:
#         return n * fac(n - 1)


# print(fac(num))
########fibonacci#########################
# num = int(input())


# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n - 2) + fib(n - 1)


# print(fib(n))
############palindrome##################
# def recursion(s, l, r, cnt):
#     if l >= r:
#         cnt += 1
#         return 1, cnt
#     elif s[l] != s[r]:
#         cnt += 1
#         return 0, cnt
#     else:
#         cnt += 1
#         return recursion(s, l + 1, r - 1, cnt)


# def isPalindrome(s):
#     return recursion(s, 0, len(s) - 1, 0)


# num = int(input())
# for _ in range(num):
#     word = input()
#     print(*isPalindrome(word), sep=" ")
############병합정렬################
# def merge_sort(li, s, e, zero, target):
#     if e - s <= 0:
#         return
#     mid = (e + s) // 2
#     merge_sort(li, s, mid, zero, target)
#     merge_sort(li, mid + 1, e, zero, target)
#     merge(li, s, mid + 1, e, zero, target)
#     return zero[0]


# def merge(li, start, mid, end, zero, target):
#     merged = []
#     s, m = start, mid
#     while s < mid and m <= end:
#         if li[s] < li[m]:
#             merged.append(li[s])
#             s += 1
#         else:
#             merged.append(li[m])
#             m += 1
#     while s < mid:
#         merged.append(li[s])
#         s += 1
#     while m <= end:
#         merged.append(li[m])
#         m += 1
#     st = start
#     for i in merged:
#         li[st] = i
#         st += 1
#         zero[0] += 1
#         if zero[0] == target[0]:
#             print(i)
#     return zero[0]


# length, t = map(int, input().split())
# li = list(map(int, input().split()))
# k = [t]
# zero = [0]
# result = merge_sort(li, 0, length - 1, zero, target=k)
# if result < k[0]:
#     print(-1)
##########220111####별찍기##################


# def star(n, icon):
#     if n <= 3:
#         li = [[icon, icon, icon], [icon, " ", icon], [icon, icon, icon]]
#         return li
#     else:
#         s = [[] for _ in range(n)]
#         n //= 3
#         pre = star(n, icon)
#         for i in range(n):
#             for j in range(n):
#                 if pre[i][j] == icon:
#                     s[i * 3].extend([icon, icon, icon])
#                     s[i * 3 + 1].extend([icon, " ", icon])
#                     s[i * 3 + 2].extend([icon, icon, icon])
#                 else:
#                     s[i * 3].extend([" ", " ", " "])
#                     s[i * 3 + 1].extend([" ", " ", " "])
#                     s[i * 3 + 2].extend([" ", " ", " "])
#         return s


# num = int(input())
# result = star(num, "*")
# for i in result:
#     print(*i, sep="")
# ####### 230112 하노이탑 ########################
# from collections import deque


# def move(li, start, end):
#     li[end].append(li[start].pop())
#     print(start + 1, end + 1)
#     print(li)


# def hanoi(num, li, start, mid, end):
#     if num == 1:
#         move(li, start, end)
#     else:
#         hanoi(num - 1, li, start, end, mid)
#         move(li, start, end)
#         hanoi(num - 1, li, mid, start, end)


# num = int(input())
# li = [deque([i for i in range(num, 0, -1)]), deque(), deque()]

# print(2**num - 1)
# hanoi(num, li, 0, 1, 2)
############# 230113 VPS #############
# num = int(input())
# for _ in range(num):
#     a = input()
#     long = len(a)
#     left = a.count("(")
#     right = a.count(")")
#     if left != right:
#         print("NO")
#     else:
#         for _ in range(len(a)):
#             a = a.replace("()", "")
#         if a:
#             print("NO")
#         else:
#             print("YES")
# ############ 체스 보드판 색칠 #########
# import sys


# answer1 = "BWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWB"
# answer2 = "WBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBW"


# def cut_board(board, N, M):
#     row_range = N - 8 + 1
#     col_range = M - 8 + 1
#     board_str_list = []
#     for row_index in range(row_range):
#         new_board = board[row_index : row_index + 8]
#         for col_index in range(col_range):
#             board_str = ""
#             for i in range(8):
#                 board_str += new_board[i][col_index : col_index + 8]
#             board_str_list.append(board_str)
#     count_li = []
#     for board_str in board_str_list:
#         count1 = 0
#         count2 = 0
#         for i in range(64):
#             if board_str[i] != answer1[i]:
#                 count1 += 1
#             if board_str[i] != answer2[i]:
#                 count2 += 1
#         count_li.append(count1)
#         count_li.append(count2)
#     print(min(count_li))


# N, M = map(int, input().split())
# board = [i.split()[0] for i in sys.stdin.readlines()]
# cut_board(board, N, M)
# ########## 블랙잭 #################
# N, M = map(int, input().split())

# num_li = list(map(int, input().split()))
# num_li.sort()


# def find_numbers(li, M):
#     length = len(num_li)
#     temp = 0
#     for i in range(0, length):
#         for j in range(i + 1, length):
#             for k in range(j + 1, length):
#                 total = li[i] + li[j] + li[k]
#                 if total < M:
#                     temp = max(total, temp)
#                 elif total == M:
#                     return total
#                 else:
#                     break
#     return temp


# print(find_numbers(num_li, M))
# #############################
def define_part(y, x):
    st = x // 3 * 3
    en = x // 3 * 3 + 3
    row = y // 3 * 3
    print("\033[102m\033[1m", st, en, row, "\033[0m")


define_part(3, 8)
