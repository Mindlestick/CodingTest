n=int(input())
arr=[]
for i in range(n):
    d=input().split()
    arr.append((d[0],int(d[1])))

arr=sorted(arr,key=lambda i: i[1])

for i in arr:
    print(i[0], end=' ')