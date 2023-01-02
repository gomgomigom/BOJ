# # 230102--------------------------------------------
# n, x = map(int, input().split())
# num_list = list(map(int, input().split()))
# for i in num_list:
#     if i < x:
#         print(i, end=" ")
# # --------------------------------------
# n = input()
# num_list = list(map(int, input().split()))
# print(min(num_list), max(num_list))
# # ------------------------------------
# import sys

# num_list = list(map(int, sys.stdin.readlines()))
# max_num = max(num_list)
# print(max_num)
# print(num_list.index(max_num) + 1)
# # ------------------------------------
# import sys

# num_list = list(map(int, sys.stdin.readlines()))
# result = [num for num in range(1, 31) if num not in num_list]
# print(min(result))
# print(max(result))
# # ------------------------------------------
# import sys

# num_list = list(map(int, sys.stdin.readlines()))
# left = [num % 42 for num in num_list]
# print(len(set(left)))
# # ----------------------------
# n = int(input())
# score_list = list(map(int, input().split()))
# m = max(score_list)
# tampered_score = [score / m * 100 for score in score_list]
# print(sum(tampered_score) / n)
# # -------------------------------------------
# import sys

# n = int(input())
# ox_list = [ox.rstrip() for ox in sys.stdin.readlines()]

# for ox_string in ox_list:
#     total_score = 0
#     temp_score = 0
#     for ox in ox_string:
#         if ox == "O":
#             temp_score += 1
#         else:
#             temp_score = 0
#         total_score += temp_score
#     print(total_score)
# # --------------------------------------------------------
# import sys

# case_num = int(input())
# for _ in range(case_num):
#     case = list(map(int, sys.stdin.readline().split()))
#     num = case[0]
#     case_avg = sum(case[1:]) / num
#     above_avg = 0
#     for i in case[1:]:
#         if i > case_avg:
#             above_avg += 1
#     print(f"{above_avg/num*100:.3f}%")
# # # --------------------------------------


def solve():
    def d(n):
        for i in str(n):
            n += int(i)
        return n

    def li_d(n):
        dest = n
        if len(str(n)) >= 3:
            dest = (len(str(n))) * 10

        li = [d(i) for i in range(n - 1, n - dest, -1)]
        return li

    n = 1
    while n <= 10000:
        if n not in li_d(n):
            print(n)
        n += 1


solve()
