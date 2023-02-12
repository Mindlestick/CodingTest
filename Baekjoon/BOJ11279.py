# 최대 힙
from queue import PriorityQueue
import sys
input=sys.stdin.readline
q=PriorityQueue()

n=int(input())
qsize=0
for i in range(n):
    x=int(input())
    if x==0:
        if qsize==0:
            print(0)
        else:
            print(-q.get())
            qsize-=1
    else:
        q.put(-x)
        qsize+=1