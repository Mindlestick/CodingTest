dic={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8}
k, r, n = input().split()
g=[[0]*8 for i in range(8)]
kx, ky = dic[k[0]]-1,int(k[1])-1
rx, ry = dic[r[0]]-1,int(r[1])-1

g[kx][ky]=1
g[rx][ry]=2

for i in range(int(n)):
    a=input()
    #상하좌우
    if len(a)==1:
        nx, ny = kx, ky
        if a=='R':
            nx+=1
        elif a=='L':
            nx-=1
        elif a=='B':
            ny-=1
        elif a=='T':
            ny+=1
        
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
            # 돌이 범위 벗어나면 무시
            if mx < 0 or my < 0 or mx >= 8 or my >= 8:
                continue
            g[rx][ry]=0
            rx,ry=mx,my
            g[rx][ry]=2

        g[kx][ky]=0
        kx,ky=nx,ny
        g[kx][ky]=1
    #대각선
    else:
        nx, ny = kx, ky
        if a == 'RT':
            nx += 1
            ny += 1
        elif a == 'LT':
            nx -= 1
            ny+=1
        elif a == 'RB':
            nx+=1
            ny -= 1
        elif a == 'LB':
            nx-=1
            ny -= 1

        # 범위 벗어나면 무시
        if nx < 0 or ny < 0 or nx >= 8 or ny >= 8:
            continue

        # 가는 방향에 돌이 있으면
        if g[nx][ny] == 2:
            # 돌 먼저 옮기기
            mx, my = rx, ry
            if a == 'RT':
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
            g[rx][ry] = 0
            rx, ry = mx, my
            g[rx][ry] = 2

        g[kx][ky] = 0
        kx, ky = nx, ny
        g[kx][ky] = 1

    print(a,g)
print(chr(kx)+'A',ky)