# input = int(input())
# for i in range(1, 10):
#     print(f"{input} * {i} = {input * i}")

# 230101-------------------------------------------
import sys

len_num = int(sys.stdin.readline())
num_list = [
    list(map(int, sys.stdin.readline().split())) for i in range(len_num)
]
for i in num_list:
    print(i[0] + i[1])

# ------------------
import sys

num = int(sys.stdin.readline())
sum = 0
for i in range(1, num + 1):
    sum += i
print(sum)
# ---------------------
import sys

sum = int(sys.stdin.readline())
length = int(sys.stdin.readline())
item_list = [
    list(map(int, sys.stdin.readline().split())) for item in range(length)
]
sum_test = 0
for item in item_list:
    sum_test += item[0] * item[1]
if sum_test == sum:
    print("Yes")
else:
    print("No")
# ----------------------------
import sys

len_num = int(sys.stdin.readline())
for index, i in enumerate(range(len_num), start=1):
    a, b = map(int, sys.stdin.readline().split())
    print(f"Case #{index}: {a} + {b} = {a+b}")
# ---------------------------
import sys

len_num = int(sys.stdin.readline())
for i in range(1, len_num + 1):
    star = "*" * i
    print(f"{star: >{len_num}}")
# ----------------------
import sys

lines = sys.stdin.readlines()
for line in lines:
    a, b = map(int, line.split())
    print(a + b)
# ------------------------
n = input()
if int(n) < 10:
    n = "0" + n
i = 0
answer = n
while True:
    n = str(n[-1]) + str(int(n[0]) + int(n[1]))[-1]
    i += 1
    if n == answer:
        break
print(i)
