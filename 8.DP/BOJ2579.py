#계단 오르기
d=[0]*301
arr=[0]

def dp(x):
    if x==1:
        return arr[1]
    if x==2:
        return arr[1]+arr[2]
    if x==3:
        return max(arr[1]+arr[3], arr[2]+arr[3])

    if d[x]!=0:
        return d[x]

    d[x]=max(arr[x-1]+dp(x-3)+arr[x],dp(x-2)+arr[x])
    return d[x]

n=int(input())
for i in range(n):
    arr.append(int(input()))

print(dp(n))