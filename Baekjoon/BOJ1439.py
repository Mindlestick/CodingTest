#2839 뒤집기

s = input()
num0=0
num1=0

#첫글자 1
if s[0]=='1':
    num0+=1
else:
    num1+=1

for i in range(len(s)-1):
    if s[i]!=s[i+1]:
        if s[i+1]=='1':
            num0+=1
        else:
            num1+=1

print(min(num0,num1))
