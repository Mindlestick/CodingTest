#팩토리얼 재귀함수
def fact(x):
    if x==0 or x==1:
        return 1
    return x*fact(x-1)

#최대공약수(유클리드 호제법)
def GCD(a,b):
    if a%b==0:
        return b
    else:
        return GCD(b,a%b)

print(fact(6))
print(GCD(192,162))
