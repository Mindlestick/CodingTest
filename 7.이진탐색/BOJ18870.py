# 좌표 압축
import sys
from bisect import bisect_right
input = sys.stdin.readline

def find(arr,target):
    right_id=bisect_right(arr,target)
    return right_id-1

n=int(input())
x=list(map(int,input().split()))
s=sorted(set(x))

for i in x:
    print(find(s,i),end=' ')
