# 회전하는 큐
import sys
from collections import deque
input = sys.stdin.readline

def left(dq):
    tmp=dq.popleft()
    dq.append(tmp)

def right(dq):
    tmp=dq.pop()
    dq.appendleft(tmp)

n,m = map(int,input().split())
q=deque(i for i in range(1,n+1))
target=deque(map(int,input().split()))

cnt=0
lc=0
rc=0
while(len(q)):
    if len(target)==0:
        break
    if q[0]==target[0]:
        q.popleft()
        target.popleft()
    else:
        for i in range(len(q)):
            if q[i]==target[0]:
                lc=i
                rc=len(q)-i
                if lc<=rc:
                    for j in range(lc):
                        left(q)
                    cnt+=lc
                else:
                    for j in range(rc):
                        right(q)
                    cnt+=rc
                q.popleft()
                target.popleft()
                break
print(cnt)