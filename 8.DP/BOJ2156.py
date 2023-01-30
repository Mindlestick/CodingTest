#포도주
import sys
input=sys.stdin.readline

n=int(input())
k=[0]*10000
for i in range(n):
    k[i]=int(input())

d=[0]*10000
d[0]=k[0]
d[1]=k[0]+k[1]
d[2]=max(k[2]+k[0],k[2]+k[1],d[1])
for i in range(3,n):
    d[i]=max(k[i]+d[i-2],k[i]+k[i-1]+d[i-3],d[i-1])
print(max(d))