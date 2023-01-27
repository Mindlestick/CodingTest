#나무 자르기
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=list(map(int,input().split()))

start=0
end=max(arr)
result=0

while start <= end:
    mid=(start+end)//2
    sum=0
    for i in arr:
        if i>mid:
            sum+=i-mid

    if sum < m:
        end=mid-1
    else:
        result=mid
        start=mid+1

print(result)
"""
4 6
19 15 10 17
"""