# 먹을 것인가 먹힐 것인가
import sys
input=sys.stdin.readline
t=int(input())
for i in range(t):
    answer=0
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a.sort()
    b.sort()

    p=0
    for j in range(len(a)):
        while 1:
            #print(j,p,answer)
            if p==m or a[j]<=b[p]:
                answer+=p
                break
            else:
                p+=1

    print(answer)