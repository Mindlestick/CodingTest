def solution(s):
    s=s.lower()
    s=list(s)
    s[0]=s[0].upper()
    for i in range(1,len(s)):
        if s[i-1].isspace():
            s[i]=s[i].upper()
            continue
        
    answer="".join(s)
    return answer