# 모든 순열
def dfs(start):
    if len(answer)==n:
        print(' '.join(map(str,answer)))
        return
    
    for i in range(1,n+1):
        if i in answer:
            continue
        answer.append(i)
        dfs(i+1)
        answer.pop()
        
n=int(input())
answer=[]
dfs(0)