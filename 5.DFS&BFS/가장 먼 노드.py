from collections import deque
def solution(n, edge):
    def bfs(curr):
        q.append(curr)
        visited[curr]=1

        while(len(q)):
            curr=q.popleft()
            print(curr)
            
            for n in g[curr]:
                if visited[n]==0:
                    q.append(n)
                    visited[n]=visited[curr]+1
        print(visited)
            
    answer = 0
    q=deque()
    g=[[] for i in range(n+1)]
    visited=[0]*(n+1)
    for i in edge:
        a,b =i[0],i[1]
        g[a].append(b)
        g[b].append(a)
    bfs(1)

    answer=visited.count(max(visited))
    return answer