# 미로 만들기
from collections import deque
n=int(input())
nlist=list(input())
# 방향 설정
dx=[0,-1,0,1]
dy=[1,0,-1,0]
# 초기 사이즈 설정
xsize, ysize = 1,1
d,x,y=0,0,0
# 그래프 초기화
g=deque([deque('.')])

for i in nlist:
    # 오른쪽으로 회전하는 경우
    if i=='R':
        d+=1
    # 왼쪽으로 회전하는 경우
    elif i =='L':
        d-=1
    # 전진하는 경우
    elif i=='F':
        # 설정한 방향으로 앞으로 가기
        x+=dx[d%4]
        y+=dy[d%4]
        # print(x,y,xsize,ysize)
        # 오른쪽으로 나아가는 경우
        if x >= xsize:
            xsize += 1
            for i in range(ysize):
                g[i].append('#')
        # 왼쪽으로 나아가는 경우
        elif x <= -1:
            xsize+=1
            for i in range(ysize):
                g[i].appendleft('#')
            x=0
        # 아래쪽으로 나아가는 경우
        elif y >= ysize:
            ysize += 1
            g.append(deque('#'*xsize))
        # 위쪽으로 나아가는 경우
        elif y <= -1:
            ysize+=1
            g.appendleft(deque('#'*xsize))
            y=0
        # 경로 표시하기
        g[y][x]='.'
        # '#'으로 채우기
        for i in range(ysize):
            if len(g[i])<xsize:
                g[i].append('#'*(xsize-len(g[i])))

    #     for i in range(ysize):
    #         print(g[i])
for i in range(ysize):
    print(''.join(map(str,g[i])))