def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reDic = {i : 0 for i in id_list}
    
    for r in set(report):
        x,y = r.split()
        reDic[y] += 1
        
    for r in set(report):
        x,y = r.split()
        if reDic[y] >= k:
            answer[id_list.index(x)] += 1    
    
    return answer
