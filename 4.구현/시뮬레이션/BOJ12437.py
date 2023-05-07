# 새로운 달력 (Small)
def cnt_calendar(y,m,d):
    answer=0
    if m%d==0:
        tmp=m//d
        answer = y * tmp
    else:
        g=[[0]*d for i in range(100)]

        nm,nd=0,0
        for i in range(y):
            for j in range(m):
                g[nm][nd]=j+1
                nd+=1
                if nd==d:
                    nd=0
                    nm+=1
                elif j+1==m:
                    nm+=1

        answer=nm
    return answer

t=int(input())
for i in range(t):
    y,m,d = map(int,input().split())

    print('Case #',end='')
    print( i+1,end='')
    print(':', cnt_calendar(y,m,d))