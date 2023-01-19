import sys
from functools import reduce

N = int(input())
li = sorted([int(i.rstrip()) for i in sys.stdin.readlines()])


def gcd(a, b):
    if b > a:
        a, b = b, a
    if a % b == 0:
        return b
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


# def factorization(num, num_li=[0]):
#     if num < max(num_li):
#         # print("🔥", num_li, num)
#         num_li.remove(0)
#         new_li = []
#         for i in range(len(num_li)):
#             for j in range(i + 1, len(num_li) + 1):
#                 new_li.append(reduce(lambda x, y: x * y, num_li[i:j]))
#         print("✨", new_li)
#         return sorted(set(new_li))
#     else:
#         print("❌else")
#         for i in range(2, num + 1):
#             if num % i == 0:
#                 print("🔥", "i:", i, "num:", num, "num_li:", num_li)
#                 num_li.append(i)
#                 return factorization(num // i, num_li)


def factorization2(num):
    divisor = set([num])
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            divisor.add(num // i)
            divisor.add(i)
    return sorted(divisor)


li = new_li_maker(li)
GCD = li_gcd(li)
result = factorization2(GCD)
print(*result)
