#바이러스

n=int(input())
v=int(input())
g=[[] for i in range(n+1)]
visit=[0]*(n+1)

for i in range(v):
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)

def dfs(v):
    visit[v]=1
    for i in g[v]:
        if visit[i]==0:
            dfs(i)

dfs(1)
#print(visit)
print(sum(visit)-1)


"""
7
6
1 2
2 3
1 5
5 2
5 6
4 7
"""