from collections import deque

# BFS(넓이우선)
def bfs(g,start,visit):
    q = deque([start])

    #현재 노드 방문처리
    visit[start] = True

    #큐 빌때까지 반복
    while len(q):
        #큐에서 원소 뽑기
        v=q.popleft()
        print(v, end=' ')

        #아직 방문하지 않은 인접 원소들 큐에 삽입
        for i in g[v]:
            if visit[i]==False:
                q.append(i)
                visit[i]=True

g=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visit=[False]*9

bfs(g,1,visit)
