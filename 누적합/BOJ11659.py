# 구간 합 구하기 4
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
q=list(map(int,input().split()))
pre=[0]
s=0
for i in q:
    s+=i
    pre.append(s)
for i in range(m):
    a,b = map(int,input().split())
    print(pre[b]-pre[a-1])