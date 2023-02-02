# =============== 230202 ===============
from collections import deque

N = int(input())
n_arr = deque([i for i in range(1, N + 1)])

while len(n_arr) >= 1:
    result = n_arr.popleft()
    n_arr.rotate(-1)

print(result)
