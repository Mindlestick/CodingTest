n,m=map(int,input().split())

arr=[]
for i in range(n):
    arr.append(int(input()))

d=[10001]*(m+1)
d[0]=0
for i in range(n):
    for j in range(arr[i], m+1):
        d[j]=min(d[j],d[j-arr[i]]+1)

if d[m]!=10001:
    print(d[m])
else:
    print(-1)
#print(d)

"""
3 7
2
3
5
"""