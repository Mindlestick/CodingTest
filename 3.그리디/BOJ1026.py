# 보물
import sys
input=sys.stdin.readline

n=int(input())
a=[]
b=[]

a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
a.sort()
b.sort(reverse=True)
for i in range(n):
    c.append(a[i]*b[i])

print(sum(c))