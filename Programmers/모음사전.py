def solution(word):
    answer = 0
    d={'A':0,'E':1,'I':2,'O':3,'U':4}
    
    s=[1]
    for i in range(1,5):
        s.append(s[i-1]+5**i)
    s.reverse()
    #print(s) #	[781, 156, 31, 6, 1]
    answer+=len(word)
    
    for i in range(len(word)):
        print(word[i],i)
        answer+=d[word[i]]*s[i]

    return answer