# 연결 요소의 개수
import sys
from collections import deque
input=sys.stdin.readline

def bfs(start):
    q=deque()
    q.append(start)
    visit[start]=True

    while len(q):
        curr=q.popleft()

        for i in g[curr]:
            if visit[i] == False:
                q.append(i)
                visit[i]=True

n,m=map(int,input().split())
g=[[] for i in range(n+1)]
for i in range(m):
    u,v=map(int,input().split())
    g[u].append(v)
    g[v].append(u)

visit=[False]*(n+1)
visit[0]=True

answer=0
for i in range(1,n+1):
    if visit[i]==False:
        answer+=1
        bfs(i)
print(answer)