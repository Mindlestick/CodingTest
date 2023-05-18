# 침투
from collections import deque
dx=[0,0,-1,1]
dy=[1,-1,0,0]
def bfs(x,y):
    q=deque()
    q.append((x,y))
    g[x][y]=2

    while len(q):
        x,y = q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or ny<0 or nx>=m or ny>=n:
                continue
            if g[nx][ny]==0:
                g[nx][ny]=2
                q.append((nx,ny))

m,n=map(int,input().split())
g=[[]*n for i in range(m)]
for i in range(m):
    g[i]=list(map(int,input()))

for i in range(n):
    if g[0][i]==0:
        bfs(0,i)

if 2 in g[-1]:
    print('YES')
else:
    print('NO')