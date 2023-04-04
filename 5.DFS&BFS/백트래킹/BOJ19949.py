# 영재의 시험
def dfs(depth):
    global result
    
    if depth==10:
        score=0
        for i in range(10):
            if li[i] == answer[i]:
                score+=1
        if score>=5:
            result+=1
        return
            
    for i in range(1,6):
        if depth>=2 and i == li[depth-1] ==li[depth-2]:
            continue
        li.append(i)
        dfs(depth+1)
        li.pop()

answer=list(map(int,input().split()))
li=[]
result=0
dfs(0)
print(result)