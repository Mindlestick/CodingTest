# 알파벳 공부
T=int(input())
for t in range(T):
    s=list(input())
    answer=0
    for i in range(len(s)):
        if ord('a')+i==ord(s[i]):
            answer+=1
        else:
            break
    print('#'+str(t+1),answer)

"""
5
abcdefghijklmnopqrstu
abcdefghijklmnopqrstuvwzyx
abcefghijk
xyz
absolute
"""