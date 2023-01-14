d= [0]*1001
def dp(x):
    #종료 조건
    if x==1 :
        return 1
    if x==2:
        return 2
    
    #이미 구한 적 있는 수
    if d[x]!=0:
        return d[x]
    #기록
    d[x] = (dp(x-1)+dp(x-2)) % 10007
    return d[x]

n=int(input())
print(dp(n))