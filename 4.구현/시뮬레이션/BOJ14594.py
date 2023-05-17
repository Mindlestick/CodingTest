# 동방 프로젝트 (Small)

n=int(input())
nlist=[0]*(n+1)
m=int(input())
for i in range(m):
    a,b=map(int,input().split())
    for j in range(a,b):
        nlist[j]=1
print(nlist.count(0)-1)