# 근손실
n,k=map(int,input().split())
nlist=list(map(int,input().split()))

answer=[]
global result
result=0

def dfs(start):
    if len(answer)==n:
        init=500
        #print(answer)
        for i in answer:
            init+=nlist[i]
            init-=k
            if init<500:
                return
        #print(init)
        
        global result
        result+=1
        return
    
    for i in range(n):
        if not i in answer:
            answer.append(i)
            dfs(i)
            answer.pop()

dfs(0)
print(result)