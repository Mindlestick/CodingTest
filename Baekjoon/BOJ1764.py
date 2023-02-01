# 듣보잡
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
a=set()
b=set()
for i in range(n):
    a.add(input().strip())
for i in range(m):
    b.add(input().strip())

c=list(a.intersection(b))
c.sort()
print(len(c))
print('\n'.join(c))