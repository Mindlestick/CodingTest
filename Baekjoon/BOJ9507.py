#Generations of Tribbles
d=[0]*68

def dp(x):
    if x<2:
        return 1
    if x==2:
        return 2
    if x==3:
        return 4
    if d[x]!=0:
        return d[x]
    d[x]=dp(x-1)+dp(x-2)+dp(x-3)+dp(x-4)
    return d[x]

t=int(input())
for i in range(t):
    a=int(input())
    print(dp(a))