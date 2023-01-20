#연속합
n=int(input())
a=list(map(int,input().split()))
d=[]
d.append(a[0])

for i in range(n-1):
    d.append(max(d[i]+a[i+1],a[i+1]))
print(max(d))