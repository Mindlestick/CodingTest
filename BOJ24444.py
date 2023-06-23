from collections import deque
import sys
input=sys.stdin.readline

def bfs(curr):
    o=1
    q = deque()
    visited[curr]=True
    q.append(curr)
    order[curr]=o

    while len(q):
        u=q.popleft()
        for e in g[u]:
            if visited[e]==False:
                q.append(e)
                visited[e]=True
                o += 1
                order[e] = o


n,m,r=map(int,input().split())
g=[[] for i in range(n+1)]
visited=[False]*(n+1)
order=[0]*(n+1)
for i in range(m):
    a,b=map(int,input().split())
    g[a].append(b)
    g[b].append(a)
for i in range(n):
    g[i].sort()
bfs(r)
print('\n'.join(map(str,order[1:])))

