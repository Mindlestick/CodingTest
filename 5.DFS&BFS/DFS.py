# DFS(재귀)
def dfs(g,v,visit):
    visit[v]=True
    print(v,end=' ')
    for i in g[v]:
        if visit[i]==False:
            dfs(g,i,visit)

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
dfs(g,1,visit)
