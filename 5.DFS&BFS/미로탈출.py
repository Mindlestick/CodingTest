from collections import deque

n,m=map(int,input().split())
g=[]
for i in range(n):
    g.append(list(map(int,input())))

#상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    q=deque()
    q.append((x,y))

    #큐 빌 때까지 반복
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            #범위 벗어나면 무시
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            #벽 무시
            if g[nx][ny] == 0:
                continue

            #처음 방문하는 경우에만 최단거리 기록
            if g[nx][ny] ==1:
                g[nx][ny]=g[x][y]+1
                q.append((nx,ny))
    #가장 오른쪽 아래 반환
    return g[n-1][m-1]

print(bfs(0,0))

"""
3 4
1100
1110
0011
"""