# 기타줄
import sys
input=sys.stdin.readline
one=[]
pack=[]
case=[]

n,m=map(int,input().split())
for i in range(m):
    p,o = map(int,input().split())
    pack.append(p)
    one.append(o)
pm=min(pack)
om=min(one)
if n%6==0:
    case.append((n//6)*pm)
    case.append(n*om)
else:
    case.append(((n//6)+1)*pm)
    case.append(n*om)
    case.append((n//6)*pm+(n%6)*om)
print(min(case))