import sys
sys.setrecursionlimit(10**7)

d=[0]*(100000+1)
def fibo(x):
    if x==1 or x==2:
        return 1
    if d[x]!=0:
        return d[x]
    d[x] = fibo(x-1)+fibo(x-2)
    return d[x]
        
def solution(n):
    answer = fibo(n)
    return answer%1234567