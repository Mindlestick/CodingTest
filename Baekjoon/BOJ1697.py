#숨바꼭질
import sys
from queue import PriorityQueue
input=sys.stdin.readline
answer=[]

t=int(input())
for i in range(t):
    q = PriorityQueue()
    p = PriorityQueue()

    k = int(input())
    for j in range(k):
        a=input().split()
        if a[0]=='I':
            if q.qsize()==0 and p.qsize()==0:
                q.put(int(a[1]))
                continue

            qitem=q.get()
            if int(a[1]) < qitem:
                q.put(int(a[1]))
                p.put(-qitem)
            else:
                q.put(qitem)
                p.put(-int(a[1]))

        elif a[0]=='D':
            if q.qsize()==0 and p.qsize()==0:
                continue
            if a[1]=='-1':
                if q.qsize()==0:
                    p.get()
                else:
                    q.get()
            elif a[1]=='1':
                if p.qsize()==0:
                    q.get()
                else:
                    p.get()

        if p.qsize() == 2 and q.qsize() == 0:
            maxitem = -p.get()
            minitem = -p.get()
            q.put(minitem)
            p.put(-maxitem)
        if p.qsize() == 0 and q.qsize() == 2:
            minitem = q.get()
            maxitem = q.get()
            p.put(-maxitem)
            q.put(minitem)

    if q.qsize()==0 and p.qsize()==0:
        print('EMPTY')
    else:
        while(q.qsize()):
            answer.append(q.get())
        while(p.qsize()):
            answer.append(-p.get())
        print(max(answer), min(answer))
