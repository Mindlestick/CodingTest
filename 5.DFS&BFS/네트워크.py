def dfs(g,visit,curr):
    visit[curr]=True
    
    for next in g[curr]:
        if visit[next]==False:
            dfs(g,visit,next)            
         
def solution(n, computers):
    answer = 0
    g=[[] for i in range(n+1)]
    visit=[False]*(n+1)

    for i in range(len(computers)):
        for j in range(len(computers[0])):
            if computers[i][j] and i!=j:
                g[i+1].append(j+1)
                
    for i in range(1,n+1):
        if visit[i]==False:
            dfs(g,visit,i)
            answer+=1
            
    return answer