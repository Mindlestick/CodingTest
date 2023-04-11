# 정수 삼각형

n=int(input())
nlist=[[] for i in range(n)]

for i in range(n):
    nlist[i]= list(map(int,input().split()))
    

for i in range(1,n):
    for j in range(i+1):
        if j==0:
            nlist[i][j]+=nlist[i-1][j]
        elif j==i:
            nlist[i][j]+=nlist[i-1][j-1]
        else:
            nlist[i][j] = max(nlist[i-1][j] + nlist[i][j],nlist[i-1][j-1] + nlist[i][j])

print(max(nlist[-1]))