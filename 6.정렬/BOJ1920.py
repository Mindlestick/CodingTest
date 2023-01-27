#수 찾기
import sys
input = sys.stdin.readline

n=int(input())
na=set(map(int,input().split()))

m=int(input())
ma=list(map(int,input().split()))

for i in ma:
    if i in na:
        sys.stdout.write('1\n')
    else:
        sys.stdout.write('0\n')