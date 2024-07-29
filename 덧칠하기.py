def solution(n, m, section):
    
    lenN = len(section)
    num = section[0]
    cnt = 0
    while(num <= section[lenN-1]):
        for i in range(m):
            num += 1
        cnt += 1
    
    return cnt
