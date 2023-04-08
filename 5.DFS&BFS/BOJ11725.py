# 트리의 부모 찾기
import sys
sys.setrecursionlimit(10**7)
input=sys.stdin.readline

def dfs(curr,par):
    v[curr]=True
    p[curr]=par
    
    for c in g[curr]:
        if v[c]==False:
            dfs(c,curr)

n=int(input())
g=[[] for i in range(n+1)]
v=[False]*(n+1)
p=[0]*(n+1)

for i in range(n-1):
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)

dfs(1,0)
for i in range(2,n+1):
    print(p[i])