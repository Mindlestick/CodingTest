# 가위 바위 보
k=int(input())

for i in range(k):
    n=int(input())
    nlist=[[] for _ in range(n)]
    lose = []
    for j in range(n):
        nlist[j]=input()
    for j in range(len(nlist[0])):
        li=[]
        for k in range(n):
            if k in lose:
                continue
            li.append(nlist[k][j])
        s=list(set(li))
        if len(s)==2:
            for k in range(n):
                if 'S' in s and 'R' in s:
                    if nlist[k][j]=='S':
                        lose.append(k)
                if 'R' in s and 'P' in s:
                    if nlist[k][j]=='R':
                        lose.append(k)
                if 'S' in s and 'P' in s:
                    if nlist[k][j]=='P':
                        lose.append(k)
    lose=list(set(lose))
    if n-len(lose)>1:
        print(0)
    elif n-len(lose)==1:
        for j in range(n):
            if j not in lose:
                print(j+1)

