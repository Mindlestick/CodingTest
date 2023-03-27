# N과 M (1)
def dfs(d,n,m):
    if d==m:
        print(' '.join(map(str,answer)))
        
    for i in range(1,n+1):
        if visited[i]==False:
            visited[i] =True
            answer.append(i)
            dfs(d+1,n,m)
            visited[i]=False
            answer.pop()

n,m=map(int,input().split())
visited=[False]*(n+1)
answer=[]
dfs(0,n,m)