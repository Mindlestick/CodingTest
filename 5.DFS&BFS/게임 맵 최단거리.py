#게임 맵 최단거리

from collections import deque
def bfs(g,x,y):
    #가로, 세로 길이 구해놓기
    n=len(g)
    m=len(g[0])

    #상하좌우
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    q=deque()
    q.append((x,y))
    
    #큐 빌 때까지 반복
    while len(q):
        x,y = q.popleft()
        #상하좌우 탐색
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            #범위 벗어남
            if nx < 0 or ny < 0 or nx>=n or ny>=m:
                continue
            #벽(0)인 경우
            if g[nx][ny]==0:
                continue
            #길(1)인 경우 1 더해서 저장
            if g[nx][ny]==1:
                g[nx][ny]=g[x][y]+1
                q.append((nx,ny))
    #print(g)
    if g[-1][-1] ==1:
        return -1
    else:
        return g[-1][-1]
            

def solution(maps):
    answer = bfs(maps,0,0)
    return answer