def solution(t, p):
    answer = 0
    
    pLen = len(p)
    tLen = len(t)
    
    for i in range(tLen - pLen + 1):
        numArr = []
        cnt = i
        for j in range(pLen):
            numArr.append(t[cnt])
            cnt += 1
        num = int(''.join(numArr))
        
        if num <= int(p):
            answer += 1
            
    return answer
