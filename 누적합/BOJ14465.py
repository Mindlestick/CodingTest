# 소가 길을 건너간 이유 5
n,k,b=map(int,input().split())
nlist=[1 for i in range(n)]
for i in range(b):
    e=int(input())
    nlist[e-1]=0

init=sum(nlist[:k])
answer=[init]
for i in range(n-k):
    init=init-nlist[i]+nlist[i+k]
    answer.append(init)
print(k-max(answer))