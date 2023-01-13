
d= [0]*100

def fibo(x):
    #초기값
    if x==1 or x==2:
        return 1
    #이미 구한 적 있는 수
    if d[x]!=0:
        return d[x]
    #기록
    d[x] = fibo(x-1)+fibo(x-2)
    return d[x]

print(fibo(10))