def solution(s):
    cnt = 0
    same = 0
    diff = 0
    res = 0
    
    for i in range(len(s)) :
        x = s[cnt]
        if s[i] == x :
            same += 1
        else :
            diff += 1
        
        if same == diff :
            res += 1
            cnt = i + 1
            same = 0
            diff = 0
        elif same != diff and i == len(s) - 1:
            res += 1
            
    return res
