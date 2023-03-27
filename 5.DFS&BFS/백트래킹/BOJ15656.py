# N과 M (7)
n,m=map(int,input().split())
nlist=list(map(int,input().split()))
nlist.sort()
answer=[]

def dfs(start):
    if len(answer)==m:
        print(' '.join(map(str,answer)))
        return
    
    for i in range(n):
        answer.append(nlist[i])
        dfs(i)
        answer.pop()
        
dfs(0)