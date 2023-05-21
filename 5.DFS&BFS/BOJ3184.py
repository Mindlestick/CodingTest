# 양
from collections import deque
dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(sx,sy):
    q=deque()
    q.append((sx,sy))
    s,w=0,0
    if g[sx][sy]=='o':
        s += 1
    elif g[sx][sy] == 'v':
        w += 1
    g[sx][sy]='#'

    while len(q):
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or ny<0 or nx>=r or ny>=c or g[nx][ny]=='#':
                continue
            if g[nx][ny]=='o':
                s+=1
            elif g[nx][ny]=='v':
                w+=1
            g[nx][ny]='#'
            q.append((nx,ny))
    if s>w:
        return [s,0]
    else:
        return [0,w]

r,c=map(int,input().split())
g=[[]*c for i in range(r)]
answer=[0,0]
for i in range(r):
    g[i]=list(input())

for i in range(r):
    for j in range(c):
        if g[i][j]!='#':
            tmp=bfs(i,j)
            answer[0]+=tmp[0]
            answer[1]+=tmp[1]
print(' '.join(map(str,answer)))
