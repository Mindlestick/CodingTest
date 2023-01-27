#부품 찾기
n=int(input())
na=set(map(int,input().split()))

m=int(input())
ma=list(map(int,input().split()))

for i in ma:
    if i in na:
        print('yes',end=' ')
    else:
        print('no',end=' ')

"""
5
8 3 7 9 2
3
5 7 9        
"""