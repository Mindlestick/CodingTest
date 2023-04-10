# 조합
n,m=map(int,input().split())
np=1
nf=1
for i in range(m):
    np*=n-i
    nf*=m-i
print(np//nf)