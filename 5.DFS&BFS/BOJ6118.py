# 숨바꼭질
from collections import deque
def bfs():
    q=deque()
    q.append(1)
    visited[1]=True

    while len(q):
        curr=q.popleft()

        for next in g[curr]:
            if visited[next]==False:
                q.append(next)
                dist[next]=dist[curr]+1
                visited[next]=True

n,m=map(int,input().split())
g=[[] for i in range(n+1)]
visited=[False]*(n+1)
dist=[0]*(n+1)
for i in range(m):
    a,b=map(int,input().split())
    g[a].append(b)
    g[b].append(a)

bfs()
m=max(dist)
print(dist.index(m),m,dist.count(m))