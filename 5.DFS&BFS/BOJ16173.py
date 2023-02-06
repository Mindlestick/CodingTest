#점프왕 쩰리 (Small)

import sys
from collections import deque

dx=[1,0]
dy=[0,1]

def bfs(x,y):
    q=deque()
    q.append((x,y))
    visit[x][y]=True

    while len(q):
        x,y=q.popleft()

        for i in range(2):
            nx=g[x][y]*dx[i]+x
            ny=g[x][y]*dy[i]+y

            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if g[nx][ny]==-1:
                return 'HaruHaru'

            if visit[nx][ny]==False:
                q.append((nx,ny))
                visit[nx][ny]=True
    return 'Hing'


n=int(input())
g=[]
visit=[[False]*n for i in range(n)]
for i in range(n):
    g.append(list(map(int,input().split())))
print(bfs(0,0))