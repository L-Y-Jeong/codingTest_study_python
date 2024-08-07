def solution(s, skip, index):
    answer = []
    n = len(s)

    
    for i in range(n) :
        alph = s[i]
        for j in range(index):
            if (chr(ord(alph)) in skip):
                alph = chr(ord(alph) + 2)
            else :
                alph = chr(ord(alph) + 1)
            if (ord(alph) > ord('z')):
                alph = 'a'
        answer.append(alph)
            
                
    return ''.join(alph)
        
