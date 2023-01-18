#1, 2, 3 더하기

d = [0] * 12
d[1]=1
d[2]=2
d[3]=4
def dp(x):
    if d[x]!=0:
        return d[x]

    for i in range(4,x+1):
        d[i]=dp(i-1)+dp(i-2)+dp(i-3)
    return d[i]

T=int(input())
for i in range(T):
    n = int(input())
    dp(n)
    print(d[n])

