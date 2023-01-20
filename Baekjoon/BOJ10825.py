#국영수
n=int(input())
arr=[]
for i in range(n):
    tmp=input().split()
    arr.append((tmp[0],int(tmp[1]),int(tmp[2]),int(tmp[3])))
arr=sorted(arr,key=lambda x: (-x[1],x[2],-x[3],x[0]))
for i in arr:
    print(i[0])