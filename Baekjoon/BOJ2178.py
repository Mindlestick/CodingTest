#미로 탐색
import sys
from collections import deque
input=sys.stdin.readline

g=[]
n,m=map(int,input().split())
for i in range(n):
    g.append(list(map(int,input().strip())))

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    q=deque()
    q.append((x,y))

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            #범위 벗어남
            if nx >= n or ny >= m or nx < 0 or ny < 0:
                continue
            #벽
            if g[nx][ny]==0:
                continue
            #처음 방문하는 경우 기록
            if g[nx][ny]==1:
                g[nx][ny]=g[x][y]+1
                q.append((nx,ny))
    #오른쪽 아래 반환
    return g[n-1][m-1]

print(bfs(0,0))