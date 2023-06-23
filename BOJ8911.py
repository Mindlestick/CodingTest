dx=[0,1,0,-1]
dy=[-1,0,1,0]
t=int(input())
for i in range(t):
    inputt=list(input())
    x, y, d = 0, 0, 0
    mx,my=0,0
    Mx,My=0,0
    plus=False
    for s in inputt:
        if s=='F':
            x+=dx[d%4]
            y+=dy[d%4]
        elif s=='B':
            x-=dx[d%4]
            y-=dy[d%4]
        elif s=='L':
            d-=1
        elif s=='R':
            d+=1
        # print(x,y)
        if Mx<x:
            Mx=x
        if My<y:
            My=y
        if mx>x:
            mx=x
        if my>y:
            my=y
    print((Mx-mx)*(My-my))