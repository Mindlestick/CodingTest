d= [0]*1001
def dp(x):
    #종료 조건
    if x==0:
        return 1
    if x==1 :
        return 0
    if x==2:
        return 3
    
    #이미 구한 적 있는 수
    if d[x]!=0:
        return d[x]
    #기록
    tmp=3*dp(x-2)
    for i in range(3,x+1):
        if i%2==0:
            tmp+=2*dp(x-i)
    d[x] = tmp
    return d[x]

n=int(input())
print(dp(n))