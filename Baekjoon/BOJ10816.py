#숫자 카드 2
import sys
from collections import Counter
input=sys.stdin.readline
n=int(input())
nlist = list(map(int,input().split()))
m=int(input())
mlist = list(map(int,input().split()))

C=Counter(nlist)
for i in mlist:
    if i in C:
        print(C[i],end=' ')
    else:
        print('0',end=' ')