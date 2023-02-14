# 큐2
import sys
from collections import deque
input=sys.stdin.readline
q=deque()

n=int(input())
for i in range(n):
    c = input().split()
    if c[0]=='push':
        a=int(c[1])
        q.append(a)
    elif c[0]=='front':
        if len(q)==0:
            print(-1)
        else:
            print(q[0])
    elif c[0]=='back':
        if len(q)==0:
            print(-1)
        else:
            print(q[-1])
    elif c[0]=='size':
        print(len(q))
    elif c[0]=='empty':
        if len(q):
            print(0)
        else:
            print(1)
    elif c[0]=='pop':
        if len(q)==0:
            print(-1)
        else:
            print(q.popleft())