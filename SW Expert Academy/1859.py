# 백만 장자 프로젝트

T = int(input())
for i in range(T):
    n = int(input())
    nlist = list(map(int, input().split()))
    answer = 0

    nlist.reverse()
    max_num = 0
    for j in range(n):
        if max_num < nlist[j]:
            max_num = nlist[j]
        else:
            answer+=max_num-nlist[j]

    print('#' + str(i+1), answer)