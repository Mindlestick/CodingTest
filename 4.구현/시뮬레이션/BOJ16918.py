# 봄버맨
def Bomb(g1,g2):
    blist=[]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    for i in range(len(g1)):
        for j in range(len(g1[0])):
            if g1[i][j]=='O':
                blist.append((i,j))

    for x,y in blist:
        g2[x][y] = '.'
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=len(g1) or ny>=len(g1[0]):
                continue
            g2[nx][ny]='.'


r,c,n = map(int,input().split())
m1 = [[]*c for i in range(r)]
m2 = [['O']*c for i in range(r)]
m3 = [['O']*c for i in range(r)]
for i in range(r):
    m1[i]=list(input())

if n==0 or n==1:
    for i in range(r):
        print(''.join(map(str,m1[i])))
elif n%2==0:
    for i in range(r):
        print(''.join(map(str,m2[i])))
elif n%4==1:
    Bomb(m1,m2)
    Bomb(m2,m3)
    for i in range(r):
        print(''.join(map(str,m3[i])))
elif n%4==3:
    Bomb(m1,m2)
    for i in range(r):
        print(''.join(map(str,m2[i])))

"""
<반례>
3 4 5
O...
..O.
O...

<answer>
OO..
OOO.
OO..
"""