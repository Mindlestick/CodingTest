# 기상캐스터
h,w=map(int,input().split())
g=[[]*w for i in range(h)]
answer=[[0]*w for i in range(h)]
for i in range(h):
    g[i]=list(map(str,input()))

#print(g)
for i in range(h):
    n=-1
    f=False
    for j in range(w):
        if g[i][j]=='.' and f:
            n+=1
        elif g[i][j]=='c':
            n=0
            f=True
        #answer[i][j] = n
        print(n,end=' ')
    print()

#print(answer)