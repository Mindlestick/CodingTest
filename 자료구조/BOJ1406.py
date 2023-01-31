#에디터
from collections import deque
import sys
l=deque(list(sys.stdin.readline().strip()))
r=deque()

n=int(sys.stdin.readline())
for i in range(n):
    t=sys.stdin.readline().strip()
    if t[0]=='P':
        l.append(t[2])
    if t[0]=='L' and len(l)!=0:
        tmp=l.pop()
        r.appendleft(tmp)
    if t[0]=='D'and len(r)!=0:
        tmp=r.popleft()
        l.append(tmp)
    if t[0]=='B'and len(l)!=0:
        l.pop()
s=l+r
sys.stdout.write(''.join(s))