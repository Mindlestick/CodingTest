# N과 M (2)
def dfs(start):
    if len(answer)==m:
        print(' '.join(map(str,answer)))
        return
        
    for i in range(start,n+1):
        if not i in answer:
            answer.append(i)
            dfs(i+1)
            answer.pop()
            
n,m=map(int,input().split())
answer=[]
dfs(1)