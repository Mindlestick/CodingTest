# 토마토
import sys
from collections import deque
input=sys.stdin.readline

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs():
    while len(q):
        x,y=q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if g[nx][ny]==-1:
                continue
            if g[nx][ny]==0:
                g[nx][ny]=g[x][y]+1
                q.append((nx,ny))

m,n=map(int,input().split())
g=[]
for i in range(n):
    g.append(list(map(int,input().split())))
q=deque()

for i in range(n):
    for j in range(m):
        if g[i][j]==1:
            q.append((i,j))
bfs()

for i in range(n):
    if 0 in g[i]:
        print(-1)
        exit()

print(max(map(max,g))-1)