from collections import deque
def bfs(num):
    q=deque()
    visited = [-1] * (n + 1)
    q.append(num)
    visited[num] = 0
    while len(q):
        curr=q.popleft()
        for next in g[curr]:
            if visited[next]==-1:
                visited[next]=visited[curr]+1
                q.append(next)
    # print(visited)
    score[num]=max(visited)
    # print(score)

n=int(input())
g=[[] for i in range(n+1)]

score=[0]*(n+1)
while 1:
    a,b=map(int,input().split())
    if a==-1 and b==-1:
        break
    g[a].append(b)
    g[b].append(a)
# print(g)
for i in range(n+1):
    bfs(i)
m=min(score[1:])
print(m,score.count(m))
for i in range(n+1):
    if score[i]==m:
        print(i,end=' ')
