# N과 M (9)
n,m=map(int,input().split())
nlist=list(map(int,input().split()))
nlist.sort()
answer=[]
num=[0]*(max(nlist)+1)

for i in nlist:
    num[i]+=1

def dfs(start):
    if len(answer)==m:
        print(' '.join(map(str,answer)))
        return
    
    for i in range(max(nlist)+1):
        if num[i]>0:
            answer.append(i)
            num[i]-=1
            dfs(i)
            answer.pop()
            num[i]+=1

dfs(0)
