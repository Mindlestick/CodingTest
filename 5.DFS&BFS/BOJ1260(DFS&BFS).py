#DFS와 BFS

from collections import deque

def dfs(curr):
    #방문
    visit[curr]=True
    print(curr,end=' ')
    
    #방문 안한 노드 처리
    for next in g[curr]:
        if visit[next]==False:
            dfs(next)

def bfs():
    #방문
    q=deque()
    q.append(v)
    visit[v]=True
    
    #큐 빌 때까지
    while len(q):
        curr=q.popleft()
        print(curr,end=' ')

        #방문 안한 인접노드 처리
        for next in g[curr]:
            if visit[next]==False:
	   q.append(next) #큐에 넣고
                visit[next]=True #방문
                

n,m,v=map(int,input().split())
g=[]
g = [[] for i in range(n+1)]

for i in range(m):
    a = list(map(int,input().split()))
    #그래프 만들기
    g[a[0]].append(a[1])
    g[a[1]].append(a[0])

for i in range(len(g)):
    g[i].sort()

visit=[False]*10001
dfs(v)
print()
visit=[False]*10001
bfs()