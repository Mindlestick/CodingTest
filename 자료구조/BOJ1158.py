# 요세푸스 문제
import sys
input = sys.stdin.readline
n,k=map(int,input().split())

s=[x for x in range(1,n+1)]
c=0
answer=[]
while(len(s)):
    c=(c+k-1)%len(s)
    #print(s[c])
    answer.append(s[c])
    s = s[:c] + s[c+1:]

print('<{}>'.format(', '.join(map(str,answer))))