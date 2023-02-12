# 이중 우선순위 큐
import sys
from queue import PriorityQueue
input=sys.stdin.readline

t=int(input())
for i in range(t):
    p1 = PriorityQueue()
    p2 = PriorityQueue()
    d=dict()
    v=0

    q=int(input())
    for j in range(q):
        a=input().split()
        a[1]=int(a[1])
        if a[0]=='I':
            if a[1] in d:
                d[a[1]]=d[a[1]]+1
            else:
                d[a[1]]=1
            p1.put(a[1])
            p2.put(-a[1])

        elif a[0] == 'D':
            if a[1] == -1:
                while p1.qsize():
                    v = p1.get()
                    if d[v]>0:
                        d[v] = d[v] - 1
                        break
            elif a[1]==1:
                while p2.qsize():
                    v=-p2.get()
                    if d[v]>0:
                        d[v] = d[v] - 1
                        break

    flag=True
    n1,n2=0,0

    while p1.qsize():
        n1=p1.get()
        if d[n1]!=0:
            flag=False
            break
    while p2.qsize():
        n2=-p2.get()
        if d[n2]!=0:
            break

    if flag:
        print('EMPTY')
    else:
        print(n2, n1)
