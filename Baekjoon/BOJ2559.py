# 수열
n,k=map(int,input().split())
nlist=list(map(int,input().split()))
init=sum(nlist[:k])
answer=[init]
for i in range(n-k):
    init=init-nlist[i]+nlist[i+k]
    answer.append(init)
print(max(answer))