#단지번호붙이기
import sys
from collections import deque
input=sys.stdin.readline

dx=[0,0,-1,1]
dy=[-1,1,0,0]

def bfs(g,x,y):
    q=deque()
    q.append((x,y))
    cnt=0

    while len(q):
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if g[nx][ny]==0:
                continue
            if g[nx][ny]==1:
                g[nx][ny]=0
                cnt+=1
                q.append((nx,ny))
    if cnt==0:
        h.append(1)
    else:
        h.append(cnt)

n=int(input())
g=[]
h=[]
for i in range(n):
    g.append(list(map(int,input().strip())))

answer=0
for i in range(n):
    for j in range(n):
        if g[i][j]==1:
            bfs(g,i,j)
            answer+=1
print(answer)
h.sort()
for i in h:
    print(i)