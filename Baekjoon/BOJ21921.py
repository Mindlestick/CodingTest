n,x=map(int,input().split())
nlist=list(map(int,input().split()))
init=sum(nlist[:x])
answer=[init]
for i in range(n-x):
    init=init-nlist[i]+nlist[i+x]
    answer.append(init)
if max(answer)==0:
    print('SAD')
else:
    print(max(answer))
    print(answer.count(max(answer)))