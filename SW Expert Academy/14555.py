# 공과 잡초
t=int(input())
for i in range(t):
    answer=0
    s=input()
    while '()' in s or '(|' in s or '|)' in s:
        s = s.replace('()','c')
        s = s.replace('|)', 'c')
        s = s.replace('(|', 'c')

    print('#'+str(i+1), s.count('c'))