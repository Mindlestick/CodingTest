def dfs(x,y):
    #범위 벗어남
    if x<0 or x>=n or y<0 or y>=m:
        return False

    #현재 노드가 방문 전
    if g[x][y] ==0:
        #방문처리
        g[x][y]=1

        #상하좌우 재귀호출(연결된 노드 방문처리)
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

n,m = map(int, input().split())
g=[]
for i in range(n):
    g.append(list(map(int,input())))

answer=0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            answer+=1
print(answer)

"""
4 5
00110
00011
11111
00000
"""