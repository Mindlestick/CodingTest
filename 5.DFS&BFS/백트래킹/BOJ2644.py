# 촌수계산
answer=[]
def dfs(curr):
    global answer
    # 목표한 사람과 현재 탐색중인 번호가 같으면 촌수 출력 후 정지
    if curr == b:
        print(len(answer))
        exit(0)

    visited[curr]=True
    for next in g[curr]:
        if visited[next] == False:
            visited[next] = True
            answer.append(next)
            dfs(next)
            answer.pop()
    return -1

n=int(input())
a,b=map(int,input().split())
m=int(input())
g=[[] for i in range(n+1)]
visited=[False]*(n+1)

for i in range(m):
    x,y=map(int,input().split())
    g[x].append(y)
    g[y].append(x)
print(dfs(a))

