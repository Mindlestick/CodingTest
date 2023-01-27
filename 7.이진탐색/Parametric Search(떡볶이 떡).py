#Parametric Search : 최적화 문제를 '예' 혹은 '아니오'로 바꾸어 해결하는 기법
#떡볶이 떡 만들기
n,m=map(int,input().split())
arr=list(map(int,input().split()))

start=0
end=max(arr)

result=0
while(start<=end):
    sum =0
    mid = (start+end)//2
    for i in arr:
        if i > mid:
            sum+=i-mid
    if sum < m:
        end=mid-1
    else:
        result = mid
        start = mid+1

print(result)
"""
4 6
19 15 10 17
"""