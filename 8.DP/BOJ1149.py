# RGB거리
import sys
input = sys.stdin.readline

n=int(input())
r,g,b=[0]*(n+1),[0]*(n+1),[0]*(n+1)

d=[[] for i in range(n)]
for i in range(n):
    d[i]=list(map(int,input().split()))

r[0],g[0],b[0] = d[0][0],d[0][1],d[0][2]
for x in range(1,n):
    r[x]=min(g[x-1],b[x-1])+d[x][0]
    g[x]=min(r[x-1],b[x-1])+d[x][1]
    b[x]=min(g[x-1],r[x-1])+d[x][2]
print(min(r[n-1],g[n-1],b[n-1]))
