#숫자 카드
n=int(input())
nlist=set(map(int,input().split()))

m=int(input())
mlist=list(map(int,input().split()))

for i in mlist:
    if i in nlist:
        print(1,end=' ')
    else:
        print(0,end=' ')