# 킹
d=['A','B','C','D','E','F','G','H']
k, r, n = input().split()
g=[[0]*8 for i in range(8)]
kx, ky = d.index(k[0]),int(k[1])-1
rx, ry = d.index(r[0]),int(r[1])-1

g[kx][ky]=1
g[rx][ry]=2

for i in range(int(n)):
    a=input()
    nx, ny = kx, ky
    #상하좌우
    if len(a)==1:
        if a=='R':
            nx+=1
        elif a=='L':
            nx-=1
        elif a=='B':
            ny-=1
        elif a=='T':
            ny+=1
    # 대각선
    else:
        if a == 'RT':
            nx += 1
            ny += 1
        elif a == 'LT':
            nx -= 1
            ny += 1
        elif a == 'RB':
            nx += 1
            ny -= 1
        elif a == 'LB':
            nx -= 1
            ny -= 1

    #범위 벗어나면 무시
    if nx<0 or ny<0 or nx>=8 or ny>=8:
        continue

    # 가는 방향에 돌이 있으면
    if g[nx][ny] == 2:
        # 돌 먼저 옮기기
        mx, my = rx,ry
        if a=='R':
            mx+=1
        elif a=='L':
            mx-=1
        elif a=='B':
            my-=1
        elif a=='T':
            my+=1
        elif a == 'RT':
            mx += 1
            my += 1
        elif a == 'LT':
            mx -= 1
            my += 1
        elif a == 'RB':
            mx += 1
            my -= 1
        elif a == 'LB':
            mx -= 1
            my -= 1
         # 돌이 범위 벗어나면 무시
        if mx < 0 or my < 0 or mx >= 8 or my >= 8:
            continue
        g[rx][ry]=0
        rx,ry=mx,my
        g[rx][ry]=2

    g[kx][ky]=0
    kx,ky=nx,ny
    g[kx][ky]=1

print(str(d[kx])+str(ky+1))
print(str(d[rx])+str(ry+1))