# 등수 구하기
n,score,p=map(int,input().split())
if n==0 and p>0:
    print(1)
else:
    nlist=list(map(int,input().split()))
    nlist.sort(reverse=True)
    rank=[sorted(nlist, reverse=True).index(i)+1 for i in nlist]
    cnt_h=0
    cnt_s=0
    for i in range(n):
        if score<nlist[i]:
            cnt_h+=1
        elif score==nlist[i]:
            cnt_s+=1
    if (cnt_h+cnt_s)<p:
        if cnt_s==0:
            print(cnt_h+1)
        else:
            print(rank[nlist.index(score)])
    else:
        print(-1)