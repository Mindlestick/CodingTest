# 알고리즘 수업 - 깊이 우선 탐색 2
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

def dfs(s):
    global cnt
    visited[s]=True
    sequence[s]=cnt
    #print(s,sequence)

    g[s].sort(reverse=True)
    for n in g[s]:
        if visited[n]==False:
            cnt+=1
            dfs(n)

n,m,r=map(int,input().split())
g=[[] for i in range(n+1)]
visited=[False]*(n+1)
sequence=[0]*(n+1)
cnt=1

for i in range(m):
    a,b=map(int,input().split())
    g[a].append(b)
    g[b].append(a)

dfs(r)
for i in range(1,n+1):
    print(sequence[i])