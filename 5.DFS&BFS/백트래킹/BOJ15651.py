# N과 M (3)
def dfs(start):
    if len(answer)==m:
        print(' '.join(map(str,answer)))
        return
        
    for i in range(1,n+1):
        answer.append(i)
        dfs(i+1)
        answer.pop()
            
n,m=map(int,input().split())
answer=[]
dfs(1)