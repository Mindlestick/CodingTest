# 맥주 마시면서 걸어가기
from collections import deque
def bfs(s):
    q=deque()
    q.append(g[s]) # 시작점
    visited[s]=True

    while len(q):
        x,y=q.popleft()
        # 목적지와의 거리가 1000 이하면 결과는 happy
        if abs(x-g[-1][0]) + abs(y-g[-1][1])<=1000:
            print('happy')
            return

        # start 노드와 end 노드를 제외하고 순회
        for i in range(1,n+1):
            # 방문하지 않은 노드만
            if visited[i]==False:
                nx,ny=g[i]
                # 현재 노드와 거리가 1000 이하면 큐에 방문 처리하고 큐에 넣기
                if abs(x-nx)+abs(y-ny)<=1000:
                    visited[i]=True
                    q.append(g[i])
    print('sad')

t=int(input())
for _ in range(t):
    n=int(input())
    g=[]
    visited=[False]*(n+2)
    for i in range(n+2):
        g.append(list(map(int,input().split())))
    bfs(0)