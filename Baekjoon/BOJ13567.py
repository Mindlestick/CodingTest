# 로봇
m,n=map(int,input().split())
g=[[]*m for i in range(m)]
x,y=0,0
dx=[1,0,-1,0]
dy=[0,1,0,-1]
d=0
move=0
answer=0
for i in range(n):
    TM,dir = map(str,input().split())
    if TM=='TURN':
        if dir=='0':
            d+=1
        elif dir=='1':
            d-=1
    elif TM=='MOVE':
        move=int(dir)
        x=x+dx[d%4]*move
        y=y+dy[d%4]*move

    if x<0 or y<0 or x>=m or y>=m:
        print(-1)
        exit(0)

print(x,y)


