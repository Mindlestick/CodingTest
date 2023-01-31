#키로거
import sys
input=sys.stdin.readline

n=int(input())

for i in range(n):
    L = []
    R = []
    c=list(input().strip())
    for j in c:
        if j=='-':
            if len(L)==0:
                continue
            L.pop()
        elif j=='<':
            if len(L)==0:
                continue
            R.append(L.pop())
        elif j=='>':
            if len(R)==0:
                continue
            L.append(R.pop())
        else:
            L.append(j)
    R.reverse()
    print(''.join(L+R))