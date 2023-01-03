# # 230103-----------------------
# num = int(input())
# count = 0
# for i in range(1, num + 1):
#     if i < 100:
#         count += 1
#     else:
#         str_i = str(i)
#         delta = set()
#         for j in range(len(str_i) - 1):
#             delta.add(int(str_i[j]) - int(str_i[j + 1]))
#         if len(delta) == 1:
#             count += 1
# print(count)
# # ------------------------------------
# alp = input()
# print(ord(alp))
# # --------------------------------
# length = input()
# num = input()
# sum = 0
# for i in num:
#     sum += int(i)
# print(sum)
# # ----------------------------
# import sys

# length = int(input())
# for i in range(length):
#     data = sys.stdin.readline().split()
#     repeat = int(data[0])
#     data_str = data[1]
#     result = ""
#     for j in data_str:
#         result += j * repeat
#     print(result)
# # ---------------------------------
# input_str = input().upper()
# alp_list = [0 for _ in range(26)]
# for i in input_str:
#     target = ord(i) - 65
#     alp_list[target] += 1
# max = max(alp_list)
# if alp_list.count(max) >= 2:
#     print("?")
# else:
#     print(chr(alp_list.index(max) + 65))
# # ---------------------------------------
# m = [*map("Mississipi".upper().count, map(chr, range(65, 91)))]
# print([chr(65 + m.index(max(m))), "?"][m.count(max(m)) > 1])
# # ------------------------------------------------------------
# word_list = input().split()
# print(len(word_list))
# # -------------------
# a, b = input().split()
# new_a, new_b = "", ""
# for i in range(-1, -4, -1):
#     new_a += a[i]
#     new_b += b[i]
# new_list = [*map(int, [new_a, new_b])]
# print(max(new_list))
# # ------------------------------------------------------------
# word = input()
# time = [i for i in range(3, 11)]
# time.append(10)


# def position(w):
#     num = ord(w) - 65
#     if num < 15:
#         result = num // 3
#     elif num < 19:
#         result = 5
#     else:
#         result = (num - 1) // 3
#     return result


# sum = 0
# for i in word:
#     sum += time[position(i)]
# print(sum)
# # ------------------------------------------------------------
# import re

# word = "ljes=njak"
# croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
# count = 0
# for i in croatia:
#     if i in word:
#         while i in word:
#             word = re.sub(i, "*", word, 1)
#             count += 1
# word = re.sub("\*", "", word)
# count += len(word)
# print(count)
