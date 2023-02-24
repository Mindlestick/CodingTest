def dfs(g, curr, visit):
    visit[curr]=True
    
    for next in g[curr]:
        if visit[next]==False:
            dfs(g,next,visit)

def solution(n, wires):
    g=[[] for i in range(n+1)]
    visit=[False]*(n+1)
    for i,j in wires:
        g[i].append(j)
        g[j].append(i)

    diff=[]
    for i,j in wires:
        visit=[False]*(n+1)
        g[i].remove(j)
        g[j].remove(i)

        dfs(g,i,visit)
        d=visit.count(True)
        diff.append(abs((n-d)-d))

        g[j].append(i)
        g[i].append(j) 
        
    answer = min(diff)
    return answer