def solution(t, p):
    tl = len(t)
    pl = len(p)
    #print(tl,pl)

    n=""
    cnt=0
    for i in range(tl-pl+1):
        for j in range(pl):
            n+=t[i+j]
        print(int(n))
        if int(n) <= int(p):
            cnt+=1
        n=""

    return cnt