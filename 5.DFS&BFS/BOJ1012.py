# 유기농 배추

# 재귀 limit 설정
import sys
sys.setrecursionlimit(10000)

t=int(input())
for i in range(t):
    m, n, k = map(int, input().split())
    g = [[0] * m for i in range(n)]

    for i in range(k):
        x, y = map(int, input().split())
        g[y][x] = 1

    answer = 0
    def dfs(x, y):
        # 범위 벗어남
        if x < 0 or y < 0 or x >= n or y >= m:
            return 0
        # 1방문
        if g[x][y] == 1:
            g[x][y] = 0 #방문처리
            #상하좌우 탐색
            dfs(x, y - 1)
            dfs(x, y + 1)
            dfs(x - 1, y)
            dfs(x + 1, y)
            return 1
        return 0

    for i in range(n):
        for j in range(m):
            if dfs(i, j) == 1:
                answer += 1
    print(answer)