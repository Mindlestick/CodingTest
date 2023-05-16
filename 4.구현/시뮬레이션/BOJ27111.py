# 출입 기록
import sys
input=sys.stdin.readline
n=int(input())
a=[False] * (200000+1)
answer=0
for i in range(n):
    ai,bi = map(int,input().split())
    if bi==1:
        if a[ai]:
            answer+=1
        else:
            a[ai]=True
    elif bi==0:
        if a[ai]==False:
            answer+=1
        else:
            a[ai]=False
answer+=a.count(True)
print(answer)
