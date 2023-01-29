#어두운 굴다리
import sys
input=sys.stdin.readline

n=int(input())
m=int(input())
x=list(map(int,input().split()))

d=[0]*(n+1)
h=max(x[0],n-x[-1])
for i in range(1,len(x)):
    h=max(h,(x[i]-x[i-1]+1)//2)
print(h)