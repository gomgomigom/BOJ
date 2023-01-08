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
import sys

line = int(sys.stdin.readline())
counting = [0] * 10000
for _ in range(line):
    number = int(sys.stdin.readline())
    counting[number - 1] += 1

for index, i in enumerate(counting, start=1):
    if i:
        for _ in range(i):
            print(index)
