# 조커 찾기
# PyPy3로 제출하면 시간초과 안남
import sys
from collections import deque
input=sys.stdin.readline

card=[1]
card+=[0]*26
n=int(input())
for i in range(n):
    nq=deque()
    left=deque(card[:13])
    right=deque(card[13:27])

    a=list(map(int,input().split()))
    for j in range(len(a)):
        if j%2==0:
            nq+=list(right)[:a[j]]
            for k in range(a[j]):
                right.popleft()
        else:
            nq+=list(left)[:a[j]]
            for k in range(a[j]):
                left.popleft()
    card=list(nq)
print(nq.index(1)+1)