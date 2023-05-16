# 섬의 개수
import sys
from collections import deque
input=sys.stdin.readline
dx=[0,0,1,-1,-1,1,-1,1]
dy=[1,-1,0,0,-1,1,1,-1]

def bfs(x,y):
    q=deque()
    q.append((x,y))
    g[x][y]=0

    while len(q):
        x,y=q.popleft()
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or ny<0 or nx>=h or ny>=w:
                continue
            if g[nx][ny]==1:
                g[nx][ny]=0
                q.append((nx,ny))

while 1:
    w,h=map(int,input().split())
    if w==0 and h==0:
        break
    g=[[]*w for i in range(h)]
    cnt=0
    for i in range(h):
        g[i]=list(map(int,input().split()))
    for i in range(h):
        for j in range(w):
            if g[i][j]:
                bfs(i,j)
                cnt+=1
    print(cnt)