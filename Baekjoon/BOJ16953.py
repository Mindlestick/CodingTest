# A → B
import sys
from collections import deque
input=sys.stdin.readline

def bfs(a,b):
    cnt=1
    q.append((a,cnt))

    while len(q):
        value,cnt=q.popleft()
        if value==b:
            return cnt
        if value > b:
            continue
        cnt+=1
        s = str(value) + '1'
        q.append((value * 2,cnt))
        q.append((int(s), cnt))
    return -1

a,b=map(int,input().split())
q=deque()
answer=bfs(a,b)
print(answer)