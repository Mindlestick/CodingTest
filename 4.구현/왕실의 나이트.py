data="c2"
row=int(data[1])
col=int(ord(data[0]))-int(ord('a'))+1

#8가지 이동방식
dx=[-2,-2,2,2,-1,1,-1,1]
dy=[-1,1,-1,1,-2,-2,2,2]

cnt=0
tmpx=0
tmpy=0
for i in range(len(dx)):
    tmpx = row+dx[i]
    tmpy = col+dy[i]
    if tmpx > 0 and tmpy > 0 and tmpx <= 8 and tmpy <= 8:
        cnt += 1

print(cnt)