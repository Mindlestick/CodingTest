# 국회의원 선거
answer = 0
n = int(input())
nlist = []
target = int(input())
for i in range(n - 1):
    nlist.append(int(input()))

if n == 1 or target > max(nlist):
    print(0)
    exit()

while (1):
    if target > max(nlist):
        break
    nlist.sort(reverse=True)
    target += 1
    nlist[0] -= 1

    answer += 1
    # print(nlist)
print(answer)