#안테나
n=int(input())
arr=list(map(int,input().split()))
arr.sort()
print(arr[(n-1)//2])