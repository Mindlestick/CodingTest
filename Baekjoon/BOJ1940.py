# 주몽
n=int(input())
m=int(input())
nlist=list(map(int,input().split()))
nlist.sort()
#print(nlist)
answer=0

for i in nlist:
    if m-i in nlist:
        answer+=1

print(answer//2)