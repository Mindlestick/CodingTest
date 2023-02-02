# 동전 0
import sys
input=sys.stdin.readline

n,k=map(int,input().split())
coin=[]
for i in range(n):
    coin.append(int(input()))
coin.reverse()

answer=0
for i in coin:
    if i <=k:
        answer+=k//i
        k=k%i
print(answer)
