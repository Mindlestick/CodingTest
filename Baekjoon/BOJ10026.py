# 적록색약
import sys
from collections import deque
input=sys.stdin.readline

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(x,y):
    q=deque()
    q.append((x,y))
    visit[x][y]=True

    while len(q):
        x,y=q.popleft()
        #print(x,y)

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or ny<0 or nx>=n or ny >= n:
                continue
            if visit[nx][ny]==False and g[x][y]==g[nx][ny]:
                q.append((nx,ny))
                visit[nx][ny]=True

n=int(input())
g=[]
for i in range(n):
    g.append(list(input().strip()))
visit=[[False]*n for i in range(n)]

answer0=0
answer1=0
for i in range(n):
    for j in range(n):
        if visit[i][j]==False:
            bfs(i,j)
            answer0+=1
print(answer0,end=' ')

for i in range(n):
    for j in range(n):
        if g[i][j]=='R':
            g[i][j]='G'

visit=[[False]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if visit[i][j]==False:
            bfs(i,j)
            answer1+=1
print(answer1)