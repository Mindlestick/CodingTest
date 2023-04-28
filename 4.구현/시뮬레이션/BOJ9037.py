# The candy war
def isSame(li):
    tmp = li[0]
    for i in range(1,len(li)):
        if tmp!=li[i]:
            return False
    return True

t=int(input())

for i in range(t):
    answer=0
    
    n=int(input())
    nlist=list(map(int,input().split()))
    if n==1:
        print(0)
        continue
    
    j=0
    while(1):
        if j==300:
            break
        
        #홀수이면 채우기
        for k in range(n):
            if nlist[k%n]%2!=0:
                nlist[k%n]+=1

        #print(nlist)
        
        #모두 같으면
        if isSame(nlist):
            break
        
        #옆에 반 넘기기

        tmp=[p//2 for p in nlist]
        for k in range(n):
            nlist[k]=nlist[k]//2+tmp[k-1]

        answer+=1
        j+=1
    print(answer)