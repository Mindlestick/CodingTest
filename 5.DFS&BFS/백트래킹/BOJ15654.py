# N과 M (5)
n,m=map(int,input().split())
nlist=list(map(int,input().split()))
nlist.sort()
answer=[]

def dfs(start):
    if len(answer)==m:
        print(' '.join(map(str,answer)))
        return
    
    for i in range(n):
        if nlist[i] not in answer:
            answer.append(nlist[i])
            dfs(i+1)
            answer.pop()

dfs(0)