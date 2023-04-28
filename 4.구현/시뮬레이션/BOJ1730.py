# 판화
n = int(input())
s = input()

g=[['.']*n for i in range(n)]
x,y=0,0

p=[[False]*(n+1) for i in range(n+1)]
h=[[False]*(n+1) for i in range(n+1)]

def isVal(x,y):
    if x<0 or x >=n or y<0 or y >= n:
        return False
    return True

for i in range(len(s)):
    if s[i]=='U':
        if isVal(x-1,y)==False:
            continue
        p[x][y]=True
        p[x-1][y]=True
        x-=1
    elif s[i]=='D':
        if isVal(x+1,y)==False:
            continue
        p[x][y]=True
        p[x+1][y]=True
        x+=1
    elif s[i]=='L':
        if isVal(x,y-1)==False:
            continue
        h[x][y]=True
        h[x][y-1]=True
        y-=1
    elif s[i]=='R':
        if isVal(x,y+1)==False:
            continue
        h[x][y]=True
        h[x][y+1]=True 
        y+=1
    
for i in range(n):
    for j in range(n):
        if p[i][j] and h[i][j]:
            print("+",end='')
        elif p[i][j]:
            print("|",end='')
        elif h[i][j]:
            print('-',end='')
        else:
            print('.',end='')
    print()