# 최후의 승자는 누구?
n,m=map(int,input().split())
nlist=[[] for i in range(n)]
score=[0]*n
for i in range(n):
    tmp=list(map(int,input().split()))
    tmp.sort(reverse=True)
    nlist[i]=tmp
for i in range(m):
    t=[]
    for j in range(n):
        t.append(nlist[j][i])
    #print(t,max(t))
    for j in range(n):
        if nlist[j][i]==max(t):
            score[j]+=1
max_score=max(score)
for i in range(n):
    if score[i]==max_score:
        print(i+1, end=' ')
