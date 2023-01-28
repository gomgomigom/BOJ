# a = list(map(int, input().split()))
# A, B = a
# if A > B:
#     print(">")
# elif B > A:
#     print("<")
# else:
#     print("==")

# a = int(input())
# if a >= 90:
#     print("A")
# elif a >= 80:
#     print("B")
# elif a >= 70:
#     print("C")
# elif a >= 60:
#     print("D")
# else:
#     print("F")

# a = int(input())
# if a % 4 == 0 and (a % 100 != 0 or a % 400 == 0):
#     print(1)
# else:
#     print(0)

# a = int(input())
# b = int(input())
# result = ""
# if a > 0 and b > 0:
#     print(1)
# elif a > 0 and b < 0:
#     print(4)
# elif a < 0 and b > 0:
#     print(2)
# else:
#     print(3)

# a = list(map(int, input().split()))
# x, y = a

# if y - 45 < 0:
#     x -= 1
#     y = 60 - 45 + y
#     if x < 0:
#         x = 23
# else:
#     y = y - 45
# print(x, y)

# a = list(map(int, input().split()))
# t = int(input())
# h, m = a
# if t >= 60:
#     h += t // 60
#     t = t % 60
#     if h >= 24:
#         h = h % 24
# if m + t >= 60:
#     h += 1
#     m = m + t - 60
#     if h == 24:
#         h = 0
# else:
#     m = m + t
# print("%d %d" % (h, m))
# #

a = list(map(int, input().split()))
s = set()
length = len(set(a))
if length == 1:
    print(10000 + max(a) * 1000)
elif length == 2:
    dup = list({x for x in a if x in s or (s.add(x) or False)})
    print(1000 + dup[0] * 100)
else:
    print(max(a) * 100)
