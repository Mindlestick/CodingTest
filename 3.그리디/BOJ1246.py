# 온라인 판매
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
p=[]
answer=[]
for i in range(m):
    p.append(int(input()))
p.sort()
#print(p)
for i in range(m):
    c=sum(1 for j in p if j>=p[i])
    #최대 계란 개수 넘어가지 않게
    if c>n:
        c=n
    answer.append(p[i]*c)
print(p[answer.index(max(answer))],max(answer))