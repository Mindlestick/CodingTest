# 수들의 합 2
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
nlist=list(map(int,input().split()))

start,end=0,0
answer=0
s=0
while start<n and end<=n:
    if s==m:
        s-=nlist[start]
        answer+=1
        start+=1
    if start>=n:
        break

    if end>=n:
        s-=nlist[start]
        start+=1
    if s<m and end<n:
        s += nlist[end]
        end+=1
    if s>m:
        s-=nlist[start]
        start+=1
    #print(start,end,s)
print(answer)