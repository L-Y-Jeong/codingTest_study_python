def solution(lottos, win_nums):
    answer = []
    
    score = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    
    low = 0
    high = 0
    cnt = 0
    
    zero = lottos.count(0)

    for i in lottos:
        if i in win_nums:
            cnt += 1
                        
    low = score[cnt]
    high = score[cnt+zero]
    
    answer.extend([high, low])
    
    return answer
