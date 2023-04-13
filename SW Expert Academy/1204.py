# [S/W 문제해결 기본] 1일차 - 최빈수 구하기

T = int(input())
for i in range(T):
    n = int(input())
    nlist = list(map(int, input().split()))
    max_num = 0
    max_cnt = 0

    for j in range(0,101):
        if max_cnt < nlist.count(j):
            max_cnt = nlist.count(j)
            max_num = j
        elif max_cnt == nlist.count(j):
            if j > max_num:
                max_num=j
                max_cnt=nlist.count(j)

    print('#' + str(n), max_num)