# 나이트의 이동
import sys
from collections import deque
input=sys.stdin.readline

dx=[-2,-2,-1,-1,1,1,2,2]
dy=[1,-1,2,-2,2,-2,1,-1]

def bfs(x,y):
    q=deque()
    q.append((x,y))

    while len(q):
        if g[tx][ty] != 0:
            return g[tx][ty]
        x,y=q.popleft()

        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]

            #범위 벗어남
            if nx<0 or ny<0 or nx>=size or ny>=size:
                continue
            if g[nx][ny]==0:
                g[nx][ny]=g[x][y]+1
                q.append((nx,ny))
    return g[tx][ty]

n=int(input())
for i in range(n):
    size=int(input())
    g=[[0]*size for i in range(size)]
    cx,cy=map(int,input().split())
    tx,ty=map(int,input().split())
    if cx==tx and cy==ty:
        print(0)
    else:
        print(bfs(cx,cy))