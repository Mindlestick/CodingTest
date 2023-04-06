# 로마 숫자 만들기
def dfs(start):
    if n==len(s):
        answer[sum(s)]=True
        return
    
    for i in range(start,4):
        s.append(r[i])
        dfs(i)
        s.pop()
    
r=[1,5,10,50]
s=[]
answer=[False]*((50*20)+1)

n=int(input())
dfs(0)
print(sum(answer))