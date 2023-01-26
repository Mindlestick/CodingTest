#괄호 끼워넣기

s=list(input())
l=[]
l.append(s[0])
for i in range(1,len(s)):
    if len(l)==0:
        l.append(s[i])
    else:
        if l[-1]==s[i]:
            l.append(s[i])
        if l[-1]==')' and s[i]=='(':
            l.append(s[i])
        if l[-1]=='(' and s[i]==')':
            l.pop()

print(len(l))