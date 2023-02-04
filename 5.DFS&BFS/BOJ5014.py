# 스타트링크

import sys
from collections import deque
input=sys.stdin.readline

def bfs():
    q.append(s)
    visit[s]=1

    while len(q):
        a=q.popleft()
        c=visit[a]+1

        if a==g:
            return visit[g]-1

        if a+u<=f and visit[a+u]==0 :
            q.append(a+u)
            visit[a+u] = c
        if a-d>0 and visit[a-d]==0:
            q.append(a-d)
            visit[a-d] = c
    return -1

f,s,g,u,d=map(int,input().split())
if d==0 and s>g:
    print('use the stairs')
    exit()

q=deque()
visit=[0]*(f+1)

answer=bfs()
if answer==-1:
    print('use the stairs')
else:
    print(answer)