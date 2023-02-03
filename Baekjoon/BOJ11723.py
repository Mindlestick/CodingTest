#집합
import sys
input=sys.stdin.readline
m = int(input())
s = set()
for i in range(m):
    a = list(input().strip().split())
    if a[0] == 'add':
        s.add(int(a[1]))
    if a[0] == 'remove' and len(s)!=0:
        s.remove(int(a[1]))
    if a[0] == 'check':
        if int(a[1]) in s:
            print(1)
        else:
            print(0)
    if a[0] == 'toggle':
        if int(a[1]) in s:
            s.remove(int(a[1]))
        else:
            s.add(int(a[1]))
    if a[0] == 'all':
        s = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    if a[0] == 'empty':
        s = set()
