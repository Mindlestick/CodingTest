#파도반 수열

d=[0]*101

def dp(x):
    if x<=3:
        return 1
    if d[x]!=0:
        return d[x]
    d[x]=dp(x-2)+dp(x-3)
    return d[x]
n=int(input())
for i in range(n):
    a=int(input())
    print(dp(a))