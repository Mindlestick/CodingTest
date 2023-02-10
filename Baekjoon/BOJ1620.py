# 나는야 포켓몬 마스터 이다솜
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
book={}
num={}

for i in range(n):
    name=input().strip()
    book[name]=i+1
    num[i+1]=name
for i in range(m):
    a=input().strip()
    if a[0]>='A' and a[0]<='Z':
        print(book.get(a))
    else:
        print(num.get(int(a)))