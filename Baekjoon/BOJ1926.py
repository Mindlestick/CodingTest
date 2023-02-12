# 그림
import sys
from collections import deque
input=sys.stdin.readline

dx=[-1,1,0,0]
dy=[0,0,-1,1]
c=[]
def bfs(x,y):
    q.append((x,y))
    g[x][y]=0
    t=1

    while len(q):
        x,y=q.popleft()
        for i in  range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if g[nx][ny]==0:
                continue
            if g[nx][ny]==1:
                q.append((nx,ny))
                g[nx][ny]=g[x][y]
                t+=1
    c.append(t)

n,m=map(int,input().split())
g=[]
q=deque()
visit=[[False]*m for i in range(n)]

for i in range(n):
    g.append(list(map(int,input().split())))

cnt=0
for i in range(n):
    for j in range(m):
        if g[i][j]==1:
            bfs(i,j)
            cnt+=1

if cnt==0:
    answer=0
else:
    answer = max(c)
print(cnt)
print(answer)