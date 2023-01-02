# # 230103-----------------------
num = int(input())
count = 0
for i in range(1, num + 1):
    if i < 100:
        count += 1
    else:
        str_i = str(i)
        delta = set()
        for j in range(len(str_i) - 1):
            delta.add(int(str_i[j]) - int(str_i[j + 1]))
        if len(delta) == 1:
            count += 1
print(count)
