# 피보나치 함수
import sys
input = sys.stdin.readline
d=[0]*41

def fibo(x):
    if x<=0:
        return 0
    if x==1:
        return 1

    if d[x]!=0:
        return d[x]
    d[x]=fibo(x-1)+fibo(x-2)
    return d[x]

t=int(input())
for i in range(t):
    n=int(input())
    if n==0:
        print('1 0')
    else:
        print(fibo(n-1),fibo(n))