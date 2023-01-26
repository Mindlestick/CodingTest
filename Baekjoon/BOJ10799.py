#쇠막대기
s=list(input())
l=[]
n=0

for i in range(len(s)):
    if s[i]=='(':
        l.append(s[i])

    if s[i]==')':
        #레이저
        if s[i-1]=='(':
            l.pop()
            n+=len(l)
        else:
            l.pop()
            n+=1
print(n)