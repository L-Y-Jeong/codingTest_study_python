def solution(sizes):
    answer = 0
    maxL, maxS = 0, 0
    
    for size in sizes:
        if size[0] > size[1] :
            l, s = size[0], size[1]
        else :
            l, s = size[1], size[0]
        if maxL < l :
            maxL = l
        if maxS < s :
            maxS = s

    answer = maxL * maxS
                  
    return answer
