# ############ 230114 분해합 #############
# n = input()


# def constructor_finder(n):
#     constructor = []
#     n_len = len(n)
#     n = int(n)
#     if n < 20:
#         for num in range(1, n):
#             num_str = str(num)
#             num_sum = 0
#             for i in num_str:
#                 num_sum += int(i)
#             if num + num_sum == n:
#                 constructor.append(num)
#     else:
#         for num in range(n - n_len * 9, n):
#             num_str = str(num)
#             num_sum = 0
#             for i in num_str:
#                 num_sum += int(i)
#             if num + num_sum == n:
#                 constructor.append(num)
#     return constructor


# constructor = constructor_finder(n)
# constructor and print(min(constructor))
# constructor or print(0)
# ######### 덩치 ##########
# import sys

# n = int(input())
# member_li = [list(map(int, (i.strip().split()))) for i in sys.stdin.readlines()]
# member_len = len(member_li)
# rank_li = []


# for i in range(member_len):
#     rank = 1
#     for j in range(member_len):
#         if (member_li[i][0] < member_li[j][0]) and (
#             member_li[i][1] < member_li[j][1]
#         ):
#             rank += 1
#     rank_li.append(rank)

# print(*rank_li)
########### 영화감독 숌 ############
n = int(input())


def count_six(s):
    count = 0
    for i in s:
        if i == "6":
            count += 1
        else:
            count = 0
    return count


def create_end_num(n):
    end_num = "666"
    count = 1
    for i in range(n):
        if i % 10 == 6:
            six_count = count_six(str(i))
            for j in range(10**six_count):
                n_end_num = (
                    str(i)[:-six_count] + end_num + str(f"{j:0{six_count}}")
                )
                if count == n:
                    return int(n_end_num)
                count += 1
        else:
            n_end_num = str(i) + end_num
            if count == n:
                return int(n_end_num)
            count += 1


print(create_end_num(n))
