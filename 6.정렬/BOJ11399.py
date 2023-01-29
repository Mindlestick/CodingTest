#ATM
import sys
input = sys.stdin.readline

n=int(input())
a=list(map(int,input().split()))
a.sort()
s=0
result=[]
for i in a:
    s+=i
    result.append(s)
sys.stdout.write(str(sum(result)))