############ 230128 ###########
###### 피보나치 수1 24416 #######
N = int(input())


def fibonacci(n):
    if n <= 2:
        return 1
    pre, cur = 1, 1
    count = 0
    for i in range(n - 2):
        count += 1
        cur, pre = pre + cur, cur
    return cur, count


print(*fibonacci(N))
