n=6
k=[1,3,1,5,8,7]
d = [0]*n

d[0]=k[0]
d[1]=max(k[0],k[1])
for i in range(2,n):
    d[i] = max(k[i]+d[i-2],d[i-1])

print(d)
print(max(d))