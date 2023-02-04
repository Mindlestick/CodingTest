# 노드사이의 거리
import sys
from collections import deque
input=sys.stdin.readline

def bfs(sn,en):
    q = deque()
    q.append((sn,0))
    visit = [False] * (n + 1)
    visit[sn]=True

    while len(q):
        curr,d = q.popleft()
        if curr==en:
            return d

        for i,j in g[curr]:
            if visit[i]==False:
                visit[i]=True
                q.append((i,d+j))


n,m=map(int,input().split())
g=[[] for i in range(n+1)]

for i in range(n-1):
    s,e,l=map(int,input().split())
    g[s].append((e,l))
    g[e].append((s,l))

for i in range(m):
    sn,en=map(int,input().split())
    print(bfs(sn,en))