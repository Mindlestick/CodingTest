# 물병
def pour(before,f,t):
    after=list(before)
    n=0
    if t==0:
       n=a
    elif t==1:
        n=b
    elif t==2:
        n=c

    if after[f] <= n-after[t]:
        after[t] += after[f]
        after[f]=0
    else:
        after[f]-=(n-after[t])
        after[t]=n

    return after

def func(curr):
    next_status=[]
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            tmp = pour(curr, i, j)
            if tmp not in visited:
                visited.append(tmp)
                next_status.append(tmp)
    return next_status


a,b,c=map(int,input().split())
visited=[[0,0,c]]
answer=[]

q=func([0,0,c])
for curr in q:
    q+=func(curr)

for v in visited:
    if v[0]==0:
        answer.append(v[2])
answer.sort()
print(' '.join(map(str,answer)))