# 베스트셀러
import sys
input=sys.stdin.readline

n=int(input())
book=dict()
for i in range(n):
    name=input().strip()
    if name in book:
        book[name]+=1
    else:
        book[name]=1
s_book=sorted(book.items(), key= lambda x : (-x[1],x[0]))
print(s_book[0][0])
